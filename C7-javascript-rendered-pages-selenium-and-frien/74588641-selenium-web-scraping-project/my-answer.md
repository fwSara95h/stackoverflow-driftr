---
title: "Selenium web scraping project"
site: stackoverflow
question_id: 74588641
answer_id: 74589557
url: https://stackoverflow.com/a/74589557
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-27T11:16:48Z
last_edited: 2022-11-27T11:25:04Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74589557/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7b5dca792aef6264842227068c9501f6ccf39a04f901408fab54df93fcaa7d63
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74589557>, 2022-11-27, last edited 2022-11-27; **accepted**; score 0. Text as retrieved 2026-10-12.

> But my soup is still showing the page with the "accept cookie", resulting in none of the class to be able to be found

But [the listings should show up even without closing cookies notice][1], and the part of your code to close the cookies notice looks fine anyway (maybe refreshing brings it back....?)

---

You might have noticed that at first the page looks like 
[![loading page][2]][2]

So, I think you need to give some time for the listings to load after refreshing. (About that, why are you refreshing? If you don't refresh, the 10sec wait should be enough time to load...)

```python
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

## [ BEFORE BeautifulSoup ] ##

maxWait = 10 # adjust as preferred
wait =  WebDriverWait(driver, maxWait)
wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'js-listing-item')))

## [ NOW YOU CAN PARSE WITH BeautifulSoup ] ##
```
that should force the program to wait until the listings are loaded.

---

Btw, *`.find_all('a', class_="new--listing-item js-listing-item")`* might not be the most reliable way to get `rooms`, since the `new--listing-item` class only shows up for wide screens; it might be better to use **`.find_all('a', {'class': 'js-listing-item'})`** or **`.select('a.js-listing-item')`** instead.

---

> <sub>rooms would return empty string</sub>

<sub>Are you sure? `find_all` is supposed to return a [`ResultSet`](https://tedboy.github.io/bs4_doc/generated/generated/bs4.ResultSet.html), which is closer to a list...</sub>

---

Also, [this isn't very essential, but] it's better that the identifiers passed to `find_element` are as unique as possible; there are at least 3 other elements with the `new--icon-cross` class  (even though close-cookies is the first, so that bit of your code should work anyway), but only the close-cookies button has the `js-cookie-close` class.


  [1]: https://i.sstatic.net/dDb9o.png
  [2]: https://i.sstatic.net/FjGb5.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-12-02): @explorevaluechain glad it helped! [btw I'm still v curious - why are you refreshing the page?]
