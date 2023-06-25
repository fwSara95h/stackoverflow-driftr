---
title: "How do I get a specific element from a bs4.element.ResultSet?"
site: stackoverflow
question_id: 76552348
url: https://stackoverflow.com/q/76552348
asked: 2023-06-25T20:48:34Z
asked_by: "Hanuman Rajagopal "
asked_by_url: https://stackoverflow.com/users/20895808
last_edited: never
tags: [python, web-scraping, beautifulsoup, python-3.8]
score: 2
views_at_snapshot: 150
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: de62823bb342f4b48846845cd1b4533e4e6ee90938f6cb687e14722b4c20b5ae
---

# How do I get a specific element from a bs4.element.ResultSet?

Asked by [Hanuman Rajagopal ](https://stackoverflow.com/users/20895808) on Stack Overflow, <https://stackoverflow.com/q/76552348>, 2023-06-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to select a specific element from a particular bs4.element.ResultSet. 


Here's what I tried to do:

```
from bs4 import BeautifulSoup
import requests
CompanyNOT = "apple"

url = "https://www.annualreports.com/Companies?search="
page_to_scrape = requests.get(url+CompanyNOT)

soup=BeautifulSoup(page_to_scrape.content,"html.parser")
urls = soup.find_all('a', href=True)
```

which gives me an output of:
```
[<a href="/"><img alt="AnnualReports.com" src="/img/ar/logo.webp"/></a>,
 <a href="javascript:;">BROWSE BY</a>,
 <a href="/Browse/Exchange">Exchanges</a>,
 <a href="/Browse/Industry">Industry</a>,
 <a href="/Search">Other Filters</a>,
 <a href="javascript:;">BROWSE BY</a>,
 <a href="/Browse/Exchange">Exchanges</a>,
 <a href="/Browse/Industry">Industry</a>,
 <a href="/Search">Other Filters</a>,
 <a href="/Cart"><img alt="" src="/img/ar/cart.webp"/></a>,
 <a href="/Company/apple-hospitality-reit-inc">Apple Hospitality REIT Inc</a>,
 <a class="addbtn" company_id="6874" href="">Request</a>,
 <a href="/Company/apple-inc">Apple Inc.</a>,
 <a href="/Company/maui-land-pineapple-co-inc">Maui Land &amp; Pineapple Co. Inc.</a>,
 <a href="/Company/pineapple-energy-inc">Pineapple Energy Inc.</a>,
 <a href="/Browse/Exchange">Exchanges</a>,
 <a href="/Browse/Industry">Industry</a>,
 <a href="/Search">More Filters</a>,
 <a href="/">AnnualReports.com</a>,
 <a href="/">Home</a>,
 <a href="/About">About</a>,
 <a href="/Contact">Contact</a>,
 <a href="/FAQ">FAQs</a>,
 <a href="/Disclaimer">Legal</a>,
 <a href="https://www.irsolutions.com">Visit IR Solutions</a>,
 <a href="/AddCompany">Add My Company</a>]
```

How would I from this be able to extract all the elements with "/Company" in them?

So I would like something like: [/Company/apple-hospitality-reit-inc, /Company/apple-in, /Company/maui-land-pineapple-co-inc,  /Company/pineapple-energy-inc]
