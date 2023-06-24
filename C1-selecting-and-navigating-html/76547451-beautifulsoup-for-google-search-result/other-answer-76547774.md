---
title: "beautifulsoup for google search result"
site: stackoverflow
question_id: 76547451
answer_id: 76547774
url: https://stackoverflow.com/a/76547774
author: "jackal"
author_url: https://stackoverflow.com/users/17580381
posted: 2023-06-24T19:54:09Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: aa789d82740838e7fa585f653b045260d40baee6693de61aaa0ff1c26c5ce656
role: another answer on the same question, kept as context; not my work
---

# Answer by [jackal](https://stackoverflow.com/users/17580381) — 2023-06-24

Posted on Stack Overflow, <https://stackoverflow.com/a/76547774>, 2023-06-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You will need to provide a User-Agent.

You should write a function to acquire the query string.

Then:

    import requests
    from bs4 import BeautifulSoup as BS
    
    GOOGLE = 'https://www.google.com/search'
    
    # Use this function to get the query - e.g., user input, command line argument
    def get_query() -> str:
        return 'Up Daily News'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15'
    }
    
    query = get_query()

    params = {
        'q': query
    }
    
    with requests.get(GOOGLE, params=params, headers=headers) as response:
        response.raise_for_status()
        soup = BS(response.text, 'lxml')
        if (h3 := soup.find_all('h3')):
            for h in h3[:3]:
                print(h.getText())
