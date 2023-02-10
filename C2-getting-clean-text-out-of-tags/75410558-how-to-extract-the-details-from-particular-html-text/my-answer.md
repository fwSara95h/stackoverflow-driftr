---
title: "How to extract the details from particular HTML text"
site: stackoverflow
question_id: 75410558
answer_id: 75411642
url: https://stackoverflow.com/a/75411642
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-10T13:15:01Z
last_edited: 2023-02-10T13:22:48Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75411642/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 09c6479f11a75bef2060ac857e91d2f3249a8002ee3a55a31cbcd19972de3681
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75411642>, 2023-02-10, last edited 2023-02-10; score 0. Text as retrieved 2026-10-12.

When I try your code, it prints 

> ```lang-none
> Address
> ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
> ```

You should take note of the second line, because *`item.findAll("td").text`* will always raise error; you can instead do something like `'\n'.join([td.text for td in item.findAll("td")])` and that should not raise any error.

However, it will return only an empty string [as `item.findAll("td")` is an empty `ResultSet`] because with *`for item in labels....item.findAll("td")...`*, you're looking for `td` tags *inside* the `label` tags when they're actually in a `table` tag **next** to the label. 

---

#### Solution 1: Using [`.find_next_siblings`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-next-siblings-and-find-next-sibling)

```python 
soup = BeautifulSoup(html_content, 'html.parser')
form_data = soup.find("div",{"id":"formContents"})
if form_data:
    section_data = soup.find_all("div",{"class":"sectionDiv expanded"})
    for datas in section_data:
        labels = datas.find_all("label",{"class":"fieldLabel"})
        for item in labels: 
            print(item.text) ## label
            for nxtTable in item.find_next_siblings('table'):
                print('\n'.join([td.text for td in nxtTable.find_all("td")]))
                break ## [ only takes the first table ]
```

<sup>[Like this, you shouldn't need the `try...except` either.]</sup>

And [for me] that printed

>```python
> Address
> 
> 
> 1183
> Pelham Wood Dr, Rock Hill, SC 29732
> 
> 
>```

---

#### Solution 2: Using [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) 

```python
soup = BeautifulSoup(html_content, 'html.parser')

section_sel = 'div#formContents div.sectionDiv.expanded'
label_sel = 'label.fieldLabel'
for datas in soup.select(f'{section_sel}:has({label_sel}+table td)'):
    labels = datas.select(f'{label_sel}:has(+table td)')
    labels = [' '.join(l.get_text(' ').split()) for l in labels]
    entity_data = [' '.join([
        ' '.join(td.get_text(' ').split()) for td in ed.select('td')
    ]) for ed in datas.select(f'{label_sel}+table:has(td)')]
    # data_dict = dict(zip(labels, entity_data))
    for l, ed in zip(labels, entity_data): print(f'{l}: {ed}')
```

And that should print 

> ```python
> Address: 1183 Pelham Wood Dr, Rock Hill, SC 29732
> ```

Btw, *`dict(zip(labels, entity_data))`* would have returned <kbd>`{'Address': '1183 Pelham Wood Dr, Rock Hill, SC 29732'}`</kbd>, and I've used `' '.join(td.get_text(' ').split())` instead of just `td.text` (and same with `l` in `labels`) to minimize whitespace and get everything in one line.

---

**Note:** Both solutions become less reliable unless each label is for exactly one table; the second solution assumes that the table is [directly adjacent](https://facelessuser.github.io/soupsieve/selectors/combinators/#adjacent-sibling-combinator) to the label (and will skip any labels without an adjacent table with `td` tags); and the first solution risks taking a table from the next label if a label is missing a table after it.
