---
title: "How to make a dictionary from 2 lists from web scraping"
site: stackoverflow
question_id: 74596046
url: https://stackoverflow.com/q/74596046
asked: 2022-11-28T04:39:25Z
asked_by: "Raffel Ravionaldo"
asked_by_url: https://stackoverflow.com/users/18388803
last_edited: 2022-11-28T05:27:13Z
tags: [python, dataframe, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 162
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7a126b138642cd222b9710cbd40ffb08e2f98290c924c91b7d4c0c7dbf6ce464
---

# How to make a dictionary from 2 lists from web scraping

Asked by [Raffel Ravionaldo](https://stackoverflow.com/users/18388803) on Stack Overflow, <https://stackoverflow.com/q/74596046>, 2022-11-28, last edited 2022-11-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to make a dataframe from web scrapping this page : https://www.airlinequality.com/airline-reviews/british-airways. 

The value i have is reviews from passenger and rating that passenger give, but i dont know how to make it to be a dataframe

this is my code : 


    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    
    base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
    pages = 5 #10
    page_size = 1 #100
    
    reviews = []
    aircraft = []
    seat_type = []
    route = []
    recommended = []
    rating = []
    category = []
    
    for i in range(1, pages + 1):
    
        print(f"Scraping page {i}")
    
        # Create URL to collect links from paginated data
        url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"
    
        # Collect HTML data from this page
        response = requests.get(url)
    
        # Parse content
        content = response.content
        parsed_content = BeautifulSoup(content, 'html.parser')
        for para in parsed_content.find_all("div", {"class": "text_content"}):
            reviews.append(para.get_text())
            
        for para2 in parsed_content.find_all("div", {"class" : "review-stats"}):
            for para3 in para2.find_all('td',{'class' : 'review-value'}):
                rating.append(para3.get_text())
            recomend = rating[-1]
            rating = rating[:-1]
            for para4 in para2.find_all('td',{'class' : 'review-rating-stars stars'}):
                para5 = len(para4.find_all('span', {'class' : 'star fill'}))
                rating.append(para5)
            rating.append(recomend)
            #print(rating)
            for para6 in para2.find_all('td',{'class' : 'review-rating-header'}):
                category.append(para6.get_text())
            #print(category)
            
        print(f"   ---> {len(reviews)} total reviews")

output i get : 
[![enter image description here][1]][1]
[![enter image description here][2]][2]
[![enter image description here][3]][3]

in a simple way, that is what I was asking :

first looping: category is  [a, b, c, d, e] rating is [1, 2, 3, 4, 5]

second looping: the category will append with [a, c, e, o, p, q] and rating will append with [9, 8, 7, 6, 5, 4]

so the final data :

category = [a, b, c, d, e, a, c, e, o, p, q]

rating   = [1, 2, 3, 4, 5, 9, 8, 7, 6, 5, 4]

output that I want:

[![enter image description here][5]][5]


  [1]: https://i.sstatic.net/Xni5F.png
  [2]: https://i.sstatic.net/k7Lmn.png
  [3]: https://i.sstatic.net/LWC4X.png
  [4]: https://i.sstatic.net/tAXq9.png
  [5]: https://i.sstatic.net/x8fG6.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Shrirang Mahajan](https://stackoverflow.com/users/17353907)** (2022-11-28): Use `pd.Dataframe()` and pass the data in it.
- **[Raffel Ravionaldo](https://stackoverflow.com/users/18388803)** (2022-11-28): I tried it and just created two columns, I've entered your input results
- **[Rabinzel](https://stackoverflow.com/users/15521392)** (2022-11-28): `pd.DataFrame([rating], columns=category)` will get what you want here.
