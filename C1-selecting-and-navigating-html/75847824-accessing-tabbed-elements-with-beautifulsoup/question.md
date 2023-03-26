---
title: "Accessing tabbed elements with BeautifulSoup"
site: stackoverflow
question_id: 75847824
url: https://stackoverflow.com/q/75847824
asked: 2023-03-26T12:44:48Z
asked_by: "Siggerud"
asked_by_url: https://stackoverflow.com/users/21494016
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 30
answer_count: 1
accepted_answer_id: 75852976
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7b62411fadb0ef79fd49b01dcf7813f051ea4b7db1f847efc895741762bf7b47
---

# Accessing tabbed elements with BeautifulSoup

Asked by [Siggerud](https://stackoverflow.com/users/21494016) on Stack Overflow, <https://stackoverflow.com/q/75847824>, 2023-03-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to scrape all the currency tabs under Currency pairs on this site: https://markets.businessinsider.com/currencies. However I can only get the currency pairs that are active by default when I load the page which is US-Dollar. How can I access the rest of the items with Beautifulsoup? 

Using the code below I get all the US-dollar pairs, but none of the other pairs.

```import requests
from bs4 import BeautifulSoup

response = requests.get("https://markets.businessinsider.com/currencies")
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

currencyTags = soup.find_all("td", class_="table__td bold")
print(currencyTags)```
