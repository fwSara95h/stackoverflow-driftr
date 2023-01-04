---
title: "Error bs4: find_all | development vs production"
site: stackoverflow
question_id: 75011354
url: https://stackoverflow.com/q/75011354
asked: 2023-01-04T21:08:41Z
asked_by: "Felipe"
asked_by_url: https://stackoverflow.com/users/20751338
last_edited: 2023-01-04T22:15:39Z
tags: [python, beautifulsoup]
score: -1
views_at_snapshot: 66
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 44c3a04f88ee74f93279512820aa76a611417dcd38b4a9ef4e7c7576c0fdc543
---

# Error bs4: find_all | development vs production

Asked by [Felipe](https://stackoverflow.com/users/20751338) on Stack Overflow, <https://stackoverflow.com/q/75011354>, 2023-01-04, last edited 2023-01-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have no issues while running the below code in my development machine (localhost):

```
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

exampleFile = requests.get(f'https://statusinvest.com.br/acoes/petr4',headers=headers)
exampleSoup = bs4.BeautifulSoup(exampleFile.text, features="html.parser")
container_indicadores = exampleSoup.find('div', {'class': "indicator-today-container"}).find_all('div', {'title': True})
```

But, I've just pushed to Railway server (production) and now it rises the error:

```
'NoneType' object has no attribute 'find_all'
```

My goal is to grab all **divs** who have anything inside **title** and are inside the `div class="indicator-today-container"`

Info:

- python version is almost the same: production 3.10.8 | localhost: 3.10.1

- bs4 is in requirements as 4.11.1 - I'm assuming there is no difference between production and localhost

- Windows OS is in my localhost and I assume Linux is @ Railway server

Any idea?


EDIT:

I added 02 variables to find out the error:

    example = exampleFile.text
    first = exampleSoup.find('div', {'class': "indicator-today-container"})

Values:

     example = ('<!DOCTYPE html>\n'
     '<html lang="en-US">\n'
     '<head>\n'
     '    <title>Just a moment...</title>\n'
     '    <meta http-equiv="Content-Type" content="text/html; 
     charset=UTF-8">\n'
     '    <meta http-equiv="X-UA-Compatible" content="IE=Edge">\n'
     '    <meta name="robots" content="noindex,nofollow">\n'
     '    <meta name="viewport" content="width=device-width,initial- 
     scale=1">\n'
     '    <link href="/cdn-cgi/styles/challenges.css" 
     rel="stylesheet">\n'
     '    \n'
     '\n'
     '</head>\n'...)

But **first** variable is `None`

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Tim Roberts](https://stackoverflow.com/users/1883316)** (2023-01-04): Have you printed out `exampleFile.text` to see what you get?  Perhaps the site blocks certain IPs.
- **[Felipe](https://stackoverflow.com/users/20751338)** (2023-01-04): @TimRoberts, I just edited the question to print out the error! It seems `example` variable is a string and has value but `first` variable is None type.
