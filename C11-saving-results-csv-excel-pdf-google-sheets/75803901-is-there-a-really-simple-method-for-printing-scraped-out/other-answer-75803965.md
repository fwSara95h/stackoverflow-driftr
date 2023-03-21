---
title: "Is there a really simple method for printing scraped output to a csv file?"
site: stackoverflow
question_id: 75803901
answer_id: 75803965
url: https://stackoverflow.com/a/75803965
author: "AKX"
author_url: https://stackoverflow.com/users/51685
posted: 2023-03-21T16:37:24Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bacd3f86460e612a126497f1fa1c5954cd9065f14af8a9c2b193771b77928b9b
role: another answer on the same question, kept as context; not my work
---

# Answer by [AKX](https://stackoverflow.com/users/51685) — 2023-03-21

Posted on Stack Overflow, <https://stackoverflow.com/a/75803965>, 2023-03-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Sure – the easiest is the standard library `csv` module.

I took the liberty of refactoring your `.replace().strip()` stuff with a single function; we're also gathering up all of the case data into a list-of-dicts first before writing it out to a file. This makes it easier to add new columns without having to deal with their names twice.

```
from bs4 import BeautifulSoup
import requests
import csv


def process_text(s):
    return s.replace(" ", " ").strip()


html_text = requests.get("https://dockets.justia.com/docket/puerto-rico/prdce/3:2023cv01127/175963").text
soup = BeautifulSoup(html_text, "lxml")
cases = soup.find_all("div", class_="wrapper jcard has-padding-30 blocks has-no-bottom-padding")

data = []

for case in cases:
    data.append(
        {
            "case_title": process_text(case.find("div", class_="title-wrapper")),
            "case_plaintiff": process_text(case.find("td", {"data-th": "Plaintiff"})),
            "case_defendant": process_text(case.find("td", {"data-th": "Defendant"})),
            "case_number": process_text(case.find("td", {"data-th": "Case Number"})),
            "case_filed": process_text(case.find("td", {"data-th": "Filed"})),
            "court": process_text(case.find("td", {"data-th": "Court"})),
            "case_nature_of_suit": process_text(case.find("td", {"data-th": "Nature of Suit"})),
            "case_cause_of_action": process_text(case.find("td", {"data-th": "Cause of Action"})),
            "jury_demanded": process_text(case.find("td", {"data-th": "Jury Demanded By"})),
        }
    )

with open("cases.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-21): Again, I apologize for being new to this - and have to spend much more time researching error codes etc. than a normal Python user (but also don't want to leave you hanging and appear ungrateful). For this, I get the error;  Traceback (most recent call last):    line 19, in <module>     "case_title": process_text(case.find("div", class_="title-wrapper")),                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    line 7, in process_text     return s.replace(" ", " ").strip()            ^^^^^^^^^^^^^^^^^^^ TypeError: 'NoneType' object is not callable
- **[AKX](https://stackoverflow.com/users/51685)** (2023-03-21): That means the thing you're passing to the function is `None` - do all cases have a title?
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-21): Yes, they all do.
