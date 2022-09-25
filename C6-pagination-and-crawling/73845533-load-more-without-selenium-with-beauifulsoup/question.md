---
title: "Load more without Selenium with beauifulsoup"
site: stackoverflow
question_id: 73845533
url: https://stackoverflow.com/q/73845533
asked: 2022-09-25T15:04:47Z
asked_by: "Mari"
asked_by_url: https://stackoverflow.com/users/18067394
last_edited: never
tags: [beautifulsoup]
score: 0
views_at_snapshot: 162
answer_count: 2
accepted_answer_id: 73846784
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b5825676c433d5f4dfc66b153ff8caca0e75c4a6cb181a2c74ec91ad433fe187
---

# Load more without Selenium with beauifulsoup

Asked by [Mari](https://stackoverflow.com/users/18067394) on Stack Overflow, <https://stackoverflow.com/q/73845533>, 2022-09-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

im trying to do web-scraping of 100 reviews on the movie Mulan 1998 from IMDb, however with the following code it only loads 25 (all reviews from the first page, it has "load more" button):

``` 
from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook() 
sheet = excel.active 
sheet.title = 'mulan reviews'
sheet.append(['title', 'review_date', 'review_text'])
    
source = requests.get("https://www.imdb.com/title/tt0120762/reviews?ref_=tt_urv")
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')

reviews = soup.find_all('div', class_="review-container")
    
for review in reviews:
    title= review.find('div',class_="lister-item-content").a.text.replace('\n', '')
    review_date= review.find('span',class_="review-date").text
    review_text= review.find('div', class_="content").div.text       
    more_button = review.find('div', class_="ipl-load-more ipl-load-more--loaded")
    
    print(title, review_date, review_text)
    sheet.append([title, review_date, review_text]) 

excel.save('mulan review 8.xlsx')
```

i was unsuccessful in installing selenium, therefore i wanted to ask if there is another way to do it. Thank you.
