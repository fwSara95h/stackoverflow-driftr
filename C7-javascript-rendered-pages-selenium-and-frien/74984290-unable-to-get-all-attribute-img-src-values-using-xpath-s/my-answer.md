---
title: "Unable to get all attribute(img @src) values using xpath selenium python"
site: stackoverflow
question_id: 74984290
answer_id: 74988832
url: https://stackoverflow.com/a/74988832
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-03T03:35:06Z
last_edited: 2023-01-03T03:54:23Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74988832/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a33fd380ba444a5678ce013b9e307b22801b4849e45d63a29c650ab01deabbfe
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74988832>, 2023-01-03, last edited 2023-01-03; score 0. Text as retrieved 2026-10-12.

You should consider doing something like 

```python
xpBanners = '//div[contains(@id,"dismissible")]/ytd-thumbnail/a'
## WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpBanners)))
## scroll to load all Banners (will explain below)

Banners_imgs = driver.find_elements_by_xpath(f'{xpBanners}//img')
Banners_src = [b.get_attribute('src') for b in Banners_imgs]
```

instead of 

> ```python 
> Banners_src = [] 
> for element in Banners:
>     Banners_src.append(element.find_element_by_xpath('.//img').get_attribute('src'))
> ```

because `element.find_element...` behaves unexpectedly sometimes [see [this](https://stackoverflow.com/a/74631249/6146136) and [this](https://stackoverflow.com/a/74777214/6146136) for example].

---

On my browser, I start with just 30 `//div[contains(@id,"dismissible")]/ytd-thumbnail/a` and have to scroll to the bottom to load the next 30. Normally, I'd suggest that you either scroll to the last element using

```python
# import time
scrollCt = 10 # 5 should be enough, but just in case...
scrollWait = 2 # in seconds - adjust according to loading speed
xpBanner = '//div[contains(@id,"dismissible")]/ytd-thumbnail/a'

## wait to load... as necessary
for x in range(scrollCt):
    lastBanner = driver.find_elements_by_xpath(xpBanner)[-1]
    driver.execute_script('arguments[0].scrollIntoView(false);', lastBanner)
    time.sleep(scrollWait)
```

or scroll to the bottom of the page with

```python 
for x in range(scrollCt):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(scrollWait)    
```

**But neither of those seem to work with YouTube pages...** So instead, you could try to scrolling bit by bit with **`PGDN`** .

```python
# import time
# from selenium.webdriver.common.keys import Keys

pgCt = 10 # adjust according to your browser (mine needs 7 - used 10 just in case)
scrollCt = 10 # 5 should be enough, but just in case...
scrollWait = 2 # in seconds - adjust according to loading speed

for x in range(scrollCt):
    driverD.find_element(By.XPATH, '//body').send_keys(Keys.PAGE_DOWN)
    if x%pgCt == 0: time.sleep(scrollWait)
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Siva Ranjjan](https://stackoverflow.com/users/18726958)** (2023-01-04): Thanks for your suggestion. xpBanners size  50 Banners_images size 171  123 values out of 171 extracted. This is what I get as per ur suggestion. Still unable to get all 171 values. In the beginning of the script itself I scroll to end of the page then i collect the xpath values.
- **me** (2023-01-04): @SivaRanjjan I got 171 with both manual and `Keys.PAGE_DOWN` scrolling....how many times did you scroll to the bottom? Did you wait to see if more thumbnails loaded? Like I said each time you scroll to the bottom a few more loads and then you have to scroll to the bottom again....although 123 is a strange number.  Btw, did you check in the inspect tab **of the selenium-driven window** how many `//div[contains(@id,"dismissible")]/ytd-thumbnail/a//img` there were? Did the page look different from when manually browsing?
