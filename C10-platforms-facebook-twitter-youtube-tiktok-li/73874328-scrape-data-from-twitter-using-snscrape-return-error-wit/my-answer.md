---
title: "Scrape Data from Twitter using Snscrape, return error with Tweet object has no attribute 'likeCount'"
site: stackoverflow
question_id: 73874328
answer_id: 73888211
url: https://stackoverflow.com/a/73888211
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-28T21:54:52Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73888211/revisions
accepted: true
score: 1
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 61b4bff1c923fba528c04c894440cc13a572b4357eba55c4f4321ef3ace60a0d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73888211>, 2022-09-28; **accepted**; score 1. Text as retrieved 2026-10-12.

You need to install the [developer version of snscrape][1] to get attributes like `likeCount`. You can either try to install the developer version and run your code again; or if you're ok with only what your current version gives you, you can try:

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('sex for grades since:2021-07-05 until:2022-07-06').get_items()):
        if i>150:
            break
        
        attributes_container.append(
            dict(
                (name, getattr(tweet, name)) for name in dir(tweet) 
                if not name.startswith('_') and name not in ['count','index']
            ) 
        )
        
    tweets_df = pd.DataFrame(attributes_container)
and then `tweets_df.columns` gives me the output:

    Index(['content', 'date', 'id', 'outlinks', 'outlinksss', 'tcooutlinks',
           'tcooutlinksss', 'url', 'username'],
          dtype='object')
and these are the only data I can access with my version of snscrape. [You *might* get something different.]

  [1]: https://github.com/JustAnotherArchivist/snscrape#installation
