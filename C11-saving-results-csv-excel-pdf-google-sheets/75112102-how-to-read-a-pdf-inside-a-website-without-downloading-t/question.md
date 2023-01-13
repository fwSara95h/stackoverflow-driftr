---
title: "how to read a pdf inside a website without downloading the file"
site: stackoverflow
question_id: 75112102
url: https://stackoverflow.com/q/75112102
asked: 2023-01-13T16:46:44Z
asked_by: "j-hugo-ta"
asked_by_url: https://stackoverflow.com/users/21001805
last_edited: 2023-01-13T16:49:36Z
last_editor: "eshirvana"
last_editor_url: https://stackoverflow.com/users/1367454
tags: [python, database, pdf, web-scraping, tabula]
score: -2
views_at_snapshot: 256
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 866202ec93b121fdbedfa5607cdca5db9c7b1041ca6d6903583a0aa805095071
---

# how to read a pdf inside a website without downloading the file

Asked by [j-hugo-ta](https://stackoverflow.com/users/21001805) on Stack Overflow, <https://stackoverflow.com/q/75112102>, 2023-01-13, last edited 2023-01-13 by [eshirvana](https://stackoverflow.com/users/1367454). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to get the data from a pdf that its inside a website, i have tried with tabula but it gave me the following error:

```
CalledProcessError: Command '['java', '-Dfile.encoding=UTF8', '-jar', 'C:\\Users\\Hector\\anaconda3\\lib\\site-packages\\tabula\\tabula-1.0.5-jar-with-dependencies.jar', '--guess', '--format', 'JSON', 'C:\\Users\\Hector\\AppData\\Local\\Temp\\3231632d-81cd-4914-b5e9-cc12f03b607e.pdf']' returned non-zero exit status 1.
```

![enter image description here](https://i.sstatic.net/VUUOg.png)

```
from tabula import read_pdf

df = read_pdf("url")
```
