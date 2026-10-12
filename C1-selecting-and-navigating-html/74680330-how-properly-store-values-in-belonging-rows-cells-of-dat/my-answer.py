# Code from my Stack Overflow answer https://stackoverflow.com/a/74681188 (posted 2022-12-04), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def getText_bySelector(tagSoup, selector, sep=None):
    selTags = tagSoup.select(selector) if selector else [tagSoup]
    if type(sep) == str: 
        return sep.join([s.get_text(' ').strip() for s in selTags])
    return selTags[0].get_text(' ').strip() if selTags else None

# --- block 2 ---
refDict = {
    'title': ('.page_title', None), 
    'authors': ('.authors .name', ', '),
    'affiliations': ('.item.authors .affiliation', '; ')
}

# --- block 3 ---
dictList = []
for i in urls: 
    page = requests.get(link)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")

    dictList += [{
        k: getText_bySelector(a, vsel, vsep) 
        for k, (vsel, vsep) in refDict.items()
    } for a in soup.select('article.obj_article_details')]

# --- block 4 ---
{
  'title': 'Lorem ipsum dolor sit amet',
  'authors': 'Brandon Scott, Alvaro Cote',
  'affiliations': 'Villanova University, Pennsylvania; Carleton College, Minnesota' 
}

# --- block 5 ---
dictList = []
for i in urls: 
    page = requests.get(link)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")

    for a in soup.select('article.obj_article_details'):
        dets = {}
        for k, (sel, sep) in refDict.items():
            selTags = a.select(sel) if sel else [a]
            if type(sep) == str: 
                dets[k] = sep.join([s.get_text(' ').strip() for s in selTags])
            else: 
                dets[k] = selTags[0].get_text(' ').strip() if selTags else None
        dictList.append(dets)

# --- block 6 ---
title = []
authors = []
afiliations = []

for i in urls: 
    page = requests.get(link)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")

    for a in soup.select('article.obj_article_details'):
        titleA = a.select_one('.page_title')
        if titleA: titleA = titleA.get_text(' ').strip()
        title.append(titleA)

        authorsA = a.select('.authors .name')
        # authors.append(', '.join([aa.get_text(' ').strip() for aa in authorsA]))
        listAuth = []
        for aa in authorsA: listAuth.append(aa.get_text(' ').strip())
        authors.append(', '.join(listAuth))
        # authors.append(listAuth) # if you want a list instead of a string

        affA = a.select('.item.authors .affiliation')
        # afiliations.append('; '.join([aa.get_text(' ').strip() for aa in affA]))
        listAff = []
        for aa in affA: listAff.append(aa.get_text(' ').strip())
        afiliations.append(', '.join(listAff))
        # afiliations.append(listAff) # if you want a list instead of a string

# --- block 7 ---
refDict = {
    'title': '.page_title', 'authors': '.authors .name',
    'affiliations': '.item.authors .affiliation'
} 
listsDict = {k: [] for k in refDict}
for i in urls: 
    page = requests.get(link)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")

    for a in soup.select('article.obj_article_details'):
        for k in refDict:
            kvals = [t.get_text(' ').strip() for t in (
                a.select(refDict[k]) if refDict[k] else [a]
            )]
            listsDict[k].append('; '.join(kvals))
            # listsDict[k].append(kvals[0] if len(kvals) == 1 else kvals)

# --- block 8 ---
listsDict[k].append(kvals[0] if len(kvals) == 1 else kvals)
