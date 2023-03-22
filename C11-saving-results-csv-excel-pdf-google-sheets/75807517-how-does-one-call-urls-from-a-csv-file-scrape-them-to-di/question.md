---
title: "How does one call URLs from a csv file, scrape them, to distribute output into a second csv file?"
site: stackoverflow
question_id: 75807517
url: https://stackoverflow.com/q/75807517
asked: 2023-03-22T00:34:19Z
asked_by: "PressMeister"
asked_by_url: https://stackoverflow.com/users/21433696
last_edited: 2023-03-23T16:54:20Z
tags: [python, csv, beautifulsoup]
score: -1
views_at_snapshot: 121
answer_count: 1
accepted_answer_id: 75818064
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a6ba4f2fa0c10a249407d3ad9c89e049ba9f8e56f12999110c5cddc5fef05fb2
---

# How does one call URLs from a csv file, scrape them, to distribute output into a second csv file?

Asked by [PressMeister](https://stackoverflow.com/users/21433696) on Stack Overflow, <https://stackoverflow.com/q/75807517>, 2023-03-22, last edited 2023-03-23. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

*Python 3.11.2; PyCharm 2022.3.3 (Community Edition) - Build PC-223.8836.43; OS: Windows 11 Pro, 22H2, 22621.1413; Chrome 111.0.5563.65 (Official Build) (64-bit)*

The editing box behaved wonkily, so I have omitted a couple of the intermediate attempts that were unsuccessful.


---
Is there a way to (1) call URLs in a one-column 10-item list contained in a csv (i.e., "caselist.csv"); and (2) execute a scraping script for each of those URLs (see below) and output all the data to a second csv file ("caselist_output.csv") in which the output is distributed in columns (i.e., case_title, case_plaintiff, case_defendant, case_number, case_filed, case_filed, court, case_nature_of_suit, case_cause_of_action, jury_demanded) and rows (each of the 10 cases contained in the csv file)?

The ten URLs contained in caselist.csv are:

```
https://dockets.justia.com/docket/alabama/alndce/6:2013cv01516/148887
https://dockets.justia.com/docket/arizona/azdce/2:2010cv02664/572428
https://dockets.justia.com/docket/arkansas/aredce/4:2003cv01507/20369
https://dockets.justia.com/docket/arkansas/aredce/4:2007cv00051/67198
https://dockets.justia.com/docket/arkansas/aredce/4:2007cv01067/69941
https://dockets.justia.com/docket/arkansas/aredce/4:2008cv00172/70993
https://dockets.justia.com/docket/arkansas/aredce/4:2008cv01288/73322
https://dockets.justia.com/docket/arkansas/aredce/4:2008cv01839/73965
https://dockets.justia.com/docket/arkansas/aredce/4:2008cv02513/74818
https://dockets.justia.com/docket/arkansas/aredce/4:2008cv02666/74976
```

After failing miserably with my own scripts, I tried @Driftr95's two suggestions:

    from bs4 import BeautifulSoup
    import requests
    import csv
    
    th_fields = { 'case_plaintiff': 'Plaintiff', 'case_defendant': 'Defendant', 'case_number': 'Case Number',
                  'case_filed': 'Filed', 'court': 'Court', 'case_nature_of_suit': 'Nature of Suit',
                  'case_cause_of_action': 'Cause of Action',  'jury_demanded': 'Jury Demanded By' }
    fgtParams = [('div', {'class': 'title-wrapper'})] + [('td', {'data-th': f}) for f in th_fields.values()]
    
    with open('caselist.csv') as f:
        links = [l.strip() for l in f.read().splitlines() if l.strip().startswith('https://dockets.justia.com/docket')]
    
    def find_get_text(bsTag, tName='div', tAttrs=None):
        t = bsTag.find(tName, {} if tAttrs is None else tAttrs)
        if t: return t.get_text(' ',strip=True) # safer as a conditional
    
    def scrape_docketsjustia(djUrl, paramsList=fgtParams):
        soup = BeautifulSoup((r:=requests.get(djUrl)).content, 'lxml')
        cases_class = 'wrapper jcard has-padding-30 blocks has-no-bottom-padding'
        cases = soup.find_all('div', class_=cases_class)
    
        # print(f'{len(cases)} cases <{r.status_code} {r.reason}> from {r.url}')
        return [[find_get_text(c, n, a) for n, a in paramsList] for c in cases]
    
    all_ouputs = []
    for url in links:
        all_ouputs += scrape_docketsjustia(url)
    
    with open("posts/caselist_output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(['case_title', *th_fields]) # [ header row with column names ]
        writer.writerows(all_ouputs)

This script did not produce any output. Not really sure what's going on...

I also tried @Driftr95's second suggestion:

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd # [I just prefer pandas]
    
    input_fp = 'caselist.csv'
    output_fp = 'caselist_output.csv'
    th_fields = { 'case_plaintiff': 'Plaintiff', 'case_defendant': 'Defendant', 'case_number': 'Case Number',
                  'case_filed': 'Filed', 'court': 'Court', 'case_nature_of_suit': 'Nature of Suit',
                  'case_cause_of_action': 'Cause of Action',  'jury_demanded': 'Jury Demanded By' }
    fgtParams = [('case_title', 'div', {'class': 'title-wrapper'})] + [(k, 'td', {'data-th': f}) for k,f in th_fields.items()]
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
    ## main logic ##
    
    ## load list of links
    # links = list(pd.read_csv(input_fp, header=None)[0]) # [ if you're sure ]
    links = [l.strip() for l in pd.read_csv(input_fp)[0] # header will get filtered anyway
             if l.strip().startswith('https://dockets.justia.com/docket/')] # safer
    
    ## scrape for each link
    df = pd.DataFrame([scrape_docketsjustia(u) for u in links])
    # df = pd.DataFrame(map(scrape_docketsjustia,links)).dropna(axis='rows') # drop empty rows
    # df['links'] = links # [ add another column with the links ]
    
    ## save scraped data
    # df.to_csv(output_fp, index=False, header=False) # no column headers
    df.to_csv(output_fp, index=False)

This produced the following error messages:

Traceback (most recent call last):
  File "C:\Users\cs\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\indexes\base.py", line 3802, in get_loc
    return self._engine.get_loc(casted_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 165, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5745, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5753, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\cs\PycharmProjects\pythonProject1\solution2.py", line 29, in <module>
    links = [l.strip() for l in pd.read_csv(input_fp)[0] # header will get filtered anyway
                                ~~~~~~~~~~~~~~~~~~~~~^^^
  File "C:\Users\cs\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\frame.py", line 3807, in __getitem__
    indexer = self.columns.get_loc(key)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\cs\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\indexes\base.py", line 3804, in get_loc
    raise KeyError(key) from err
KeyError: 0

----
I just ran the script, which I thought worked - but now, all of a sudden, it returns no output (even with the revised `links = [l.strip() for l in pd.read_csv(input_fp , header=None )[0] if l.strip().startswith('https://dockets.justia.com/docket/')]`:

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd # [I just prefer pandas]
    
    input_fp = 'caselist.csv'
    output_fp = 'caselist_output.csv'
    th_fields = { 'case_plaintiff': 'Plaintiff', 'case_defendant': 'Defendant', 'case_number': 'Case Number',
                  'case_filed': 'Filed', 'court': 'Court', 'case_nature_of_suit': 'Nature of Suit',
                  'case_cause_of_action': 'Cause of Action',  'jury_demanded': 'Jury Demanded By' }
    fgtParams = [('case_title', 'div', {'class': 'title-wrapper'})] + [(k, 'td', {'data-th': f}) for k,f in th_fields.items()]
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
    ## main logic ##
    
    ## load list of links
    # links = list(pd.read_csv(input_fp, header=None)[0]) # [ if you're sure ]
    links = [l.strip() for l in pd.read_csv(input_fp , header=None )[0] if l.strip().startswith('https://dockets.justia.com/docket/')] # safer
    
    ## scrape for each link
    df = pd.DataFrame([scrape_docketsjustia(u) for u in links])
    # df = pd.DataFrame(map(scrape_docketsjustia,links)).dropna(axis='rows') # drop empty rows
    # df['links'] = links # [ add another column with the links ]
    
    ## save scraped data
    # df.to_csv(output_fp, index=False, header=False) # no column headers
    df.to_csv(output_fp, index=False)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Marcelo Paco](https://stackoverflow.com/users/11286032)** (2023-03-22): Welcome to stackoverflow. Please checkout the [welcome tour](https://stackoverflow.com/tour), [help/on-topic] and [how to ask](https://stackoverflow.com/help/how-to-ask).
