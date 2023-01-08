---
title: "Extracting the first mention from retweets in a python dataframe"
site: stackoverflow
question_id: 75045613
answer_id: 75045740
url: https://stackoverflow.com/a/75045740
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-08T05:42:05Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75045740/revisions
accepted: false
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7f297312c64e69599c326ea23c779d10c44fe182fe07c1cc5fa8d4972fe0c1fa
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75045740>, 2023-01-08; score 1. Text as retrieved 2026-10-12.

I would [personally] find it easier to create values for the new column from `record`. If you added it into `record`, you wouldn't need to change the DataFrame after (which I prefer since I'm not great with `numpy`, so I would just end up extracting the column as list an doing what I've done below anyway).

```python
# allowedChars = '' # '+-.' # add allowed characters
record['usr_rt'] = ['' if not rt == 'RT' else ''.join(
    c for c in txt.split('@', 1)[-1].split(':')[0].lower() 
    if c.isalpha() or c.isdigit() # or c in allowedChars
) for txt, rt in zip(record['text_con_RT_t'], record['rt'])]
```

`if c.isalpha()` allows only characters from the alphabet to remain; remove `or c.isdigit()` if you want to get rid of any numeric character from username as well, and make use of `allowedChars` and *`or c in allowedChars`* if you want to allow some special characters (that includes spaces btw, though I don't think usernames have any). 

Anyways, now `pd.DataFrame(record)` would return a DataFrame that looks like

| text_con_RT_t                           | rt   | usr_rt   |
|:----------------------------------------|:-----|:---------|
| RT @Blanc_: ramdon text #hashtag quiere | RT   | blanc    |
| @GonM ramdon text                       |      |          |
| RT @IvEc: @GonzM ramdon text            | RT   | ivec     |
| hOLA ramdon text                        |      |          |
