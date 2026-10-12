# Code from my Stack Overflow answer https://stackoverflow.com/a/74739128 (posted 2022-12-09), extracted verbatim; may need the question's context to run.
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
}
url = 'https://www.google.com/search?client=safari&rls=en&q=프로그래밍+공부&ie=UTF-8&oe=UTF-8'

response = requests.get(url, headers=headers)
reqErr = response.raise_for_status() # just a good habit to check
if reqErr: print(f'!"{reqErr}" - while getting ', url)

soup = BeautifulSoup(response.content, 'html.parser')

find = soup.select('#taw')
if not find: ## save html to check [IN AN EDITOR, NOT a browser] if expected elements are missing
    hfn = 'x.html'
    with open(hfn, 'wb') as f: f.write(response.content)
    print(f'saved html to  "{hfn}"')

print(find)
