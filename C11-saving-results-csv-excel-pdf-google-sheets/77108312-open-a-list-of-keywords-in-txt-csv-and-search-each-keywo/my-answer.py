# Code from my Stack Overflow answer https://stackoverflow.com/a/77109059 (posted 2023-09-15), extracted verbatim; may need the question's context to run.
search_list = ['weather', 'home depot', 'USPS Tracking'] ## FOR EXAMPLE
url = 'https://www.google.com/search'

headers = {
    'Accept' : '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}

results_list = []
for search in search_list:
    parameters = {'q': search}

    page = requests.get(url, headers = headers, params = parameters)
    try: page.raise_for_status()
    except Exception as e: 
        results_list.append({'keyword': search, 'error': repr(e)})
        continue
    soup = BeautifulSoup(page.content, 'html.parser')

    first_link = soup.select_one('#search a[href]:has(h3)')
    results_list.append({
        'keyword': search, 
        'first result': first_link.h3.get_text(' ', strip=True),
        'first link': first_link['href']
    })

    print(*[f'{k}: {v}' for k, v in results_list[-1].items()], '-'*80, sep='\n')
