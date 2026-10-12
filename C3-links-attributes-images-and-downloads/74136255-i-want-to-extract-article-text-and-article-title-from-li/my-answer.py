# Code from my Stack Overflow answer https://stackoverflow.com/a/74147483 (posted 2022-10-21), extracted verbatim; may need the question's context to run.
for i in range(0,len(df)):
    j = df.iloc[i].values
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    page = requests.get(j[0],headers = headers)#loading text in url

    if page.status_code != 200 or not page.content:
        cMsg = '' if page.content else 'Empty content - '
        print(f'{cMsg}{page.status_code} {page.reason} - with url {j[0]}')
        break

    soup = BeautifulSoup(page.content,'html.parser')#parsing url text
    content = soup.findAll(attrs = {'class':'td-post-content'})#extracting only text part

    # empty content if not td-post-content found
    content = content[0].text if len(content) > 0 else '' 

    title = soup.findAll(attrs = {'class':'entry-title'})#extracting title of website
    #title = title[16].text
    print(content)
