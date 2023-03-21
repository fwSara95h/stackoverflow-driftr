---
title: "Is there a really simple method for printing scraped output to a csv file?"
site: stackoverflow
question_id: 75803901
answer_id: 75805366
url: https://stackoverflow.com/a/75805366
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-21T18:58:14Z
last_edited: 2023-03-21T19:13:20Z
revisions: 3
revision_history: https://stackoverflow.com/posts/75805366/revisions
accepted: true
score: -1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c19b62728ccd2217508a1e6927582f14190aeef27d6e3f729e73bc27f7edd176
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75805366>, 2023-03-21, last edited 2023-03-21; **accepted**; score -1. Text as retrieved 2026-10-12.

`pandas` has a [`.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) method.

```py
# import pandas as pd
csv_filename = 'x.csv' #<--name or path to file

th_fields = ['Plaintiff', 'Defendant', 'Case Number', 'Filed', 'Court', 
             'Nature of Suit', 'Cause of Action', 'Jury Demanded By']
case_rows = []
for c in cases:
    title = c.find("div", class_ = "title-wrapper")
    row = {'title': title.text.strip()} if title else {}
    for td in c.find_all('td',{'data-th':(lambda th: th in th_fields)}): 
        row[td['data-th']] = td.text.strip()
    case_rows.append(row)

pd.DataFrame(case_rows).to_csv(csv_filename, index=False)
# pd.DataFrame(case_rows).T.to_csv(csv_filename, index=False, header=False)
```

[![op1][1]][1]

You can also [transpose][2] it with [`.T`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html).

[![op1.5][3]][3]

---

You can also get all the tables from the URL directly with [`read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)

```py
# import pandas as pd
url=f'https://dockets.justia.com/docket/puerto-rico/prdce/3:2023cv01127/175963'
csv_filename = 'x.csv'
for ti, df in enumerate(pd.read_html(url)):
    df.to_csv(csv_filename, mode='a' if ti else 'w', index=False)
    pd.DataFrame({'':[]}).to_csv(csv_filename, mode='a')
```

[![op2][4]][4]


  [1]: https://i.sstatic.net/HJzkB.png
  [2]: https://i.sstatic.net/lp6Zd.png
  [3]: https://i.sstatic.net/HNTne.png
  [4]: https://i.sstatic.net/0kYuB.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-21): That last script sure is simple and effective but includes too much extraneous information. Also the row contents should be columns (even as that would create a hell of a lot of columns for for cases with 3-4000 docket entries.
- **me** (2023-03-22): It's simple *because* it just grabs all the tables without any filtering or extra processing; however, you can transpose with `df.T` you can limit the number of rows (which will become transposed to columns) with `.loc` (eg.: [**like this**](https://i.sstatic.net/i0IXu.png) -  *`.loc[:4 if ti else len(df)]`* limits it to 4+1 entries, and it's conditional so that everything from the first table remains)
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-22): Love the simplicity! Thanks so much!
