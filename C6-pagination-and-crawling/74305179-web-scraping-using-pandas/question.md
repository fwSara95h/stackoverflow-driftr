---
title: "web scraping using pandas"
site: stackoverflow
question_id: 74305179
url: https://stackoverflow.com/q/74305179
asked: 2022-11-03T15:00:14Z
asked_by: "tony michael"
asked_by_url: https://stackoverflow.com/users/18194427
last_edited: never
tags: [python, pandas, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 70
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b82a6332e7ecc00537145a8c13bc7f40ef506a0b6c5a2bbb4c9758518fd0fc50
---

# web scraping using pandas

Asked by [tony michael](https://stackoverflow.com/users/18194427) on Stack Overflow, <https://stackoverflow.com/q/74305179>, 2022-11-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to scrape multiple pages of website using Python, but I'm getting  ***Remote Connection closed error.***
Here is my code
```
import pandas as pd
url_link = 'https://www.taneps.go.tz/epps/viewAllAwardedContracts.do?d-3998960-p={}&selectedItem=viewAllAwardedContracts.do'
LIST = []
for number in range(1,5379):
  url = url_link.format(number)
  dframe = pd.read_html(url, header=None)[0] 
  LIST.append(dframe)
Result_df = pd.concat(LIST)
Result_df.to_csv('Taneps_contracts.csv')
```
Any idea how to solve it?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Kkameleon](https://stackoverflow.com/users/12094184)** (2022-11-03): I believe you need to be authentified to access the page. You haven't provided any headers.
- **[tony michael](https://stackoverflow.com/users/18194427)** (2022-11-03): Yes, there is no need to be authenticated,, How do I provide headers?
- **[Glauco](https://stackoverflow.com/users/3194618)** (2022-11-03): It seems you have 2 issue: the first is to create a scraper, for this is better to use[scrapy](https://scrapy.org/) and collect all pages locally. In a second steps you should read and 'understand' the content of the pages. Don't do all in a once, can become painfull.
- **me** (2022-11-06): why have you tagged beautifulsoup?
