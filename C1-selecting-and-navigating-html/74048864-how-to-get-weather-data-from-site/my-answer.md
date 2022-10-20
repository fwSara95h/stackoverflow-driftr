---
title: "How to get weather data from site?"
site: stackoverflow
question_id: 74048864
answer_id: 74135961
url: https://stackoverflow.com/a/74135961
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-20T07:31:10Z
last_edited: 2022-10-20T16:53:28Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74135961/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bbbcdef8603bd485dce3eb476c1e44cc63ab03789fcbe93b065b5101f41ebb4f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-20

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74135961>, 2022-10-20, last edited 2022-10-20; **accepted**; score 0. Text as retrieved 2026-10-12.

bs4's [BeautifulSoup](https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3#stepping-through-a-page-with-beautiful-soup) is often used to parse html and extract data. In your case, it can be utilized in several ways; first parse and get the html tree [`soup`] with

```python
import requests
from bs4 import BeautifulSoup

resp = requests.get("https://weather.gc.ca/city/pages/ab-52_metric_e.html")
soup = BeautifulSoup(resp.content, "html.parser")
```
[I like using the [`select`](https://www.codespeedy.com/find-elements-by-css-selector-in-beautifulsoup/) function, and you can consult [this reference](https://www.w3schools.com/cssref/css_selectors.asp) if you're confused by any of the selectors.]

<hr>

Now, if you want the current weather, then
```python
selector = '#mainContent details.visible-xs dt+dd'
for s in soup.select(selector):
    print(s.find_previous_sibling().text.strip(), s.text.strip(), end=' ')
```
will output
```lang-none
Wind: NE 8 km/h Temperature: 18.2°C Pressure: 101.9 kPa Dew point: -8.1°C Visibility: 24 km Humidity: 16% Date: 8:00 PM MDT Wednesday 19 October 2022 Observed at: Calgary Int'l Airport 
```
but you also commented about wanting the Condition and Tendency, and you *could* get the Condition simply with 
```python
print(f"Condition: {soup.select_one('details.visible-xs div>img+p')}")
```
but Tendency is actually in a different section which is not visible. You could change `selector` to `'#mainContent section:first-of-type dt+dd'` or even to just `'dt+dd'` and run `for s in soup.select(selector)....` again, but you will several repeated values and unwanted data, so we probably need a more structured approach.

<hr> <hr>

So I defined a function that will take a section of the tree and return *one* value per condition - 
```python
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
```

Now you can define which parts of the data you want, and what order you want it in:

```python
toPrint = [
    'Condition', 'Pressure', 'Tendency', 'Temperature', 
    'Dew point', 'Humidity', 'Wind', 'Visibility'
] # the parts you mentioned wanting

cwc = getWeatherData(soup.select_one('#mainContent section'), toPrint)
print(f'\n##############\nAs Dictionary:\n{cwc}')
```
and that will output
```markdown
Condition: Partly Cloudy Pressure: 101.3 kPa Tendency: Rising Temperature: 8.9°C Dew point: -0.3°C Humidity: 52% Wind: N 43  gust 54 km/h Visibility: 24 km 

##############
As Dictionary:
{'Condition': 'Partly Cloudy', 'Pressure': '101.3 kPa', 'Tendency': 'Rising', 'Temperature': '8.9°C', 'Dew point': '-0.3°C', 'Humidity': '52%', 'Wind': 'N 43  gust 54 km/h', 'Visibility': '24 km'}
```
[Send `pEnd='\n'` if you want each value printed on a separate line, or `pEnd=False` if you don't want to print at all; and send `pKeys='all'` (instead of `toPrint`) if you want to see all available data.]

<hr><hr>

If you wanted, you could also see all collapsible sections (hidden and visible) with
```python
wcSects = [s.find_parent('details') for s in soup.select('details dd+dt')]

for s in list(set(wcSects)):
  print('\n#######', end=' ')  
  h2 = s.select_one('summary h2')
  print((h2 if h2 else s.summary).text.strip(), '#######')
  getWeatherData(s, 'all', pEnd=' | ')
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[laisp-lostlamb](https://stackoverflow.com/users/20162704)** (2022-10-20): Thanks, this is working very nicely, is it possible to use the text as dictionary key, and the readings as the dictonary value like so ?  mydict = {"Pressure": "101.0 kPa","Condition": "Mostly Cloudy"...} mylist = ["Pressure: 101.0 kPa, "Condition: Mostly Cloudy"...] I know I haven't asked this initially, either list or dictonary like above would work nicely for the next section needing this result.
- **me** (2022-10-20): @laisp-CAD please see the edited function and output
- **[laisp-lostlamb](https://stackoverflow.com/users/20162704)** (2022-10-20): @Drifter95, thank you for the prompt response, this is what I am looking for, appreciate your help!
- **[laisp-lostlamb](https://stackoverflow.com/users/20162704)** (2022-10-20): @Drifter95 I do have another similiar post for web scrapping that I will need help on... Soon I will have to ask if bs4 package and be converted or added in IronPython2....it's possible this environment may change...which I'm also not familiar with.
- **me** (2022-10-20): @laisp-CAD I'm not particularly familiar with IronPython myself, but bs4 is a purely python library so it *should* be unproblematic. good luck!
- **[laisp-lostlamb](https://stackoverflow.com/users/20162704)** (2022-10-20): @Drifter95 Thanks, your other solution worked as well, though I end up asking for a bit extra on top hope you don't mind.
