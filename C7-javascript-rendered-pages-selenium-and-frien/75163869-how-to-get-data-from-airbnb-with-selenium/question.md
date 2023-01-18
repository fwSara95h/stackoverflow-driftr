---
title: "How to get data from Airbnb with selenium"
site: stackoverflow
question_id: 75163869
url: https://stackoverflow.com/q/75163869
asked: 2023-01-18T18:39:42Z
asked_by: "Bruhlickd"
asked_by_url: https://stackoverflow.com/users/17686452
last_edited: 2023-01-19T08:35:56Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, selenium, web-scraping]
score: 0
views_at_snapshot: 829
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2eec448aa2f234effb20424fb5ab767b1d6de81eb9badcada53a4e1a49d766b6
---

# How to get data from Airbnb with selenium

Asked by [Bruhlickd](https://stackoverflow.com/users/17686452) on Stack Overflow, <https://stackoverflow.com/q/75163869>, 2023-01-18, last edited 2023-01-19 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to web-scrape Airbnb with selenium. However it's been a HUGE impossible mission.

First, I create a drive, where the argument "executable_path" is where my chromedriver is installed. 

    driver = webdriver.Chrome(executable_path=r'C:\directory\directory\directory\chromedriver.exe')

Secondly, I do the other stuffs:

    driver.get('https://www.airbnb.com.br/')
    a = driver.find_element(By.CLASS_NAME, "cqtsvk7 dir dir-ltr")
    a.click()
    a.send_keys('Poland')

Here I received the error: `NoSuchWindowException: Message: no such window: target window already closed from unknown error: web view not found`

Moreover, when I create the variables to store the html elements, it doesn't work as well:

    title = driver.find_elements(By.CLASS_NAME, 'a-size-base-plus a-color-base a-text-normal')
    place = driver.find_elements(By.ID, 'title_49247685') 
    city = driver.find_elements(By.CLASS_NAME, 'f15liw5s s1cjsi4j dir dir-ltr')
    price = driver.find_elements(By.CLASS_NAME, 'p11pu8yw dir dir-ltr')

Please, someone could help me? How can I get the place, city and price of all of my query of place to travel in airbnb? (I know how to store all in a pandas df, my problem is the use of selenium. Those "get_elements" seem not to work properly in airbnb.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[undetected Selenium](https://stackoverflow.com/users/7429447)** (2023-01-18): Once you do `driver.get('https://www.airbnb.com.br/')` what is the next step you are trying to automate? Where are you trying to invoke `send_keys('Poland')`?
- **[Bruhlickd](https://stackoverflow.com/users/17686452)** (2023-01-18): I want that selenium search for me the country where I want to extract the data (Poland, in this case). After that, I want that selenium goes over throught the result pages and colect the name of the city, the location and the price of the houses.
- **[undetected Selenium](https://stackoverflow.com/users/7429447)** (2023-01-18): _want that selenium search for me the country where I want to extract the data (Poland, in this case)_: What are the manual steps for that?
- **[Bruhlickd](https://stackoverflow.com/users/17686452)** (2023-01-18): Have you tryed that code above? It gives me an error message, probably because: the html element is wrong. I tryed a lot of html elements, and even so it doesn't work. Looks like some stuff of airbnb itself. I don't know, because of that I posted the question.
