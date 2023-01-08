---
title: "Extracting the first mention from retweets in a python dataframe"
site: stackoverflow
question_id: 75045613
url: https://stackoverflow.com/q/75045613
asked: 2023-01-08T05:08:16Z
asked_by: "Saríah"
asked_by_url: https://stackoverflow.com/users/19833088
last_edited: never
tags: [python, pandas, dataframe]
score: 0
views_at_snapshot: 75
answer_count: 2
accepted_answer_id: 75045644
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bc79228dc9e0244a94826985da26c825799f64731333435830b23d59f0306934
---

# Extracting the first mention from retweets in a python dataframe

Asked by [Saríah](https://stackoverflow.com/users/19833088) on Stack Overflow, <https://stackoverflow.com/q/75045613>, 2023-01-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

My df looks like this:

```
record = { 
 'text_con_RT_t' : ['RT @Blanc_: ramdon text #hashtag quiere ', '@GonM ramdon text', 'RT @IvEc: @GonzM ramdon text', 'hOLA ramdon text ' ], 
 'rt' : ['RT', '' , 'RT','' ]
}
    
# create a dataframe 
dataframe2 = pd.DataFrame(record,
                         columns = ['text_con_RT_t', 'rt']) 
```

I would like to get something like this:


| text_con_RT_t| rt |usr_rt |
| -------- | -------- |-------- |
| RT @Blanc_: ramdon text #hashtag quiere   | RT |blanc  |
| @GonM ramdon text  |    |   |
| RT @IvEc: @GonzM ramdon text | RT  | ivec |
| hOLA ramdon text  |    |   |



But i havent succeded, in cases where there is starts with mention, but not retweet, my results looks like this:

| text_con_RT_t| rt |usr_rt |
| -------- | -------- |-------- |
| RT @Blanc_: ramdon text #hashtag quiere   | RT |blanc  |
| @GonM ramdon text  |    | gonm ramdon text  |
| RT @IvEc: @GonzM ramdon text | RT  | ivec |
| hOLA ramdon text  |    | NaN  |



I have tried with this:


```
try:
   dataframe2["usr_rt"] = dataframe2.text_con_RT_t.str.lower().str.split(':').str[0].str.split('@').str[1]
except dataframe2["rt"]==None: # complicated failed
   dataframe2["usr_rt"] = ""
```

Also with this


```
if dataframe2["rt"] == "RT":
  return (dataframe2["usr_rt"] == dataframe2.text_con_RT_t.str.split(':').str[0].str.split('@').str[1])
```

What am I missing? thanks
