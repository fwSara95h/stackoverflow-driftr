# Code from my Stack Overflow answer https://stackoverflow.com/a/77077760 (posted 2023-09-10), extracted verbatim; may need the question's context to run.
from bs4 import BeautifulSoup 
from requests_html import HTMLSession

url = "https://www.anisearch.de/anime/2788,naruto"
source = HTMLSession().get(url)
# source.raise_for_status() ## good habit in general

soup = BeautifulSoup(source.content, 'html.parser')
