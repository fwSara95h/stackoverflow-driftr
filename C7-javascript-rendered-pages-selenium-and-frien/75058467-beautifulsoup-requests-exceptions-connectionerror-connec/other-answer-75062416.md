---
title: "Beautifulsoup: requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response"
site: stackoverflow
question_id: 75058467
answer_id: 75062416
url: https://stackoverflow.com/a/75062416
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2023-01-09T20:07:52Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3b11440107f23ba12f081588ea5697fd7cfa4575aa4e4c3b9d5e1aed2e8d4c65
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2023-01-09

Posted on Stack Overflow, <https://stackoverflow.com/a/75062416>, 2023-01-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Try to use real web-browser User Agent instead random one from `pyuser_agent`. For example:

```py
import requests
from bs4 import BeautifulSoup

URL = f"https://www.edmunds.com/inventory/srp.html?radius=5000&sort=publishDate%3Adesc&pagenumber=2"


headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}


response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
overview = soup.find()
print(overview)
```

---

The possible explanation could be that server keeps a list of real-world User Agents and don't serve any page to some non-existent ones.
