---
title: "Scraping nested items with Selenium and Python"
site: stackoverflow
question_id: 74192587
answer_id: 74197108
url: https://stackoverflow.com/a/74197108
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-25T16:10:19Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74197108/revisions
accepted: false
score: 0
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 863302381c0d61b3158801ef52ebe00f23638ff457b10e1cabb6142f337d98ad
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74197108>, 2022-10-25; score 0. Text as retrieved 2026-10-12.

You just need to target the part of the class that does not change - the `CommentContent`, and `CommentText` parts.

In bs4, `select` with [css selectors](https://www.w3schools.com/cssref/css_selectors.php) is great for targeting nested tags, or tags by partial attributes:
```python
containers = soup.select('div[class*="CommentContent"]') # comment content
commentItems = soup.select('div[class*="CommentItem"]') # outermost comment containers
commentTexts = soup.select('div[class*="CommentContent"] p[class*="CommentText"]') # same as find_all('p',{'data-e2e':'comment-level-1'})
commenterNames = soup.select('div[class*="CommentContent"] span[class*="UserName"]') # usernames of commenters
```

The same elements can be targeted with selenium and [xpath](https://devhints.io/xpath)
```python
containers = browser.find_element_by_xpath('//div[contains(@class, "CommentContent")]')  
commentItems = browser.find_element_by_xpath('//div[contains(@class, "CommentItem")]') 
commentTexts = browser.find_element_by_xpath('//div[contains(@class, "CommentContent")]//p[contains(@class, "CommentText")]') 
commenterNames = browser.find_element_by_xpath('//div[contains(@class, "CommentContent")]//span[contains(@class, "UserName")]')
```
