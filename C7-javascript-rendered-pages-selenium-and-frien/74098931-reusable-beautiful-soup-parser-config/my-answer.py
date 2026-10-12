# Code from my Stack Overflow answer https://stackoverflow.com/a/74104518 (posted 2022-10-18), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def getSoupData(mSoup, dataStruct, maxDepth=None, curDepth=0):
    if type(dataStruct) != dict:
        # so selector/targetAttr can also be sent as a single string 
        if str(dataStruct).startswith('"ta":'):
            dKey = 'targetAttr'
        else:
            dKey = 'cssSelector'
        dataStruct = str(dataStruct).replace('"ta":', '', 1)
        dataStruct = {dKey: dataStruct}

    # default values: isList=False, items={}
    isList = dataStruct['isList'] if 'isList' in dataStruct else False
    if 'items' in dataStruct and type(dataStruct['items']) == dict:
        items = dataStruct['items']
    else: items = {}

    # no selector -> just use the input directly
    if 'cssSelector' not in dataStruct:
        soup = mSoup if type(mSoup) == list else [mSoup]
    else:
        soup = mSoup.select(dataStruct['cssSelector'])
        # so that unneeded parts are not processed:
        if not isList: soup = soup[:1]

    # return empty nothing was selected
    if not soup: return [] if isList else None

    # return text or attribute values - no more recursion
    if items == {}:
        if 'targetAttr' in dataStruct:
            targetAttr = dataStruct['targetAttr']
        else:
            targetAttr = '"text"'  # default

        if targetAttr == '"text"':
            sData = [s.get_text(strip=True) for s in soup]
        # can put in more options with elif
        else:
            sData = [s.get(targetAttr) for s in soup]

        return sData if isList else sData[0]

    # return error - recursion limited
    if maxDepth is not None and curDepth > maxDepth:
        return {
            'errorMsg': f'Maximum [{maxDepth}] exceeded at depth={curDepth}'
        }

    # recursively get items
    sData = [dict([(i, getSoupData(
        s, items[i], maxDepth, curDepth + 1
    )) for i in items]) for s in soup]

    return sData if isList else sData[0]
    # return list only if isList is set

# --- block 2 ---
# import json
configC = json.load(open('crawlerConfig_paedriactia.json', 'r'))

url = configC['url']
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

dStruct = configC['data_structure']
getSoupData(soup, dStruct)
