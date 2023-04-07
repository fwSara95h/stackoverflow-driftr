---
title: "Python3 AttributeError: 'NoneType' object has no attribute 'find_all'"
site: stackoverflow
question_id: 75953316
answer_id: 75955862
url: https://stackoverflow.com/a/75955862
author: "user510170"
author_url: https://stackoverflow.com/users/21048071
posted: 2023-04-07T06:06:52Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b2225c6b28b59594db12a82eff3912bc5183cb7035e59a938a57e9a2ebc0feda
role: another answer on the same question, kept as context; not my work
---

# Answer by [user510170](https://stackoverflow.com/users/21048071) — 2023-04-07

Posted on Stack Overflow, <https://stackoverflow.com/a/75955862>, 2023-04-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You have an error in this place `genres_div = soup.find('div', class_='genres')` . you are looking for the `'div'` tag, but you should be looking for the `'ul'` tag. Here is the working code:

    import requests
    from bs4 import BeautifulSoup
    
    url = 'https://otakudesu.lol/genre-list/'
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    genres_div = soup.find('ul', class_='genres')
    genre_links = genres_div.find_all('a')
    
    path = []
    text = []
    
    for link in genre_links:
        path.append(link['href'])
        text.append(link.text)
    
    print(path)
    print(text)

Result:

    ['/genres/action/', '/genres/adventure/', '/genres/comedy/', '/genres/demons/', '/genres/drama/', '/genres/ecchi/', '/genres/fantasy/', '/genres/game/', '/genres/harem/', '/genres/historical/', '/genres/horror/', '/genres/josei/', '/genres/magic/', '/genres/martial-arts/', '/genres/mecha/', '/genres/military/', '/genres/music/', '/genres/mystery/', '/genres/psychological/', '/genres/parody/', '/genres/police/', '/genres/romance/', '/genres/samurai/', '/genres/school/', '/genres/sci-fi/', '/genres/seinen/', '/genres/shoujo/', '/genres/shoujo-ai/', '/genres/shounen/', '/genres/slice-of-life/', '/genres/sports/', '/genres/space/', '/genres/super-power/', '/genres/supernatural/', '/genres/thriller/', '/genres/vampire/']
    ['Action', 'Adventure', 'Comedy', 'Demons', 'Drama', 'Ecchi', 'Fantasy', 'Game', 'Harem', 'Historical', 'Horror', 'Josei', 'Magic', 'Martial Arts', 'Mecha', 'Military', 'Music', 'Mystery', 'Psychological', 'Parody', 'Police', 'Romance', 'Samurai', 'School', 'Sci-Fi', 'Seinen', 'Shoujo', 'Shoujo Ai', 'Shounen', 'Slice of Life', 'Sports', 'Space', 'Super Power', 'Supernatural', 'Thriller', 'Vampire']
