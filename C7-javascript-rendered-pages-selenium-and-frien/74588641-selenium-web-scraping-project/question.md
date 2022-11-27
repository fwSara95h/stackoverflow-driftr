---
title: "Selenium web scraping project"
site: stackoverflow
question_id: 74588641
url: https://stackoverflow.com/q/74588641
asked: 2022-11-27T08:45:27Z
asked_by: "explorevaluechain"
asked_by_url: https://stackoverflow.com/users/20612537
last_edited: never
tags: [python, selenium, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 60
answer_count: 1
accepted_answer_id: 74589557
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f5014b13d53c567d6970e5713ab3f27c47073b99b4419b57c853a74fcf8b39e9
---

# Selenium web scraping project

Asked by [explorevaluechain](https://stackoverflow.com/users/20612537) on Stack Overflow, <https://stackoverflow.com/q/74588641>, 2022-11-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am new to using selenium. I previously wrote a scrapper using Beautiful Soup and it was working fine until I ran into "accept cookie". [enter image description here](https://i.sstatic.net/NXT74.png)

I attempted to use Selenium to click on the "X" button, and then I wanted to pass the page_source to Beautifulsoup to reuse my previous script. But my soup is still showing the page with the "accept cookie", resulting in none of the class to be able to be found.

This is the website I want to scrape: https://sturents.com/s/newcastle/newcastle?ne=54.9972%2C-1.5544&sw=54.9546%2C-1.6508

Here is the script:

```
driver = webdriver.Chrome(PATH)

driver.get(link)

soup = BeautifulSoup(r_more_housing.text, 'html.parser')

element = driver.find_element(By.CLASS_NAME, "new--icon-cross")

element.click()

time.sleep(10)

driver.refresh()

soup = BeautifulSoup(driver.page_source)

rooms = soup.find_all('a', class_="new--listing-item js-listing-item")
```

rooms would return empty string.

```
```

tried to return soup where it showed the page without clicking on button

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Heelara](https://stackoverflow.com/users/2886158)** (2022-11-27): Does SO thread [Handling "Accept Cookies" popup with Selenium in Python](https://stackoverflow.com/questions/64032271/handling-accept-cookies-popup-with-selenium-in-python) help?
