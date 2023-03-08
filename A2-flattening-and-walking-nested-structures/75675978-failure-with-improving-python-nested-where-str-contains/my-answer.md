---
title: "Failure with improving Python nested where(str.contains)"
site: stackoverflow
question_id: 75675978
answer_id: 75677851
url: https://stackoverflow.com/a/75677851
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-08T20:19:09Z
last_edited: 2023-04-04T01:41:04Z
revisions: 3
revision_history: https://stackoverflow.com/posts/75677851/revisions
accepted: false
score: 0
chapter: A2
chapter_title: "Flattening and walking nested structures"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4701358aaeea7f90e1af083ec0b17588bb3e24a519a3999eb3eb61a0492b4c43
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75677851>, 2023-03-08, last edited 2023-04-04; score 0. Text as retrieved 2026-10-12.

You could define a function instead of a `lambda` expression

```py
term_map = {
    'FLOORS': ('FLOOR', 'FLR', 'TF', 'FT'),
    'WALLS': ('WALL', 'WL', 'TW'),
    'CARPET': ('CAR', 'CPT'),
    'KITCHEN BACKSPLASH': ('KBS', 'BACKSPLASH'),
    'FIREPLACE': ('FIRE', 'FP', 'FRP'),
    'WOOD': ('WOOD', 'WD'),
    'VINYL': ('VINYL', 'LVP', 'VP'),
    'PREWALK': ('PREWALK', 'PW'),
    'TILE': ('TILE',),
    'FINE TUNE': ('FINE', 'F/T')
}

def get_kw(fullStr, ref_map=term_map):
    if fullStr in ref_map or not isinstance(fullStr, str): return fullStr
    for kw, lk in ref_map.items():
        # if re.match('|'.join(lk), fullStr): return fullStr
        for k in lk:
            if k in fullStr: return kw
    return fullStr

df['Job Type'] = df['Job Type'].apply(get_kw)
```

---

#### ADDED EDIT:

In retrospect, it might be better to just flatten the dictionary and use [`.str.extract`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html) and [`.map`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html) instead of using `.apply` with a function with a nested loop:

```py
# term_map = ... ## [ same as above ]
term_map_inv = {k: kw for kw, lk in term_map.items() for k in lk}

df['Job Type'] = df['Job Type'].str.extract(
    f'({"|".join(term_map_inv)})', expand=False
).map(term_map_inv).fillna(df['Job Type'])
```

or you could `.apply` the following version of `get_kw` that uses regex:

```py
def get_kw(fullStr, ref_map=term_map_inv, reg_pat = '|'.join(term_map_inv)):
    if isinstance(fullStr, str): 
        if (rsearch:=re.search(reg_pat, fullStr)): 
            return term_map_inv.get(rsearch.group(0), fullStr)
    return fullStr
```

[They seem to take about the same amount of time.]

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[James Ogle](https://stackoverflow.com/users/9381740)** (2023-04-03): Thanks for the help and the suggestion.  Finally got back to cleaning this up.  Your code resulted in an error, "type 'float' is not iterable for if k in fullStr: return kw"  However I was able to fix that by inserting an if instance(fullStr, str) statement at the start of the function.  Now that it is running that brings up another question.  This is slightly slower than the original nested wheres using str functions.  Is that because it is creating a function and the dataset is is somewhat small so efficiency will improve with a larger dataset or are str functions just more effecient?
- **me** (2023-04-04): @JamesOgle I've edited the string check into my answer; as for the timing, while `.apply` might seem to be a bit slower in general than most other Series methods (since it's calling an external function), I think the main issue is the nested loop inside `get_kw`. Regex seems to be faster, so I've suggested another method using it above
