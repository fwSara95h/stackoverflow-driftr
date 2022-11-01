---
title: "Webscraping - Python - attribute href"
site: stackoverflow
question_id: 74282355
url: https://stackoverflow.com/q/74282355
asked: 2022-11-01T22:12:17Z
asked_by: "Hélder Neves"
asked_by_url: https://stackoverflow.com/users/20392176
last_edited: 2022-11-01T22:14:01Z
tags: [python, html, web-scraping, beautifulsoup, python-requests]
score: 0
views_at_snapshot: 38
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8cf2903fb3827954a848ed2f254ad6b0cc986bb4897b356ad60af0ab9279207e
---

# Webscraping - Python - attribute href

Asked by [Hélder Neves](https://stackoverflow.com/users/20392176) on Stack Overflow, <https://stackoverflow.com/q/74282355>, 2022-11-01, last edited 2022-11-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I got the fallowing:
```
<h4><a class="" href="https://www.eloscimento.com.br/diversos/" title="Diversos">Diversos</a></h4>,
<h4><a class="" href="https://www.eloscimento.com.br/pintura/" title="Pintura">Pintura</a></h4>,
```

I am trying to get only the attribute href in this html website. My script:


```
request = requests.get('https://www.eloscimento.com.br')

site_html = BeautifulSoup(request.text, 'html.parser')
site_html

h4 = site_html.find_all('h4')
h4.get('href')
```
I'm learning beautifulsoup and selenium and i appreciate if you guys help me with this error. Thanks!!!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrew Ryan](https://stackoverflow.com/users/7451892)** (2022-11-01): as you are using `find_all()` you are creating a list of elements. Therefore to get the items you should instead do `for item in h4: print(item.get('href'))` so that you can access each individual element and print out the href for that element
- **[Hélder Neves](https://stackoverflow.com/users/20392176)** (2022-11-01): Hi, Andrew. I've tried what you said and i got this return:  for item in h4:     print(item.get('href'))  output: None None None None None None None None None None None None None None None None None None
- **[Andrew Ryan](https://stackoverflow.com/users/7451892)** (2022-11-01): Yeah it is outputting None because the item that you want to get is to first get the `a` tag's `href` which is not what you are doing you are just getting the h4 item's href which there is none.
- **[Community](https://stackoverflow.com/users/-1)** (2022-11-01): Please clarify your specific problem or provide additional details to highlight exactly what you need. As it's currently written, it's hard to tell exactly what you're asking.
- **[Hélder Neves](https://stackoverflow.com/users/20392176)** (2022-11-02): Andrew, I want to get the url. I want all of then in a list.    - In this case, i want url:  ** https://www.eloscimento.com.br/diversos/ ** https://www.eloscimento.com.br/pintura/  but when I try to get the url, my output is printing  <h4><a class="" href="https://www.eloscimento.com.br/diversos/" title="Diversos">Diversos</a></h4>
