---
title: "How to scrape news articles from cnbc with keyword \"Green hydrogen\"?"
site: stackoverflow
question_id: 74067792
answer_id: 74075841
url: https://stackoverflow.com/a/74075841
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-15T00:17:53Z
last_edited: 2022-10-15T00:26:37Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74075841/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1413bf218bee878dad4442bda99870449f5174d5c60c93c5d5a8d9087517b982
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-15

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74075841>, 2022-10-15, last edited 2022-10-15; score 0. Text as retrieved 2026-10-12.

As mentioned in another answer, the data about the articles are loaded using another link, which you can find via [the networks tab in devtools][1]. [In chrome, you can open devtools with `Ctrl`+`Shift`+`I`, then go to the networks tab to see requests made, and then click on the name starting with 'json.aspx?...' to see details, then copy the Request URL from Headers section.]

Once you have the Request URL, you can copy it and make the request in your code to get the data:
```python
# dataReqUrl contains the copied Request URL
dataReq = requests.get(dataReqUrl)
for r in dataReq.json()['results']: print(r['cn:title'])
```

If you don't feel like trying to find that one request in 250+ other requests, you might also try to assemble a shorter form of the url with something like:
```python
# import urllib.parse

# find link to js file with api key
jsLinks = bsobj.select('link[href][rel="preload"]')
jUrl = [m.get('href') for m in jsLinks if 'main' in m.get('href')][0]

jRes = requests.get(jUrl) # request js file api key

# get api key from javascript
qKey = jRes.text.replace(' ', '').split(
    'QUERYLY_KEY:'
)[-1].split(',')[0].replace('"', '').strip()

# form url
qParams = {
    'queryly_key': qKey,
    'query': search_for, # = 'green hydrogen'
    'batchsize': 10 # can go up to 100 apparently
}
qUrlParams = urllib.parse.urlencode(qParams, quote_via=urllib.parse.quote)
dataReqUrl = f'https://api.queryly.com/cnbc/json.aspx?{qUrlParams}'
```

Even though the assembled `dataReqUrl` is not identical to the copied one, it seems to be giving the same results (I checked with a few different search terms). However, I don't know how reliable this method is, especially compared to the much less convoluted approach with [selenium](https://medium.com/featurepreneur/an-introduction-to-web-automation-using-selenium-python-2ad84814b11c):
```python
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# define chromeDriver_path <-- where you saved 'chromedriver.exe'
cnbc_url = "https://www.cnbc.com/search/?query=green%20hydrogen&qsearchterm=green%20hydrogen"
driver = webdriver.Chrome(chromeDriver_path)
driver.get(cnbc_url)

ctSelector = 'span.Card-title'
WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ctSelector)))
cardTitles = driver.find_elements(By.CSS_SELECTOR, ctSelector)

cardTitles_text = [ct.get_attribute('innerText') for ct in cardTitles] 
for c in cardTitles_text: print(c)
```
In my opinion, this approach is more reliable as well as simpler.


  [1]: https://i.sstatic.net/3sDQf.png
