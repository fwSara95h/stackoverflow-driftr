---
title: "Beautiful Soup scraping Realtor.com. Four elements have same class. How to search using data-label?"
site: stackoverflow
question_id: 74483760
url: https://stackoverflow.com/q/74483760
asked: 2022-11-18T00:43:09Z
asked_by: "jbarratt"
asked_by_url: https://stackoverflow.com/users/20004643
last_edited: 2022-11-18T01:10:41Z
last_editor: "andrewJames"
last_editor_url: https://stackoverflow.com/users/12567365
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 111
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c9285b9cad5c1be37766cd23e4ad590b9d9b59852e6c20629d3e97d36f1cad40
---

# Beautiful Soup scraping Realtor.com. Four elements have same class. How to search using data-label?

Asked by [jbarratt](https://stackoverflow.com/users/20004643) on Stack Overflow, <https://stackoverflow.com/q/74483760>, 2022-11-18, last edited 2022-11-18 by [andrewJames](https://stackoverflow.com/users/12567365). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm attempting my first web scraping using realtor.com.

While trying to extract property card info I ran into an issue searching by class. # bedrooms/#bathrooms/home square feet, and property square feet have the exact same class name. 
When doing a find_all search I am unable to print "text only" because find_all prints to a list.

Is there a way for me to expand search criteria by searching by data-label?? 

Here is my code:

    from bs4 import BeautifulSoup
    import requests

    #have to use to agent faker (below) specific to windows and chrome!
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,         like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    url = "https://www.realtor.com/realestateandhomes-search/Spring-Hill_FL"
    page = requests.get(url, headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    lists = soup.find_all('li', class_="jsx-1881802087 component_property-card")
    #print(lists)
    print('___________________________________________________')
    #for item in soup.select('.component_property-card'): 
    #    print(item)
    #    print('---------------')

    for list in lists:
        price = list.find('div', class_='ldp-redesign-price').text
        address = list.find('div', class_='address').text
        #summary = list.find('div', class_='summary-wrap').text

        beds = list.find('li', class_='prop-meta')

        info = [price, address, beds]
        print(info)
