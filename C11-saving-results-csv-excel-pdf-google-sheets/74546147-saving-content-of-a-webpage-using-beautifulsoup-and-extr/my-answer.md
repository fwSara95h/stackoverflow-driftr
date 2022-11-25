---
title: "Saving content of a webpage using BeautifulSoup and extract data"
site: stackoverflow
question_id: 74546147
answer_id: 74569002
url: https://stackoverflow.com/a/74569002
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-25T06:28:20Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74569002/revisions
accepted: false
score: 0
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1c5e40c6b2d714108b73ef5f082b0e63cf529fc0919268f21952143dbab000df
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74569002>, 2022-11-25; score 0. Text as retrieved 2026-10-12.

It's not quite clear how you want to structure the data in the csv, but any pandas DataFrame can be expected to be saved as CSV with [`.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html). For example:
```python
csvRows = []
for pCont in soup.find_all('pre'): 
    csvRows += [( 
        ('[About Query]', '\n'.join([
            ql[1:].strip() for ql in pb.split('\n')[2:5]
        ])) if pi == 0 else tuple(pb.split(f"\n{'#'*80}\n")[:2]) 
    ) for pi, pb in enumerate(pCont.get_text().split(f"{'#'*80}\n#  "))]
pandas.DataFrame(csvRows, columns=[
    'Result Header', 'Result Lines'
]).to_csv('Cotey_synopsc.csv', index=False)
```
would result in a file that [looks like this][1].

---
---

Although, I think it would be better [visually] to split it up a bit more - something like 
```python
aboutQuery, qresBlocks, bHeads = [], [], []
for pci, pCont in enumerate(soup.find_all('pre')):
    pBlocks = pCont.get_text().split(f"{'#'*80}\n#  ")

    aboutQuery.append({k: v for v, k in zip([pci]+[
        ql[1:].strip() for ql in pBlocks[0].split('\n')[2:5]
    ], ['qIndex', 'Query Time', 'Query', 'Query Inerval'])})

    for pbi, pb in enumerate(pBlocks[1:]):
        if f"\n{'#'*80}\n" not in pb: continue # unknown format
        bhead, blines = pb.split(f"\n{'#'*80}\n")[:2]
        bhead = bhead.strip().split(' | ')
        bHeads.append({k: v for k, v in [
            ('qIndex', pci), ('bIndex', pbi), ('from', bhead[0]), 
            ('N', ''.join(bhead[1:2])), ('W', ''.join(bhead[2:3])),
            ('m', ''.join(bhead[3:4])), ('extra', ' | '.join(bhead[4:]))
        ] if v != ''})
        for bl in blines.split('=\n')[:-1]:
            line1 = bl.split('\n')[0].strip()
            ldate = line1.split(' ')[0]
            line1 = line1.replace(ldate, '', 1)
            line2 = '\n'.join([l.strip() for l in bl.split('\n')[1:]])
            if line2 == '' and line1.endswith(' NIL'):
                line1, line2 = line1[:-4], 'NIL'
            qresBlocks.append({
                'qIndex': pci, 'bIndex': pbi, 'date?': ldate,
                'firstLine': line1, 'lastLine(/s)': f'{line2}='
            })

listsByName = [
    ('About Query', aboutQuery), 
    ('Result Blocks - Headers', bHeads), 
    ('Result Blocks - Lines', qresBlocks)
]
```

---

You can save to separate CSVs with 
```python
for name, nList in listsByName:
    pandas.DataFrame(nList).to_csv(f'{name}.csv', index=False)
```

---

or to separate sheets of a single Excel file with
```python
with pandas.ExcelWriter('Cote_synopsc.xlsx') as w:
    for name, nList in listsByName:
        pandas.DataFrame(nList).to_excel(w, name, index=False)
```

---

The outputs look like: ["About Query"][2] ["Result Blocks - Headers"][3] ["Result Blocks - Lines"][4]


  [1]: https://i.sstatic.net/23kks.png
  [2]: https://i.sstatic.net/ACDz8.png
  [3]: https://i.sstatic.net/pcTil.png
  [4]: https://i.sstatic.net/P9NXf.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[divinite dom](https://stackoverflow.com/users/20580636)** (2022-11-28): Thanks for your answer, about the the database, I want all the information in 'pre' to be in specific cell, to make the manipulation more easy
- **me** (2022-11-28): @divinitedom if you don't want to process at all, then you can just do it all in one statement with `pandas.DataFrame([{'function usage': f.get_text()} for f in soup.select('pre')]).to_csv('function_usage.csv', index=False)` [ [screenshot of output csv](https://i.sstatic.net/9CtSb.png) for the link that *used* to be in your question ] (btw, **why** did you remove your code from your q? the problem is pretty much impossible to understand now - I wouldn't have known what it's about if if I hadn't seen it before the edit)
