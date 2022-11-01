---
title: "Pandas Read HTML wont scrape the clickable image"
site: stackoverflow
question_id: 74232047
answer_id: 74273504
url: https://stackoverflow.com/a/74273504
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T08:53:09Z
last_edited: 2022-11-03T16:59:42Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74273504/revisions
accepted: false
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 469d852250feff9a6c888f6d409c247c8a7b8bb1b6bc43ff1bd35a6d358e3d0e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74273504>, 2022-11-01, last edited 2022-11-03; score 1. Text as retrieved 2026-10-12.

I don't think the image link is anywhere on the page. Clicking the "hyperlink" takes you to a page where you can view hundreds of images one-by-one, but the link in the address bar is the same for all rows - the pages on this site all seem to be rendered after a series of requests and redirects, so a simple link will not suffice. Even a link like [https://apps.proni.gov.uk/Val12B/RelatedVolume.aspx?6139](https://apps.proni.gov.uk/Val12B/RelatedVolume.aspx?6139) will be redirected to the search page unless you click from one of their pages first [try opening in incognito mode from here and you might notice].

I think, at best, you can code to click on each link and get the image url of the first, index and last images (and a fixed number of extra images, if you want, but each image is an extra click, an extra set of requests...), and add a column for each image_url. Obviously that will be considerably slower than your current method because of having to click so many things, and probably the waits as well if they don't load immediately.

Skeleton code:
```python
prefVals = [
    e.get_attribute('value') for e in 
    driver.find_elements_by_xpath(".//table[@id='gvSearchResults']//td/input")
]
val_scraped = []
max_scrapes = len(table_elements) # or whatever you prefer

valImgs = []

for i in range(max_scrapes):
    prefs = [
        e for e in 
        driver.find_elements_by_xpath(".//table[@id='gvSearchResults']//td/input")
        if e.get_attribute('value') not in val_scraped
    ]
    if not prefs: break # all scraped

    val_i = prefs[0].get_attribute('value')
    prefs[0].click()
    # add wait if necessary

    first_image = driver.find_element_by_xpath('.//img[@id="ImgCtrlLarge"]').get_attribute('src')

    # click for more images if you want

    val_scraped.append(val_i)
    valImgs.append([val_i, first_image, ...]) # add all image links for val_i

    # use "< Search Results" button to go back
    driver.find_element_by_xpath('.//input[@id="backButton"]').click()
    # add wait if necessary

imgCols = [[r for r in valImgs if r[0] == v] for v in prefVals]
imgCols = [r[0] if len(r) > 0 else [] for r in imgCols]
imgCol_headers = ['PRONI_REFERENCE_VALUE', 'FIRST_IMAGE', ....] # add in headers as appropriate

imgDfs = pd.DataFrame(imgCols, columns=imgCol_headers)

finalDf = pd.concat([dfs[0], imgDfs], axis=1)

```
