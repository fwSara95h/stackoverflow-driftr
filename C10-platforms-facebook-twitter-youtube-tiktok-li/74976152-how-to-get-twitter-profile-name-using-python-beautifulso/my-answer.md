---
title: "How to get twitter profile name using python BeautifulSoup module?"
site: stackoverflow
question_id: 74976152
answer_id: 75010441
url: https://stackoverflow.com/a/75010441
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-04T19:34:59Z
last_edited: 2023-01-04T20:40:46Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75010441/revisions
accepted: false
score: 1
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: [linkToSoup, linkToSoup_selenium, selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6afaab248312bf972d4554b234c8cab010ad181f037f4293942cd2b76351ad11
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75010441>, 2023-01-04, last edited 2023-01-04; score 1. Text as retrieved 2026-10-12.

> `html = requests.get(url).text`

Twitter profile links cannot be scraped simply through `requests` like this since the contents of the profile pages are loaded with JavaScript [via the API], as you might notice if you [**previewed the source HTML**](https://i.sstatic.net/WCU4Z.png) on you browser's [network logs](https://support.happyfox.com/kb/article/882-accessing-the-browser-console-and-network-logs/) or [**checked the fetched HTML**](https://i.sstatic.net/utDaw.png).

---

> ```python
> name_element = soup.find('span', {'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
> ```

> ```python
>     display_name = name_element.text
> ```

Even after fetching the right HTML, calling `.find` like that will result in `display_name` containing *`'To view keyboard shortcuts, press question mark'`* or *`'Don’t miss what’s happening'`* because there are [67 `span` tags with that class](https://i.sstatic.net/IDSOP.png). Calling `.find_all(....)[6]` *might* work but it's definitely not a reliable approach. You should instead consider using [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) to [target the name](https://i.sstatic.net/FR2Yx.png).

```python
name_element = soup.select_one('div[data-testid="UserName"] span>span')
```

The `.find` equivalent would be

```python
# name_element = soup.find('div', {'data-testid': 'UserName'}).span.span ## too many weak points
name_element = soup.find(lambda t: t.name == t.parent.name == 'span' and t.find_parent('div', {'data-testid': 'UserName'}))
```

but I find `.select` much more convenient.

---

#### Selenium Example

Using two functions I often use for scraping - [`linkToSoup_selenium`](https://pastebin.com/kEC9gPC8) (which takes a URL and returns a `BeautifulSoup` object after using [selenium](https://www.scrapingbee.com/blog/selenium-python/) and `bs4` to load and parse the HTML), and [`selectForList`](https://pastebin.com/ZnZ7xM6u) (which extracts details from bs4 Tags based on selectors [like in the `selectors` dictionary below])

Setup:

```python
# imports ## PASTE FROM https://pastebin.com/kEC9gPC8
# def linkToSoup_selenium... ## PASTE FROM https://pastebin.com/kEC9gPC8
# def selectForList... ## PASTE FROM https://pastebin.com/ZnZ7xM6u 

## JUST FOR REDUCING WHITESPACE - not important for extracting information ##
def miniStr(o): return ' '.join(w for w in str(o).split() if w)

profileUrls = ['https://twitter.com/twitterID', 'https://twitter.com/jokowi', 'https://twitter.com/sep_colin']

# ptSel = 'article[data-testid="tweet"]:has(div[data-testid="socialContext"])'
# ptuaSel = 'div[data-testid="User-Names"]>div>div>div>a'
selectors = {
    'og_url': ('meta[property="og\:url"][content]', 'content'),
    'name_span': 'div[data-testid="UserName"] span>span',
    'name_div': 'div[data-testid="UserName"]',
    # 'handle': 'div[data-testid="UserName"]>div>div>div+div',
    'description': 'div[data-testid="UserDescription"]',
    # 'location': 'span[data-testid="UserLocation"]>span',
    # 'url_href': ('a[data-testid="UserUrl"][href]', 'href'),
    # 'url_text': 'a[data-testid="UserUrl"]>span',
    # 'birthday': 'span[data-testid="UserBirthdate"]',
    # 'joined': 'span[data-testid="UserJoinDate"]>span',
    # 'following': 'div[data-testid="UserName"]~div>div>a[href$="\/following"]',
    # 'followers': 'div[data-testid="UserName"]~div>div>a[href$="\/followers"]',
    # 'pinnedTweet_uname': f'{ptSel} div[data-testid="User-Names"] span>span',
    # 'pinnedTweet_handl': f'{ptSel} {ptuaSel}:not([aria-label])',
    # 'pinnedTweet_pDate': (f'{ptSel} {ptuaSel}[aria-label]', 'aria-label'),
    # 'pinnedTweet_text': f'{ptSel} div[data-testid="tweetText"]',
}


def scrapeTwitterProfile(profileUrl, selRef=selectors):
    soup = linkToSoup_selenium(profileUrl, ecx=[
        'div[data-testid="UserDescription"]'  # wait for user description to load
        # 'article[data-testid="tweet"]'  # wait for tweets to load
    ], tmout=3, by_method='css', returnErr=True)
    if not isinstance(soup, str): return selectForList(soup, selRef)
    return {'Error': f'failed to scrape {profileUrl} - {soup}'}
```

<sup>Setting `returnErr=True` returns the error message (a string instead of the BeautifulSoup object) if anything goes wrong. `ecx` should be set based on which part/s you want to load (it's a list so it can have multiple selectors). `tmout` doesn't have to be passed (default is 25sec), but if it is, it should be adjusted for the other arguments and your own device and browser speeds - on my browser, `tmo=0.01` is enough to load user details, but loading the first tweets takes at least `tmo=2`.</sup>

I wrote `scrapeTwitterProfile` mostly so that I could get `tuDets` [below] in one line. The for-loop after that is just for printing [the results](https://i.sstatic.net/IJGcv.png).

```python
tuDets = [scrapeTwitterProfile(url) for url in profileUrls]
for url, d in zip(profileUrls, tuDets):
    print('\nFrom', url)
    for k, v in d.items(): print(f'\t{k}: {miniStr(v)}')
```

---

#### snscrape Example

[snscrape](https://github.com/JustAnotherArchivist/snscrape#installation) has a module for Twitter that can be used to access Twitter data without having registered up for the [API](https://developer.twitter.com/en/docs) yourself. The example below prints a similar [output](https://i.sstatic.net/l1p5R.png) to the previous example, but is faster.

```python
# import snscrape.modules.twitter as sns_twitter
# def miniStr(o): return ' '.join(w for w in str(o).split() if w)

# profileIDs = [url.split('twitter.com/', 1)[-1].split('/')[0] for url in profileUrls]
profileIDs = ['twitterID', 'jokowi', 'sep_colin']
keysList = ['username', 'id', 'displayname', 'description', 'url']

for pid in profileIDs:
    tusRes, defVal = sns_twitter.TwitterUserScraper(pid).entity, 'no such attribute'
    print('\nfor ID', pid)
    for k in keysList: print('\t', k, ':', miniStr(getattr(tusRes, k, defVal)))
```

<sub>You can get most of [the attributes](https://i.sstatic.net/hvOZq.png) in `.entity` [with `.__dict__`](https://i.sstatic.net/rLwKY.png) or print them all all with something like</sub>

```python
print('\n'.join(f'{a}: {miniStr(v)}' for a, v in [
    (n, getattr(tusRes, n)) for n in dir(tusRes)
] if not (a[:1] == '_' or callable(v))))
```

See [this example](https://gist.github.com/rashidesai24/a3090f71b780e57bb933288bf94ebab9/raw/9314522b6074442a99d136affa4aa6dfcba2d967/Scrape%20tweets%20from%20a%20username) from [this tutorial](https://medium.com/dataseries/how-to-scrape-millions-of-tweets-using-snscrape-195ee3594721#543a) if you are interested in scraping tweets as well.
