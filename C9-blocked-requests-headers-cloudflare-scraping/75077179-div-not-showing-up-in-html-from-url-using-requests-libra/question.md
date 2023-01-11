---
title: "div not showing up in html from url using requests library and bs4"
site: stackoverflow
question_id: 75077179
url: https://stackoverflow.com/q/75077179
asked: 2023-01-11T00:17:31Z
asked_by: "Tendekai Muchenje"
asked_by_url: https://stackoverflow.com/users/1029902
last_edited: never
tags: [python, web-scraping, beautifulsoup, python-requests]
score: -1
views_at_snapshot: 106
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ef7669c14bafbd324b60d467da3d04664bf7dea7c908006feb8bb2a2c7c05487
---

# div not showing up in html from url using requests library and bs4

Asked by [Tendekai Muchenje](https://stackoverflow.com/users/1029902) on Stack Overflow, <https://stackoverflow.com/q/75077179>, 2023-01-11. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a simple script where I want to scrape a menu from a url:

https://untappd.com/v/glory-days-grill-of-ellicott-city/3329822

When I inspect the page using dev tools, I identify that the menu contained in the menu section `<div class="menu-area" id="section_1026228">`

So my script is fairly simple as follows:

    import requests
    from bs4 import BeautifulSoup
    
    venue_url = 'https://untappd.com/v/glory-days-grill-of-ellicott-city/3329822'
    
    response = requests.get(venue_url, headers = {'User-agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    menu = soup.find('div', {'class': 'menu-area'})
    print(menu.text)

I have tried this on a locally saved page of the url and it works. But when I do it to the full url using the requests library, it does not work. It cannot find the div. It throws this error:

    print(menu.text)
    AttributeError: 'NoneType' object has no attribute 'text'

which basically means it cannot find the div. Does anyone know why this is happening and how to fix it?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-01-11): I'm not seeing a `menu-area` on this page. Do you need to be logged-in to see it?
- **[Tendekai Muchenje](https://stackoverflow.com/users/1029902)** (2023-01-11): @AndrejKesely interesting. It seems so. I just logged out from my browser and it showed me a different page. However, my script has no login part at all. Not even sure how that would work
- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-01-11): Probably this is relevant: https://stackoverflow.com/questions/11892729/how-to-log-in-to-a-website-using-pythons-requests-module
- **[Parsa Abbasi](https://stackoverflow.com/users/9346942)** (2023-01-11): As @AndrejKesely said, you should log in first by creating a `requests.Session()` and making a POST request.  Furthermore, the ID you provided may change over time as I suppose it is associated with your account. Therefore, I recommend to search for a more general identifier or selector.
