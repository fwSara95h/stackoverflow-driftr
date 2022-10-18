---
title: "Facebook Scraping Python"
site: stackoverflow
question_id: 74100308
answer_id: 74105681
url: https://stackoverflow.com/a/74105681
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-18T04:20:36Z
last_edited: 2022-10-19T04:46:48Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74105681/revisions
accepted: false
score: 3
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: [linkToSoup]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9556ddfab70ab4f0b78402fc1c2f0c2260bc180362d1c17d1a2bf12692f3a953
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-18

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74105681>, 2022-10-18, last edited 2022-10-19; score 3. Text as retrieved 2026-10-12.

You can't scrape facebook as simply as this - as mentioned in comments fb intentionally makes their pages harder to scrape. Also, the page you're fetching has no human-readable data at all - all of that is loaded afterwards with scripts, and so cannot be fetched with a simple request.

If you *must* use  request and bs, you can start with [this tutorial](https://python.gotrained.com/scraping-facebook-posts-comments/) as a guide, but I really think it would be easier to use an api like [FacebookPostsScraper](https://github.com/hhsm95/FacebookPostsScraper) or even to use [selenium](https://medium.com/nerd-for-tech/collecting-public-data-from-facebook-using-selenium-and-beautiful-soup-f0f918971000) (although if you've never used selenium before, you might want to start with [this beginner tutorial](https://pythonalgos.com/web-scraping-the-easy-way-python-selenium-beautiful-soup/) first).

Also, when I inspected the page, there were no `h2` elements with the class you specified, although *"Forgot Account?"* link did happen to have that same class; and  the email isn't in a `h2` element at all - it's inside a `span`.

If you're willing to use selenium, I have this function for getting BeautifulSoup tree for pages that don't load all at once (and also for pages with blockers like cloudscraper):
```python
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def linkToSoup_selenium(l, ecx=None):
    try:
        driver = webdriver.Chrome('chromedriver.exe')
        # I copy chromedriver.exe to every folder with py file that will need to scrape with selenium

        driver.get(l)
        if ecx:
            WebDriverWait(driver, 25).until(
                EC.visibility_of_all_elements_located((By.XPATH, ecx)))

        lSoup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.close()
        del driver
        return lSoup
    except Exception as e:
        print(e)
        return None
```
Pages that load all at once don't need the `ecx` argument, but fb will; `'//h2//span//*[contains(text(),"Intro")]'` can be used to ensure the [intro section][1] is loaded at least (see [this documentation](https://selenium-python.readthedocs.io/locating-elements.html) and [this xpath cheatsheet](https://devhints.io/xpath) for further explanation).

The function can be used to get a proper tree of the page with

```python
soup = linkToSoup_selenium(
    'https://www.facebook.com/KNOW-MORE-training-center-111698018315706/?ref=page_internal', 
    '//h2//span//*[contains(text(),"Intro")]'
)
```

then you *might* be able to get the email with
 
```python
# import re
a = soup.find('div', attrs={"data-pagelet": "ProfileTilesFeed_0"}).find(
   lambda l: l.name == 'span' and re.search('\S+@\S+', l.text)).text)
).text
print(a)
```

or, to be more cautious of possible NoneType/AttributeErrors:

```python
# import re
if soup:
   introSection = soup.find('div', attrs={"data-pagelet": "ProfileTilesFeed_0"}) 
   if introSection:
      emailEl = introSection.find(
         lambda l: l.name == 'span' and re.search('\S+@\S+', l.text)).text)
      )
      if emailEl:
         print(emailEl.text)
      else: print('!could not find any span tag with email within section!')
   else: print('!could not find intro section!')
else: print('!could not extract!')
```

[See [this short tutorial](https://www.geeksforgeeks.org/extracting-email-addresses-using-regular-expressions-python/) if you're unfamiliar with regex]

However, the `div` with `data-pagelet="ProfileTilesFeed_0"` only appears when not logged in; and even then, I don't know if it will always appear or have the same attribute value every time, so we might have to be even more convoluted like:
```python
# import re

#if soup:
h2span = [s for s in soup.select('h2 span') if 'Intro' in s.text]
if len(h2span) > 0:
    introSection = [
        p for p in h2span[0].parents if p.name == 'div' and
        p.get('class') and len(p.get('class')) == 1
    ]
    if len(introSection) > 0:
        # as before, but introSection[0] because list
        emailEl = introSection[0].find(
            lambda l: l.name == 'span' and re.search('\S+@\S+', l.text)
        )
        if emailEl:
            print(emailEl.text)
        else: print('could not find any span tag with email within section')
    else: print('could not find intro section in h2span ancestors')
else:  print('found no span with h2 ancestor')
```

Seems like a lot for just an email address, but potentially useful if you're scraping lots of pages; it's possibly more common to scrape the entire Intro section and then split it up later....

  [1]: https://i.sstatic.net/7uvvN.png
