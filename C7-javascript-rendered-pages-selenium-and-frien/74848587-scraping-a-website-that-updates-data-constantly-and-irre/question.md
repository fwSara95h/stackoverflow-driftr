---
title: "Scraping a website that updates data constantly and irregularly"
site: stackoverflow
question_id: 74848587
url: https://stackoverflow.com/q/74848587
asked: 2022-12-19T09:34:19Z
asked_by: "Martii"
asked_by_url: https://stackoverflow.com/users/16257814
last_edited: 2022-12-19T09:36:55Z
tags: [python, selenium, web-scraping]
score: 0
views_at_snapshot: 1464
answer_count: 2
accepted_answer_id: 74926301
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1e454a2e218358120d92bba673ada4d25147446dd95dcf57c29496406015f7cb
---

# Scraping a website that updates data constantly and irregularly

Asked by [Martii](https://stackoverflow.com/users/16257814) on Stack Overflow, <https://stackoverflow.com/q/74848587>, 2022-12-19, last edited 2022-12-19. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape a web application to get values of the table . How do I scrape the table every time new values are added to the table or otherwise how can I scrape the website? [The website](https://play.pakakumi.com)

My basic code only lets me scrape manually resulting to many values not being scraped. Also, 
```
driver.find_elements_by_xpath
``` 
does not return anything but 
```
WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located() 
```
works.


Below is my code
```
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

website = "https://play.pakakumi.com/"
path = r'D:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')


'''
k =driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div[2]/div/table/tbody/tr/td[1]')


for item in k:
    print(item.text)
'''
foo = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div[2]/div/table/tbody/tr/td[1]')))
for b in foo:
    print(b.text)
#print(foo)
```

```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Gunesh Shanbhag](https://stackoverflow.com/users/5235168)** (2022-12-19): make use of lxml and requests libray instead of chromedriver and selenium. Save scraped data in a nosql db like mongo db and check with db everytime u scarp for new values/ also add a cron job to run the python script after every interval of time
