---
title: "How can I update my Dataframe with new columns and rows while webscraping?"
site: stackoverflow
question_id: 75044698
answer_id: 75052654
url: https://stackoverflow.com/a/75052654
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-09T02:21:10Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75052654/revisions
accepted: false
score: 0
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 00040886fa48e3534dd7ee2646f485778bfa3113615d47ff99b107dc633d5236
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75052654>, 2023-01-09; score 0. Text as retrieved 2026-10-12.

Just [concatenating](https://pandas.pydata.org/docs/reference/api/pandas.concat.html) all the secondary tables should do - build a list of all the secondary DataFrames, and then **`pd.concat(dfList)`**.

Btw, have you considered just using [`.read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html) instead of looping through the cells? 
```python
#create the main DataFrame
link1 = links[0]
url_linked = url_l + link1
page_linked = requests.get (url_linked)
soup_linked = BeautifulSoup(page_linked.text, 'lxml')
table_linked = soup_linked.find('table', class_="XXXXX")

if table_linked:
    primaryDf = pd.read_html(table_linked.prettify())[0]
    headers_link = [h.get_text(' ').strip() for h in table_linked.find_all('th')]
    dfList = [pd.DataFrame(columns=headers_link if headers_link else primaryDf.columns)]
else: primaryDf, dfList = None, []  

count = 0
for link in links:
    count += 1
    url_linked = url_l + link
    page_linked = requests.get (url_linked)
    soup_linked = BeautifulSoup(page_linked.text, 'lxml')
    table_linked = soup_linked.find('table', class_="table table-directory-responsive")

    if not table_linked:
        ## to see if any response errors or redirects
        print(f'[{page_linked.status_code} {page_linked.reason} from {page_linked.url}]')   

        ## print error message and move to next link
        print(f'Found no tables with required class at link#{count}', url_linked)
        continue
    tempDf = pd.read_html(table_linked.prettify())[0] ## read table as df [if found]

    ## get rid of empty rows and empty columns
    tempDf = tempDf.dropna(axis='rows', 'how'='all').dropna(axis='columns', 'how'='all') 
    dfList.append(tempDf.loc[:]) ## .loc[:] to append a copy, not original (just in case)
    print(f'Completed link#{count} with {len(tempDf)} rows from {url_linked}')
combinedDF = pd.concat(dfList)
```
