---
title: "Read csv file from url"
site: stackoverflow
question_id: 74827440
url: https://stackoverflow.com/q/74827440
asked: 2022-12-16T16:47:41Z
asked_by: "Amen Aziz"
asked_by_url: https://stackoverflow.com/users/17344809
last_edited: never
tags: [python, selenium, web-scraping]
score: 0
views_at_snapshot: 142
answer_count: 2
accepted_answer_id: 74827588
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: aaa4f9a423d60a3c78fdc139fae81c30bd53ed9552cca6ea35b0853492509a81
---

# Read csv file from url

Asked by [Amen Aziz](https://stackoverflow.com/users/17344809) on Stack Overflow, <https://stackoverflow.com/q/74827440>, 2022-12-16. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

  I want to read url but they give me error that `URL must be a string` is there any possible solution for that kindly recommend me how to make the URL string kindly suggest any method

    from selenium import webdriver           
    import time
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
    import pandas as pd
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    import requests
    from csv import writer
    
    
    with open("data.csv") as file:
        start_urls=[line.strip() for line in file]  
    
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
        driver.get(start_urls)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Je Je](https://stackoverflow.com/users/1536343)** (2022-12-16): you need to iterate through your start_urls list, and provide start_urls[i] in driver.get()
- **[Amen Aziz](https://stackoverflow.com/users/17344809)** (2022-12-16): like that `driver.get(start_urls[i])`
- **[Je Je](https://stackoverflow.com/users/1536343)** (2022-12-16): yes, have provided an answer as well. both answers should work.
