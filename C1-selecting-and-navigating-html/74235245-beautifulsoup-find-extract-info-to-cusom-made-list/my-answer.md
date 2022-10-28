---
title: "BeautifulSoup find extract info to cusom-made list"
site: stackoverflow
question_id: 74235245
answer_id: 74237349
url: https://stackoverflow.com/a/74237349
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-28T15:08:17Z
last_edited: 2022-11-03T10:21:08Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74237349/revisions
accepted: true
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 37d74f381d1163c0b559ba218c76ec3ab39cef7d28a0a2e4bd62101dd869632f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74237349>, 2022-10-28, last edited 2022-11-03; **accepted**; score 1. Text as retrieved 2026-10-12.

You could search for each part individually:

```python
def bs2customList(soup): 
    fwb = soup.find("span", class_="font-weight-bold")

    #fdesc = [] if fwb is None else [( #(text, filter1, filter2, filter3)
        #d.get_text(strip=True), d.parent.get('class', []), d.parent.get('translate'), len(d.parent.select('span')) 
    #) for d in fwb.descendants if d.name is None and d.parent.name == 'span' and d.get_text(strip=True) ]
    fdesc = [] if fwb is None else [( #(text, filter1, filter2, filter3)
        str(d).strip(), d.parent.get('class', []), d.parent.get('translate'), len(d.parent.select('span')) 
    ) for d in fwb.descendants if 'NavigableString' in str(type(d)) and d.parent.name == 'span' and str(d).strip()]

    filters = [([], '', 0), (['ng-star-inserted'], None, 0), (['ng-star-inserted'], None, 1)]
    issueNum, ydate, num_ext = [[d[0] for d in fdesc if d[1:] == f] for f in filters]  
    num = num_ext[0].split()[0] if num_ext else []
    ext = num_ext[0].split()[1:] if num_ext else []
  
    return [(d[0] if d else None) for d in [issueNum, num, ext, ydate]]
```

or maybe this is more understandable:

```python
def bs2customList(soup): 
    fwb = soup.find("span", class_="font-weight-bold")
    if fwb is None or not fwb.select('span.ng-star-inserted'): 
        return [ None ]*4

    snsi = fwb.select('span.ng-star-inserted') 
    
    snsi1 = [t for t in snsi if t.select('span[translate]')]
    if snsi1 != []:
        issueNum = snsi1[0].select_one('span[translate]').get_text(strip=True)

        #ext = [
        #    c.get_text(strip=True) for c in snsi1[0].children 
        #    if c.name is None and c.get_text(strip=True)
        #]
        ext = [
            str(c).strip() for c in snsi1[0].children 
            if 'NavigableString' in str(type(c)) and str(c).strip()
        ]

        if ext:
            ext = [e for e in ext[0].split() if e]

            # keep ext[0].isdigit() only if "number" is always integer
            if len(ext) > 1 and ext[0].isdigit(): 
                num = ext[0]
                ext = ' '.join(ext[1:])
            else: num, ext = ' '.join(ext), None
        else: num, ext = None, None
    else: issueNum, num, ext = [ None ]*3    

    ydate = [t for t in snsi if not t.select('span[translate]')]
    ydate = ydate[0].get_text(strip=True) if ydate else None

    return [issueNum, num, ext, ydate]
```

<hr><hr>

Whichever version of the function is used, with the below test set:

```html
htmls = [
    '''
    <html>
      <body>
        <span _ngcontent-dna-c199="" class="font-weight-bold">
          <span _ngcontent-dna-c199="" class="ng-star-inserted">
            <span _ngcontent-dna-c199="" translate="">
              issue_number
            </span>
            4 Näköispainos
          </span>
          <span _ngcontent-dna-c199="" class="ng-star-inserted">
            6.12.1939
          </span>
        </span>
      </body>
    </html>
    ''',
    '''
    <html>
      <body>
        <span _ngcontent-sut-c199="" class="font-weight-bold">
          <span _ngcontent-sut-c199="" class="ng-star-inserted">
            <span _ngcontent-sut-c199="" translate="">
              issue_number
            </span>
            8
          </span>
          <span _ngcontent-sut-c199="" class="ng-star-inserted">
            1998
          </span>
        </span>
      </body>
    </html>
    ''',
    '''
    <html>
      <body>
        <span _ngcontent-dgu-c199="" class="font-weight-bold">
          <span _ngcontent-dgu-c199="" class="ng-star-inserted">
            1905
          </span>
        </span>
      </body>
    </html>
    ''',
    '<html><body><span class="font-weight-bold"></span></body></html>',
    '' # empty str
]
```

<hr>

printing with
```python
for h in htmls: print(bs2customList(BeautifulSoup(h, 'lxml')))
```
gives the same output [with both versions]:
```python
['issue_number', '4', 'Näköispainos', '6.12.1939']
['issue_number', '8', None, '1998']
[None, None, None, '1905']
[None, None, None, None]
[None, None, None, None]
```
(The last 2 tests are with an empty [textless] html and an empty string.)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[farid](https://stackoverflow.com/users/5437090)** (2022-11-03): I get this error running the code, both def functions: `AttributeError: 'NavigableString' object has no attribute 'get_text'`
- **me** (2022-11-03): @FaridAlijani sorry, I didn't anticipate that error because I'd never had issues with using `get_text` on NavigableStrings before (maybe it's a version thing?...) Anyway, I've edited in alternate way [the `fdesc = [...` and `ext = [...` lines], but left the original lines in comments so they're easier to find. Would you mind giving them one more try? (Sorry again since I cannot test it myself as the error is not raised for me)
- **[farid](https://stackoverflow.com/users/5437090)** (2022-11-04): Dude, Thanks I appreciate your time for answering this! I actually had different `html` snippets (more complete) which I did not notice at the time I posted this question. Therefore, I opened a new question: https://stackoverflow.com/questions/74317095/beautifulsoup-extract-desired-information-in-custome-made-list-from-different-ht could you please take a look at this too I do not know how to manipulate this for information extraction! thanks in advance
