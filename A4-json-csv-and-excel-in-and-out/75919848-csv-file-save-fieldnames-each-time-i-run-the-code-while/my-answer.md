---
title: "CSV file save fieldnames each time I run the code while converting dictionary to CSV"
site: stackoverflow
question_id: 75919848
answer_id: 75920474
url: https://stackoverflow.com/a/75920474
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-03T14:18:13Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75920474/revisions
accepted: true
score: 0
chapter: A4
chapter_title: "JSON, CSV and Excel in and out"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f83f4bc4bb00067df74dfb4583134ae0b7b90a42564bbbbfa70eeb2e6abb1a81
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75920474>, 2023-04-03; **accepted**; score 0. Text as retrieved 2026-10-12.

Only add header if file doesn't exist - one way to check is with [`os.path.isfile`](https://docs.python.org/3/library/os.path.html#os.path.isfile)

```py
# import os

def is_known():
    input_fp = "data/data_known.csv"
    is_new_file = not os.path.isfile(input_fp)
    with open(input_fp, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=current_card.keys())
            if is_new_file: 
                writer.writeheader()
                is_new_file = False ## update flag in case this is in a loop
            writer.writerow(current_card)
```
