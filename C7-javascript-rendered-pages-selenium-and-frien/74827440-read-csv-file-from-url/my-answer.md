---
title: "Read csv file from url"
site: stackoverflow
question_id: 74827440
answer_id: 74827588
url: https://stackoverflow.com/a/74827588
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-16T17:01:01Z
last_edited: 2022-12-16T17:09:33Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74827588/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fb41d4adcdbfc6d60167d0c468554bfe5015ebe48743fdad6bf9a1091ea0b6f6
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74827588>, 2022-12-16, last edited 2022-12-16; **accepted**; score 1. Text as retrieved 2026-10-12.

As commented by [@JeJe](https://stackoverflow.com/users/1536343/je-je), 
> you need to iterate through your start_urls list

`start_urls` is a LIST of strings, and `driver.get` expects just *one* url as string - something like

```python
# driver.get(start_urls) # NOT like this
for sUrl in start_urls:
    driver.get(sUrl)
    ### SCRAPE AS NEEDED ###
```

or, if you want to keep track of progress, something like

```python
suLen = len(start_urls)
for si, sUrl in enumerate(start_urls):
    print(f'[{si} of {suLen}] reading {sUrl}')
    driver.get(sUrl)
    ### SCRAPE AS NEEDED ###
```

---


Btw, you don't need to do everything under `with open...` - getting `start_urls` is enough:

```python
with open("data.csv") as file:
    start_urls=[line.strip() for line in file]  

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

suLen = len(start_urls)
for si, sUrl in enumerate(start_urls):
    print(f'[{si} of {suLen}] reading {sUrl}')
    driver.get(sUrl)
    ### SCRAPE AS NEEDED ###
```

but you can only use just `start_urls=[line.strip() for line in file]` if you csv has only on column with no headers.
