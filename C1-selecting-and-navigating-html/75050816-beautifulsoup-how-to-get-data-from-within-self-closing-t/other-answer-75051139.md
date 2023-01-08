---
title: "beautifulsoup - how to get data from within self closing tag"
site: stackoverflow
question_id: 75050816
answer_id: 75051139
url: https://stackoverflow.com/a/75051139
author: "amkawai"
author_url: https://stackoverflow.com/users/13294040
posted: 2023-01-08T20:43:25Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7ff147043fc603388a6509912183f3d10e6da2cdc7f7929a67bb19f0e2de6dba
role: another answer on the same question, kept as context; not my work
---

# Answer by [amkawai](https://stackoverflow.com/users/13294040) — 2023-01-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75051139>, 2023-01-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Considering the text you need to parse is on the *file* variable, you can use the following code:

    soup = BeautifulSoup(file, "html.parser")
    
    X = soup.find('input').get('value')
    print(X)
