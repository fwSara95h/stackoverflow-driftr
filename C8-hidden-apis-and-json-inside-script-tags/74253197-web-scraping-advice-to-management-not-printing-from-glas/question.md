---
title: "Web Scraping 'Advice to management\" not printing from Glassdoor"
site: stackoverflow
question_id: 74253197
url: https://stackoverflow.com/q/74253197
asked: 2022-10-30T12:50:59Z
asked_by: "user19810494"
asked_by_url: https://stackoverflow.com/users/19810494
last_edited: 2022-10-30T20:19:25Z
tags: [python, html, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 365
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 11f96143d38262a67ccc17988da00c1944493cf89025f3b3c2d3b4dc994c85e7
---

# Web Scraping 'Advice to management" not printing from Glassdoor

Asked by [user19810494](https://stackoverflow.com/users/19810494) on Stack Overflow, <https://stackoverflow.com/q/74253197>, 2022-10-30, last edited 2022-10-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm new to python and web scraping. I have trouble printing the "advice to management" part in the review from Glassdoor. Everything else is printing expect for "advice to management".

If you check below in the review we have 'advice to management' but in the output it's not getting scrapped with the rest of the datapoints.


Can anyone help me please?!! This is so important to me. It's the data I'm going to be using for my thesis.



I have tried this code:



```

import requests
from bs4 import BeautifulSoup
import pandas as pd 


def extract(pg): 
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.80 Safari/537.36'}
    url = f'https://www.glassdoor.com/Reviews/Google-Engineering-Reviews-EI_IE9079.0,6_DEPT1007_IP{pg}.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng'

    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')# this a soup function that retuen the whole html
    return soup

def transform(soup): #to get reviews
  

    divs = soup.find_all('div', class_='gdReview')
    for item in divs:

        try:
          Title = item.find('h2', class_= 'mb-xxsm mt-0 css-93svrw el6ke055').text
        except:
          Title = None

        try:
          Rating = item.find('span', class_= 'ratingNumber mr-xsm').text.replace('<span class="ratingNumber mr-xsm">', '').strip()
        except:
          Rating = None    

        try:
          Employee_Situation= item.find('span', class_= 'pt-xsm pt-md-0 css-1qxtz39 eg4psks0').text.replace('<span class="pt-xsm pt-md-0 css-1qxtz39 eg4psks0">', '').strip()
        except:
          Employee_Situation = None  

        try:   
          Pros = item.find('span',  {'data-test':'pros'}).text.replace('<span data-test="pros">', '').strip()
        except:
          Pros = None

        try:  
          Cons = item.find('span',  {'data-test':'cons'}).text.replace('<span data-test="cons">', '')
        except:
          Cons: None

        try:    
          Advice_To_Management = item.find('span', {'data-test':'advice-management'}).text
        except: 
          Advice_To_Management = None

        try:
          Auhtor_Info = item.find('span', class_= 'common__EiReviewDetailsStyle__newUiJobLine').text.replace('<span class="common__EiReviewDetailsStyle__newUiJobLine"><span><span class="middle common__EiReviewDetailsStyle__newGrey">', '').strip()
        except:  
          Auhtor_Info = None


        Reviews = {
            'Title' : Title,
            'Rating': Rating,
            'Employee_Situation' : Employee_Situation,
            'Pros' : Pros,
            'Cons' : Cons,
            'Advice_To_Management' : Advice_To_Management,
            'Auhtor_Info' : Auhtor_Info,
        } 

        ReviewsList.append(Reviews) # to add reviews elements to our list 'ReviewList'
    return
   

ReviewsList = []


#loop into pages
for i in range(1,3,1):
    soup = extract( f'https://www.glassdoor.com/Reviews/Google-Engineering-Reviews-EI_IE9079.0,6_DEPT1007_IP{i}.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng')
    print(f' page {i}')
    
    transform(soup)
    
    print(len(ReviewsList))
    if not soup.find("data-test", class_ = "nextButton css-1hq9k8 e13qs2071"):
        pass
    else:
        break


df = pd.DataFrame(ReviewsList)

df2 = df.drop_duplicates(subset=["Title", "Rating", "Employee_Situation", "Pros", "Cons", "Auhtor_Info"], keep='first')

df2.to_csv('Google Reviews.csv')
print(len(df2))


```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-10-31): When I go to one of the pages on my browser, I don't see any `span` elements with attribute `data-test="advice-management"` or any *"advice to management"* section at all...can you share a screenshot of the part of the page you're trying to scrape and also paste the outerHtml of the `span` element (or maybe it's parent element if it's not too large)?
- **[user19810494](https://stackoverflow.com/users/19810494)** (2022-11-03): I couldn't share a screenshot here. Try to open another review page you'll find in the review Pros, Cons, then Advice to management. I have tried the parent element and it didn't work.
- **me** (2022-11-05): I see it now. I couldn't post earlier, but I've added my suggested solution/s now. hope they're helpful
