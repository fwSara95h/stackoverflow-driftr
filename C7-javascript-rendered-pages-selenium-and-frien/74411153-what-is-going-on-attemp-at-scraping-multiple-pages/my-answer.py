# Code from my Stack Overflow answer https://stackoverflow.com/a/74418899 (posted 2022-11-13), extracted verbatim; may need the question's context to run.
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

url = "https://www.gumtree.com/search?search_category=all&q=ferrari"  
maxTries = 6 # or as you prefer
pageTryCt = 0

while url: 
    print('', end=url)
    response = HTMLSession().get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    # you can use html.parser but you probably need to have html5lib atleast installed

    name = soup.find_all("h2", class_="listing-title") # h2 not div
    price = soup.find_all("strong", class_="h3-responsive") # specify class_

    next_page = soup.select_one("li.pagination-next > a:not(.pagination-disabled)") 
    # class is pagination-next not pagination-page
    # add :not(.pagination-disabled) to exclude disabled button (on last page)

    if name and price: print('')
    for p, n in zip(price, name):
        print(f'{p.text.strip():>10}   {n.text.strip()}') # just to line up

    if next_page:
        next_url = next_page.get("href")
        url = urljoin(url, next_url)

        pageTryCt = 0
        time.sleep(3)
        print('\n') # just adding space to separate pages
    else:
        if pageTryCt < maxTries and len(price+name) == 0:
            pageTryCt += 1 
            print('', end=f'\r[after {45*pageTryCt}sec wait] ')
            time.sleep(45*pageTryCt)
        else: url = None
