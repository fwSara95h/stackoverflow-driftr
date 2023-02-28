---
title: "Adding sum of value back to Dictionary"
site: stackoverflow
question_id: 75597589
url: https://stackoverflow.com/q/75597589
asked: 2023-02-28T21:42:15Z
asked_by: "Coder94"
asked_by_url: https://stackoverflow.com/users/21307344
last_edited: 2023-02-28T21:50:46Z
last_editor: "mkrieger1"
last_editor_url: https://stackoverflow.com/users/4621513
tags: [python, dictionary]
score: -3
views_at_snapshot: 58
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6bb56ddbbd528fcc205c92b37fdf1345082bbeeca5f09f7b603006770ac7b9b8
---

# Adding sum of value back to Dictionary

Asked by [Coder94](https://stackoverflow.com/users/21307344) on Stack Overflow, <https://stackoverflow.com/q/75597589>, 2023-02-28, last edited 2023-02-28 by [mkrieger1](https://stackoverflow.com/users/4621513). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a dictionary, and I'm trying to add 100 to the values. I'm able to do so, but I can't seem to figure out how to insert the new values to show up in the dictionary.

    for value in artist_dict.values():
      value += 100
      
    print(artist_dict)

I tried `.append(value)` and received an error message. Also, `value = artist_dict.values()`, `artist_dict.update(value)`, `artist_dict.values() = value`, and `artist_dict.updated(value +=100)` all received an error message.
