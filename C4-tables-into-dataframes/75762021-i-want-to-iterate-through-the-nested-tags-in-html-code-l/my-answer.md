---
title: "i want to iterate through the nested tags in html code like a list or json file"
site: stackoverflow
question_id: 75762021
answer_id: 75796283
url: https://stackoverflow.com/a/75796283
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-20T23:53:59Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75796283/revisions
accepted: false
score: 0
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8f04e4767d2b5e4d3a56e7d1ec9de91ed7de9b748141363683e2313b25754c0e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-20

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75796283>, 2023-03-20; score 0. Text as retrieved 2026-10-12.

Assuming you have

```py
# from bs4 import BeautifulSoup

code_str = '''
<div class = "las">
    <div class = "asas">
      <table style="width:100%">
        <tr><th>Firstname</th><th>Lastname</th><th>Age</th></tr>
        <tr><td>Jill</td><td>Smith</td><td>50</td></tr>
        <tr><td>Eve</td><td>Jackson</td><td>94</td></tr>
        <tr><td>John</td><td>Doe</td><td>80</td></tr>
      </table>
    </div>
</div>
''' 
code = BeautifulSoup(code_str).div 
```

---

> *how can i acces the `<td>Smith</td>` tag for example like that: `code[0][0][1][1]`*

> *I use Beautiful Soup and the only way I know to iterate through the nested tags is with .`parents` and `.children` which becomes pretty confusing*


[ So I'm guessing you won't be happy with just `code.div.table.select('tr')[1].select('td')[1]` or `code.select_one('div>table>tr:nth-child(2)>td:nth-child(2)')` or anything like that. ]

There's also [`.contents`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#contents-and-children) [which returns a list instead of a generator like `.children`], but I would be careful about using *`code.contents[0].contents[0].contents[1].contents[1]`* because `.contents` can include whitespace <sup>(view [`code.table.contents`][1] for example)</sup>.

<br>

You could remove the whitespaces between tags with [regex](https://docs.python.org/3/library/re.html)

```py
# import re
# from bs4 import BeautifulSoup
code = BeautifulSoup(re.sub('>\s*<', '><', code_str).div
```

and then `code.contents[0].contents[0].contents[1].contents[1]` should return `<td>Smith</td>`.

<br>

Or you could write a class that converts `.contents` to nested lists

```py
# import bs4
class indexableTag:
    def __init__(self, origTag:bs4.element.Tag, ignore_whitespace=True):
        self.tag = origTag
        self.tag_contents = [
            indexableTag(c) if isinstance(c,bs4.element.Tag) else c 
            for c in origTag.children
            if not (ignore_whitespace and isinstance(c,str) and not c.strip())
        ]
        
    def __getitem__(self, key): 
        return self.tag_contents[key]

code = indexableTag(bs4.BeautifulSoup(code_str).div)
```

and then `code[0][0][1][1].tag` should return the bs4 Tag `<td>Smith</td>`.

<br>

---

<br>

> *Maybe you can convert the table into `pandas` DataFrame and select the data from it.*  
> &nbsp;&nbsp;&nbsp;&nbsp;– [comment](https://stackoverflow.com/questions/75762021/i-want-to-iterate-through-the-nested-tags-in-html-code-like-a-list-or-json-file#comment133647964_75762021) by [AndrejKesely](https://stackoverflow.com/users/10035985/andrej-kesely)

You can convert the table to a DataFrame with [`read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)<sup>([view DataFrame][2])</sup>

```py
# import pandas as pd 

df = pd.read_html(code_str)[0] ##-> df.loc[0]['Lastname'] #='Smith'
df_dict = df.to_dict() ##-> df_dict['Lastname'][0] #='Smith'
df_recs = df.to_dict('records') ##-> df_recs[0]['Lastname'] #='Smith'
```


  [1]: https://i.sstatic.net/7zO6A.png
  [2]: https://i.sstatic.net/EvV7a.png
