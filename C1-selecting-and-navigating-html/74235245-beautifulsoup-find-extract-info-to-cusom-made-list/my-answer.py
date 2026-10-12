# Code from my Stack Overflow answer https://stackoverflow.com/a/74237349 (posted 2022-10-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def bs2customList(soup): 
    fwb = soup.find("span", class_="font-weight-bold")

    #fdesc = [] if fwb is None else [( #(text, filter1, filter2, filter3)
        #d.get_text(strip=True), d.parent.get('class', []), d.parent.get('translate'), len(d.parent.select('span')) 
    #) for d in fwb.descendants if d.name is None and d.parent.name == 'span' and d.get_text(strip=True) ]
    fdesc = [] if fwb is None else [( #(text, filter1, filter2, filter3)
        str(d).strip(), d.parent.get('class', []), d.parent.get('translate'), len(d.parent.select('span')) 
    ) for d in fwb.descendants if 'NavigableString' in str(type(d)) and d.parent.name == 'span' and str(d).strip()]

    filters = [([], '', 0), (['ng-star-inserted'], None, 0), (['ng-star-inserted'], None, 1)]
    issueNum, ydate, num_ext = [[d[0] for d in fdesc if d[1:] == f] for f in filters]  
    num = num_ext[0].split()[0] if num_ext else []
    ext = num_ext[0].split()[1:] if num_ext else []

    return [(d[0] if d else None) for d in [issueNum, num, ext, ydate]]

# --- block 2 ---
def bs2customList(soup): 
    fwb = soup.find("span", class_="font-weight-bold")
    if fwb is None or not fwb.select('span.ng-star-inserted'): 
        return [ None ]*4

    snsi = fwb.select('span.ng-star-inserted') 

    snsi1 = [t for t in snsi if t.select('span[translate]')]
    if snsi1 != []:
        issueNum = snsi1[0].select_one('span[translate]').get_text(strip=True)

        #ext = [
        #    c.get_text(strip=True) for c in snsi1[0].children 
        #    if c.name is None and c.get_text(strip=True)
        #]
        ext = [
            str(c).strip() for c in snsi1[0].children 
            if 'NavigableString' in str(type(c)) and str(c).strip()
        ]

        if ext:
            ext = [e for e in ext[0].split() if e]

            # keep ext[0].isdigit() only if "number" is always integer
            if len(ext) > 1 and ext[0].isdigit(): 
                num = ext[0]
                ext = ' '.join(ext[1:])
            else: num, ext = ' '.join(ext), None
        else: num, ext = None, None
    else: issueNum, num, ext = [ None ]*3    

    ydate = [t for t in snsi if not t.select('span[translate]')]
    ydate = ydate[0].get_text(strip=True) if ydate else None

    return [issueNum, num, ext, ydate]

# --- block 3 ---
for h in htmls: print(bs2customList(BeautifulSoup(h, 'lxml')))

# --- block 4 ---
['issue_number', '4', 'Näköispainos', '6.12.1939']
['issue_number', '8', None, '1998']
[None, None, None, '1905']
[None, None, None, None]
[None, None, None, None]
