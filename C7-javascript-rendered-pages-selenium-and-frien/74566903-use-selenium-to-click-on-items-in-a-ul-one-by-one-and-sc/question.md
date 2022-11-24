---
title: "Use Selenium to click on items in a UL one by one and scrape some information"
site: stackoverflow
question_id: 74566903
url: https://stackoverflow.com/q/74566903
asked: 2022-11-24T22:51:01Z
asked_by: "Darman"
asked_by_url: https://stackoverflow.com/users/10872352
last_edited: 2022-11-24T23:18:52Z
tags: [python, selenium, web-scraping]
score: 0
views_at_snapshot: 110
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 933ccb119eab371ea7892a54d58cf5ae6cbb1071a65da3e29cf6dae0de1b94e7
---

# Use Selenium to click on items in a UL one by one and scrape some information

Asked by [Darman](https://stackoverflow.com/users/10872352) on Stack Overflow, <https://stackoverflow.com/q/74566903>, 2022-11-24, last edited 2022-11-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

i'm just practicing scraping with selenium 

[![inspect element image][1]][1]

What i would like to do is go through each item in the unordered list


[![href][2]][2]


  [1]: https://i.sstatic.net/12mhd.png
  [2]: https://i.sstatic.net/fAcwK.png

get every list item

 

     wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='main_content']/ul" )))
    ul_element = driver.find_element(By.XPATH, "//*[@id='main_content']/ul")

    all_li_element = ul_element.find_elements(By.CSS_SELECTOR, "li")

then after i got the list items to go to each one and scrape some data

is there a better way because the way i'm thinking about it, it will turn into a nested list
