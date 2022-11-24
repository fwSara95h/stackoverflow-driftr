---
title: "Is there a way I can modify some lines in site html code so it marks the checkbox?"
site: stackoverflow
question_id: 74565163
url: https://stackoverflow.com/q/74565163
asked: 2022-11-24T18:53:04Z
asked_by: "wasdy"
asked_by_url: https://stackoverflow.com/users/20593521
last_edited: never
tags: [python, html, selenium, parsing, beautifulsoup]
score: 0
views_at_snapshot: 140
answer_count: 1
accepted_answer_id: 74565584
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 21023d373dee14800dbf219b2d52d7a60f60466ec26e08476ea648fa3d33e1a7
---

# Is there a way I can modify some lines in site html code so it marks the checkbox?

Asked by [wasdy](https://stackoverflow.com/users/20593521) on Stack Overflow, <https://stackoverflow.com/q/74565163>, 2022-11-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So, there's a site I'm trying to parse so it can automatically raising my offers every two hours.
The site designed in that way that you have to mark with checkboxes the lots you want to raise.
Somehow in html code the checkbox doesn't have value, instead it looks like this: 



I have to click it manually via using 
  
```
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "idk what to write so it checks it"))).click()
```

But I really don't know how do I find it so it can be clicked.

```
<label>
  <input type="checkbox" value="613" checked=""> 
  # value - lot id, checked - means the checkbox is marked
<label>
  # and non-checked checkbox code looks like this:

<label>
  <input type="checkbox" value="613">
<label>
```
