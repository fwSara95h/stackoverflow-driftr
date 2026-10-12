# Code from my Stack Overflow answer https://stackoverflow.com/a/75052654 (posted 2023-01-09), extracted verbatim; may need the question's context to run.
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
