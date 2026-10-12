# Code from my Stack Overflow answer https://stackoverflow.com/a/74947523 (posted 2022-12-29), extracted verbatim; may need the question's context to run.

# --- block 1 ---
selRef = {
    'title': 'div.content>a.post-link[href]', 'date': 'p.text-date',
    'url': ('div.content>a.post-link[href]', 'href'),
    # 'category': 'div.content>p.post-category-timeline',
    # 'excerpt': 'div.content>p.post-content-rendered',
}

soup = linkToSoup_selenium('https://danskfolkeparti.dk/nyheder/', ecx=[
    'div.timeline>div>div.content>a.post-link[href]',  # load links [+titles]
    'div.timeline>div>p.text-date'  # load dates [probably redundant]
], clickFirst=[
    'a[role="button"][data-cli_action="accept_all"]'  # accept cookies [optional]
], by_method='css', scrollN=(20, 5), returnErr=True) # scroll 20x with 5sec breaks

# --- block 2 ---
if isinstance(soup, str):
    print(type(soup), miniStr(soup)[:100])  # print error message
    prTimeline = []
else:
    prTimeline = [{k: v for k, v in zip(
        list(selRef.keys()), selectForList(pr, list(selRef.values()))
    )} for pr in soup.select('div.timeline>div')]

# --- block 3 ---
## [only the first 3 of 76 are included below] ##
[{'title': 'Året 2022 viste hvad Dansk Folkeparti er gjort af',
  'date': '23/12/2022',
  'url': 'https://danskfolkeparti.dk/nyheder/mortens-nyhedsbrev/aaret-2022-viste-hvad-dansk-folkeparti-er-gjort-af/'},
 {'title': 'Mette Frederiksen har stemt danskerne hjem til 2001',
  'date': '13/12/2022',
  'url': 'https://danskfolkeparti.dk/nyheder/mortens-nyhedsbrev/mette-frederiksen-har-stemt-danskerne-hjem-til-2001/'},
 {'title': 'Vi klarede folketingsvalget – men der skal kæmpes lidt endnu',
  'date': '23/11/2022',
  'url': 'https://danskfolkeparti.dk/nyheder/mortens-nyhedsbrev/vi-klarede-folketingsvalget-men-der-skal-kaempes-lidt-endnu/'}]

# --- block 4 ---
# import  cloudscraper
qStr = 'categories=20,85,15,83,73,84,&before=2022-12-28T23:59:59'
qStr += '&after=1990-05-08T01:01:01&per_page=99&page=1'
apiUrl = f'https://danskfolkeparti.dk/wp-json/wp/v2/posts?{qStr}'
prTimeline = [{
    'title': pr['title']['rendered'],
    'date': pr['date'], # 'date': pr['date_gmt'], 
    'url': pr['link']
} for pr in cloudscraper.create_scraper().get(apiUrl).json()]

# --- block 5 ---
prTimeline, rStatus = danskfolkeparti_apiScraper(pathsRef={'title': ['title', 'rendered'], 'date': ['date'], 'url': ['link']})

# --- block 6 ---
# from bs4 import BeautifulSoup

### FIRST PASTE EVERYTHING FROM https://pastebin.com/aSQrW9ff ###

prTimeline, prtStatus = danskfolkeparti_apiScraper()
prCats = danskfolkeparti_catNames([pr['category'] for pr in prTimeline])
for pi, (pr, prCat) in enumerate(zip(prTimeline, prCats)):
    prTimeline[pi]['category'] = prCat
    cTxt = BeautifulSoup(pr['content']).get_text(' ')
    cTxt = ' '.join(w for w in cTxt.split() if w) # reduce whitescpace
    prTimeline[pi]['content'] = cTxt

# --- block 7 ---
# import pandas 

fileName = 'prTimeline.csv' # 'dfn_prTimeline_api.csv' # 'dfn_prTimeline_sel.csv'
pandas.DataFrame(prTimeline).to_csv(fileName, index=False)
