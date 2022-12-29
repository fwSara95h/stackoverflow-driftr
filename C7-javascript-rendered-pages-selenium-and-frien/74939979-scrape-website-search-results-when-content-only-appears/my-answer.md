---
title: "Scrape website search results when content only appears after clicking 'search' (Python - Beautiful soup)"
site: stackoverflow
question_id: 74939979
answer_id: 74947523
url: https://stackoverflow.com/a/74947523
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-29T05:17:39Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74947523/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [function set, linkToSoup, linkToSoup_selenium, selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d5747eee34b66f41b62b9c7e1967223fb6ff2f71d3c04949091e48635739f493
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-29

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74947523>, 2022-12-29; **accepted**; score 0. Text as retrieved 2026-10-12.

> `the HTML does not appear until AFTER the search is clicked`

That was not what I experienced - when I went to the [nyheder](https://danskfolkeparti.dk/nyheder/) page, there were already 10 posts on the timeline, and more loaded when I scrolled down. 

However, it's true that the by HTML fetched `requests.get` [does not contain the timeline](https://i.sstatic.net/TBjBP.png). It's an empty frame with just the top and bottom panes of the page, and the rest is rendered with JavaScript. I can suggest 2 ways to get around this - either use selenium or scrape via their API.

---
---

### Solution 1: Selenium 

I have 2 functions which I often use for scraping:
- [`linkToSoup_selenium`](https://pastebin.com/kEC9gPC8) which takes a URL and [if everything goes ok] returns a BeautifulSoup object. For this site, you can use it to:
    - scroll down a certain number of times [it's best to over-estimate how many scrolls you need]
    - wait for the links and dates to load
    - click "Accept Cookies" (if you want to, doesn't make a difference tbh)
- [`selectForList`](https://pastebin.com/ZnZ7xM6u) which takes a bs4 Tag and list of CSS selectors and returns the corresponding details from that Tag 
    - (If you are unfamiliar with CSS selectors, I often use [this reference](https://www.w3schools.com/cssref/css_selectors.php) as a cheatsheet.)

So, you can set up a reference dictionary (`selRef`) of selectors [that will be passed to `selectForList` later] and then fetch and parse the loaded HTML with `linkToSoup_selenium`:

```python
selRef = {
    'title': 'div.content>a.post-link[href]', 'date': 'p.text-date',
    'url': ('div.content>a.post-link[href]', 'href'),
    # 'category': 'div.content>p.post-category-timeline',
    # 'excerpt': 'div.content>p.post-content-rendered',
}

soup = linkToSoup_selenium('https://danskfolkeparti.dk/nyheder/', ecx=[
    'div.timeline>div>div.content>a.post-link[href]',  # load links [+titles]
    'div.timeline>div>p.text-date'  # load dates [probably redundant]
], clickFirst=[
    'a[role="button"][data-cli_action="accept_all"]'  # accept cookies [optional]
], by_method='css', scrollN=(20, 5), returnErr=True) # scroll 20x with 5sec breaks
```

Since `returnErr=True` is set, the function will return a string containing an error message if something causes it to fail, so you should habitually check for that before trying to extract the data.

```python
if isinstance(soup, str):
    print(type(soup), miniStr(soup)[:100])  # print error message
    prTimeline = []
else:
    prTimeline = [{k: v for k, v in zip(
        list(selRef.keys()), selectForList(pr, list(selRef.values()))
    )} for pr in soup.select('div.timeline>div')]
```

Now `prTimeline` looks something like 

```python
## [only the first 3 of 76 are included below] ##
[{'title': 'Året 2022 viste hvad Dansk Folkeparti er gjort af',
  'date': '23/12/2022',
  'url': 'https://danskfolkeparti.dk/nyheder/mortens-nyhedsbrev/aaret-2022-viste-hvad-dansk-folkeparti-er-gjort-af/'},
 {'title': 'Mette Frederiksen har stemt danskerne hjem til 2001',
  'date': '13/12/2022',
  'url': 'https://danskfolkeparti.dk/nyheder/mortens-nyhedsbrev/mette-frederiksen-har-stemt-danskerne-hjem-til-2001/'},
 {'title': 'Vi klarede folketingsvalget – men der skal kæmpes lidt endnu',
  'date': '23/11/2022',
  'url': 'https://danskfolkeparti.dk/nyheder/mortens-nyhedsbrev/vi-klarede-folketingsvalget-men-der-skal-kaempes-lidt-endnu/'}]
```

---
---

### Solution 2: API 

If you open [open the Network Tab](https://support.happyfox.com/kb/article/882-accessing-the-browser-console-and-network-logs/) before clicking search (or just scrolling all the way down, or refreshing the page), you might see [this request](https://i.sstatic.net/UXWTd.png) with [a JSON response](https://i.sstatic.net/nXOm0.png) that is being used to fetch the data for populating the timeline. So, you just need to replicate this API request.

However, as [@SergeyK](https://stackoverflow.com/users/6593287/sergey-k) commented,
> site have Cloudflare protection, so u cant get result without setting up cookies

and the same seems to be true for the API as well. I'm not good with setting headers and cookies as needed; so instead, I tend to just use **[`cloudscraper`](https://pypi.org/project/cloudscraper/)** [or [`HTMLSession`](https://requests.readthedocs.io/projects/requests-html/en/latest/#tutorial-usage) sometimes] in such cases.

```python
# import  cloudscraper
qStr = 'categories=20,85,15,83,73,84,&before=2022-12-28T23:59:59'
qStr += '&after=1990-05-08T01:01:01&per_page=99&page=1'
apiUrl = f'https://danskfolkeparti.dk/wp-json/wp/v2/posts?{qStr}'
prTimeline = [{
    'title': pr['title']['rendered'],
    'date': pr['date'], # 'date': pr['date_gmt'], 
    'url': pr['link']
} for pr in cloudscraper.create_scraper().get(apiUrl).json()]
```

and [the resulting `prTimeline`](https://i.sstatic.net/jGD1s.png) looks pretty similar to the Selenium output.

---

There's an expanded version using a [set of functions](https://pastebin.com/aSQrW9ff) that lets you [get the same results](https://i.sstatic.net/8TrgO.png) with 

```python
prTimeline, rStatus = danskfolkeparti_apiScraper(pathsRef={'title': ['title', 'rendered'], 'date': ['date'], 'url': ['link']})
```

But you can do much more, like passing `searchFor={'before': '2022-10-01T00:00:00'}` to only get [posts before October](https://i.sstatic.net/4su0E.png), or `searchFor="search terms"` to [search by keywords](https://i.sstatic.net/hvHwb.png) but 
- you can't search for keywords and also set parameters like category/time/etc
- you have to make sure that `before` and `after` are in [ISO format](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat), and that `page` is a positive integer, and that `categories` is a list of integers [or they might be ignored]

---

You can get more information if you leave the default arguments and make use of all of the functions, as below:

```python
# from bs4 import BeautifulSoup

### FIRST PASTE EVERYTHING FROM https://pastebin.com/aSQrW9ff ###

prTimeline, prtStatus = danskfolkeparti_apiScraper()
prCats = danskfolkeparti_catNames([pr['category'] for pr in prTimeline])
for pi, (pr, prCat) in enumerate(zip(prTimeline, prCats)):
    prTimeline[pi]['category'] = prCat
    cTxt = BeautifulSoup(pr['content']).get_text(' ')
    cTxt = ' '.join(w for w in cTxt.split() if w) # reduce whitescpace
    prTimeline[pi]['content'] = cTxt 
```

---

### FULL RESULTS

The full results from the last code snippet, as well as the selenium solution (with ALL of `selRef` uncommented) have been uploaded to [this spreadsheet](https://docs.google.com/spreadsheets/d/1yiDCrMi3Sog7qLcT_6pS-71xL1FkgNQnOS5ngPlMf_M/edit?usp=sharing). The CSVs were saved using [pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html).

```python
# import pandas 

fileName = 'prTimeline.csv' # 'dfn_prTimeline_api.csv' # 'dfn_prTimeline_sel.csv'
pandas.DataFrame(prTimeline).to_csv(fileName, index=False)
```

Also, if you are curious, you can [see the categories in the default API call](https://i.sstatic.net/CGf9U.png) with `danskfolkeparti_categories([20,85,15,83,73,84])`.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[zach dickson](https://stackoverflow.com/users/15538310)** (2022-12-29): Thanks so much for taking the time to put this together -- very appreciated!
