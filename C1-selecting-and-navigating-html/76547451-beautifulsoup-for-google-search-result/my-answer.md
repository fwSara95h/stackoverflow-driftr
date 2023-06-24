---
title: "beautifulsoup for google search result"
site: stackoverflow
question_id: 76547451
answer_id: 76547860
url: https://stackoverflow.com/a/76547860
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-24T20:23:26Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76547860/revisions
accepted: false
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ed16e9a6a0e23aac850e02d5c08cc2eef7e2a849a596bc8e1358b4087decd049
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76547860>, 2023-06-24; score 1. Text as retrieved 2026-10-12.

> Expecting this:
> 
> 1. Title, Link, Description of Search Results for first three result only

You can use [selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors-through-the-css-property) to target these; for example:

```py
def search_google(text, max_results=3):
    ## split then join to convert spaces to + in link
    url = 'https://google.com/search?q=' + '+'.join(text.split())
    print('From', url, '\n---\n')
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    ## loop through only the first results up to max_results
    for d in soup.select('div:has(>div>a[href] h3)')[:max_results]:
        print(d.h3.get_text(' ').strip()) ## title

        ## link
        res_link = d.select_one('a[href]:has(h3)').get('href') 
        if res_link.startswith('/url?q='):
            res_link = res_link.split('=',1)[1].split('&')[0]
        print(res_link) 

        ## description
        print(d.select_one('div:has(>a[href] h3)+div').get_text(' ').strip())

        print('\n---\n') ## separate results
```

---

> Expecting this:

> 2. Below code I mentioned keyword in python file itself. how to make it dynamic(when run the file, it should ask me for keyword)

Notice how I parametrized `text` in the function above. There are several ways to take user input in python, `sys.argv[1:]` would be one method, but I personally prefer the [`input`](https://www.programiz.com/python-programming/methods/built-in/input) function, especially since you can put `search_google` in a while loop and search as many times as the user want.

```py
while (q:=input("Enter query [or q to exit]")) != 'x': search_google(q)
```


---

See these two examples using `input` and the `search_google` function from above:


|Search Query|Rendered HTML|Printed Output|
|:-:|:-:|:-:|
|"UP Daily News"|[![html1][1]][1]|[![op1][2]][2]|
|"iPhone Prices"|[![html2][3]][3]|[![op2][4]][4]|


  [1]: https://i.sstatic.net/zZSDs.png
  [2]: https://i.sstatic.net/OhyXK.png
  [3]: https://i.sstatic.net/KqLsp.png
  [4]: https://i.sstatic.net/ok1WE.png
