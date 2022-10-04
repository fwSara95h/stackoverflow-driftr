---
title: "Elements able to be found using XPATH but not using CSS Selector. Am I searching using the correct value?"
site: stackoverflow
question_id: 73942961
answer_id: 73943396
url: https://stackoverflow.com/a/73943396
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-04T05:18:51Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73943396/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 657c5ad5b22253baab6419cd287dfa70a6e4c38024a027ac7806736d23a50c80
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73943396>, 2022-10-04; score 0. Text as retrieved 2026-10-12.

I believe the XPath for these list items would be `//li[@class="Card___StyledLi4-ulg8ho-7 jmevwM"]` (or `//*[@class="Card___StyledLi4-ulg8ho-7 jmevwM"]` if you want all elements with that class rather than just `li` tags). You can take a look at [this cheatsheet](https://devhints.io/xpath) and [this tutorial](https://www.guru99.com/xpath-selenium.html) for further rules and examples of XPath.

You can also just [use CSS Selectors](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements-by-css-selectors) like `(By.CSS_SELECTOR, '.Card___StyledLi4-ulg8ho-7.jmevwM')` in this case.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Xaldin](https://stackoverflow.com/users/20154862)** (2022-10-04): Thank you so much!! I forgot the first “.” in my code! Also bigger thank you for the cheat sheet!
