# Code from my Stack Overflow answer https://stackoverflow.com/a/73887424 (posted 2022-09-28), extracted verbatim; may need the question's context to run.
from bs4 import BeautifulSoup
import requests

r = requests.get("https://welovemanga.one/2777/92578/")
soup = BeautifulSoup(r.content, "html.parser")
thumbnail_elements = soup.find_all("img", class_ = "chapter-img")
proxyRoot = 'https://welovekai.com/proxy.php?link='

for element in thumbnail_elements:
    print(proxyRoot+''.join(element['data-original'].split()))
