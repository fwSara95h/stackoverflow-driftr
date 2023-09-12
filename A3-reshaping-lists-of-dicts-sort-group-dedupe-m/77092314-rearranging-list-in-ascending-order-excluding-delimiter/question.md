---
title: "Rearranging list in ascending order excluding delimiter"
site: stackoverflow
question_id: 77092314
url: https://stackoverflow.com/q/77092314
asked: 2023-09-12T19:55:24Z
asked_by: "Danieliusr"
asked_by_url: https://stackoverflow.com/users/22546591
last_edited: 2023-09-12T20:08:43Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, list]
score: -3
views_at_snapshot: 54
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6fd1ff23f69ecf3bb2f61ac75c9ed3d122eb5cb170a460647ada54655f45518a
---

# Rearranging list in ascending order excluding delimiter

Asked by [Danieliusr](https://stackoverflow.com/users/22546591) on Stack Overflow, <https://stackoverflow.com/q/77092314>, 2023-09-12, last edited 2023-09-12 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I came across a problem while trying to rearranging a list with data  that has delimiter '='.
For example:

```
list = ['1=8.06225774829855', '2=2.23606797749979', '3=8.602325267042627', '4=7.280109889280518', '5=3.1622776601683795']
```
In the end product I want my list to have number after delimiter rearranged in ascending order while keeping text before delimiter.
Expected Output: 
```
['2=2.23606797749979','5=3.1622776601683795','4=7.280109889280518', '1=8.06225774829855','3=8.602325267042627']
```
