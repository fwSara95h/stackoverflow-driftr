---
title: "How to make a comprehensive composition table efficiently"
site: stackoverflow
question_id: 75923863
url: https://stackoverflow.com/q/75923863
asked: 2023-04-03T21:21:07Z
asked_by: "hiro"
asked_by_url: https://stackoverflow.com/users/15115362
last_edited: never
tags: [python, pandas, chemistry]
score: 0
views_at_snapshot: 87
answer_count: 1
accepted_answer_id: 75925193
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f39eb36601cc6460e7ebf2ae182b4e86f4a455b7379b5a38fb927730bb9d84ba
---

# How to make a comprehensive composition table efficiently

Asked by [hiro](https://stackoverflow.com/users/15115362) on Stack Overflow, <https://stackoverflow.com/q/75923863>, 2023-04-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to make a comprehensive compositon table for composite development (in chemistry field) based on the specific rules.

The rules are
 - The numbers in a table mean the weight percentage of each raw material in the ccomposite
 - There are three raw materials(A, B, C), and I can use up to two materials to make a composite
 - Each number in a table must be a multiple of x and the sum of each row must be less than or equal to y
 - I have to write every possible combination which meets the rules above.

For example, if x=1 and y=2, I can make a table shown below.

```
	        Material A	Material B	Material C
Composite1	        0         	0          	0
Composite2	        1       	0	        0
Composite3	        0       	1       	0
Composite4	        0       	0       	1
Composite5	        1       	1       	0
Composite6	        1        	0       	1
Composite7       	0       	1       	1
Composite8	        2       	0        	0
Composite9	        0        	2       	0
Composite10     	0        	0       	2
```
(Actually, the weight percentage of Material D is omitted, so it's unnecessary to think that the sum of a row is not 100.)

When x and y are small numbers I can make the table manually (using Excel), but if x and y are big numbers I can't.
Thus, I would like to know python codes which make the table efficiently regardless of x and y.
