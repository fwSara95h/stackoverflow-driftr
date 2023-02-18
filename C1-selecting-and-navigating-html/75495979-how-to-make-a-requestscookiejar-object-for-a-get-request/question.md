---
title: "How to make a \"RequestsCookieJar\" object for a GET request from an existing cookie as \"dictionary\" type in Python"
site: stackoverflow
question_id: 75495979
url: https://stackoverflow.com/q/75495979
asked: 2023-02-18T19:46:45Z
asked_by: "RezA"
asked_by_url: https://stackoverflow.com/users/17942760
last_edited: 2025-10-08T10:30:36Z
last_editor: "VLAZ"
last_editor_url: https://stackoverflow.com/users/3689450
tags: [python, dictionary, cookies, python-requests]
score: 1
views_at_snapshot: 381
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0838f4f181c7db30ad632ed8256f4c1fe7ceb866d427eb3b0cc1b25fb95a14ec
---

# How to make a "RequestsCookieJar" object for a GET request from an existing cookie as "dictionary" type in Python

Asked by [RezA](https://stackoverflow.com/users/17942760) on Stack Overflow, <https://stackoverflow.com/q/75495979>, 2023-02-18, last edited 2025-10-08 by [VLAZ](https://stackoverflow.com/users/3689450). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I've extracted some cookies in my python code in the form of a list of Dictionaries and each dictionary is a cookie like example below:

    [
        {
            "domain": "x.com",
            "httpOnly": True,
            "name": "Username_COOKIE",
            "path": "/",
            "sameSite": "Lax",
            "secure": False,
            "value": "some value",
        },
        {
            "domain": "x.com",
            "expiry": 1676724072,
            "httpOnly": False,
            "name": "ASP.NET_SessionId",
            "path": "/",
            "sameSite": "Lax",
            "secure": False,
            "value": "some value",
        },
        {
            "domain": "x.com",
            "expiry": 1676810425,
            "httpOnly": False,
            "name": "_gid",
            "path": "/",
            "sameSite": "Lax",
            "secure": False,
            "value": "some value",
        }

Now I want to send a new GET request using these cookies. The `request.get()` method gets cookies in it's parameter as "RequestsCookieJar" object. My question is how can I make a "RequestsCookieJar" object using my dictionaries to pass it to the `request.get()` method?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[dskrypa](https://stackoverflow.com/users/19070573)** (2023-02-18): Does this answer your question? [Trying to load cookie into requests session from dictionary](https://stackoverflow.com/questions/31928942/trying-to-load-cookie-into-requests-session-from-dictionary)
- **[RezA](https://stackoverflow.com/users/17942760)** (2023-02-24): @dskrypa No my cookies are in the form of a list of dictionaries and I want to make a "RequestsCookieJar" object.
