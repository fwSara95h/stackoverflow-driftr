---
title: "How do I get a specific element from a bs4.element.ResultSet?"
site: stackoverflow
question_id: 76552348
answer_id: 76552364
url: https://stackoverflow.com/a/76552364
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2023-06-25T20:53:34Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b1a61e793035f670c6ba94fc9ae4b5113e194cccd24d3bea4f0d54365aca2942
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2023-06-25

Posted on Stack Overflow, <https://stackoverflow.com/a/76552364>, 2023-06-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can use CSS selector API:

```py
import requests
from bs4 import BeautifulSoup

url = "https://www.annualreports.com/Companies?search=apple"
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

for a in soup.select('a[href*="/Company/"]'):
    print(a['href'])
```

Prints:

```none
/Company/apple-hospitality-reit-inc
/Company/apple-inc
/Company/maui-land-pineapple-co-inc
/Company/pineapple-energy-inc
```

---

Or `bs4` API:

```py
for a in soup.find_all(lambda tag: tag.name == 'a' and '/Company/' in tag.get('href', '')):
    print(a['href'])
```

---

Or: select all `<a>` tags and filter it in list-comprehension:

```py
hrefs = [a['href'] for a in soup.find_all('a') if '/Company/' in a.get('href', '')]
print(*hrefs, sep='\n')
```
