---
title: "NoneType' object is not subscriptable : bs4 task fails permanently"
site: stackoverflow
question_id: 75828625
url: https://stackoverflow.com/q/75828625
asked: 2023-03-23T22:50:49Z
asked_by: "zero"
asked_by_url: https://stackoverflow.com/users/525865
last_edited: 2023-03-25T20:30:24Z
tags: [python, pandas, csv, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 255
answer_count: 2
accepted_answer_id: 75838329
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 35d79bd41258bbfabf645ad8b559e1fe5083250385bc950088ffa4caf395e011
---

# NoneType' object is not subscriptable : bs4 task fails permanently

Asked by [zero](https://stackoverflow.com/users/525865) on Stack Overflow, <https://stackoverflow.com/q/75828625>, 2023-03-23, last edited 2023-03-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

**update:**  tried the scripts of Driftr95 .. in google-colab - and got some questions - the scripts failed - and was not succesful - queston. at the beginning of the scripts i have noticed that some lines are commendted out. why is this so.  i will try to investigate more - meanwhile thanks alot..-. awesome.


two ideas that come up to mind: 
a. the whole site of a result-page contains even more data: see


see the results of one (of 700 ) pages: 

the digital innovation hub: **4PDIH - Public Private People Partnership Digital Innovation Hub**

https://s3platform.jrc.ec.europa.eu/digital-innovation-hubs-tool/-/dih/17265/view?_eu_europa_ec_jrc_dih_web_DihWebPortlet_backUrl=%2Fdigital-innovation-hubs-tool


the dataset with the categories:

    Hub Information
    Description
    Contact Data
    Organisation
    Technologies
    Market and Services
    Service Examples
    Funding
    Customers
    Partners


[![enter image description here][1]][1]

second idea: with the awesme-scripts: 





    NameError("name 'pd' is not defined") from https://s3platform.jrc.ec.europa.eu/digital-innovation-hubs-tool?_eu_europa_ec_jrc_dih_web_DihWebPortlet_cur=1
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-3-c1f39e3c2547> in <module>
         11 
         12 # pd.concat(dfList).to_csv(output_fp, index=False) ## save without page numbers
    ---> 13 df=pd.concat(dfList, keys=list(range(1,len(dfList)+1)),names=['from_pg','pgi'])
         14 df.reset_index().drop('pgi',axis='columns').to_csv(output_fp, index=False)
    
    NameError: name 'pd' is not defined


and besides that - in the next trial

    NameError                                 Traceback (most recent call last)
    <ipython-input-5-538670405002> in <module>
          1 # df = pd.concat(dfList.....
    ----> 2 orig_cols = list(df.columns)
          3 for ocn in orig_cols:
          4     if any(vals:=[cv for cv,*_ in df[ocn]]): df[ocn[0]] = vals
          5     if any(links:=[c[1] for c in df[ocn]]): df[ocn[0].split()[0]+' Links'] = links
    
    NameError: name 'df' is not defined


and the next trail 


    NameError                                 Traceback (most recent call last)
    <ipython-input-1-4a00208c3fe6> in <module>
         10     pg_num += 1
         11     if isinstance(max_pg, int) and pg_num>max_pg: break
    ---> 12     pgSoup = BeautifulSoup((pgReq:=requests.get(next_link)).content, 'lxml')
         13     rows = pgSoup.select('tr:has(td[data-ecl-table-header])')
         14     all_rows += [{'from_pg': pg_num, **get_row_dict(r)} for r in rows]
    
    NameError: name 'BeautifulSoup' is not defined

end of the update: 

the **full story:** 

I am currently trying to learn Beautiful Soup (BS4), starting with fetching data.

With a scraper that should work with beautiful soup and scrapes the dataset of [this](https://s3platform.jrc.ec.europa.eu/digital-innovation-hubs-tool) page and puts the data into a csv format or uses pandas. If I run this in Google colab - I am facing some weird issues. See below: 




    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    
    # Make a request to the webpage
    url = 'https://s3platform.jrc.ec.europa.eu/digital-innovation-hubs-tool'
    response = requests.get(url)
    
    # Parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table with the data
    table = soup.find('table')
    
    # Extract the table headers
    headers = []
    for th in table.find_all('th'):
        headers.append(th.text.strip())
    
    # Extract the table rows
    rows = []
    for tr in table.find_all('tr')[1:]:
        row = []
        for td in tr.find_all('td'):
            row.append(td.text.strip())
        rows.append(row)
    
    # Find the total number of pages
    num_pages = soup.find('input', {'id': 'paginationPagesNum'})['value']
    
    # Loop through each page and extract the data
    for page in range(2, int(num_pages) + 1):
        # Make a request to the next page
        page_url = f'{url}?page={page}'
        page_response = requests.get(page_url)
    
        # Parse the HTML content with Beautiful Soup
        page_soup = BeautifulSoup(page_response.content, 'html.parser')
    
        # Find the table with the data
        page_table = page_soup.find('table')
    
        # Extract the table rows
        for tr in page_table.find_all('tr')[1:]:
            row = []
            for td in tr.find_all('td'):
                row.append(td.text.strip())
            rows.append(row)
    
    # Create a Pandas DataFrame with the data
    df = pd.DataFrame(rows, columns=headers)
    
    # Save the DataFrame to a CSV file
    df.to_csv('digital-innovation-hubs.csv', index=False)


see what i am getting back - if i run this in google-colab

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-1-f87e37f02fde> in <module>
         27 
         28 # Find the total number of pages
    ---> 29 num_pages = soup.find('input', {'id': 'paginationPagesNum'})['value']
         30 
         31 # Loop through each page and extract the data
    
    TypeError: 'NoneType' object is not subscriptable



update: see what is gotten back: 

[![enter image description here][2]][2]


due to the help of riley.johnson3 i found out that the pagination wrapper should be fixed.
 - awesome many thanks for the quick help and the explanation - have gathered a set of data - its a sample. have to find out now how to get the full set of data. all the 700 records - with all the data.. - guess that we are allmost there. - again many thanks for your outstanding help. this is great... and appreciated alot... ;) 


  [1]: https://i.sstatic.net/DEX4K.jpg
  [2]: https://i.sstatic.net/qbKXY.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Unmitigated](https://stackoverflow.com/users/9513184)** (2023-03-23): It didn't find the element.
- **[Carcigenicate](https://stackoverflow.com/users/3000206)** (2023-03-23): That just means the `soup.find('input', {'id': 'paginationPagesNum'})` element wasn't found. It may only exist sometimes. If that's the case, you'll need to check if it was found before trying to subscript into it.
- **[zero](https://stackoverflow.com/users/525865)** (2023-03-24): thanks alot - have gathered a set of data - its a sample. have to find out now how to get the full set of data. all the 700 records - with all the data.. - guess that we are allmost there. - again many thanks for your outstanding help. this is great... and appreciated alot... ;)
