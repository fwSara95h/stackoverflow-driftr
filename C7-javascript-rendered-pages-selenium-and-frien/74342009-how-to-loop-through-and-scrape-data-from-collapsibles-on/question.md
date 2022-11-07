---
title: "How to loop through and scrape data from collapsibles on a website using Selenium?"
site: stackoverflow
question_id: 74342009
url: https://stackoverflow.com/q/74342009
asked: 2022-11-07T04:34:21Z
asked_by: "noideawhatimdoingtbh"
asked_by_url: https://stackoverflow.com/users/20436783
last_edited: never
tags: [python, selenium, web-scraping, beautifulsoup, automation]
score: 0
views_at_snapshot: 63
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 641b0ccbc203d23525c8e0f0883c82b331e93f3865c177f37b20daa36c8a3f8a
---

# How to loop through and scrape data from collapsibles on a website using Selenium?

Asked by [noideawhatimdoingtbh](https://stackoverflow.com/users/20436783) on Stack Overflow, <https://stackoverflow.com/q/74342009>, 2022-11-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

pretty beginner coder here but I am trying to scrape email addresses of tux rental places from this website (https://www.jimsformalwear.com/stores) using Selenium. The email addresses are displayed once the 'Details' link is clicked. I am able to loop through and click details under each stores' name but am only able to pull the email address of the first store. Any help is appreciated

```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

ser = Service("C:\\chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)

s.get("https://www.jimsformalwear.com/stores")
search = s.find_element(by=By.ID, value='address')
search.send_keys("Des Moines, IA")
search.send_keys(Keys.RETURN)

time.sleep(3)

stores = []
email = []

store_names = s.find_elements(by=By.CLASS_NAME, value='store-name')
for name in store_names:
    stores.append(name.text)

link_details = s.find_elements(By.LINK_TEXT, 'DETAILS')
for n in link_details:
    try:
        WebDriverWait(s, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'DETAILS')))
        n.click()
        time.sleep(3)
        emails = s.find_element(by=By.CLASS_NAME, value='store-email.store-contact-item')
        email.append(emails.text)
        time.sleep(3)
    except:
        s.quit()

s.quit()

dict1 = {
    "Store Name": stores,
    "Email": email
}

df1 = pd.DataFrame.from_dict(dict1)

print(df1)
```
