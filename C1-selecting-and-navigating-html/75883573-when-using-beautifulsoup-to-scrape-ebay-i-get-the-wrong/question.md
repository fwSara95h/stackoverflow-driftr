---
title: "When using BeautifulSoup to scrape Ebay, I get the wrong price for a listing"
site: stackoverflow
question_id: 75883573
url: https://stackoverflow.com/q/75883573
asked: 2023-03-30T02:12:16Z
asked_by: "Behnam Mozafari"
asked_by_url: https://stackoverflow.com/users/21523196
last_edited: 2023-03-30T05:22:09Z
last_editor: "imxitiz"
last_editor_url: https://stackoverflow.com/users/12446721
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 171
answer_count: 1
accepted_answer_id: 75884306
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 15094cc929a737346ebff0ebf1b4cefacfb9f961a4ddeebf108540f046adca07
---

# When using BeautifulSoup to scrape Ebay, I get the wrong price for a listing

Asked by [Behnam Mozafari](https://stackoverflow.com/users/21523196) on Stack Overflow, <https://stackoverflow.com/q/75883573>, 2023-03-30, last edited 2023-03-30 by [imxitiz](https://stackoverflow.com/users/12446721). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am using BeautifulSoup to scrape the eBay site, however I got a different price than from the actual eBay page. I want to search for multiple different products later on and get the price for each of them, that's why I use `search_term`.

Here is my code:
```
from bs4 import BeautifulSoup
import requests

# Set the search term
search_term = 'Ryco Air Filter A1785'

# Make a GET request to the eBay search page with the search term as a parameter
response = requests.get('https://www.ebay.com.au/sch/i.html', params={'_nkw': search_term})

# Parse the response content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the price of the first item
print(soup.find("span", attrs={"class": "s-item__price"}))
```
I get this output:
```
<span class="s-item__price">$20.00</span>
```
However on the eBay page it says the product is $22.84.
