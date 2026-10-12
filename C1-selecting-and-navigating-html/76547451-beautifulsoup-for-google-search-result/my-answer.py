# Code from my Stack Overflow answer https://stackoverflow.com/a/76547860 (posted 2023-06-24), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def search_google(text, max_results=3):
    ## split then join to convert spaces to + in link
    url = 'https://google.com/search?q=' + '+'.join(text.split())
    print('From', url, '\n---\n')
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    ## loop through only the first results up to max_results
    for d in soup.select('div:has(>div>a[href] h3)')[:max_results]:
        print(d.h3.get_text(' ').strip()) ## title

        ## link
        res_link = d.select_one('a[href]:has(h3)').get('href') 
        if res_link.startswith('/url?q='):
            res_link = res_link.split('=',1)[1].split('&')[0]
        print(res_link) 

        ## description
        print(d.select_one('div:has(>a[href] h3)+div').get_text(' ').strip())

        print('\n---\n') ## separate results

# --- block 2 ---
while (q:=input("Enter query [or q to exit]")) != 'x': search_google(q)
