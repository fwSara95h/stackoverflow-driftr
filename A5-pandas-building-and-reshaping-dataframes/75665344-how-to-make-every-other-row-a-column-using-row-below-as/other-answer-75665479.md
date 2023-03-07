---
title: "How to make every other row a column using row below as the value in Pandas?"
site: stackoverflow
question_id: 75665344
answer_id: 75665479
url: https://stackoverflow.com/a/75665479
author: "Shubham Sharma"
author_url: https://stackoverflow.com/users/12833166
posted: 2023-03-07T17:42:12Z
last_edited: never
accepted: true
score: 3
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5ed8082a1e47169ac2e93f533df5f94d4093535d86a08ac8ac751c7cdb8b03a3
role: another answer on the same question, kept as context; not my work
---

# Answer by [Shubham Sharma](https://stackoverflow.com/users/12833166) — 2023-03-07

Posted on Stack Overflow, <https://stackoverflow.com/a/75665479>, 2023-03-07; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

### Code

    # check if value is the header/column name
    m = df['type'].str.endswith('Product')

    # mask and forward fill to associate
    # column name with each value below it
    df['cols'] = df['type'].mask(~m).ffill()
    
    # pivot to reshape to wide format
    result = df[~m].pivot(index='id', columns='cols', values='type')


### Result

    cols  First Product Second Product
    id                                
    cust1         chair          table
    cust2         chair           desk
