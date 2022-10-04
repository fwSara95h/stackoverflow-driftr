---
title: "How to get the substring (photo url) from the snscrape?"
site: stackoverflow
question_id: 73952246
url: https://stackoverflow.com/q/73952246
asked: 2022-10-04T18:38:14Z
asked_by: "hard worker"
asked_by_url: https://stackoverflow.com/users/13771254
last_edited: 2022-10-04T20:10:22Z
tags: [python, web-scraping]
score: 0
views_at_snapshot: 638
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f6c553b8bebe36ac6a24fd43702fa2f82c761ae0a15a99351dc1be6cfbf1ce0a
---

# How to get the substring (photo url) from the snscrape?

Asked by [hard worker](https://stackoverflow.com/users/13771254) on Stack Overflow, <https://stackoverflow.com/q/73952246>, 2022-10-04, last edited 2022-10-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Edit, since I realize it also has the vedio url,
My question is how can I only get the photo url in the following loop?
I want to add a attribute called photourl which is the full url from the media.


```
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('sex for grades since:2021-07-05 until:2022-07-06').get_items()):
    if i>150:
        break
    attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content, tweet.media])
    
# Creating a dataframe to load the list
tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet","media"])

```





When I used the snscrape to scrape tweet from the twitter,
I want to filter the photo image from the photo graph. I get the media object like the following:

```
media=[Photo(previewUrl='https://pbs.twimg.com/media/FePrYL7WQAQDKEB?format=jpg, fullUrl='https://pbs.twimg.com/media/FePrYL7WQAQDKEB?format=jpg&name=large')]

```

So How can I just get the PreviewUrl'https://pbs.twimg.com/media/FePrYL7WQAQDKEB?format=jpg, and full url sperately',

use the python code?


Thanks

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-10-04): Did you miss a `'` at the end of the `previewUrl` value? Anyway, you can try `pUrl = media[0].previewUrl` and see if that gets you what you want
- **[hard worker](https://stackoverflow.com/users/13771254)** (2022-10-04): I have one more question, since I realize in the media column it not only has the photo url. It also has the media url, and blank. I just want to get the photo url in the loop. please see my edited post for the new code.
