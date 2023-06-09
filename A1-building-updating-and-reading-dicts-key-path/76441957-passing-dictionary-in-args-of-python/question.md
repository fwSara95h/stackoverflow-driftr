---
title: "Passing dictionary in args of python"
site: stackoverflow
question_id: 76441957
url: https://stackoverflow.com/q/76441957
asked: 2023-06-09T16:02:40Z
asked_by: "Devarshi Chatterjee"
asked_by_url: https://stackoverflow.com/users/8076639
last_edited: never
tags: [python-3.x, dictionary, arguments]
score: 0
views_at_snapshot: 51
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c4e5506acdc704b143a623654a2508f98ff377993c049fb16ae48769ca7ee60b
---

# Passing dictionary in args of python

Asked by [Devarshi Chatterjee](https://stackoverflow.com/users/8076639) on Stack Overflow, <https://stackoverflow.com/q/76441957>, 2023-06-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a function defined as following:-def abc(\*args):Blah blahI am calling the function as abc(dict\['1'\]\['2\],"111","1221")In the function abc I am trying to extract the dictionary name and keys associated with as the user passed. But on trying to do args\[0\] to extract it , the absolute value present at dict\['1'\]\['2'\] is getting printed .

Any idea on how to get the dictionary name and keys associated and not the absolute value

Thanks.

For eg :def abc(\*args):

" Need to extract name of dictionary and the key associated here and not the value of thisdict\["brand"\]\["color"\] "

thisdict = {"brand": {"color":"Red","model": "Mustang"},"manufactured": {"year":"1964","month":"Oct"}}

The function call is like this abc(thisdict\["brand"\]\["color"\],"111","222")

Thanks

An answer on how to solve the problem
