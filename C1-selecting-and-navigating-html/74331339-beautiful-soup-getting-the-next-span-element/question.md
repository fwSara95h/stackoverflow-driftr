---
title: "Beautiful soup getting the next span element"
site: stackoverflow
question_id: 74331339
url: https://stackoverflow.com/q/74331339
asked: 2022-11-05T20:39:54Z
asked_by: "Michael Roebbeling"
asked_by_url: https://stackoverflow.com/users/6814963
last_edited: never
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 108
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b0e65814eb5bf2e6c039b6aa8ef698bc35d0aefb26bd73efbd9f62cb08b41cd8
---

# Beautiful soup getting the next span element

Asked by [Michael Roebbeling](https://stackoverflow.com/users/6814963) on Stack Overflow, <https://stackoverflow.com/q/74331339>, 2022-11-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have problems to get the data I want from beautiful soup. I have the following html page:

    <br/>
    <h4>Dieses Jahr</h4>
    <br/>
    <span class="parName">Diesen Monat:</span> <span class="parValue">67.54 kWh</span> | 
    <span class="parName">Januar:</span> <span class="parValue">143.92 kWh</span> | 
    <span class="parName">Februar:</span> <span class="parValue">350.51 kWh</span> | 


I need to access the value in the 2nd span 67.54 kWh (after the span with "Diesen Monat:".
Im able to access the "Diesen Monat" span and thought I could use next sibling from there, but this does not work.

    find("span", string="Diesen Monat:").next_sibling

Any idea what I do not get right with beautiful soup
