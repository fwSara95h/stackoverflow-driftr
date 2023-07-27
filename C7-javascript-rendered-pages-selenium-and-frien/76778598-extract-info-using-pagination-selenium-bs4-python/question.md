---
title: "Extract info using pagination- selenium bs4 python"
site: stackoverflow
question_id: 76778598
url: https://stackoverflow.com/q/76778598
asked: 2023-07-27T10:00:36Z
asked_by: "Sushmitha"
asked_by_url: https://stackoverflow.com/users/20271577
last_edited: never
tags: [python-3.x, selenium-webdriver, web-scraping, beautifulsoup, pagination]
score: -1
views_at_snapshot: 35
answer_count: 1
accepted_answer_id: 76789943
closed: 2023-07-28T17:35:19Z (Needs details or clarity)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 882a5aa6ae20e60c0c60d455e867abf7024102c91e2fa69307d1dbea5c257843
---

# Extract info using pagination- selenium bs4 python

Asked by [Sushmitha](https://stackoverflow.com/users/20271577) on Stack Overflow, <https://stackoverflow.com/q/76778598>, 2023-07-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am working with web scraping sales navigator. I was able to navigate to 1st page, scroll 8 times and extract all the names, titles using selenium and beautiful. below is the code.

```
driver.get(dm)
time.sleep(5)

time.sleep(5)
section = driver.find_element(By.XPATH, "//*[@id='search-results-container']")
time.sleep(5)

counter = 0

while counter < 8:  # this will scroll 8 times
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                 section)
    counter += 1
    # add a timer for the data to fully load once you have scrolled the section

    time.sleep(7) # You might need to install time library to use this statement

src2 = driver.page_source
 
# Now using beautiful soup
soup = BeautifulSoup(src2, 'lxml')

name_soup = soup.find_all('span', {'data-anonymize': 'person-name'})

names = []
for name in name_soup:
    names.append(name.text.strip())
    
```

However, there are 8 more pages and I need to extract all the names and append it to names list.

Please help

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[chitown88](https://stackoverflow.com/users/7752296)** (2023-07-28): really hard to help if you don't share the url
