---
title: "Is there a really simple method for printing scraped output to a csv file?"
site: stackoverflow
question_id: 75803901
url: https://stackoverflow.com/q/75803901
asked: 2023-03-21T16:31:31Z
asked_by: "PressMeister"
asked_by_url: https://stackoverflow.com/users/21433696
last_edited: never
tags: [python, csv, beautifulsoup]
score: 0
views_at_snapshot: 76
answer_count: 3
accepted_answer_id: 75805366
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 43a2f7d59e7f1167ab0764291c4993ce03ff0800cf2dc84df43fb6e6c94d7a2f
---

# Is there a really simple method for printing scraped output to a csv file?

Asked by [PressMeister](https://stackoverflow.com/users/21433696) on Stack Overflow, <https://stackoverflow.com/q/75803901>, 2023-03-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

*Python: Python 3.11.2
Python Editor: PyCharm 2022.3.3 (Community Edition) - Build PC-223.8836.43
OS: Windows 11 Pro, 22H2, 22621.1413
Browser: Chrome 111.0.5563.65 (Official Build) (64-bit)*

I have a URL (e.g., `https://dockets.justia.com/docket/puerto-rico/prdce/3:2023cv01127/175963`) from which I'm scraping nine items. I'm looking to have the script create a csv file and write my scraped output (nine items) to columns in the csv file.  Is there a really simple way of doing this? 


```
from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get("https://dockets.justia.com/docket/puerto-rico/prdce/3:2023cv01127/175963").text
soup = BeautifulSoup(html_text, "lxml")
cases = soup.find_all("div", class_ = "wrapper jcard has-padding-30 blocks has-no-bottom-padding")

for case in cases:
    case_title = case.find("div", class_ = "title-wrapper").text.replace(" "," ")
    case_plaintiff = case.find("td", {"data-th": "Plaintiff"}).text.replace(" "," ")
    case_defendant = case.find("td", {"data-th": "Defendant"}).text.replace(" "," ")
    case_number = case.find("td", {"data-th": "Case Number"}).text.replace(" "," ")
    case_filed = case.find("td", {"data-th": "Filed"}).text.replace(" "," ")
    court = case.find("td", {"data-th": "Court"}).text.replace(" "," ")
    case_nature_of_suit = case.find("td", {"data-th": "Nature of Suit"}).text.replace(" "," ")
    case_cause_of_action = case.find("td", {"data-th": "Cause of Action"}).text.replace(" "," ")
    jury_demanded = case.find("td", {"data-th": "Jury Demanded By"}).text.replace(" "," ")

    print(f"{case_title.strip()}")
    print(f"{case_plaintiff.strip()}")
    print(f"{case_defendant.strip()}")
    print(f"{case_number.strip()}")
    print(f"{case_filed.strip()}")
    print(f"{court.strip()}")
    print(f"{case_nature_of_suit.strip()}")
    print(f"{case_cause_of_action.strip()}")
    print(f"{jury_demanded.strip()}")
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-03-21): There are many tutorials and examples on the web that explain how to create a csv file using python.  I'm not sure what your actual question is.
- **[AKX](https://stackoverflow.com/users/51685)** (2023-03-21): @JohnGordon Your "write those nine values to it" approach completely ignores e.g. escaping commas within a single field.
- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-03-21): @AKX I'm aware.  Overly simplistic solutions are a way to get the questioner to provide more detail about what they _really_ need.
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-21): @John Gordon Sorry, I should have emphasized my neophyte-ness. I basically need the items in the printed output - which in the script I provided basically just prints the scraped data to the console in rows - distributed across columns in a csv file.
