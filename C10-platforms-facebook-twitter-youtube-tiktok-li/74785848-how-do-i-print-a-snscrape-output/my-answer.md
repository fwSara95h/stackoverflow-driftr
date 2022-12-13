---
title: "How do I print a snscrape output"
site: stackoverflow
question_id: 74785848
answer_id: 74788681
url: https://stackoverflow.com/a/74788681
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-13T17:24:15Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74788681/revisions
accepted: false
score: 0
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7be6d849162d530471e476b32df9ca54a1d998d79110dc20757100cde5ee34a7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74788681>, 2022-12-13; score 0. Text as retrieved 2026-10-12.

**Note:** printing after you `open` the file with `mode='w'` [in write-mode] means the file will be over-written with every print and only the last print will show up. If you want all the `tweets` objects preserved, you should be appending instead, **inside** the loop [because if you print outside the loop, again only the last will be saved as `tweets` is also over-written every loop]:

```python
# for i, tweet in...
    # tweets = ....
    with open('file.txt', 'a', encoding="utf-8") as f:
        print(tweets, file=f)
```

---

This doesn't make any sense - that's a *warning* message, not an error message, and it shouldn't halt or break your program; and also, that warning shouldn't appear **unless you have something like `tweet.username` somewhere in you code** [and if you do, then you should probably replace it with `tweet.user.username` as the warning instructs].

I am unable to reproduce the error, and how you print shouldn't really have anything to do with triggering the message, but if that's really the **only** difference between when the message appears and when it doesn't, then you can try some other method to save it to the file, like collecting all the tweets into a list [in the loop] and then [after the loops] converting that list to multi-line string to write to the file:

```python
import snscrape.modules.twitter as twitter
maxTweets = 10
keyword='salvation'
timeStr = 'since:2021-11-01 until:2023-01-01 lang:"en" '
twGen = twitter.TwitterSearchScraper(f'{keyword} {timeStr} ').get_items() 

allTweets = []
for i, tweet in enumerate(twGen):
    if i > maxTweets: break

    tweets = {
             "tweet.url" : tweet.url
            }   
    allTweets.append(tweets)

## [OUTSIDE loop]
with open('file.txt', 'w', encoding="utf-8") as f:
    f.write('\n'.join[str(t) for t in allTweets])
```
