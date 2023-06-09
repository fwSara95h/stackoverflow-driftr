---
title: "Modifying date using Selenium and Python on Google Travel website"
site: stackoverflow
question_id: 76437746
url: https://stackoverflow.com/q/76437746
asked: 2023-06-09T06:30:45Z
asked_by: "Siddhesh Menon"
asked_by_url: https://stackoverflow.com/users/22045984
last_edited: 2023-06-09T13:16:53Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, selenium-webdriver, web-scraping, beautifulsoup, automation]
score: -1
views_at_snapshot: 130
answer_count: 1
accepted_answer_id: 76440789
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bf0c524cb27e616ed63c874df7dfa56f38b6d1a40e6a3dc3032886bf36508aa7
---

# Modifying date using Selenium and Python on Google Travel website

Asked by [Siddhesh Menon](https://stackoverflow.com/users/22045984) on Stack Overflow, <https://stackoverflow.com/q/76437746>, 2023-06-09, last edited 2023-06-09 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to create a simple web scraper through which I can scrape rates of a hotel for 5 consecutive dates. However using Selenium, I am unable to navigate into the calendar dropdown to select the required date or directly insert the date I want into the date input box.
[Element I want to automate marked in red](https://i.sstatic.net/peNnb.png)

How do I proceed? 

Link for website: https://www.google.com/travel/search

I tried using the class for the div and input tags, but that returned an 'elementclickinterceptedexception' error.


```py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 


checkin_query= ['Tue, Aug 1', 'Wed, Aug 2', 'Thu, Aug 3']
search_query= ['JW Marriott Mumbai', 'Sofitel Mumbai']

options = webdriver.ChromeOptions()
#options.add_argument('--headless')

for j in range(len(checkin_query)):
    for i in range(len(search_query)):
        browser = webdriver.Chrome("chromedriver", options= options)
        browser.get('http://www.google.com/travel/search')

        searchElement = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Search for places, hotels and more")]')
        checkinElement = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Check-in")]')
    
        checkinElement.send_keys(search_query[j])

        searchElement.clear()
        searchElement.send_keys(search_query[i])
        time.sleep(2)

        dropdownElement= browser.find_element(By.XPATH, '//li[contains(@role,"option")]').click()
```

I have attached the code snippet. Apart from the date insertion option, everything works fine

  [1]: https://i.sstatic.net/h88y9.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[theNishant](https://stackoverflow.com/users/7787197)** (2023-06-09): Can you show what you tried?
- **[Siddhesh Menon](https://stackoverflow.com/users/22045984)** (2023-06-09): I have modified the query to add the piece of code I tried
- **[darren](https://stackoverflow.com/users/7318120)** (2023-06-09): `webdriver` is not defined.   the question needs sufficient code for a minimal reproducible example: https://stackoverflow.com/help/minimal-reproducible-example
