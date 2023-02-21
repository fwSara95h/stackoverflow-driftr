---
title: "Pandas - look up key and map dictionary to a column"
site: stackoverflow
question_id: 75515493
url: https://stackoverflow.com/q/75515493
asked: 2023-02-21T01:07:54Z
asked_by: "kms"
asked_by_url: https://stackoverflow.com/users/3380902
last_edited: never
tags: [python, pandas, dictionary]
score: -1
views_at_snapshot: 91
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dbe420fd3ba081eb993b5bacaf745f178e0cca282648d97a7cfe1bc451427e5d
---

# Pandas - look up key and map dictionary to a column

Asked by [kms](https://stackoverflow.com/users/3380902) on Stack Overflow, <https://stackoverflow.com/q/75515493>, 2023-02-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to `.map` a dictionary to a pandas DataFrame. One of the columns in pandas DataFrame is the key in dict. Here's a reproducible example, 

    import pandas as pd
    
    df = pd.DataFrame({
                       'id': [0, 1, 2],
                       'nm': ['pn1','pn2','pn3],
                       'v': [np.nan, 25, 0],
                       'd': [{'k1':'v1','k2':'v2','k3':'v3'}]
                     })
 
    dtd = { 
           'pn1':{'s':100,'v':20, sv:{['sv1': 500]}},
           'pn2':{'s':150,'v':30, sv:{['sv1': 400]}}
          }

I'd like to to look the `key` and parse the value `sv1` from the nested dictionary and assign it to pandas series `df.v`. 

Series would look like this:

    v
    500
    400
    0
