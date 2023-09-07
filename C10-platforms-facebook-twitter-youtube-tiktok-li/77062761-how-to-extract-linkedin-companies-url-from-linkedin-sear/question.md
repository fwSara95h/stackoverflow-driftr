---
title: "How to extract linkedin companies URL from linkedin search using python"
site: stackoverflow
question_id: 77062761
url: https://stackoverflow.com/q/77062761
asked: 2023-09-07T20:46:46Z
asked_by: "Abdelali Fihri"
asked_by_url: https://stackoverflow.com/users/21597357
last_edited: never
tags: [python, html, selenium-webdriver, beautifulsoup, spring-social-linkedin]
score: -2
views_at_snapshot: 913
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5805d170e02665a325fcdf9b890e61c6ad12d3160c7efc7d5140775e88099bfc
---

# How to extract linkedin companies URL from linkedin search using python

Asked by [Abdelali Fihri](https://stackoverflow.com/users/21597357) on Stack Overflow, <https://stackoverflow.com/q/77062761>, 2023-09-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrap company's profile URL from a LinkedIn search but I got "not found".
Every things worked well in my code here it is:

    import requests 
    import csv
    import time
    import numpy
    from bs4 import BeautifulSoup
    from time import sleep
    from selenium import webdriver
    import pandas as pd
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time
    import re





    # Read the keywords from a file
    with open("keywords.txt", "r") as file:
      keywords = file.read().splitlines()

    # Define the User-Agent header
    edgedriver_path = '/path/to/edgedriver'
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options, executable_path=edgedriver_path)
    driver.implicitly_wait(10)
    driver.get('https://www.linkedin.com/login')


    email_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    email_input.send_keys('*************')
    password_input.send_keys('*************')
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)



    # Create a new CSV file and write the headers
    with open("results.csv", "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerow(["Keyword", "Total Results"])

    # Perform the search for each keyword and write the results in CSV file
    for keyword in keywords:
        URL = 'https://www.linkedin.com/search/results/companies/?keywords=' + keyword
        driver.get(url=URL)
        driver.implicitly_wait(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        a_href = soup.find_all('a', {'class':'app-aware-link '})
        if a_href:
            link= link.get('href')
            writer.writerow([keyword, link])
            print(f"Keyword: {keyword}, linkedin: {link}")
        else:
            writer.writerow([keyword, "Not found"])
            print(f"Keyword: {keyword}, linkedin: Not found")

The problem is in # Perform the search for each keyword and write the total number of results to the CSV file party. I don't how to use href, a, class and find all to get url of the first result. for example if search for meta the result should be https://www.linkedin.com/company/meta/

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-09-11): did you observe the opened edge window controlled by selenium? was it logging in and searching as expected?
- **me** (2023-09-11): btw, was your csv getting filled out properly? I'd expect it to write only in the `with open...` block, but I could ofc be wrong about that
