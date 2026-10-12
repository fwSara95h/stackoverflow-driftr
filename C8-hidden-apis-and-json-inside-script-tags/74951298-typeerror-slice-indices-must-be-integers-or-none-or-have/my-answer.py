# Code from my Stack Overflow answer https://stackoverflow.com/a/74961326 (posted 2022-12-30), extracted verbatim; may need the question's context to run.

# --- block 1 ---
cont = requests.get('https://www.facebook.com:443/help', headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})

# --- block 2 ---
> TypeError: slice indices must be integers or None or have an __index__ method
>

# --- block 3 ---
print('start:', start)
if start == "":
    print('{__bbox":} not found')
    return

count = 0

# --- block 4 ---
# soup = bs4.BeautifulSoup(cont.content, "html5lib")
soup = bs4.BeautifulSoup(cont.content) # don't define the parser 
# soup = bs4.BeautifulSoup(cont.content, "html.parser") # you could also try other parsers

# --- block 5 ---
text = soup.find_all(lambda t: t.name == 'script' and '"__bbox"' in t.get_text())

for mystr in [s.get_text() for s in text]:
    print("this is: ", mystr.find('__bbox":'))
    txtstr += mystr
    start = mystr.find('__bbox":') + len('__bbox":')

# --- block 6 ---
>         print('end:', end)
>

# --- block 7 ---
>         data = json.loads(txtstr[start:end+1])
>

# --- block 8 ---
# import json, requests, bs4, slimit
# from slimit.visitors import nodevisitor 
# def findObj_inJS... ## PASTE FROM https://pastebin.com/UVcLniSG

# class CmsIDs:
    def GetIDs():
        # cont=requests.get('https://www.facebook.com:443/help',headers=Static.headers)
        cont = requests.get('https://www.facebook.com:443/help', headers={
            'accept': ';'.join(
                [ 'text/html,application/xhtml+xml,application/xml',
                  'q=0.9,image/avif,image/webp,image/apng,*/*',
                  'q=0.8,application/signed-exchange',
                  'v=b3', 'q=0.9'  ])})

        ## in case of request errors ##
        try: cont.raise_for_status()
        except Exception as e:
            print('failed to fetch page HTML -', type(e), e)
            return
        print('fetched', cont.url, 'with', cont.status_code, cont.reason)

        soup = bs4.BeautifulSoup(cont.content)
        scrCond = lambda t: t.name == 'script' and '"__bbox"' in t.get_text()
        jScripts = [s.get_text() for s in soup.find_all(scrCond)] 
        print(f'Found {len(jScripts)} script tags containing {{"__bbox"}}')

        data = [findObj_inJS(s,'"__bbox"') for s in jScripts]
        print('--- search ---')
        CmsIDs.search(data) 

    # def search(data)....

# --- block 9 ---
def search(data):
    rList, dKeys = [], ['cms_object_id', 'cmsID', 'name']
    if isinstance(data, dict):
        dObj = {k: data[k] for k in dKeys if k in data}
        rList += [dObj] if dObj else []

        for k, v in dObj.items(): print(k, v)
        if dObj: print('---')

        for val in data.values(): rList += CmsIDs.search(val)
    if isinstance(data, list):
        for val in data: rList += CmsIDs.search(val)
    return rList

# --- block 10 ---
return CmsIDs.search(data)

# --- block 11 ---
# import pandas
pandas.DataFrame(cmsList).to_csv('CmsIDs_GetIDs.csv', index=False)

# --- block 12 ---
print(pandas.DataFrame(cmsList, dtype=str).fillna('').to_markdown())
