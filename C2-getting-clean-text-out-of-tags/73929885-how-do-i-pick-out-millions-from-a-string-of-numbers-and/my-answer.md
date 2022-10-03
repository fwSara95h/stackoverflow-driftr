---
title: "How do I pick out millions from a string of numbers and commas?"
site: stackoverflow
question_id: 73929885
answer_id: 73931516
url: https://stackoverflow.com/a/73931516
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-03T05:48:10Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73931516/revisions
accepted: false
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9b3753adbc571048e2bfbc8b4e9ba9ed25cbb114e8198101a361499565d65634
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73931516>, 2022-10-03; score 1. Text as retrieved 2026-10-12.

The string can be parsed by just using splits and join and some filtering:

    origString = 'Total Revenue42,965,39136,483,93920,139,65822,588,85825,067,279'
    
    cols = origString.split(',')
    
    rowName = cols[0][:] #copy
    cols[0] = ''.join(e for e in cols[0] if e.isdigit())
    rowName = rowName.replace(cols[0], '')
    
    cols = ','.join([c if len(c) < 4 else (c[:3]+'|'+c[3:]) for c in cols])
    colVals = [rowName] + cols.split('|')
and printing `colVals` will give you the output

    ['Total Revenue', '42,965,391', '36,483,939', '20,139,658', '22,588,858', '25,067,279']
The above method works as long as the commas are always supposed to separate blocks of 3 digits **AND** there is no more than one text section - which must always be at the beginning and not contain any numbers or commas. (Not having a text section would be fine - it just ends up with `rowName=''`, and the first item of `colVals` will also be `''`).

**HOWEVER**, I think the best approach is to retrieve the text from the soup in ways so that it doesn't need further parsing at all:

    tables = soup.find_all(class_ = 'fi-row')
    
    print(len(tables), 'rows found:')
    print('Breakdown       ||          TTM |   12/31/2021 |   12/31/2020 |   12/31/2019 |   12/31/2018')
    print('-------------------------------------------------------------------------------------------')
    for table in tables:
      cols = [s.text for s in table.find_all('div',{'data-test':'fin-col'})]
      rowName = table.find('span').text
      colText = ' | '.join([f'{c:>12}' for c in cols])
      nameTxt = rowName if len(rowName) < 15 else f'{rowName[:12]}...'
      print(f'{nameTxt:15} || {colText}') 
(`colText` and `nameTxt` are defined just for printing - I just didn't like the [output][1] looking like [this][2])

Also, I changed the `find_all` arguments for the rows to `class_ = 'fi-row'` because both `class_ = 'rw-expnded'` and `"div", {"data-test": "fin-row"}` include collapsible rows that are nested within, so when the outer row is being looped through, it ends up seeming to have extra columns; and `class_ = 'rw-expnded'` sometimes can't be found at all.


  [1]: https://i.sstatic.net/x0i9Y.png
  [2]: https://i.sstatic.net/K9r0y.png
