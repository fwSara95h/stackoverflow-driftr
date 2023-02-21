---
title: "Pandas - look up key and map dictionary to a column"
site: stackoverflow
question_id: 75515493
answer_id: 75515754
url: https://stackoverflow.com/a/75515754
author: "Zach Flanders"
author_url: https://stackoverflow.com/users/3669465
posted: 2023-02-21T02:18:59Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fb335171d19658ea768647ccbdf907826f5cc0bcce4ef631d89534cd7bcd53bd
role: another answer on the same question, kept as context; not my work
---

# Answer by [Zach Flanders](https://stackoverflow.com/users/3669465) — 2023-02-21

Posted on Stack Overflow, <https://stackoverflow.com/a/75515754>, 2023-02-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I made a few changes to your code to make it executable.  Try this and see if it works:
```
import pandas as pd
import numpy as np

df = pd.DataFrame({
   'id': [0, 1, 2],
   'nm': ['pn1','pn2','pn3'],
   'v': [np.nan, 25, 0],
   'd': [{'k1':'v1'},{'k2':'v2'},{'k3':'v3'}]
})

dtd = { 
   'pn1':{'s':100,'v':20, 'sv':{'sv1': 500}},
   'pn2':{'s':150,'v':30, 'sv':{'sv1': 400}}
  }

df['v'] = (
    df['nm']
    .apply(lambda x: dtd[x]['sv']['sv1'] if x in dtd else np.nan)
    .combine_first(df['v'])
)
```

output:
```
   id   nm      v             d
0   0  pn1  500.0  {'k1': 'v1'}
1   1  pn2  400.0  {'k2': 'v2'}
2   2  pn3    0.0  {'k3': 'v3'}
```

I am using the 'nm' column as the key to look up the value in 'dtd'.  If there is no value, then I am leaving the existing value in `v`.
