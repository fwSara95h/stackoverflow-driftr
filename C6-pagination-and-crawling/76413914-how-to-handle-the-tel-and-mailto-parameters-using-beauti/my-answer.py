# Code from my Stack Overflow answer https://stackoverflow.com/a/76414759 (posted 2023-06-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def extract_url(url):
    ## check BEFORE request
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ['http', 'https']:
        return []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = []

    ## add href=True to find_all --> no need to check if href
    for link in soup.find_all('a', href=True):
        urls.append(urljoin(url, link.get('href') ))

# --- block 2 ---
for link in soup.find_all('a', href=True):
    parsed_href = urlparse(href := link.get('href'))
    if parsed_href.scheme in ['', 'http', 'https']:
        urls.append(urljoin(url, href))

# --- block 3 ---
def crawl(url, word, max_visits=1000):
    visited = set()
    dead_pages = set()
    url_queue = [url]

    for url in url_queue:  # loop instead of recursion
        if url in visited:
            return
        visited.add(url)

        status_code = check_url(url)
        if status_code == 404:
            dead_pages.add(url)

        if word in url:
            print(f'URL "{url}" contains "{word}".')

        urls = extract_url(url)

        ## add to queue instead of recursive call
        url_queue += [u for u in urls if u not in url_queue] 

        if not len(visited) < max_visits:
            break ## stop when limit is reached


    return dead_pages
