---
title: "How to solve \"Move target out of bounds\" Selenium error?"
site: stackoverflow
question_id: 75011359
url: https://stackoverflow.com/q/75011359
asked: 2023-01-04T21:09:28Z
asked_by: "Amir Rouatbi"
asked_by_url: https://stackoverflow.com/users/20931257
last_edited: never
tags: [python, selenium, beautifulsoup]
score: 0
views_at_snapshot: 2450
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1c061ffcc97c76d6fe187901f01b43710702fb73cbfd4c1ef41dc51f132ff118
---

# How to solve "Move target out of bounds" Selenium error?

Asked by [Amir Rouatbi](https://stackoverflow.com/users/20931257) on Stack Overflow, <https://stackoverflow.com/q/75011359>, 2023-01-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to simulate clikcin on the "Load more listings" button on the "https://empireflippers.com/marketplace/" webpage untill the button no longer is. I tried the following code but it results in "Move target out bounds" error.


```
from selenium import webdriver      
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains




HOME_PAGE_URL = "https://empireflippers.com/marketplace/"

driver = webdriver.Chrome('./chromedriver.exe')
driver.get(HOME_PAGE_URL)

while True:
    try:
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Load More Listings')]")))
        ActionChains(driver).move_to_element(element).click().perform()

    except Exception as e:
        print (e)
        break
print("Complete")
time.sleep(10)
page_source = driver.page_source

driver.quit()
```

I'm expecting to retrieve the html code of the full web page without load more listings button.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Amir Rouatbi](https://stackoverflow.com/users/20931257)** (2023-01-04): The question wasn't answered.
