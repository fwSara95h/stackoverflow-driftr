# Code from my Stack Overflow answer https://stackoverflow.com/a/75283337 (posted 2023-01-30), extracted verbatim; may need the question's context to run.
maxPage = 9
datePublished = []
headline = []
description =[]
urls = []

for page in range(1, maxPage+1):
    url = f"https://www.consilium.europa.eu/en/press/press-releases/?page={page}"
    res = requests.get(url)
    print(f'[page {page:>3}]', res.status_code, res.reason, 'from', res.url)
    soup = BeautifulSoup(res.content, 'lxml')

    soup_content = soup.find_all('li', {'class':['list-item ceu clearfix','list-item gsc clearfix','list-item euco clearfix','list-item eg clearfix' ]})
    for i in range(len(soup_content)):
        datePublished.append(soup_content[i].find('span', {'itemprop': 'datePublished'}).attrs['content'])
        headline.append(soup_content[i].find('h3', {'itemprop': 'headline'}).get_text().strip())
        description.append(soup_content[i].find('p', {'itemprop': 'description'}).get_text().strip())
        urls.append('https://www.consilium.europa.eu{}'.format(soup.find('a', {'itemprop': 'url'}).attrs['href']))
