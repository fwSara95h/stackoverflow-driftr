---
title: "Python: can not save all links to a dict in json file, only the last one"
site: stackoverflow
question_id: 76530648
answer_id: 76530736
url: https://stackoverflow.com/a/76530736
author: "Edward"
author_url: https://stackoverflow.com/users/12856818
posted: 2023-06-22T10:01:27Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7833a5e9a448ff5522f52daecb83f474325ac33d77cc6c21b97172bead6bd8b8
role: another answer on the same question, kept as context; not my work
---

# Answer by [Edward](https://stackoverflow.com/users/12856818) — 2023-06-22

Posted on Stack Overflow, <https://stackoverflow.com/a/76530736>, 2023-06-22; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

There's a few things I notice here.

Firstly, your page numbers `range(1,2)`. In python the stop is not included in the range so the for loop will only run once with a page number of 1.

Secondly, your `all_links_dict = {}` line is resetting the dictionary to an empty dict each time.

Lastly, you are opening the file each iteration of the loop in `'w'` mode and then json dumping which will overwrite any previous contents.

I would advise to adjust your range, move the dictionary initialisation out of the for loop and dump the dictionary to your file once at the end outside of the for loop.
