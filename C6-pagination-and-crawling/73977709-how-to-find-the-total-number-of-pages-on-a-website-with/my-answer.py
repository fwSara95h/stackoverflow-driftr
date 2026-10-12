# Code from my Stack Overflow answer https://stackoverflow.com/a/73982156 (posted 2022-10-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
import requests
from bs4 import BeautifulSoup
import math

def soupFromUrl(scrapeUrl):
  req = requests.get(scrapeUrl)
  if req.status_code == 200:
    return BeautifulSoup(req.text, 'html.parser')
  else:
    raise Exception(f'{req.reason} - failed to scrape {scrapeUrl}')


def getPageTotal(url):
  soup = soupFromUrl(url)

  #totalResults = int(soup.find('label').get_text().split('(')[-1].split(')')[0])  
  totalResults = int(soup.p.strong.get_text()) # both searches should work
  perPageResults = len(soup.select('.m-show')) #probably always 20

  print(f'{perPageResults} of {totalResults} results per page') 
  if not (perPageResults > 0 and totalResults > 0):
    return 0 

  lastPageNum = math.ceil(totalResults/perPageResults)

  # Contingencies - will hopefully never be needed
  lpSoup = soupFromUrl(f'{url}?page={lastPageNum}')
  if lpSoup.select('.m-show'): #page exists
    while lpSoup.select_one('a[rel="next"]'):
      nextLink = lpSoup.select_one('a[rel="next"]')['href']
      lastPageNum = int(nextLink.split('page=')[-1])
      lpSoup = soupFromUrl(nextLink)
  else: #page does not exist
    while not (lpSoup.select('.m-show') or lastPageNum < 1): 
      lastPageNum = lastPageNum - 1
      lpSoup = soupFromUrl(f'{url}?page={lastPageNum}')
  # end Contingencies section

  return lastPageNum

# --- block 2 ---
def data_fetch(url):
  school_info = []  
  nextUrl = url
  while nextUrl:
    soup = soupFromUrl(nextUrl)

    #GET YOUR DATA FROM PAGE

    nextHL = soup.select_one('a[rel="next"]')
    nextUrl = nextHL.get('href') if nextHL else None 

  # code after fetching all pages' data

# --- block 3 ---
def data_fetch(url, maxPages):
  school_info = []  

  for p in range(1, maxPages+1):
    soup = soupFromUrl(f'{url}?page={p}')
    if not soup.select('.m-show'):
      break

    #GET YOUR DATA FROM PAGE 

  # code after fetching all pages' data [upto max]
