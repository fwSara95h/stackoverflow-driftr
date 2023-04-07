---
title: "Python3 AttributeError: 'NoneType' object has no attribute 'find_all'"
site: stackoverflow
question_id: 75953316
answer_id: 75957925
url: https://stackoverflow.com/a/75957925
author: "Alp Eren Gül"
author_url: https://stackoverflow.com/users/12406183
posted: 2023-04-07T11:17:39Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a5e7a5d0693109a955ccbbcca0a0b7cd24031f5088cd6294112e805d3ac60cdc
role: another answer on the same question, kept as context; not my work
---

# Answer by [Alp Eren Gül](https://stackoverflow.com/users/12406183) — 2023-04-07

Posted on Stack Overflow, <https://stackoverflow.com/a/75957925>, 2023-04-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Sir, you are tyring to get ** class=genre** right? The problem of your code is the class of genre is **inherited to ul** not **div**.

So that simply I changed 

`genres_div = soup.find('div', 'genres')` 

to

    genres_div = soup.find('ul', 'genres')

**If there is anything more I would be very happy to help :)** 

*Hope my answer works for you.*


    import requests
    from bs4 import BeautifulSoup
    
    url = 'https://otakudesu.lol/genre-list/'
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    genres_div = soup.find('ul', 'genres')
    genre_links = genres_div.find_all('a')
    
    path = []
    text = []
    
    for link in genre_links:
        path.append(link['href'])
        text.append(link.text)
    
    print(path)
    print(text)
