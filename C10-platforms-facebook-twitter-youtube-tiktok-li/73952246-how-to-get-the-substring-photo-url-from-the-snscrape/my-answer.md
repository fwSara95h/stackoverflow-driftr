---
title: "How to get the substring (photo url) from the snscrape?"
site: stackoverflow
question_id: 73952246
answer_id: 73953386
url: https://stackoverflow.com/a/73953386
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-04T20:35:47Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73953386/revisions
accepted: false
score: 1
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: db96eaa18dc19e7d363fd5cd03ca9bc49e905d87e6d0f9c81679be6c87944252
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73953386>, 2022-10-04; score 1. Text as retrieved 2026-10-12.

you can change your `for` loop to:

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('sex for grades since:2021-07-05 until:2022-07-06').get_items()):
        if i>150:
            break
        try:
          tweetMedia = tweet.media[0].fullUrl # .previewUrl if you want previewUrl
        except:
          tweetMedia = tweet.media # or None or '' or any default value 
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content, tweetMedia])

and then you'll have the urls [if there are any] for each tweet row.

If you want it all inside the `append` statement, you can just change that to:

    attributes_container.append([
        tweet.user.username, tweet.date, tweet.likeCount, 
        tweet.sourceLabel, tweet.content, 
            (tweet.media[0].fullUrl if tweet.media 
            and hasattr(tweet.media[0], 'fullUrl')
            else tweet.media)
    ])
[instead of adding the `try...except`]
