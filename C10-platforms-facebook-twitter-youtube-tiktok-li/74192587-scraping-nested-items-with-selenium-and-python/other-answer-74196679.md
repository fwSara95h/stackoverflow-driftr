---
title: "Scraping nested items with Selenium and Python"
site: stackoverflow
question_id: 74192587
answer_id: 74196679
url: https://stackoverflow.com/a/74196679
author: "Archiee"
author_url: https://stackoverflow.com/users/11756439
posted: 2022-10-25T15:37:43Z
last_edited: 2022-10-25T15:44:11Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5b8cd7ddfdcf9fb87f2c0bf2bd50a1ba99125bc74d8faf31e2268fb15bc95305
role: another answer on the same question, kept as context; not my work
---

# Answer by [Archiee](https://stackoverflow.com/users/11756439) — 2022-10-25

Posted on Stack Overflow, <https://stackoverflow.com/a/74196679>, 2022-10-25, last edited 2022-10-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

First of all I'll point you to some issues you have within the code, your trying to find an element by it's xpath that's always changing, thus the Simpler way is to find some class name thats 'static' so you can loop through it and get all comments!! 

   

    #change this  
    element = browser.find_element_by_xpath('//*[@id="7156976296152449797"]/div[1]/p[1]')

    #to this => and notice the element(s) not element
    element  = driver.find_elements_by_xpath('//div[contains(@class, "DivContentContainer")]/p[1]')
    
    for elem in element:
        print(elem.text)

- Nt : I Tested the code and it's retrieving all the comments you set the scrollHeight to !!!. Thus, to get Further comments include `time.sleep() or  WebDriverWait()` before scrolling bellow to get more Comments. 
- The 'Replies' are not included, Since you have to check if every comment has replies, if no skip every time.
