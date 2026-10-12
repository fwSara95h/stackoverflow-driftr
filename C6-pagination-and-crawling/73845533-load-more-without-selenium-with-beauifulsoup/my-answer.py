# Code from my Stack Overflow answer https://stackoverflow.com/a/73846749 (posted 2022-09-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def getMoreRevs(rSoup, rootUrl='https://www.imdb.com', lmSelector='div.load-more-data'):
  loadMore = rSoup.select_one(lmSelector)
  if loadMore:

# --- block 2 ---
if 'data-key' not in loadMore.attrs:
  print(f'not data-key attribute in {lmSelector} :\n', loadMore)
  return None

# --- block 3 ---
#else:
print(f"! search for {lmSelector} returned {type(loadMore)} ",loadMore)
return None

# --- block 4 ---
#imports 
#excel setup  
#def getMoreRevs...

reqUrl = "https://www.imdb.com/title/tt0120762/reviews?ref_=tt_urv"
while reqUrl:
  source = requests.get(reqUrl)
  source.raise_for_status()
  soup = BeautifulSoup(source.text,'html.parser')

  reviews = soup.find_all('div', class_="review-container") 
  #for review in reviews ...

  reqUrl = getMoreRevs(soup)

#excel.save...
