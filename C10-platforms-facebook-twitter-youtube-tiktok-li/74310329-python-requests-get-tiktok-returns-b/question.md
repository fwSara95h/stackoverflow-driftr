---
title: "Python requests.get TikTok returns b''"
site: stackoverflow
question_id: 74310329
url: https://stackoverflow.com/q/74310329
asked: 2022-11-03T22:44:04Z
asked_by: "Centrals"
asked_by_url: https://stackoverflow.com/users/17713213
last_edited: never
tags: [python, beautifulsoup, python-requests]
score: -1
views_at_snapshot: 612
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 31b85436c8d0c0b3d1be039d7dff533d8a5d15630d31801c2e93249e3280bf8f
---

# Python requests.get TikTok returns b''

Asked by [Centrals](https://stackoverflow.com/users/17713213) on Stack Overflow, <https://stackoverflow.com/q/74310329>, 2022-11-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to get the html of a TikTok video page and requests is returning b'' instead of the pages entire HTML. This works on other sites and even the tiktok home page (https://www.tiktok.com/) but not on video pages. Can someone try out my code and let me know what is going on? Also, I got the return code and it was 200.

```
import requests

headers = {
    'user-agent': MY USER AGENT,
}

page = requests.get("https://www.tiktok.com/@thatlittlepuff/video/7160116843611475246",headers=headers)

print(page.content)
```

```
b''
```

I tried to do other tiktok video pages but those don't work either

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Klaus D.](https://stackoverflow.com/users/3929826)** (2022-11-03): Sending you an empty response back is their way to tell you that they don't want to be scraped.
- **[Pedro Lobito](https://stackoverflow.com/users/797495)** (2022-11-04): I get regular HTML using your code. Are you blocked by tt?
