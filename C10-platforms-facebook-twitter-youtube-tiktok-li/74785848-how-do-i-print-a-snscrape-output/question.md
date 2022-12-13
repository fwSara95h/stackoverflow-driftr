---
title: "How do I print a snscrape output"
site: stackoverflow
question_id: 74785848
url: https://stackoverflow.com/q/74785848
asked: 2022-12-13T13:46:19Z
asked_by: "Parakeet"
asked_by_url: https://stackoverflow.com/users/18787560
last_edited: 2022-12-13T17:00:17Z
last_editor: "Alexander L. Hayes"
last_editor_url: https://stackoverflow.com/users/12439119
tags: [python, web-scraping, twitter]
score: -1
views_at_snapshot: 200
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d21e56f8730f70453740bdf92ba5a6fafb80fe381f3b3674d4cae0611086558d
---

# How do I print a snscrape output

Asked by [Parakeet](https://stackoverflow.com/users/18787560) on Stack Overflow, <https://stackoverflow.com/q/74785848>, 2022-12-13, last edited 2022-12-13 by [Alexander L. Hayes](https://stackoverflow.com/users/12439119). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to print the output of scraping a twitter feed using snscrape.  It works on command line but I can't get it to print to file.
My code:

```python
import snscrape.modules.twitter as twitter
maxTweets = 10
keyword='salvation'
for i, tweet in enumerate(twitter.TwitterSearchScraper(keyword + ' since:2021-11-01 until:2023-01-01 lang:"en" ').get_items()):
    tweets = {
             "tweet.url" : tweet.url
            }   
    print(tweets)
```

It prints to the command line but when I try:

```python
with open('file.txt', 'w', encoding="utf-8") as f:
    print(tweets, file=f)
```

then it won't print and I get an error message:

`future warning username is deprecated, use user.username instead`
