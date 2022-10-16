---
title: "Use beautifulsoup to scrape a table within a webpage?"
site: stackoverflow
question_id: 74061653
answer_id: 74090309
url: https://stackoverflow.com/a/74090309
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-16T19:56:21Z
last_edited: 2022-11-26T01:52:18Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74090309/revisions
accepted: true
score: 1
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0f76da7233e46aa09ff98a00c97566a75ae87fb25a326877cb62b0ff42d9fd98
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74090309>, 2022-10-16, last edited 2022-11-26; **accepted**; score 1. Text as retrieved 2026-10-12.

For extracting specific nested elements, I often prefer to use [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors), which uses [css selectors](https://www.w3schools.com/cssref/css_selectors.asp) (bs4 doesn't seem to have any support for [xpath](https://devhints.io/xpath) but you can also check out [these solutions using the lxml library](https://stackoverflow.com/questions/11465555/can-we-use-xpath-with-beautifulsoup)), so for your case you could use something like 
```python
soup.select_one('table[id="form1:tableEx1"]').select('tbody tr')
```
but the results might [look a bit weird][1] since the columns might not be separated -  to have separated columns/cells, you could [get the of rows as tuples][2] instead with 
```python
tableRows = [
    tuple([c.text.strip() for c in r.find_all(['th', 'td'])]) for r 
    in BeautifulSoup(tHtml).select_one(
        'table[id="form1:tableEx1"]'
    ).select('tbody tr')
]
```
(Note that you can't use the `.select(#id)` format when the id contains a ":".)

As one of the comments mentioned, you can use `pandas.read_html(htmlString)` to  [get a list of tables in the html][3]; if you want a specific table, use the `attrs` argument:
```python
# import pandas
pandas.read_html(htmlString, attrs={'id': 'form1:tableEx1'})[0]
```
but you will get the *whole* table - not just what's in `tbody`; and this will flatten any tables that are nested inside (see [results][4] with table used from [this example](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_elements)).

And the single-statement method I showed at first with `select` cannot be used at all with nested tables since the output will be scrambled. Instead, if you want to preserve any nested inner tables without flattening, and if you are likely to be scraping tables often, I have the following set of functions which can be used in general:

- first define two other function that the main table extractor depends on:
```python
# get a list of tagNames between a tag and its ancestor
def linkAncestor(t, a=None):
  aList = []
  while t.parent != a or a is None:
    t = t.parent 
    if t is None:
      if a is not None: aList = None
      break
    aList.append(t.name)
  return aList
  # if a == t.parent: return []
  # if a is None, return tagNames of ALL ancestors 
  # if a not in t.parents: return None

def getStrings_table(xSoup): 
  # not perfect, but enough for me so far
  tableTags = ['table', 'tr', 'th', 'td']
  return "\n".join([
      c.get_text(' ', strip=True) for c in xSoup.children 
      if c.get_text(' ', strip=True) and (c.name is None or (
          c.name not in tableTags and not c.find(tableTags)
      ))
  ])
```
- then, you can define the function for extracting the tables as python dictionaries:
```python
def tablesFromSoup(mSoup, mode='a', simpleOp=False):
  typeDict = {'t': 'table', 'r': 'row', 'c': 'cell'}
  finderDict = {'t': 'table', 'r': 'tr', 'c': ['th', 'td']}
  refDict = {
    'a': {'tables': 't', 'loose_rows': 'r', 'loose_cells': 'c'},
    't': {'inner_tables': 't', 'rows': 'r', 'loose_cells': 'c'},
    'r': {'inner_tables': 't', 'inner_rows': 'r', 'cells': 'c'}, 
    'c': {'inner_tables': 't', 'inner_rows': 'r', 'inner_cells': 'c'}
  }
  mode = mode if mode in refDict else 'a'

  # for when simpleOp = True
  nextModes = {'a': 't', 't': 'r', 'r': 'c', 'c': 'a'}
  mainCont = {
      'a': 'tables', 't': 'rows', 'r': 'cells', 'c': 'inner_tables'
  }

  innerContent = {} 
  for k in refDict[mode]: 
    if simpleOp and k != mainCont[mode]: 
      continue
    
    fdKey = refDict[mode][k] # also the mode for recursive call
    innerSoups = [(
        s, linkAncestor(s, mSoup)
    ) for s in mSoup.find_all(finderDict[fdKey])] 
    innerSoups = [s for s, la in innerSoups if not (
        'table' in la or 'tr' in la or 'td' in la or 'th' in la
    )]

    # recursive call
    kCont = [tablesFromSoup(s, fdKey, simpleOp) for s in innerSoups] 

    if simpleOp:
      if kCont == [] and mode == 'c': break
      return tuple(kCont) if mode == 'r' else kCont

    # if not empty, check if header then add to output
    if kCont: 
      if 'row' in k:
        for i in range(len(kCont)):
          if 'isHeader' in kCont[i]: continue
          kCont[i]['isHeader'] = 'thead' in innerSoups[i][1]
      if 'cell' in k:
        isH = [(c[0].name == 'th' or 'thead' in c[1]) for c in innerSoups]
        if sum(isH) > 0:
          if mode == 'r':
            innerContent['isHeader'] = True
          else: 
            innerContent[f'isHeader_{k}'] = isH
      
      innerContent[k] = kCont 
  
  if innerContent == {} and mode == 'c':
    innerContent = mSoup.get_text(' ', strip=True) 
  elif mode in typeDict:
    if innerContent == {}: 
      innerContent['innerText'] = mSoup.get_text(' ', strip=True)
    else:
      innerStrings = getStrings_table(mSoup)
      if innerStrings:
        innerContent['stringContent'] = innerStrings
    innerContent['type'] = typeDict[mode] 
  
  return innerContent
```

With the same [example](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_elements) as before, this function gives [this output][5]; if  the `simpleOp` argument is set to `True`, it results in a [simpler output][6], but then the headers are no longer differentiated and some other peripheral data is also excluded.


  [1]: https://i.sstatic.net/Lpnht.png
  [2]: https://i.sstatic.net/MsYRN.png
  [3]: https://i.sstatic.net/Emqcv.png
  [4]: https://i.sstatic.net/hFWGV.png
  [5]: https://i.sstatic.net/BlVd8.png
  [6]: https://i.sstatic.net/mbnpF.png
