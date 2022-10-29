---
title: "For some reason .write() does not write string to .txt file anymore"
site: stackoverflow
question_id: 74245349
answer_id: 74245423
url: https://stackoverflow.com/a/74245423
author: "Fahim"
author_url: https://stackoverflow.com/users/16945827
posted: 2022-10-29T12:49:59Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 71a8bdf751badc6236f7fe526b597e24294fe9460028205231bcc04c483a539b
role: another answer on the same question, kept as context; not my work
---

# Answer by [Fahim](https://stackoverflow.com/users/16945827) — 2022-10-29

Posted on Stack Overflow, <https://stackoverflow.com/a/74245423>, 2022-10-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

not a direct answer, but in my early days this happened with me. The **requests** module of Python sends request with headers indicating python and that could be quickly detected by websites and your IP can get blocked and you are getting unusual response that's why your working function is not working now. 

**Solution:**

Use natural request headers see the code below 

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    r = requests.get(URL, headers=headers)

Use a proxy in case you got blocked on your IP it is highly recommended

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[curies](https://stackoverflow.com/users/20364643)** (2022-10-29): thanks for the advice! Out of habit I usually have my vpn turned on anyways. Also the the website I tried this on, is mine so beeing blocked is not my problem here. Also when I put ``print(link)`` in the code I also see that I am able to find sublinks as strings. But they just don't get written in the txt. Though thank you for the guidance that will help! Where do I need to put this part of the code?
- **[Fahim](https://stackoverflow.com/users/16945827)** (2022-10-29): req = Request(link) html_page = urlopen(req) you have to use it like this                 html_page = requests(link, headers=headers).content just replace this
