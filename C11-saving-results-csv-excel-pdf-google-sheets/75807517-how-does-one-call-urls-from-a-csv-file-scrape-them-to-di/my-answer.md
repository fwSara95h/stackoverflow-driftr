---
title: "How does one call URLs from a csv file, scrape them, to distribute output into a second csv file?"
site: stackoverflow
question_id: 75807517
answer_id: 75818064
url: https://stackoverflow.com/a/75818064
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-22T23:23:00Z
last_edited: 2023-03-24T02:45:33Z
revisions: 4
revision_history: https://stackoverflow.com/posts/75818064/revisions
accepted: true
score: 1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: [selectGet]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 519e6956c4d7295772c62260d36e3566453af4e6e04227069dfc4af51c4bc2a0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-22

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75818064>, 2023-03-22, last edited 2023-03-24; **accepted**; score 1. Text as retrieved 2026-10-12.

### Solution V1

> *Is there a way to (1) call URLs in a one-column 10-item list contained in a csv (i.e., "caselist.csv")*

With [`csv.reader`](https://docs.python.org/3/library/csv.html#csv.reader) you would use something like 

```py
# import csv
with open('caselist.csv', newline='') as f:
    links = [l for l, *_ in csv.reader(f)]
```

Although, since it's just a single column with no indices of headers, you don't actually need the `csv` module for this part. You could just use `f.read()` like <kbd>*`with open('caselist.csv') as f: links = f.read().splitlines()`*</kbd>, or to be safer:

```py
with open('caselist.csv') as f:
    links = [l.strip() for l in f.read().splitlines() if l.strip().startswith('https://dockets.justia.com/docket')]
```

---

> *and (2) execute a scraping script for each of those URLs (see below)*

You could wrap your current code [except for the `csv.writer` block] in a function that takes the URL as an input and returns the `output` list; but your current code has some repetitive part which I think can be reduced to something like 

```py
from bs4 import BeautifulSoup
import requests
th_fields = { 'case_plaintiff': 'Plaintiff', 'case_defendant': 'Defendant', 'case_number': 'Case Number', 
              'case_filed': 'Filed', 'court': 'Court', 'case_nature_of_suit': 'Nature of Suit', 
              'case_cause_of_action': 'Cause of Action',  'jury_demanded': 'Jury Demanded By' }
fgtParams = [('div', {'class': 'title-wrapper'})] + [('td', {'data-th': f}) for f in th_fields.values()]
```

```py
## a simpler version of my selectGet function [ https://pastebin.com/ZnZ7xM6u ] 
def find_get_text(bsTag, tName='div', tAttrs=None):
    t = bsTag.find(tName, {} if tAttrs is None else tAttrs)
    if t: return t.get_text(' ',strip=True) # safer as a conditional

def scrape_docketsjustia(djUrl, paramsList=fgtParams):
    soup = BeautifulSoup((r:=requests.get(djUrl)).content, 'lxml')
    cases_class = 'wrapper jcard has-padding-30 blocks has-no-bottom-padding'
    cases = soup.find_all('div', class_=cases_class)

    # print(f'{len(cases)} cases <{r.status_code} {r.reason}> from {r.url}')
    return [[find_get_text(c, n, a) for n, a in paramsList] for c in cases] 
```

<br>

Once you have the function, you can just loop over all the URLs to collect all the outputs:

```py
all_ouputs = []
for url in links: 
    all_ouputs += scrape_docketsjustia(url)
```

---

> *and output all the data to a second csv file ("caselist_output.csv")*

You can save `all_ouputs` the same way you were saving `output`, although you can also use the keys of `th_fields` as column headers if you want:

```py
with open("posts/caselist_output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['case_title', *th_fields]) # [ header row with column names ]
    writer.writerows(all_ouputs)
```

---
---

### Solution V2

> *and **rows** (each of the 10 cases contained in the csv file)*

I hadn't noticed this at first, but if you're expecting only one row for every link, there's no need to return a list from `scrape_docketsjustia` - it can just return that one row. So the solution can be adjusted to something like

```py
## setup ##

import requests
from bs4 import BeautifulSoup
import pandas as pd # [I just prefer pandas]

input_fp = 'caselist.csv'
output_fp = 'posts/caselist_output.csv'
th_fields = { 'case_plaintiff': 'Plaintiff', 'case_defendant': 'Defendant', 'case_number': 'Case Number', 
              'case_filed': 'Filed', 'court': 'Court', 'case_nature_of_suit': 'Nature of Suit', 
              'case_cause_of_action': 'Cause of Action',  'jury_demanded': 'Jury Demanded By' }
fgtParams = [('case_title', 'div', {'class': 'title-wrapper'})] + [(k, 'td', {'data-th': f}) for k,f in th_fields.items()]
```

```py
## function definitions ##

def find_get_text(bsTag, tName='div', tAttrs=None):
    t = bsTag.find(tName, {} if tAttrs is None else tAttrs)
    if t: return t.get_text(' ',strip=True)

def scrape_docketsjustia(djUrl, paramsList=fgtParams):
    soup = BeautifulSoup((r:=requests.get(djUrl)).content, 'lxml')
    cases_class = 'wrapper jcard has-padding-30 blocks has-no-bottom-padding'
    for c in soup.find_all('div', class_=cases_class): 
        return {k:find_get_text(c,n,a) for k,n,a in paramsList}

    # return {} # just return empty row if cases_class can't be found
    return {'error_msg': f'no cases <{r.status_code} {r.reason}> from {r.url}'}
```

```py
## main logic ##

## load list of links 
# links = list(pd.read_csv(input_fp, header=None)[0]) # [ if you're sure ]
links = [l.strip() for l in pd.read_csv(input_fp, header=None)[0]  
         if l.strip().startswith('https://dockets.justia.com/docket/')] # safer

## scrape for each link
df = pd.DataFrame([scrape_docketsjustia(u) for u in links])
# df = pd.DataFrame(map(scrape_docketsjustia,links)).dropna(axis='rows') # drop empty rows
# df['links'] = links # [ add another column with the links ]

## save scraped data
# df.to_csv(output_fp, index=False, header=False) # no column headers
df.to_csv(output_fp, index=False) 
```

[![opdf_Read][1]][1]

---

### **ADDED EDIT:** Reading and Saving Line by Line

Altered definition of `scrape_docketsjustia` [because all rows need to have the same column order when appending, in order to maintain row alignments]:

```py
def scrape_docketsjustia(djUrl, paramsList=fgtParams):
    soup = BeautifulSoup((r:=requests.get(djUrl)).content, 'lxml')
    cases_class = 'wrapper jcard has-padding-30 blocks has-no-bottom-padding'
    print(rStatus:=f'<{r.status_code} {r.reason}> from {r.url}') 

    c1 = soup.find('div', class_=cases_class)
    case1 = {k:find_get_text(c1 if c1 else soup, n, a) for k,n,a in paramsList}
    return {**case1, 'msg': rStatus}
    # return {**case1, 'msg': rStatus, 'from_link': djUrl}
``` 

And replace the *`## main logic ##`* block with

```py
columns = [*[k for k,*_ in fgtParams], 'msg']
# columns = [*[k for k,*_ in fgtParams], 'msg', 'from_link': djUrl]

with open(input_fp) as f:
    for li, l in enumerate(f):
        if not l.strip().startswith('https://dockets.justia.com/'): continue
        df = pd.DataFrame([scrape_docketsjustia(l.strip())])

        m, h = ('a', False) if li else ('w', True) ## new file if li==0
        df[columns].to_csv(output_fp, mode=m, index=False, header=h)
```

[![op lbl][2]][2]

**Note that this will only work for single-column `input_fp`**


  [1]: https://i.sstatic.net/WpFII.png
  [2]: https://i.sstatic.net/SN5kx.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-23): Thanks so much for taking the time! I guess I like pandas, too - if I just knew more about it/them. I'm not entirely sure I understand your comment under "## load list of links". I', getting two errors: "Unresolved reference 'links'" and "Unresolved reference 'csv'"
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-23): I've entered the code you suggested in my original post as an edit. Did I get it right? At my present stage of Python-dom, I mostly rely on reverse engineering as I'm trying to figure out the terminology etc. It returns a links error - not really sure where I got it wrong.
- **me** (2023-03-23): @PressMeister the *"unresolved reference 'csv'"* error is most likely from the `with open("posts/caselist_output.csv", "w") as f...` block and the *"unresolved reference 'links'"* error is probably from `for url in links:` , both of which are from the first version of my solution (I think you might have copied them on accident). The errors are raised because `csv` wasn't imported for that solution and `links` hadn't been defined yet.
- **me** (2023-03-23): I've now edited your edit so that the part from the first solution are commented out, and also edited my own answer to that the 2 versions of my solution are more clearly separated.
- **me** (2023-03-23): @PressMeister As for the `# [ if you're sure ]` line under *`## load list of links`*, I just meant that you don't need the *`if l.strip().startswith('https://dockets.justia.com/docket/')`* bit in the next statement if you're sure that every line in "caselist.csv" is just a valid URL with no extra whitespace or any other data
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-23): The output shown in your table graphic is exactly what I'm looking for. I'm sure that there's something fundamental I'm not quite getting and why I'm getting those error messages and no output (see the edited question). I had some issues with the formatting in the edit box so had to omit a couple of my intermediate screw-ups.
- **me** (2023-03-23): @PressMeister sorry! this was due to my mistake. The statement should be `links = [l.strip() for l in pd.read_csv(input_fp` **`, header=None`** `)[0] if l.strip().startswith('https://dockets.justia.com/docket/')]`. Since I had generated my own "caselist.csv" incorrectly [so it was different from yours], so the `header=None` part wasn't necessary then. But it is for the sample you showed and I didn't notice. Sorry again
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-23): You are a pure genius! It works! Thanks so much. Please let me know if there's anything I can do for you... Letterpress printed stationery or some such thing!!
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-23): Aaargh, what I thought worked about 4 hours ago doesn't seem to work after all. It executes the script (see updated script in Question section), but neither produces an error message nor any content in the output file (i.e., "caselist_output").
- **me** (2023-03-23): @PressMeister It still works for me with your sample links, as you can see in this [testing notebook](https://colab.research.google.com/drive/19PsVGcC5D8Pfxa92Np3EfbviDPnk1jSr) (as long as you have a google account you should be able to make a copy and try it yourself). I've added a `print` statement back into `scrape_docketsjustia` so that it prints the response status (and number of case `div`s found). Please lmk what it prints for you
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-23): Thanks so much. Hate to be a bother (again), but now it generates both an input and an output file: It writes the URLs listed in the script to the input file (caselist.csv) and the scraped data from URLs contained in the script into the output file (caselist_output). In other words, it doesn't seem to read from the input csv file (i.e., caselist.csv)... am I right? Also, just out of curiosity, you wouldn't happen to know if there's an upper limit to the number of URLs one might place in the input csv?
- **me** (2023-03-24): @PressMeister There's a section where I generated the input file ([view screenshot](https://i.sstatic.net/E0Jdp.png)). You can either remove it or just comment out the *`....to_csv...`* line in that section so that your file isn't over-written.
- **me** (2023-03-24): As for the upper-limit to the number of URLs in the CSV, there isn't really - except in how many rows/cells a spreadsheet can have [~1 million rows for excel and 10million **cells** for google sheets]. However, loading a large number of URL *would* slow down your program [or maybe even crash it if it runs out of memory]; if you're concerned about that, you can read through it line by line and also save  the data row by row
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-24): You know, I can't say how much I appreciate this. Thanks so much!! It totally works now!
