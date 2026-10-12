# Code from my Stack Overflow answer https://stackoverflow.com/a/75263236 (posted 2023-01-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# generates keys to be used in dictionary - tag name or object type
def getElemKey(pEl):
    if isinstance(pEl, str): return 'string'
    pName, pClass = getattr(pEl, 'name', None), str(type(pEl))
    pClass = pClass.replace("<class '",'',1).rstrip("'>").split('.')[-1]
    return str(pName).strip() if isinstance(pName, str) else pClass

# converts list of tuples to dictionary; adds _# to avoid duplicate keys
def dict_enumKeys(tupList, noCount=['textContent', 'contents']):
    invalidT = [t for t in tupList if (
        isinstance(tupList, tuple) and len(t)==2
    )] if isinstance(tupList, list) else True
    if invalidT: return tupList
    if len(tupList)==1 and tupList[0][0] in noCount: return tupList[0][1]

    keyCt, toRet = {}, {}
    for k, v in tupList:
        kCt = keyCt[str(k)] = keyCt.get(str(k), 0) + 1
        if not (k in noCount and kCt==1): k = f'{k}_{kCt}'
        try: toRet[k] = dict_enumKeys(v)
        except RecursionError: toRet[k] = v
    return toRet



def nestHtmlChildren(pTag, chRef={}, asDict='no_str'): 
    chList, tnList = [], chRef.get(getElemKey(pTag), None)
    if tnList is not None:
        if not isinstance(tnList, list): tnList = [tnList]
        sel = ', '.join([f'{s}:not({s} {s})' for s in tnList])
        chList = [s for s in pTag.select(f':where({sel})')]
    chList = [c for c in chList if not(isinstance(c,str) and not str(c))]

    if chList:
        try: 
            tList = [(getElemKey(childEl), nestHtmlChildren(
                childEl, chRef=chRef, asDict=True
            )) for childEl in chList]
            return dict_enumKeys(tList) if asDict else tList
        except RecursionError: pass

    tCon = pTag.get_text(' ').strip() if callable(
        getattr(pTag, 'get_text', None)
    ) else str(pTag)
    return {'textContent': tCon} if asDict=='no_str' else (
        tCon if asDict else [('textContent', tCon)])


def nestHtmlSiblings(hSoup, levelsRef, cNestRef={}, recursive=False):
    sibList, isRoot = getattr(hSoup, 'contents', None), getElemKey(hSoup)
    if not hSoup: return hSoup
    if not isinstance(hSoup, list):  
        if not (sibList and isinstance(sibList, list)):
            hDict = nestHtmlChildren(hSoup, cNestRef, 'no_str') 
            return {getElemKey(hSoup): hDict} 
    else: sibList, isRoot = hSoup, False

    if not all([isinstance(s, tuple) and len(s)>1 for s in sibList]):
        sibList, retList = [
            s[:2] if isinstance(s, tuple) and len(s)>1
            else (getElemKey(s), s) for s in sibList
        ], False 
    else: retList = True 

    nestSibs, curContainer, sibContainer, curKey,  = [], [], [], None
    pKeys, maxLevel = list(levelsRef.keys()), max(levelsRef.values())
    for k, el in sibList + [(None, None)]:
        isLast = k is None and el is None
        invCur = curKey is None or curKey not in pKeys 
        if not (k in pKeys or isLast or invCur): 
            sibContainer.append((k, el))
            continue

        if curKey is not None:  
            try: 
                sibContainer = [s for s in sibContainer if not (
                    s[0]=='string' and not str(s[1]).strip()     )]
                for_cc = nestHtmlSiblings(
                    sibContainer, levelsRef, cNestRef, recursive) 
            except RecursionError: 
                for_cc = [('error', f'{type(r)} {r}'), ('curEl', str(el))]
            nestSibs += [(curKey, curContainer+(for_cc if for_cc else[]))]


        curKey, curContainer, sibContainer = k, [], []
        pKeys = [
            lk for lk,l in levelsRef.items() 
            if levelsRef.get(k, maxLevel) >= l
        ]      
        if isLast: continue

        try:
            if recursive and callable(getattr(el, 'find', None)):
                if not isinstance(el,str) and el.find(pKeys):
                    curContainer.append(('contents', nestHtmlSiblings(
                        el.contents, levelsRef, cNestRef, recursive)))
                    continue
            curContainer += nestHtmlChildren(el, cNestRef, asDict=False)
        except RecursionError as r: 
            curContainer += [('error', f'{type(r)} {r}'), 
                             ('curEl', str(el))]


    if isRoot: nestSibsDict = {isRoot: dict_enumKeys(nestSibs)} 
    elif retList: nestSibsDict = nestSibs
    else: nestSibsDict = dict_enumKeys(nestSibs)
    return nestSibsDict

# --- block 2 ---
# from bs4 import BeautifulSoup

# with <h> tag fixed to <h4>
html_string = """
  <h1>Motley Mess Menu</h1>
  <h2>Breakfast</h2>
  <h3>Omelets</h3>
  <h4>Cheese</h4>
  <p>$7</p>
  <p>American style omelet containing your choice of Cheddar, Swiss, Feta, Colby Jack or all four!</p>
  <h4>Sausage Mushroom</h4>
  <p>$8</p>
  <p>American style omelet containing sausage, mushroom and Swiss cheese</p>
  <h4>Build-Your-Own</h4>
  <p>$8</p>
  <p>American style omelet containing…you tell me!</p>
  <p>Options (+50 cents after 3):</p>
  <ul>
  <li>Cheddar</li>
  <li>Swiss</li>
  <li>Feta</li>
  <li>Colby Jack</li>
  <li>Bacon Bits</li>
  <li>Sausage</li>
  <li>Onion</li>
  <li>Hamburger</li>
  <li>Jalapenos</li>
  <li>Hash Browns</li>
  </ul>
  <h3>Combos</h3>
  <p>Each come with your choice of two sides</p>
  <h4>Eggs and Bacon</h4>
  <p>$8</p>
  <p>Eggs cooked your way and crispy bacon. Sausage substitution is fine</p>
  <h4>Glorious Smash</h4>
  <p>$10</p>
  <p>Your favorite breakfast of two pancakes, two eggs cooked your way, two sausages and two bacon, free of all trademark infringement! If you think you can finish it all then you forgot about the choice of two sides!</p>
"""
soup = BeautifulSoup(html_string, 'html5lib')

tagLevels = {**{f'h{h}':h for h in range(1,7)}, 'p':8, 'ul':8}
# tagLevels = {'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4, 'h5': 5, 'h6': 6, 'p': 8, 'ul': 8}
nestKids = {'ul': 'li'} # , 'table':'tr', 'tr':'td', 'dl':['dt','dd']}
obj = nestHtmlSiblings(soup.body.contents, tagLevels, nestKids)
