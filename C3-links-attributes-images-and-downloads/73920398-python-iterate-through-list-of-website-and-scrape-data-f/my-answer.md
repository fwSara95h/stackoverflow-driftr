---
title: "Python - Iterate through list of website and scrape data - failing at requests.get"
site: stackoverflow
question_id: 73920398
answer_id: 73929247
url: https://stackoverflow.com/a/73929247
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-02T20:48:20Z
last_edited: 2022-10-02T21:03:47Z
revisions: 2
revision_history: https://stackoverflow.com/posts/73929247/revisions
accepted: true
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 977cf8ee45b9bb4642269905f8d8445ed56d4b1e39cf6d345ad49aae49a87b86
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73929247>, 2022-10-02, last edited 2022-10-02; **accepted**; score 0. Text as retrieved 2026-10-12.

You need to set a *single* valid url. Changing your `for` loop to

    # from bs4 import BeautifulSoup 
    for website in df_actionname['Weblink']:
      detailpage = requests.get(website)
      pageSoup = BeautifulSoup(detailpage.content, 'html.parser')
      print(f'scraped "{pageSoup.title.text}" from {website}')
gives me the output 

    scraped "TruffleHog OSS · Actions · GitHub Marketplace · GitHub" from https://github.com/marketplace/actions/TruffleHog-OSS
    scraped "Metrics embed · Actions · GitHub Marketplace · GitHub" from https://github.com/marketplace/actions/Metrics-embed
    scraped "Super-Linter · Actions · GitHub Marketplace · GitHub" from https://github.com/marketplace/actions/Super-Linter

The way you were doing it, not only was your code basically trying to repeatedly sending the same GET request every loop (since `URL` was not dependent on `website` at all), the input of `requests.get` was not a single url, as you can see if you add a `print` before the request:
[![screenshot][1]][1]


  [1]: https://i.sstatic.net/5kJEZ.jpg
