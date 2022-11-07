---
title: "Webscraping using python for a webpage having \"Mehr Anseigen\" i.e(eng: Show more)"
site: stackoverflow
question_id: 74350179
url: https://stackoverflow.com/q/74350179
asked: 2022-11-07T16:57:29Z
asked_by: "Kuladeep"
asked_by_url: https://stackoverflow.com/users/20233252
last_edited: never
tags: [python, html, web-scraping]
score: 0
views_at_snapshot: 124
answer_count: 1
accepted_answer_id: 74368223
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a07c9ba7875a481db51f37065b0af7bd980aaceba62cd5a74b22e8217991ee76
---

# Webscraping using python for a webpage having "Mehr Anseigen" i.e(eng: Show more)

Asked by [Kuladeep](https://stackoverflow.com/users/20233252) on Stack Overflow, <https://stackoverflow.com/q/74350179>, 2022-11-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have been trying to scrape a web page and get a few details into an excel or CSV. But unable to get everything since the page is having `Mehr Anzeigen` which is 'Show more' in German.

URL: [https://www.gelbeseiten.de/suche/architekturb%c3%bcros/aachen?umkreis=21000](https://www.stackoverflow.com/)

``` From the above ``URL`` I would like to extract:   ```

`<h2> class='Title',`

`<address> class= 'mod-AdresseKompakt' `

`<adress> class= 'nbr' `

`. . `

`and so on.`

**Pretty much I would like to load everything automatically (*clicking 'show more' for 30 times is difficult*) and extract all details from the completely loaded website.**

I have read some available threads in Stack-Overflow and some blogs, but each one is different for different websites.

Any help would be great!!

*Python*: I know Python up to some extent, but noob in HTML, and JS.

```
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


path_to_chromedriver = '/Users/kuk/Desktop/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'https://www.gelbeseiten.de/suche/architekturb%c3%bcros/aachen?umkreis=21000'
browser.get(url)


h2 = browser.find_elements(By.TAG_NAME, 'h2')
for item in h2:  
print(item.text)
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-11-07): what do you want from the "Mehr Anzeigen" pages? title, address and number [as well as email and website] can be gotten from `url` itself...
- **[Kuladeep](https://stackoverflow.com/users/20233252)** (2022-11-08): Yes, I need email, phonenumber and website as well  Sorry, can you please explain how can I get them for all 324 entries in the page? I didn't understand what do you mean "can be gotten from `url` "  Any sample code would be helpful.
- **me** (2022-11-08): sorry, I mixed it up with the "Mehr Details" button...I've posted a potential solution that uses BeautifulSoup, because I already had a selenium+bs4 scraper function as well as one very similar to the one in the answer for getting details from bs4 tags by css selectors, so that was simpler for me; but if you want/need, I can also add a solution that just uses selenium
- **[Kuladeep](https://stackoverflow.com/users/20233252)** (2022-11-09): That's really impressive solution, and thanks for putting your time and efforts. Could you please also share the solution with only Selenium, it will be useful in other cases.
- **me** (2022-11-11): @Kuladeep- I've added an edit to my answer
