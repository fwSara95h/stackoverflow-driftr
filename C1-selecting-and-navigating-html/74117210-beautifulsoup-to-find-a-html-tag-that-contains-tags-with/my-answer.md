---
title: "BeautifulSoup to find a HTML tag that contains tags with specific class"
site: stackoverflow
question_id: 74117210
answer_id: 74120574
url: https://stackoverflow.com/a/74120574
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-19T06:07:39Z
last_edited: 2022-10-19T06:59:02Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74120574/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 96542a323217f470eefd7bb0ccf3c2061d6511c2aba60a5031aef95d867faf3c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-19

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74120574>, 2022-10-19, last edited 2022-10-19; score 0. Text as retrieved 2026-10-12.

You could use [css selectors](https://www.w3schools.com/cssref/css_selectors.asp) to get the tags with `class = "TD...3"` and then get their parent tags
```python
mtables = [s.parent for s in bs.select('*[class^="TD"][class$="3"]')]

# if you want tr only:
# mtables = [s.parent for s in bs.select('tr *[class^="TD"][class$="3"]')]

mtables = list(set(mtables)) # no duplicates
```
but this will not work if there are multiple classes (unless the first one starts with "TD" and the last ends in "3"), and you can't limit the characters in between.

<hr>

You could use `find` with `lambda` twice like this

```python
tagPat = '^TD.3$' 
# tagPat = '^TD.*3$' # if there might be more than one character between TD and 3
mtables = bs.find_all(
  lambda p: 
  p.name == 'tr' and # remove if you want all tags and not just tr
  p.find(
    lambda t: t.get('class') is not None and 
    len([c for c in t.get('class') if re.search('^TD.3$', c)]) > 0
    , recursive=False # prevent getting <tr><tr><td class="TDo3">someval</td></tr></tr>
  ))
``` 

<hr>

If you don't want to use `lambda`, you can replace the `select` in the first method with regex and `find`

```python
tagPat = '^TD.3$' # '^TD.*3$' #
mtables = [
    s.parent for s in bs.find_all(class_ = re.compile(tagPat))
    if s.parent.name == 'tr' # remove if you want all tags and not just tr
]
mtables = list(set(mtables)) # no duplicates
```

<hr><hr>

For the html in your question all 3 methods would lead to same data - you can print with
```python
for mtable in mtables: print('---\n', mtable, '\n---')
```
and get the output
```html
---
 <tr>
<td class="TDq1"><a href="p.pl?t=410">GpWl(op) 4.01/02</a></td>
<td class="TDq2"><a href="p.pl?t=410&amp;r=4">17.02.02</a></td>
<td class="TDq3">34/75</td>
<td class="TDq5">39. John Deep</td>
<td class="TDq9">68. <a href="p.pl?ply=1229">Mark Deep</a></td>
</tr> 
---
---
 <tr>
<td class="TDp1"><a href="p.pl?t=410">GpWl(op) 4.01/02</a></td>
<td class="TDp2"><a href="p.pl?t=410&amp;r=4">17.02.02</a></td>
<td class="TDp3">34/75</td>
<td class="TDp6">39. John Deep</td>
<td class="TDp8">7. <a href="p.pl?ply=10">Darius Star</a></td>
</tr> 
---
```
