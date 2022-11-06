---
title: "TypeError while webscraping using find function in BeautifulSoup"
site: stackoverflow
question_id: 74337709
url: https://stackoverflow.com/q/74337709
asked: 2022-11-06T16:31:28Z
asked_by: "Yogadharshan"
asked_by_url: https://stackoverflow.com/users/19320247
last_edited: 2022-11-06T16:32:49Z
tags: [python, web-scraping, beautifulsoup, typeerror, data-mining]
score: 1
views_at_snapshot: 50
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c7800be79c016690aa2dee917229fd9321dfa08984593767c92b595cc8fba3ef
---

# TypeError while webscraping using find function in BeautifulSoup

Asked by [Yogadharshan](https://stackoverflow.com/users/19320247) on Stack Overflow, <https://stackoverflow.com/q/74337709>, 2022-11-06, last edited 2022-11-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape a website from timesjob.com but it returns some type of error can you identify the cause? I still can't understand what causes this type of error


```
from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    job = job.text
    company_name = (job.find("h3", class_="joblist-comp-name")).text.replace(" ","")
    skills = job.find("span", class_="srp-skills").text.replace(" ","")
    published_date = job.find("span", class_="sim-posted").span.text
    print(job)


print(f"""
Company Name: {company_name}
Required Skills: {skills}
""")

print(" ")
```


This comes to be a type error:

```
Traceback (most recent call last):
  File "C:\Users\New\PycharmProjects\pythonProject1\main.py", line 15, in <module>
    company_name = (job.find("h3", class_="joblist-comp-name")).text.replace(" ","")
TypeError: find() takes no keyword arguments
```

what could be the problem with this?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[MattDMo](https://stackoverflow.com/users/1426065)** (2022-11-06): In the line above, you write `job = job.text`, meaning that `job` is now a string. There is a `str.find()` method, but it doesn't take keyword arguments. I think the `.find()` method you're trying to use is BeautifulSoup's `soup.find()`, in which case just comment out the `job = job.text` line.
