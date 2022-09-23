---
title: "Why is the value attribute excluded when making a drop-down menu's answer tag?"
site: stackoverflow
question_id: 73833338
answer_id: 73833628
url: https://stackoverflow.com/a/73833628
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-23T22:47:45Z
last_edited: 2022-09-23T23:06:26Z
revisions: 2
revision_history: https://stackoverflow.com/posts/73833628/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 435499b566c9cb9707f87d928f53d9d2851441abb62b7a4919802c5f25144550
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-23

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73833628>, 2022-09-23, last edited 2022-09-23; score 0. Text as retrieved 2026-10-12.

Inputs of type "text" start out with a value of  "" (empty string) by default (unless you set a different [default with the `defaultValue` attribute][1]),  and then the value is whatever the user types. 

You can set the value attribute your code to pre-fill the input, but it's generally not necessary. (You can also add a [`placeholder`][2], which shouldn't affect the `value`, and disappears when the user starts typing into that input since it only shows up when input is empty (`value = ""`).

And yes, the [`name`][3] attribute is the main requirement for submitting to server. Inputs generally have a default value. Even for drop-downs, default value is usually the first option ("q1" in your case), unless the [`selected`][4] attribute is added to one of the other `option`s.


  [1]: https://www.w3schools.com/jsref/prop_text_defaultvalue.asp.
  [2]: https://www.w3schools.com/jsref/prop_text_defaultvalue.asp
  [3]: https://html.com/attributes/input-name/
  [4]: https://www.w3schools.com/tags/att_option_selected.asp
