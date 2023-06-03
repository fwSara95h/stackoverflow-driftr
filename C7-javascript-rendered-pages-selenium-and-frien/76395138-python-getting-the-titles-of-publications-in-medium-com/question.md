---
title: "Python - Getting the titles of publications in medium.com"
site: stackoverflow
question_id: 76395138
url: https://stackoverflow.com/q/76395138
asked: 2023-06-03T08:14:22Z
asked_by: "Karthik Bhandary"
asked_by_url: https://stackoverflow.com/users/10755032
last_edited: 2023-06-03T08:22:43Z
tags: [python, selenium-webdriver, web-scraping, beautifulsoup]
score: -3
views_at_snapshot: 135
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cb8e186893e8bc10ada65d2a42f26fcb2594e31b7d88110cd31a4c8242059b4b
---

# Python - Getting the titles of publications in medium.com

Asked by [Karthik Bhandary](https://stackoverflow.com/users/10755032) on Stack Overflow, <https://stackoverflow.com/q/76395138>, 2023-06-03, last edited 2023-06-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am scraping medium.com. I have one problem which I'm not sure how to tackle. Medium publications have different kinds of arrangements when it comes to their article arrangement. Some of them arrange normally in a list form, while some arrange in a grid format. Now when I am scraping through the normal-looking publications Im able to get the article names but when I try to scrape from the grid type I'm not able to. Is there any way for me to tackle this? 
[![publication in list format][1]][1] 

list format. Here using h2 Im able to get the article titles.

[![publication in grid format][2]][2]

grid format. Here I've observed that div is getting used for article titles.

This is my current working code:

```
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


options = Options()
options.add_argument("--headless")
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

class Publication:
    def __init__(self, link):
        self.link = link

    def get_articles(self):
        "Get the articles of the user/publication which was given as input"
        link = self.link
        driver.get(link)
        scroll_pause = 0.5
        # Get scroll height
        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        run_time, max_run_time = 0, 1
        while True:
            iteration_start = time.time()
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, 1000*document.documentElement.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            scrolled = new_height != last_height
            timed_out = run_time >= max_run_time
            if scrolled:
                run_time = 0
                last_height = new_height
            elif not scrolled and not timed_out:
                run_time += time.time() - iteration_start
            elif not scrolled and timed_out:
                break
        elements = driver.find_elements(By.CSS_SELECTOR, "h2")
        for x in elements:
            print(x.text)
```


  [1]: https://i.sstatic.net/zUOX8.png
  [2]: https://i.sstatic.net/Gh6bh.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Karl Knechtel](https://stackoverflow.com/users/523612)** (2023-06-03): Did you try to **load the page in a web browser and look at the DOM**, in order to understand the data that will be seen by Selenium? Do you see the data you are looking for? Can you explain a *rule that tells you* how to identify it?
- **[Karthik Bhandary](https://stackoverflow.com/users/10755032)** (2023-06-03): No actually I just started out with selenium.
- **[Karl Knechtel](https://stackoverflow.com/users/523612)** (2023-06-03): All of the things I suggested that you should do now, do not involve Selenium. Or Python. Or programming. They involve using a web browser, and understanding how web pages work. If you are stuck at this step, you do not yet have a programming question.
- **[Karthik Bhandary](https://stackoverflow.com/users/10755032)** (2023-06-03): I am using the inspect tool on the browser and I found out that some publications have their titles in div while others are in h2. How do I tackle that is my question
