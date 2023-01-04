---
title: "How can I align columns if rows have different number of values?"
site: stackoverflow
question_id: 75004850
url: https://stackoverflow.com/q/75004850
asked: 2023-01-04T11:36:54Z
asked_by: "JRGN1"
asked_by_url: https://stackoverflow.com/users/20469445
last_edited: 2023-01-04T20:06:50Z
last_editor: "Robert"
last_editor_url: https://stackoverflow.com/users/1431720
tags: [python, selenium, web-scraping]
score: 0
views_at_snapshot: 98
answer_count: 2
accepted_answer_id: 75014335
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 942340cba15b4e7bc41146dfffffb737ffcb079ecfb6026e2c5a404a3050e632
---

# How can I align columns if rows have different number of values?

Asked by [JRGN1](https://stackoverflow.com/users/20469445) on Stack Overflow, <https://stackoverflow.com/q/75004850>, 2023-01-04, last edited 2023-01-04 by [Robert](https://stackoverflow.com/users/1431720). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am scraping data with python. I get a csv file and can split it into columns in excel later. But I am encountering an issue I have not been able to solve. Sometimes the scraped items have two statuses and sometimes just one. The second status is thus moving the other values in the columns to the right and as a result the dates are not all in the same column which would be useful to sort the rows.

Do you have any idea how to make the columns merge if there are two statuses for example or other solutions?

Maybe is is also an issue that I still need to separate the values into columns manually with excel.

Here is my code

```
#call packages

import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

# define driver etc.
service_obj = Service("C:\\Users\\joerg\\PycharmProjects\\dynamic2\\chromedriver.exe")
browser = webdriver.Chrome(service=service_obj)

# create loop
initiative_list = []
for i in range(0, 2):
    url = 'https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives_de?page='+str(i)
    browser.get(url)
    time.sleep(random.randint(5, 10))
    initiative_item = browser.find_elements(By.CSS_SELECTOR, "initivative-item")
    initiatives = [item.text for item in initiative_item]
    initiative_list.extend(initiatives)

    
df = pd.DataFrame(initiative_list)

#create csv

print(df)
df.to_csv('Initiativen.csv')

df.columns = ['tosplit']
new_df = df['tosplit'].str.split('\n', expand=True)

print(new_df)
new_df.to_csv('Initiativennew.csv')
```

I tried to merge the columns if there are two statuses.
