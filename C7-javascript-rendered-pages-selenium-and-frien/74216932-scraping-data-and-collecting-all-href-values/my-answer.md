---
title: "scraping data and collecting all href values"
site: stackoverflow
question_id: 74216932
answer_id: 74217161
url: https://stackoverflow.com/a/74217161
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-27T05:25:02Z
last_edited: 2022-10-28T00:17:57Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74217161/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [linkToSoup, linkToSoup_selenium]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bb2ffbd5d5ccfd93a0787a92e1b618dba06eb9c6aa10ccc043862a5855188ba5
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74217161>, 2022-10-27, last edited 2022-10-28; **accepted**; score 1. Text as retrieved 2026-10-12.

I expect you're getting the **403 Forbidden** error -  the site probably has some very good blockers, I made a quick attempt with ScrapingAnt and then tried copying the entire request for my browser, but both were blocked.

If you're open to trying selenium, I have [this function](https://gist.github.com/Driftr95/cbae6710c134df708f44ade8503f6638) for cases like this - you can paste it to your code and then just call it
```python
soup = linkToSoup_selenium('https://opensea.io/rankings?sortBy=total_volume')
values = soup.find_all(
            lambda l: l.name == 'a' and
            l.get('href') is not None and
            '/collection/' in l.get('href')
        )
# OR
# values = [a for a in soup.select('a') if a.get('href') and '/collection/' in a.get('href')]
```

<hr><hr>

**EDIT:**
To get ALL the collections:

```python
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import json

driver = webdriver.Chrome('chromedriver.exe')
url = f'https://opensea.io/rankings?sortBy=total_volume'
driver.get(url)
driver.maximize_window()
scrollCt = 0
rows = []

maxScrols = 1000  # adjust as preferred
while scrollCt < maxScrols:
    time.sleep(0.3)  # adjust as necessary - I seem to need  >0.25s
    aro = driver.find_elements_by_css_selector(
        'a[role="row"][overflow="hidden"][href*="/collection/"]')
    aro = [(
        a.get_attribute('href'),
        a.find_element_by_xpath('../..')  # parent's parent
    ) for a in aro]

    aroFil = [a for a in aro if a[0] not in [h['link'] for h in rows]]
    aroFil = [{   
        'outerHTML': [a[1].get_attribute('outerHTML')], # for BeatifulSoup
        'innerText': a[1].get_attribute('innerText').strip(),
        'link': a[0]
    } for a in aroFil]
    rows += aroFil

    print(f'[{scrollCt}] found {len(aro)}, filtered down to {len(aroFil)} rows [at {len(rows)} total]')
    if aroFil == []:
        # break # if you don't want to go to next page
        try:
            driver.find_element_by_xpath('//i[@value="arrow_forward_ios"]/..').click()
        except Exception as e:
            print('failed to go to next page', str(e))
            break

    scrollCt += 1
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)


# if you want to extract more with BeautifulSoup
for i, r in enumerate(rows):
    rSoup = BeautifulSoup(r['outerHTML'][0].encode('utf-8'), 'html5lib')

    rows[i]['bs4Text'] = rSoup.get_text(strip=True)
    ###### EXTRACT INFO AS NEEDED ######

    del rows[i]['html']  # if you don't need it anymore

# with open('x.json', 'w') as f: json.dump(rows, f, indent=4) # save json file 

driver.quit()
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[PutsandCalls](https://stackoverflow.com/users/5801127)** (2022-10-27): oh well that worked like a charm ! but for some reason, it only gave the top 38 items as opposed to all of it. Do you know how i can get all of the 100 items ?   I supposed it would be because we have to manually scroll down or something ?
- **me** (2022-10-27): @PutsandCalls wow. this is a *very* dynamic page apparently. I don't think my function will suffice for getting all 100 items; you'll probably have to write custom code - even scrolling to the bottom of the page isn't enough, because when you scroll down, *some of the top elements **get removed*** as newer element are added at the bottom...you might have to scroll down by your screen height and collect data after every scroll (and then filter down to uniques because there will probably be overlap)
- **[PutsandCalls](https://stackoverflow.com/users/5801127)** (2022-10-27): really appreciate the help ! but yeah, this page is definitely one of the harder sites i have seen
- **me** (2022-10-28): @PutsandCalls you probably don't need it anymore, but I've added an edit with code for getting all the items [I decided I need to practice scrolling with selenium, but then gave up because I couldn't figure out how to find the coordinates of the bottom item 😅 - frustratingly, it's *not* always (or ever, apparently) the last item - but a simple `body.send_keys(Keys.PAGE_DOWN)` seems to work well enough so...]
- **[PutsandCalls](https://stackoverflow.com/users/5801127)** (2022-10-29): this actually worked really well, definitely helped a ton ! thanks a lot
