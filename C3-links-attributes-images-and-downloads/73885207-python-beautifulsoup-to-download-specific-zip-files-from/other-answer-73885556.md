---
title: "python beautifulsoup to download specific .zip files from a website"
site: stackoverflow
question_id: 73885207
answer_id: 73885556
url: https://stackoverflow.com/a/73885556
author: "Md. Fazlul Hoque"
author_url: https://stackoverflow.com/users/12848411
posted: 2022-09-28T17:23:18Z
last_edited: 2022-09-28T17:47:08Z
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e085df3c02ebcdd834556d31605f418f055d54c6781259ba79aafa10e3d858df
role: another answer on the same question, kept as context; not my work
---

# Answer by [Md. Fazlul Hoque](https://stackoverflow.com/users/12848411) — 2022-09-28

Posted on Stack Overflow, <https://stackoverflow.com/a/73885556>, 2022-09-28, last edited 2022-09-28; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Try the next example
    
    import requests
    from bs4 import BeautifulSoup

    URL = "https://download.cms.gov/nppes/NPI_Files.html"
    r = requests.get(URL)
    #print(r.content)
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.prettify())
    links=[]
    
    for ref in soup.select('div.bulletlistleft > ul > li')[2:]:
        zip ='https://download.cms.gov/nppes'+ref.a.get('href').replace('./','/')
        links.append(zip)
    print(links)

**Output:**

    ['https://download.cms.gov/nppes/NPPES_Data_Dissemination_090522_091122_Weekly.zip', 'https://download.cms.gov/nppes/NPPES_Data_Dissemination_091222_091822_Weekly.zip', 'https://download.cms.gov/nppes/NPPES_Data_Dissemination_091922_092522_Weekly.zip']

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Anusha](https://stackoverflow.com/users/19907888)** (2022-09-28): thank you so much, it worked like a charm :) i have just changed to this  #links=[]  for ref in soup.select('div.bulletlistleft > ul > li')[2:]:     zip ='https://download.cms.gov/nppes'+ref.a.get('href').replace('./','/')     #links.append(zip)     wget.download(zip)
