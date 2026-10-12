# Code from my Stack Overflow answer https://stackoverflow.com/a/74090309 (posted 2022-10-16), extracted verbatim; may need the question's context to run.

# --- block 1 ---
soup.select_one('table[id="form1:tableEx1"]').select('tbody tr')

# --- block 2 ---
tableRows = [
    tuple([c.text.strip() for c in r.find_all(['th', 'td'])]) for r 
    in BeautifulSoup(tHtml).select_one(
        'table[id="form1:tableEx1"]'
    ).select('tbody tr')
]

# --- block 3 ---
# import pandas
pandas.read_html(htmlString, attrs={'id': 'form1:tableEx1'})[0]

# --- block 4 ---
# get a list of tagNames between a tag and its ancestor
def linkAncestor(t, a=None):
  aList = []
  while t.parent != a or a is None:
    t = t.parent 
    if t is None:
      if a is not None: aList = None
      break
    aList.append(t.name)
  return aList
  # if a == t.parent: return []
  # if a is None, return tagNames of ALL ancestors 
  # if a not in t.parents: return None

def getStrings_table(xSoup): 
  # not perfect, but enough for me so far
  tableTags = ['table', 'tr', 'th', 'td']
  return "\n".join([
      c.get_text(' ', strip=True) for c in xSoup.children 
      if c.get_text(' ', strip=True) and (c.name is None or (
          c.name not in tableTags and not c.find(tableTags)
      ))
  ])

# --- block 5 ---
def tablesFromSoup(mSoup, mode='a', simpleOp=False):
  typeDict = {'t': 'table', 'r': 'row', 'c': 'cell'}
  finderDict = {'t': 'table', 'r': 'tr', 'c': ['th', 'td']}
  refDict = {
    'a': {'tables': 't', 'loose_rows': 'r', 'loose_cells': 'c'},
    't': {'inner_tables': 't', 'rows': 'r', 'loose_cells': 'c'},
    'r': {'inner_tables': 't', 'inner_rows': 'r', 'cells': 'c'}, 
    'c': {'inner_tables': 't', 'inner_rows': 'r', 'inner_cells': 'c'}
  }
  mode = mode if mode in refDict else 'a'

  # for when simpleOp = True
  nextModes = {'a': 't', 't': 'r', 'r': 'c', 'c': 'a'}
  mainCont = {
      'a': 'tables', 't': 'rows', 'r': 'cells', 'c': 'inner_tables'
  }

  innerContent = {} 
  for k in refDict[mode]: 
    if simpleOp and k != mainCont[mode]: 
      continue

    fdKey = refDict[mode][k] # also the mode for recursive call
    innerSoups = [(
        s, linkAncestor(s, mSoup)
    ) for s in mSoup.find_all(finderDict[fdKey])] 
    innerSoups = [s for s, la in innerSoups if not (
        'table' in la or 'tr' in la or 'td' in la or 'th' in la
    )]

    # recursive call
    kCont = [tablesFromSoup(s, fdKey, simpleOp) for s in innerSoups] 

    if simpleOp:
      if kCont == [] and mode == 'c': break
      return tuple(kCont) if mode == 'r' else kCont

    # if not empty, check if header then add to output
    if kCont: 
      if 'row' in k:
        for i in range(len(kCont)):
          if 'isHeader' in kCont[i]: continue
          kCont[i]['isHeader'] = 'thead' in innerSoups[i][1]
      if 'cell' in k:
        isH = [(c[0].name == 'th' or 'thead' in c[1]) for c in innerSoups]
        if sum(isH) > 0:
          if mode == 'r':
            innerContent['isHeader'] = True
          else: 
            innerContent[f'isHeader_{k}'] = isH

      innerContent[k] = kCont 

  if innerContent == {} and mode == 'c':
    innerContent = mSoup.get_text(' ', strip=True) 
  elif mode in typeDict:
    if innerContent == {}: 
      innerContent['innerText'] = mSoup.get_text(' ', strip=True)
    else:
      innerStrings = getStrings_table(mSoup)
      if innerStrings:
        innerContent['stringContent'] = innerStrings
    innerContent['type'] = typeDict[mode] 

  return innerContent
