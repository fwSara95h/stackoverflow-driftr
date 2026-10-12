# Code from my Stack Overflow answer https://stackoverflow.com/a/73862506 (posted 2022-09-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
#def getReqUrl...

# --- block 2 ---
reqUrl = getReqUrl()
prevTime, prevAt = '', datetime.now()
while True:
  ures = json.loads(urlopen(reqUrl).read())
  if 'observations' not in asd:
    reqUrl = getReqUrl()
    ures = json.loads(urlopen(reqUrl).read())

# --- block 3 ---
wSpeed = ures['observations'][0]['imperial']['windSpeed']
wGust = ures['observations'][0]['imperial']['windGust']
print('',end=f'\r[+{td}s -> {obvTime}]:   {wGust} ° / {wSpeed} °mph')

# --- block 4 ---
if prevTime < obvTime:
  prevTime = obvTime
  prevAt = datetime.now()
  print('')

# --- block 5 ---
def getReqUrl():
  url = 'https://www.wunderground.com/dashboard/pws/KORPISTO1'    
  soup = BeautifulSoup(urlopen(url), 'html.parser')
  appText = soup.select_one('#app-root-state').text

# --- block 6 ---
nxtSt = json.loads(appText.replace('&q;','"'))['wu-next-state-key'] 
return [
    ns for ns in nxtSt.values() 
    if 'observations' in ns['value'] and 
    len(ns['value']['observations']) == 1
][0]['url'].replace('&a;','&')

# --- block 7 ---
def getReqUrl():
  url = 'https://www.wunderground.com/dashboard/pws/KORPISTO1'    
  soup = BeautifulSoup(urlopen(url), 'html.parser')
  appText = soup.select_one('#app-root-state').text

  rUrl = 'https://api.weather.com/v2/pws/observations/current'
  rUrl = rUrl + appText.split(rUrl)[1].split('&q;')[0]
  return rUrl.replace('&a;','&')
