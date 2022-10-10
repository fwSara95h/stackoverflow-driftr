---
title: "Python : Iterate folders trough directory then rename folders with condition"
site: stackoverflow
question_id: 74017526
url: https://stackoverflow.com/q/74017526
asked: 2022-10-10T15:52:49Z
asked_by: "Johntix"
asked_by_url: https://stackoverflow.com/users/15782335
last_edited: never
tags: [python, loops, directory, rename]
score: 0
views_at_snapshot: 110
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0b5ef444b212a97bd809dec8d26ee2fd204ceb7b63e67245b571124ef73c985f
---

# Python : Iterate folders trough directory then rename folders with condition

Asked by [Johntix](https://stackoverflow.com/users/15782335) on Stack Overflow, <https://stackoverflow.com/q/74017526>, 2022-10-10. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm looking for a way to iterate through folders (not files in it) in a repertory and renames them with a condition :
the condition will be the name of the folder itself : if it contains a certain str (who will be in a list) then nothing change. if not its name has to change with defined str

i get an error [WinError 183] who tells me that a renamed folder already exist..
can someone please help me ?
be nice with me i'm a beginner :)

here's my script :



```
import os
from pathlib import Path

list_of_str = ['apple', 'pumpkin', 'strawberry']
start_path = Path('C:\\Users\\jva\\Downloads\\here')

for dirname in os.listdir(start_path):
    f = os.path.join(start_path, dirname)

    if f == enumerate(list_of_str):
        pass
    else:
       os.rename(f,"SET_STR")

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[user11717481](https://stackoverflow.com/users/11717481)** (2022-10-10): Please clarify your specific problem or provide additional details to highlight exactly what you need. As it's currently written, it's hard to tell exactly what you're asking.
