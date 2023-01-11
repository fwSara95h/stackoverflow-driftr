---
title: "How to iterate through the articles to scrape the full content?"
site: stackoverflow
question_id: 75077320
url: https://stackoverflow.com/q/75077320
asked: 2023-01-11T00:48:44Z
asked_by: "krsnbcd"
asked_by_url: https://stackoverflow.com/users/14322290
last_edited: never
tags: [python, selenium, selenium-webdriver, web-scraping]
score: 0
views_at_snapshot: 107
answer_count: 1
accepted_answer_id: 75079960
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bca97ee47ff580182d2dea3e5056fe168b6cd7afe945bfb2cb56afbf131a9c56
---

# How to iterate through the articles to scrape the full content?

Asked by [krsnbcd](https://stackoverflow.com/users/14322290) on Stack Overflow, <https://stackoverflow.com/q/75077320>, 2023-01-11. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to collect the headline and conent from the news website (https://www.nusabali.com/search?keyword=umkm). I got the headline and the content summary/preview, but I want to retrieve the full article. I see that I would need to click into each article return to previous page and continue to the next article but I couldn't figure out how. Thank you for any help. Here is my code:

    import pandas as pd
    from selenium import webdriver 
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    
    # empty list
    headlines_list = []
    content_list = []
    
    # chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get('https://www.nusabali.com/search?keyword=umkm')
    
    count = 0
    
    while (count<5):
        try:
            time.sleep(1)
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-content > div.wrapper.clearfix > div.col-a.pull-left > section.widget-area-2.pull-right > div > div > div.row > div > button'))))
            count +=1
        except: 
            break
    
    # Select all the parent elements that contain the headline and content
    parents = driver.find_elements(By.CSS_SELECTOR, ".card-deck > .card")
    
    # Iterate through each parent element
    for parent in parents:
        try:
            # headline
            headline = parent.find_element(By.TAG_NAME, "h5")
            headlines_list.append(headline.text)
        except NoSuchElementException:
            headlines_list.append(None)
        try:
            # content
            content = parent.find_element(By.TAG_NAME, "p")
            content_list.append(content.text)
        except NoSuchElementException:
            content_list.append(None)
    
    while len(headlines_list) > len(content_list):
        headlines_list.pop()
    while len(headlines_list) < len(content_list):
        content_list.pop()
    
    # create dataframe
    df = pd.DataFrame({'Headline': headlines_list, 'Content': content_list})
