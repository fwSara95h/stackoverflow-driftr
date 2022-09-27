---
title: "Scrape Data from Twitter using Snscrape, return error with Tweet object has no attribute 'likeCount'"
site: stackoverflow
question_id: 73874328
url: https://stackoverflow.com/q/73874328
asked: 2022-09-27T22:22:04Z
asked_by: "hard worker"
asked_by_url: https://stackoverflow.com/users/13771254
last_edited: never
tags: [python, web-scraping, twitter]
score: 0
views_at_snapshot: 1964
answer_count: 1
accepted_answer_id: 73888211
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9855b868c647f3ce7849c1d5a713bf6b98cfcd9d7323b3981b684111dfb5dcde
---

# Scrape Data from Twitter using Snscrape, return error with Tweet object has no attribute 'likeCount'

Asked by [hard worker](https://stackoverflow.com/users/13771254) on Stack Overflow, <https://stackoverflow.com/q/73874328>, 2022-09-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Follow the code
```
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('sex for grades since:2021-07-05 until:2022-07-06').get_items()):
    if i>150:
        break
    attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
# Creating a dataframe to load the list
tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])

```


but it returned the error with:
AttributeError: 'Tweet' object has no attribute 'likeCount'.


Did anyone know why it happen?

Thanks.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-09-28): this version of snscrape doesn't return `likeCount` - see [this issue](https://github.com/JustAnotherArchivist/snscrape/issues/158) on github
