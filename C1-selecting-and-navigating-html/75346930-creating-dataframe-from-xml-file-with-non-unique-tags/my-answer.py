# Code from my Stack Overflow answer https://stackoverflow.com/a/75350849 (posted 2023-02-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# from bs4 import BeautifulSoup

def getXMLdata(xmlFile:str, defaultVal=None):
    with open(xmlFile, 'r') as f: xSoup = BeautifulSoup(f, 'xml')
    selRef = {
        'FileName': 'MediaLocation[sourceType="Primary"] Location',
        'Brand': 'BrandName', 'ID': 'ContentId',
        'URL': 'MediaLocation[sourceType="Proxy"] Location'
    }
    xfDets = {} # {'fromFile': xmlFile} 
    for k, sel in selRef.items():
        t = xSoup.select_one(sel)
        xfDets[k] = t.get_text(' ').strip() if t else defaultVal 

    fn = xfDets.get('FileName')
    if isinstance(fn, str) and '.' in fn:  # remove extensions like ".mp4"
        xfDets['FileName'] = '.'.join(fn.split('.')[:-1])
    return xfDets

# --- block 2 ---
{'FileName': 'zzTap_zzTop_AAAA1111999Z_30s_Pill_aa-bb',
 'Brand': 'zzTop',
 'ID': 'AAAA1111999Z',
 'URL': 'https://app.url.com/DMM/DL/wew52f'}

# --- block 3 ---
# import pandas
# filesList = ['x.xml', ...] ## LIST OF XML FILES
xDF = pandas.DataFrame([getXMLdata(x) for x in filesList])
