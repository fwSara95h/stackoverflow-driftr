---
title: "Pull data from a json and create an excel file with the data"
site: stackoverflow
question_id: 75805680
answer_id: 75807943
url: https://stackoverflow.com/a/75807943
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-22T02:21:42Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75807943/revisions
accepted: false
score: 0
chapter: A4
chapter_title: "JSON, CSV and Excel in and out"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7c714e31db7ca4b740761b4c1356f373aeeb8d97cb0353ceb6cf876922ff6ebb
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-22

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75807943>, 2023-03-22; score 0. Text as retrieved 2026-10-12.

From [comment](https://stackoverflow.com/questions/75805680/solved-trying-to-pull-data-from-a-json-and-create-an-excel-file-with-the-data#comment133720825_75805680) by [It_is_Chris](https://stackoverflow.com/users/9177877/it-is-chris)
> Based on the sample data, it is probably easiest to pull everything: 
> 
> ```py
> df = pd.json_normalize(data, 'healthRuleMembers') 
> ```
>
> and then just keep the columns you want -- 
> ```py
> df[['model.id', 'model.name', 'model.scheduleName', ... ]].to_excel('test_file.xlsx', index=False)
> ```
