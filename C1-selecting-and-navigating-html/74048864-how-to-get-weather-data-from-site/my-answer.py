# Code from my Stack Overflow answer https://stackoverflow.com/a/74135961 (posted 2022-10-20), extracted verbatim; may need the question's context to run.

# --- block 1 ---
import requests
from bs4 import BeautifulSoup

resp = requests.get("https://weather.gc.ca/city/pages/ab-52_metric_e.html")
soup = BeautifulSoup(resp.content, "html.parser")

# --- block 2 ---
selector = '#mainContent details.visible-xs dt+dd'
for s in soup.select(selector):
    print(s.find_previous_sibling().text.strip(), s.text.strip(), end=' ')

# --- block 3 ---
print(f"Condition: {soup.select_one('details.visible-xs div>img+p')}")

# --- block 4 ---
def getWeatherData(sectionSoup, pKeys='all', cwcSelector='dt+dd', pEnd=' '):
    wc = []
    for s in sectionSoup.select(cwcSelector):
        wcName = s.find_previous_sibling().text.strip()
        wcVal = s.text.strip()

        vis = 'hidden' if s.find_parent(class_='hidden-xs') else 'visible'
        wc.append((wcName, wcVal, vis)) 

    wcs = sorted(wc, key=lambda c: c[2], reverse=True) # visible first
    if pKeys == 'all' or type(pKeys) != list: 
      pKeys = list(set([c[0] for c in wc]))
      allKeys = True
    else: allKeys = False

    forOp = []
    for k in pKeys:
      kvp = [c for c in wcs if c[0].replace(':','')==k.replace(':','')]
      if kvp == []:
          # continue # if you want to skip
          if pEnd is None or type(pEnd) == str: 
              print(f'! UNAVAILABLE : "{k}" !', end=pEnd)
      else: 
          if allKeys: k = k.replace(':', '') # remove if you want to preserve originial text
          forOp.append((k, kvp[0][1]))
          if pEnd is None or type(pEnd) == str: 
              print(kvp[0][0], kvp[0][1], end=pEnd) 

    print()
    return dict(forOp)

    # if you want all the values, including repeats:
    # return {'filtered': forOp, 'unfiltered': wc}

# --- block 5 ---
toPrint = [
    'Condition', 'Pressure', 'Tendency', 'Temperature', 
    'Dew point', 'Humidity', 'Wind', 'Visibility'
] # the parts you mentioned wanting

cwc = getWeatherData(soup.select_one('#mainContent section'), toPrint)
print(f'\n##############\nAs Dictionary:\n{cwc}')

# --- block 6 ---
wcSects = [s.find_parent('details') for s in soup.select('details dd+dt')]

for s in list(set(wcSects)):
  print('\n#######', end=' ')  
  h2 = s.select_one('summary h2')
  print((h2 if h2 else s.summary).text.strip(), '#######')
  getWeatherData(s, 'all', pEnd=' | ')
