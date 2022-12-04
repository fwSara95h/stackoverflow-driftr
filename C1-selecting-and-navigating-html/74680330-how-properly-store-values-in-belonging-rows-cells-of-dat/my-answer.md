---
title: "How properly store values in belonging rows/cells of dataframe while scraping with Beautiful Soup?"
site: stackoverflow
question_id: 74680330
answer_id: 74681188
url: https://stackoverflow.com/a/74681188
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-04T21:41:43Z
last_edited: 2022-12-05T14:50:09Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74681188/revisions
accepted: true
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: [getText_bySelector, selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 40da41542899a18dd083c26558ca4b734e91132e3e6d2958a5c07df9c37e1c4a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74681188>, 2022-12-04, last edited 2022-12-05; **accepted**; score 1. Text as retrieved 2026-10-12.

For cases like this, you should use nested loops - an outer loop for the containers ResultSet (`soup.select('article.obj_article_details')` here), and the inner loop/s for the details you want - title/author/affiliation/etc. And it's also better to build a dictionary of the details for each container and add it to a list of dictionaries than to try to bind together separate lists (you've already faced some of the issues that are caused by that approach).

---

Since you're doing the same thing for each detail (`select` followed by `get_text`), it would be more convenient to move those operations to a function like
```python
def getText_bySelector(tagSoup, selector, sep=None):
    selTags = tagSoup.select(selector) if selector else [tagSoup]
    if type(sep) == str: 
        return sep.join([s.get_text(' ').strip() for s in selTags])
    return selTags[0].get_text(' ').strip() if selTags else None
```
<sub>(This is a variation of [this function](https://pastebin.com/ZnZ7xM6u), which I use in most of my bs4 projects.)</sub>

If you pass a string (like `, `/`; `/etc) as `sep`, it will join all the results with it (or return an empty string [""] if there are no results); otherwise, it will return the first result (or `None` if there are no results). 

Another reason I like using functions like this is that it allows me to use [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) instead the innermost `for` loop.

---

Then, you just need to define a reference dictionary with the arguments you'll need to pass to `getText_bySelector`
```python
refDict = {
    'title': ('.page_title', None), 
    'authors': ('.authors .name', ', '),
    'affiliations': ('.item.authors .affiliation', '; ')
} 
```

---

Now you can built a list of dictionaries with
```python
dictList = []
for i in urls: 
    page = requests.get(link)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")

    dictList += [{
        k: getText_bySelector(a, vsel, vsep) 
        for k, (vsel, vsep) in refDict.items()
    } for a in soup.select('article.obj_article_details')]
```

---

The items in `dictList` will look like
```python
{
  'title': 'Lorem ipsum dolor sit amet',
  'authors': 'Brandon Scott, Alvaro Cote',
  'affiliations': 'Villanova University, Pennsylvania; Carleton College, Minnesota' 
}
```
and you can easily use pandas to view `dictList` as a table
[![pandas op][1]][1]

---
---

**EDIT <sub>[PART 1]</sub>:** Without a function, you'd just have to do the same operations in an inner for loop:
```python
dictList = []
for i in urls: 
    page = requests.get(link)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")
 
    for a in soup.select('article.obj_article_details'):
        dets = {}
        for k, (sel, sep) in refDict.items():
            selTags = a.select(sel) if sel else [a]
            if type(sep) == str: 
                dets[k] = sep.join([s.get_text(' ').strip() for s in selTags])
            else: 
                dets[k] = selTags[0].get_text(' ').strip() if selTags else None
        dictList.append(dets)
```

---
---

**EDIT <sub>[PART 2]</sub>:** If you *must* have separate lists:
```python
title = []
authors = []
afiliations = []

for i in urls: 
    page = requests.get(link)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")

    for a in soup.select('article.obj_article_details'):
        titleA = a.select_one('.page_title')
        if titleA: titleA = titleA.get_text(' ').strip()
        title.append(titleA)

        authorsA = a.select('.authors .name')
        # authors.append(', '.join([aa.get_text(' ').strip() for aa in authorsA]))
        listAuth = []
        for aa in authorsA: listAuth.append(aa.get_text(' ').strip())
        authors.append(', '.join(listAuth))
        # authors.append(listAuth) # if you want a list instead of a string

        affA = a.select('.item.authors .affiliation')
        # afiliations.append('; '.join([aa.get_text(' ').strip() for aa in affA]))
        listAff = []
        for aa in affA: listAff.append(aa.get_text(' ').strip())
        afiliations.append(', '.join(listAff))
        # afiliations.append(listAff) # if you want a list instead of a string
```
the DataFrame arguments would be a little different this time:
[![op2][2]][2]
<sub>[I copied the html twice to create multiple rows and added `a1`/`a2` to differentiate the copies.]</sub>

---

Even that can be shortened with an inner for loop and list-comprehension
```python
refDict = {
    'title': '.page_title', 'authors': '.authors .name',
    'affiliations': '.item.authors .affiliation'
} 
listsDict = {k: [] for k in refDict}
for i in urls: 
    page = requests.get(link)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")

    for a in soup.select('article.obj_article_details'):
        for k in refDict:
            kvals = [t.get_text(' ').strip() for t in (
                a.select(refDict[k]) if refDict[k] else [a]
            )]
            listsDict[k].append('; '.join(kvals))
            # listsDict[k].append(kvals[0] if len(kvals) == 1 else kvals)
```
<sub>`refDict` was simplified, so you can't have different separators for different columns.</sub>
[![op3][3]][3]

By the ways, if you want multiple authors/affiliations as lists rather than joining them as strings, you can remove the `listsDict[k].append('; '.join(kvals))` line and uncomment the next line
```python
            listsDict[k].append(kvals[0] if len(kvals) == 1 else kvals)
```
[![op4][4]][4] 

<sub>Btw, with this last method, if there is more than one `.page_title` in a container, all of them will be includes, but with all my other methods, one the first title from each container would have been included. (I assumed that there would always only be one title per container.)</sub>

---
---

The important thing is **that the `title`/`authors`/`afiliations` lists are appended to the *same number of times* for a container** - that's why you need to separate the containers and append from there a fixed number of times.


  [1]: https://i.sstatic.net/0bTt7.png
  [2]: https://i.sstatic.net/ugkzH.png
  [3]: https://i.sstatic.net/ttJdZ.png
  [4]: https://i.sstatic.net/Nzy4N.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[drupaljac](https://stackoverflow.com/users/13264096)** (2022-12-05): thanks @Driftr95! It works like a charm!    By the way, can you tell me if there is a simple out-of-the-box fix for my code, without additional functions? I don't know why I'm getting new rows, nor do I know how to prevent them. Although the code I previously attached isn't a completely elegant solution, I find the problem to be very intriguing.
- **me** (2022-12-05): @drupaljac [I've added edits to my answer with some more methods, none of which use functions, but all them ultimately give very similar results...] the reason you're getting new rows is because some containers contain more than one tag corresponding to the  `.authors .name` and `.item.authors .affiliation` selectors, and your code doesn't have anything in it to distinguish between separate containers
