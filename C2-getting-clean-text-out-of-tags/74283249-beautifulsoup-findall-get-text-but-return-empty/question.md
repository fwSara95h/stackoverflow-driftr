---
title: "BeautifulSoup findall get text but return empty"
site: stackoverflow
question_id: 74283249
url: https://stackoverflow.com/q/74283249
asked: 2022-11-02T00:44:53Z
asked_by: "user15410844"
asked_by_url: https://stackoverflow.com/users/15410844
last_edited: 2022-11-02T10:52:17Z
last_editor: "mkrieger1"
last_editor_url: https://stackoverflow.com/users/4621513
tags: [python, web-scraping, beautifulsoup]
score: 1
views_at_snapshot: 132
answer_count: 2
accepted_answer_id: 74283261
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 524d27451e28667c4168928ea6e99d288183868a9b1c19f6218e59ced8cb4d1c
---

# BeautifulSoup findall get text but return empty

Asked by [user15410844](https://stackoverflow.com/users/15410844) on Stack Overflow, <https://stackoverflow.com/q/74283249>, 2022-11-02, last edited 2022-11-02 by [mkrieger1](https://stackoverflow.com/users/4621513). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am scraping a website and would like to find specific content based on style, so I do

    soup.find_all('style')

[![enter image description here][1]][1]

and it does return some result/text, but once I use .text `soup_name.find_all('style')[0].text` to extract the text, it returns an empty string


[![enter image description here][2]][2]

 

What can I do to extract the text in the style tag?


  [1]: https://i.sstatic.net/g63J8.png
  [2]: https://i.sstatic.net/Ry43N.png
