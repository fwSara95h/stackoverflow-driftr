# Code from my Stack Overflow answer https://stackoverflow.com/a/73887971 (posted 2022-09-28), extracted verbatim; may need the question's context to run.
from bs4 import BeautifulSoup
page = requests.get('https://indianexpress.com/section/technology/')
bSoup = BeautifulSoup(page.content, 'html.parser')
links_list = bSoup.find_all('a')

#filter links for articles:
article_links_all = [
    l.get('href') for l  in links_list 
    if 'href' in l.attrs and 'article/' in l.attrs['href']
]

# get rid of duplicates:
article_links = list(set(article_links_all))

for link in article_links:
    print(link)
