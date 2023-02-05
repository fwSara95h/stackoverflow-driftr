---
title: "How can one sort a list of dictionaries into an excel sheet such that each unique key and one corresponding key are placed into columns?"
site: stackoverflow
question_id: 75350007
answer_id: 75350314
url: https://stackoverflow.com/a/75350314
author: "David Leal"
author_url: https://stackoverflow.com/users/6237093
posted: 2023-02-05T05:31:52Z
last_edited: 2023-02-05T17:12:51Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d8fd93b2967e5eb77edc433affe1c133a8f93a40ccf4d1264c0bd642ae771828
role: another answer on the same question, kept as context; not my work
---

# Answer by [David Leal](https://stackoverflow.com/users/6237093) — 2023-02-05

Posted on Stack Overflow, <https://stackoverflow.com/a/75350314>, 2023-02-05, last edited 2023-02-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Here a solution using an Excel formula. Probably using `FILTERXML` there is shorter way, but it is not available for Excel Web, which is the version I use. In cell `B3`, you can use the following formula:

```
=LET(header, {"Group","Name"}, clean, SUBSTITUTE(TEXTSPLIT(B1,
 {"[{","'key1': ","'key2':","}]","}, {"},,1),"),",")"),
 split, WRAPROWS(clean,2), gps,INDEX(split,,2),names, INDEX(split,,1),
 gpsUx, UNIQUE(gps), out, DROP(REDUCE("", gpsUx, LAMBDA(ac,x,
  HSTACK(ac, VSTACK(header, HSTACK(x, FILTER(names, gps=x)))))),,1),
 IFERROR(out,""))
```
Here is the output:
[![excel output][1]][1]

An **alternative solution** is using a recursive function to do all the replacement. Please check my answer to the question: [Is it possible to convert words to numbers in a string without VBA?][2] I use the same function here `MultiReplace`:
```
= LAMBDA(text, old, new, IF(MIN(LEN(old))=0, text, 
  MultiReplace(SUBSTITUTE(text, INDEX(old,1), INDEX(new,1)), 
    IFERROR(DROP(old,1),""), IFERROR(DROP(new,1),""))))
```
where `old` and `new` are `nx1` arrays, where `n` is the number of substitutions.

The above function needs to be defined in the *Name Manager* since it is recursive. Now we are going to use in formula to provide the output of the question in cell `B3`:

```
=LET(header, {"Group", "Name"}, clean, MultiReplace(B1, 
  {"{'key1': " ; ", 'key2':" ; "}" ; "[(";"]]";"], ("}, 
  {"" ; "-" ; "" ; "(" ; "]" ; "] & ("}), 
 split, TEXTSPLIT(@clean,"-"," & "), gps,INDEX(split,,2),names, INDEX(split,,1), 
 gpsUx, UNIQUE(gps), out, DROP(REDUCE("", gpsUx, LAMBDA(ac,x, 
 HSTACK(ac, VSTACK(header, HSTACK(x, FILTER(names, gps=x)))))),,1), 
 IFERROR(out,""))
```

You can check the output of each name variable: `clean`, `split`, to see the intermediate results. Once we have the information in array format (`split`), then we apply `DROP/REDUCE/HSTACK` pattern. Check my answer to the question: [how to transform a table in Excel from vertical to horizontal but with different length](https://stackoverflow.com/questions/74477320/how-to-transform-a-table-in-excel-from-vertical-to-horizontal-but-with-different/74497691#74497691) for more details.

Both solutions work for multiple groups, not just for two groups as in the input sample. For each unique `key1` group it generates the **Group** and its corresponding **Name** columns and concatenate the result horizontally via `HSTACK`.


  [1]: https://i.sstatic.net/bQZ5T.png
  [2]: https://stackoverflow.com/questions/74574918/is-it-possible-to-convert-words-to-numbers-in-a-string-without-vba/74575828#74575828
  [3]: https://i.sstatic.net/dVrQI.png
