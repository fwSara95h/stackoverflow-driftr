---
title: "TypeError: 'str' object is not callable beautifulsoup"
site: stackoverflow
question_id: 74198654
url: https://stackoverflow.com/q/74198654
asked: 2022-10-25T18:31:40Z
asked_by: "Jihan Nabilah"
asked_by_url: https://stackoverflow.com/users/20333178
last_edited: 2022-10-31T02:50:05Z
last_editor: "OneCricketeer"
last_editor_url: https://stackoverflow.com/users/2308683
tags: [python, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 124
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7a6fe6bffeae3257e5a4fd0fd4833351f16326bf9a1b7288dcc4d87358f14f48
---

# TypeError: 'str' object is not callable beautifulsoup

Asked by [Jihan Nabilah](https://stackoverflow.com/users/20333178) on Stack Overflow, <https://stackoverflow.com/q/74198654>, 2022-10-25, last edited 2022-10-31 by [OneCricketeer](https://stackoverflow.com/users/2308683). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

i have this code for scraping facebook using beautifulsoup but getting an error in the 'str' part. i've read that python reads this like a variable which should be a function. but I still don't understand the point.


```
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import json
import pandas as pd
from account_credentails import username, password

class Post_Scraper:
    """
    Post_Scraper class allows to scrape Facebook Posts based on search queries.
    """
    LOGIN_URL = "https://www.facebook.com"
    REACTIONS_NAMES = ['Like', 'Angry', 'Love', 'Haha', 'Sad','Care', 'Wow']

    def __init__(self, driver_path, posts_url) -> None:
        driver_path=driver_path('C:\Program Files\Python 3.9\chromedriver.exe')
        self.driver = webdriver.Chrome(driver_path=driver_path)
        self.posts_url = posts_url.replace("www", "mbasic")


    def login(self, username, password) -> None:
        """
        Login to a Facebook Account.

        Args:
            username ('str'))
                Facebook account username/email
            password ('str')
                Facebook account password    
        """
        self.driver.get(self.LOGIN_URL)
        time.sleep(2)
        email_ = self.driver.find_element_by_name("email")
        pass_ = self.driver.find_element_by_name("pass")
        email_.send_keys(username)
        time.sleep(1)
        pass_.send_keys(password)
        time.sleep(2)
        email_.submit()
        time.sleep(10)
       

```


I am getting an error like this 'TypeError: 'str' object is not callable', so what should i do?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[It_is_Chris](https://stackoverflow.com/users/9177877)** (2022-10-25): Always provide the full traceback of the error.
- **[Aymen](https://stackoverflow.com/users/5165980)** (2022-10-26): At what line you are getting the error ?
- **me** (2022-10-29): please let me know if 'del str' works - I'm quite curious about this issue now
