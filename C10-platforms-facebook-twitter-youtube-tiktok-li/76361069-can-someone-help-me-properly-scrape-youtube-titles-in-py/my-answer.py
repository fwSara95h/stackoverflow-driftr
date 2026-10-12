# Code from my Stack Overflow answer https://stackoverflow.com/a/76366675 (posted 2023-05-30), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import json

## a general function for extracting a JavaScript variable from a bs4 object
def get_jsScriptVal(jSoup, valDecl, isJson=True):
    script_finder = lambda s: s and valDecl in s
    for sc in jSoup.find('script', string=script_finder):
        for st in  sc.string.split(';'):
            ls, rs, *_ = [s.strip() for s in (st.split('=', 1) + [''])]
            if ls == valDecl and rs: return json.loads(rs) if isJson else rs


## specifically for your case
def get_ytInitialTitles(ySoup):
    contents = get_jsScriptVal(ySoup, 'var ytInitialData')['contents']
    tab1 = contents['twoColumnBrowseResultsRenderer']['tabs'][0]
    contents = tab1['tabRenderer']['content']['richGridRenderer']['contents']
    contents = [c['richItemRenderer']['content']['videoRenderer'] 
                for c in contents if 'richItemRenderer' in c and 
                'videoRenderer' in c['richItemRenderer']['content']]
    titles = [c['title']['runs'][0]['text'] for c in contents]
    return titles

# --- block 2 ---
import requests
from bs4 import BeautifulSoup
import json

#### DON'T FORGET TO PASTE THE FUNCTION DEFINITIONS INTO YOUR CODE TOO ####
## def get_jsScriptVal....
## def get_ytInitialTitles....
##########################################################################

def get_youtube_titles():
    url = 'https://www.youtube.com/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # titles = get_ytInitialTitles(soup) # Find YouTube title elements
        # for title in titles: print(title) # Extract and print the titles

        # OR [in one line]
        for title in get_ytInitialTitles(soup): print(title)

    except Exception as e:
        print('Failed to scrape due to', type(e), ':', e)

get_youtube_titles()
