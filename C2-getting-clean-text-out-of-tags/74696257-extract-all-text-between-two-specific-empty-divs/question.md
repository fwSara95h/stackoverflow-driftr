---
title: "Extract all text between two specific empty divs"
site: stackoverflow
question_id: 74696257
url: https://stackoverflow.com/q/74696257
asked: 2022-12-06T01:27:18Z
asked_by: "Newbie"
asked_by_url: https://stackoverflow.com/users/4096212
last_edited: 2022-12-06T09:21:37Z
last_editor: "Barry the Platipus"
last_editor_url: https://stackoverflow.com/users/19475185
tags: [python, beautifulsoup, html-parsing]
score: 0
views_at_snapshot: 148
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fe15e82fe92b50f149bcdc9a6bc1a46f1a7a703714d2ddb469f5e366d575511a
---

# Extract all text between two specific empty divs

Asked by [Newbie](https://stackoverflow.com/users/4096212) on Stack Overflow, <https://stackoverflow.com/q/74696257>, 2022-12-06, last edited 2022-12-06 by [Barry the Platipus](https://stackoverflow.com/users/19475185). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have html that looks like the one shown below. I want the text between the innermost two empty divs with class name "start" and "end" respectively. In the code below - I want the text between **2nd** `<div class ="start"> </div>` and the **first** `<div class ="end"> </div>`  In between these 2 empty divs there can be multiple divs with any number of tags, and I want the text in these divs. I tried accessing the text, multiple ways using just `div.attrs['class']` and `find_next_siblings` methods, but it did not work. How to go about this?

```
many <divs> </divs> and other tags

<div class ="start"> </div>
<div> bla bla bla </div>

<div class ="start"> </div>
<div> <i> <a> <span> <p> Text I want </p></span></a></i> </div>
<div> <p> Text I want </p> <p> Text I want </p> </div>
<div class ="end"></div>

<div> bla bla bla </div>
<div class ="end"></div>

many <divs> </divs> and other tags

```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[baduker](https://stackoverflow.com/users/6106791)** (2022-12-06): Please provide a [mre].
