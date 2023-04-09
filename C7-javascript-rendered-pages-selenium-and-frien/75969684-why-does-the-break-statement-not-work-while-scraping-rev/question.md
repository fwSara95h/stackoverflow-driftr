---
title: "Why does the break statement not work while scraping reviews with Selenium and BeautifulSoup in Python?"
site: stackoverflow
question_id: 75969684
url: https://stackoverflow.com/q/75969684
asked: 2023-04-09T09:22:36Z
asked_by: "Mina"
asked_by_url: https://stackoverflow.com/users/19684355
last_edited: never
tags: [python, selenium-webdriver, beautifulsoup, while-loop, break]
score: 0
views_at_snapshot: 65
answer_count: 1
accepted_answer_id: 75969778
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 282c294eb0bda5557c4e0c5cb109a785f97a2125344fd7b738be8cf4a910fd09
---

# Why does the break statement not work while scraping reviews with Selenium and BeautifulSoup in Python?

Asked by [Mina](https://stackoverflow.com/users/19684355) on Stack Overflow, <https://stackoverflow.com/q/75969684>, 2023-04-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am scraping reviews with Selenium and BeautifulSoup in Python but the ```break``` statement does not work so that the ```while``` loop continues even after arriving at the last review page of a product. From what I understand it should work as there is no "next page" button on the last review page anymore. Can someone explain why ```break``` is not working?

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

reviewlist= []

ASINs = ['B09SXL3HPG', 'B07TP8LLQZ']
for a in range(len(ASINs)):
    url = 'https://www.amazon.de/dp/' + str(ASINs[a])
    driver.get(url)

    #Accept cookies (only if you need it)
    if a == 0:
        accept_cookies = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='sp-cc-accept']"))).click()

    #Go to all reviews
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-hook='see-all-reviews-link-foot']"))).click()

    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        reviews = soup.find_all('div', {'data-hook': 'review'})
        for item in reviews:
            review = {
                'date': item.find('span', {'data-hook': 'review-date'}).text.strip(),
                'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
                }
            reviewlist.append(review)

        try:
            next_page_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.a-pagination .a-last'))).click()
            print('click')
            time.sleep(1)
        except Exception as ex:
            print(ex,"!!!!!!!")
            break
