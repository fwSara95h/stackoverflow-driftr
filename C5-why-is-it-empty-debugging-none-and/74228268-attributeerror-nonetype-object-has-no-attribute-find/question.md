---
title: "AttributeError: nonetype object has no attribute 'find'"
site: stackoverflow
question_id: 74228268
url: https://stackoverflow.com/q/74228268
asked: 2022-10-27T21:01:32Z
asked_by: "Mikehouse627"
asked_by_url: https://stackoverflow.com/users/20352300
last_edited: 2022-10-27T21:05:03Z
last_editor: "RJ Adriaansen"
last_editor_url: https://stackoverflow.com/users/11380795
tags: [python, html, beautifulsoup, attributeerror]
score: -1
views_at_snapshot: 301
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d00efe80bd003864f5990113fe07eb2dc1082f60ae9200124a6f62b1f5dbb44c
---

# AttributeError: nonetype object has no attribute 'find'

Asked by [Mikehouse627](https://stackoverflow.com/users/20352300) on Stack Overflow, <https://stackoverflow.com/q/74228268>, 2022-10-27, last edited 2022-10-27 by [RJ Adriaansen](https://stackoverflow.com/users/11380795). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

    from bs4 import BeautifulSoup
    import requests
    
    job_request = requests.get('https://www.google.com/search?q=Software+engineer+&sxsrf'
                               '=ALiCzsaeLLjcCHZk46ernxCkoay7ldkDsA:1666897166012&source=hp&ei=DdVaY-CHOvvgkPIPxc2m6Ag'
                               '&iflsig=AJiK0e8AAAAAY1rjHgG0CdqkcKPC3aVnmBvSGuZgc6Py&uact=5&oq=Job+listings&gs_lcp'
                               '=Cgdnd3Mtd2l6EAMyBwgjEMkDECcyCggAEIAEEIcCEBQyDQgAEIAEELEDEIMBEAoyDQgAEIAEELEDEIMBEAo'
                               'yBQgAEIAEMgUIABCABDIFCAAQgAQyCggAEIAEELEDEAoyDQgAEIAEELEDEIMBEAoyDQgAEIAEELEDEIMBEAo6BAg'
                               'jECc6BQgAEJECOgsILhCABBCxAxCDAToLCAAQgAQQsQMQgwE6CwguEIAEEMcBENEDOg4ILhCABBCxAxCDARDUAjoLCC'
                               '4QgAQQsQMQ1AI6EQguEIAEELEDEIMBEMcBEK8BOggIABCABBCxAzoHCAAQgAQQCjoICAAQyQMQkQI6EAgAEIAEEIcCE'
                               'LEDEIMBEBQ6DQgAEIAEEIcCELEDEBQ6CwguELEDEMcBENEDOhMILhCABBCHAhCxAxDHARDRAxAUOgsILhCABBDHARCv'
                               'AToICC4QgAQQ5QRQAFjbFGDEFWgCcAB4AYABoQGIAcYLkgEEMy4xMJgBAKABAQ&sclient=gws-wiz&ibp=htl;jobs'
                               '&sa=X&ved=2ahUKEwijh7Dti4H7AhXzkWoFHddJCAMQudcGKAJ6BAgNEC8#fpstate=tldetail&htivrt=jobs&ht'
                               'idocid=4XlU2-oL0UgAAAAAAAAAAA%3D%3D').text

    beautify = BeautifulSoup(job_request, 'lxml')
    listing = beautify.find('li', class_ = 'iFjolb gws-plugins-horizon-jobs__li-ed')
    company = listing.find('div', class_ = 'oNwCmf').text


I am new to HTML and web scraping, I am not sure how exactly the 'div' tags are found by BS4. Any help would be appreciated. The end goal is to scrape the listings from a site and eventually import them to a DB.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[RJ Adriaansen](https://stackoverflow.com/users/11380795)** (2022-10-27): There's nothing wrond with your code, it's just that there is no div with the class `oNwCmf` in the html. You'll probably need to include a user agent to get proper code returned. You could check out working [examples](https://github.com/Nv7-GitHub/googlesearch/blob/master/googlesearch/__init__.py) for inspiration
