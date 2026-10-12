# Code from my Stack Overflow answer https://stackoverflow.com/a/73874251 (posted 2022-09-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---

def getReqUrl(scrapeUrl):
  res = requests.get(scrapeUrl)
  ercot_soup = BeautifulSoup(res.text, "html.parser")

  script = [l.split('"') for l in [
      s for s in ercot_soup.select('script')
      if 'reportListUrl' in  s.text 
      and 'reportTypeID' in s.text
  ][0].text.split('\n') if l.count('"') == 2]

  rtID = [l[1] for l in script if 'reportTypeID' in l[0]][0]
  rlUrl = [l[1] for l in script if 'reportListUrl' in l[0]][0]
  rdUrl = [l[1] for l in script if 'reportDownloadUrl' in l[0]][0]

  return f'{rlUrl}{rtID}&_={int(time.time())}', rdUrl

# --- block 2 ---
url = 'https://www.ercot.com/mp/data-products/data-product-details?id=NP3-233-CD'
reqUrl, ddUrl = getReqUrl(url)
reqRes = requests.get(reqUrl[0]).text
rsJson = json.loads(reqRes)

for doc in rsJson['ListDocsByRptTypeRes']['DocumentList']:
  d = doc['Document'] 
  downloadLink = ddUrl+d['DocID']
  #print(f"{d['FriendlyName']} {d['PublishDate']} {downloadLink}")
  print(f"Download '{d['ConstructedName']}' at\n\t {downloadLink}")
print(len(rsJson['ListDocsByRptTypeRes']['DocumentList']))
