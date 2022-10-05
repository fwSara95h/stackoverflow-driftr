---
title: "Why is my CSV file coming out empty after code runs w/no errors?"
site: stackoverflow
question_id: 73965600
url: https://stackoverflow.com/q/73965600
asked: 2022-10-05T19:46:55Z
asked_by: "Camol"
asked_by_url: https://stackoverflow.com/users/20170039
last_edited: 2022-10-06T06:43:59Z
last_editor: "Zach Young"
last_editor_url: https://stackoverflow.com/users/246801
tags: [python, csv, beautifulsoup, python-requests]
score: 0
views_at_snapshot: 1451
answer_count: 1
accepted_answer_id: 73970669
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ee25b2892c0dfc2967321b97a30d98d1b8c3d0bd97aeb4799b2f29bd836d54e4
---

# Why is my CSV file coming out empty after code runs w/no errors?

Asked by [Camol](https://stackoverflow.com/users/20170039) on Stack Overflow, <https://stackoverflow.com/q/73965600>, 2022-10-05, last edited 2022-10-06 by [Zach Young](https://stackoverflow.com/users/246801). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am very new to coding and was trying to get a basic webscraping code to work. The code works just fine, the problem is that I cannot get the CSV file to have any information on it. Any help would be appreciated.

```python3
from bs4 import BeautifulSoup

import requests

import csv

page_to_scrape = requests.get("https://www.scrapethissite.com/pages/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
descriptions = soup.findAll("p", attrs=("class" == "lead session-desc"))
titles = soup.findAll("h3", attrs=("class" == "page-title"))

with open("scrapeinformation.csv", "w", newline="") as f:
    thewriter = csv.writer(f)

    for title, desc in zip(titles, descriptions):
        print(title.text + " - " + desc.text)
        thewriter.writerow([title.text, desc.text])
f.close()
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Sören](https://stackoverflow.com/users/1707427)** (2022-10-05): Why are you formatting your python code as javascript?
- **[DarrylG](https://stackoverflow.com/users/3066077)** (2022-10-05): When I run your code the CSV file is not empty i.e. "I cannot get the CSV file to have any information on it".  Side note--you don't need f.close() at the end since you are using file context manager via the with statement.
- **[Zach Young](https://stackoverflow.com/users/246801)** (2022-10-06): I ran your code as-is and it worked, I got a CSV file with 5 rows and 2 columns. Maybe try printing `descriptions` and `titles` and make sure those lists have data; if they don't, you'll create the empty CSV file but never write a row. And, yeah, you don't need `f.close()` since you're using the `with open(...` context. Welcome, and good luck!
