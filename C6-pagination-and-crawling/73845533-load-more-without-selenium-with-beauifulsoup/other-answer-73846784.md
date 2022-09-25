---
title: "Load more without Selenium with beauifulsoup"
site: stackoverflow
question_id: 73845533
answer_id: 73846784
url: https://stackoverflow.com/a/73846784
author: "Md. Fazlul Hoque"
author_url: https://stackoverflow.com/users/12848411
posted: 2022-09-25T18:11:18Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e8b8661ec06d1be09efca5229e42fb1481004963806fe0ccf0a962e5f058f527
role: another answer on the same question, kept as context; not my work
---

# Answer by [Md. Fazlul Hoque](https://stackoverflow.com/users/12848411) — 2022-09-25

Posted on Stack Overflow, <https://stackoverflow.com/a/73846784>, 2022-09-25; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

When you will click on load more button,it will produce a new link each time dynamically via API aka `AJAX` response. So you have to inject ajax urls  in the `requests` instead

**Example:**


    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    urls = [
        'https://www.imdb.com/title/tt0120762/reviews/_ajax?ref_=undefined&paginationKey=g4wp7cjoqizdozag7gwh7mbsrdt4oarhzfmxvlnomwklyczuf43o6ss4oi2fjnzlcv4k5vpwgij3rxavgvrc4fh3xk7rdci',
        'https://www.imdb.com/title/tt0120762/reviews/_ajax?ref_=undefined&paginationKey=g4wp7cbpqm3diyye7gwxtojsrtsm2ab6y4hhzo5ziwr26fbyhvrl4ty4omzfzpzidfrndtutkdwxvupszultfj3so4pyucl5',
        'https://www.imdb.com/title/tt0120762/reviews/_ajax?ref_=undefined&paginationKey=g4wp7dzer45tmzid72uxrmbtqpq44abhzfmxvlnomwklyczuf43o6ss5oe4fxnzccr4k4gyilrq5gdyzwdh66tpk3her65y',
        'https://www.imdb.com/title/tt0120762/reviews/_ajax?ref_=undefined&paginationKey=g4wp7dziqm2tgzal7oxx3mrvrps4mbz6y4hhzo5ziwr26fbyhvrl4ty4oq2v5nrid5v5dtqwtdkd36p5cbngo6zt6ktweyiw',
        'https://www.imdb.com/title/tt0120762/reviews/_ajax?ref_=undefined&paginationKey=g4wp7dzmqaytmzyl7kxhvnjsr3r4shjjtzpwzouokkd2gbzgpnt6uc23pazvzmjpb4dwuzntzuw22wncxv32ezsep2i5o'
        ]
    
    data=[]   
    for url in urls:
        source = requests.get(url)
        #print(source)
        soup = BeautifulSoup(source.text,'html.parser')
        reviews = soup.find_all('div', class_="review-container")
    
        for review in reviews:
            title= review.find('a',class_="title").get_text(strip=True)
            review_date= review.find('span',class_="review-date").text
            review_text= review.find('div', class_="content").get_text(strip=True)     
        
            data.append({
                'title':title,
                'review_date':review_date,
                'review_text':review_text
                })
        
    df = pd.DataFrame(data)# to_csv('out.csv',index=False)
    print(df)
       
**Output:**


                                                     title  ...                                        review_text
    0                                                Great  ...  This is really a Disney classic and one of the...      
    1                                                 Wow.  ...  Definitely one of my favourite Disney movies e...      
    2    One of the best animated movies ever. A "Best ...  ...  My Take: Yet another Disney classic. Impressiv...      
    3                                             Amazing!  ...  I love Mulan! It has intense moments, great co...      
    4                          Another great Disney modern  ...  Modern Disney is kind of a funny thing with me...      
    ..                                                 ...  ...                                                ...      
    118                                   Mephisto in Onyx  ...  Tony Bancroft directs "Mulan", an animated mus...      
    119                      Not as bad as I first thought  ...  I'll be honest here. I started watching this m...      
    120                     excellent Disney animated film  ...  once again we have another excellent animated ...      
    121                                       Great Movie!  ...  MULAN is a great movie which has many memorabl...      
    122                                           briliant  ...  Mulan is probably Disney's first attempt at a ...      
    
    [123 rows x 3 columns]
