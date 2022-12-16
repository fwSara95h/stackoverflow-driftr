---
title: "Webscraping all available repos from a topic search on github"
site: stackoverflow
question_id: 74796978
answer_id: 74821773
url: https://stackoverflow.com/a/74821773
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-16T08:15:49Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74821773/revisions
accepted: true
score: 2
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f60c73410070a2e72bf568cfe00723a1abab56c443562d3e9d5835c90685fc68
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74821773>, 2022-12-16; **accepted**; score 2. Text as retrieved 2026-10-12.

Lazy fix: [`zip`](https://www.programiz.com/python-programming/methods/built-in/zip) all the lists together so that the columns are cropped to match lengths with the shortest one. <sub>[[DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) data: list of dictionaries formed using [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp).]</sub>

```python
pd.DataFrame([{'name': n, 'url': u, 'about': a} for n, u, a 
               in zip(stock_names, stock_urls, stock_about)])
```

---

But there's a problem that would then be ignored: if the lists don't match up, how can you know that `stock_names[i]` and `stock_urls[i]` and `stock_about[i]` [for any given `i`] are of the same repo? The lists don't match up because some repos are missing an "about" section, but because the lists are built individually, you don't have any way to figure out which ones.

That's why it's better to merge the loops [in a sense] - loop through the [*containers* of individual results](https://i.sstatic.net/1572f.png) and build `dico` up as a list of dictionaries right from the start, result by result:

```python
dico = []

for page in range(1, 99):

    req = requests.get(search_topics + str(page) + "&q=" + "nlp" + "&type=Repositories", headers = headers)
    soup = BeautifulSoup(req.text, "html.parser")

    # for repo in soup.find('ul', class_="repo-list").find_all('li'):
    for repo in soup.select('ul.repo-list>li:has(a.v-align-middle[href])'):
        link = repo.select_one('a.v-align-middle[href]')
        about = repo.select_one('p.mb-1') 

        dico.append({
            # 'name': re.sub(r"\/(.*)\/(.*)", "\1", link.get('href')),
            'name': ' by '.join(link.text.strip().split('/', 1)[::-1]),
            'url': "https://github.com" + link.get('href'),
            'about': about.text.strip() if about else None
        })

df = pandas.DataFrame(dico)
```

---

`df` looks something like

[![df][1]][1]


  [1]: https://i.sstatic.net/XhaKt.png
