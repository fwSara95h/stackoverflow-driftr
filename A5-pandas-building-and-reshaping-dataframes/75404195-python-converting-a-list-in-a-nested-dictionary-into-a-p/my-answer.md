---
title: "Python converting a list in a nested dictionary into a Pandas Dataframe"
site: stackoverflow
question_id: 75404195
answer_id: 75404500
url: https://stackoverflow.com/a/75404500
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-09T21:19:04Z
last_edited: 2023-02-10T19:07:46Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75404500/revisions
accepted: true
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0); the revisions listed under edited_by_others are those users' work under CC BY-SA 4.0
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 72dbd62933fa2e5e9a1243d1fe67c4752c0d435ce22898adfbec78f62ff8407c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
edited_by_others:
  - "wjandrea (https://stackoverflow.com/users/4518341), revision 2, 2023-02-10, CC BY-SA 4.0 — Fix/improve formatting. Wrap long lines for readability, which requires rearranging some code."
---

# My answer — 2023-02-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75404500>, 2023-02-09, last edited 2023-02-10; **accepted**; score 1. Text as retrieved 2026-10-12. Later revisions by other users are listed in the front matter.

You could use something like this function:

```python
# import pandas as pd

def tabulate_actions(actionsList:list, returnDf=False):
    aTbl = [{
        a['action_type']: a['value'] for a in al['actions']
        # if isinstance(a, dict) and all([k in a for k in ['action_type', 'value']])
    } for al in actionsList
    # if isinstance(al, dict) and isinstance(al.get('actions'), list)
    ]
    return pd.DataFrame(aTbl) if returnDf else aTbl
## uncomment the conditions if you're unsure of your data structure
```

`tabulate_actions(test['data'])` should return this list of dictionaries:

> ```python
> [{'link_click': '16',
>   'post_engagement': '16',
>   'page_engagement': '16'},
>  {'comment': '5',
>   'onsite_conversion.post_save': '1',
>   'link_click': '465',
>   'post': '1',
>   'post_reaction': '20',
>   'video_view': '4462',
>   'post_engagement': '4954',
>   'page_engagement': '4954'}]
> ```

and passing `returnDf=True` should make it return a DataFrame:

[![opdf][1]][1]


  [1]: https://i.sstatic.net/Mvy4M.png
