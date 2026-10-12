# Code from my Stack Overflow answer https://stackoverflow.com/a/75037729 (posted 2023-01-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
rows = soup.find('table', class_= "report").find_all('tr',  {'onmouseover': True})

# --- block 2 ---
table = soup.find('table', class_= "report")
rows = table.find_all('tr',  {'onmouseover': True}) if table else []

# --- block 3 ---
rows = []
for table in soup.find_all('table', class_= "report"): 
    rows += table.find_all('tr',  {'onmouseover': True})

# --- block 4 ---
# if there might be other tables with report AND other classes that you don't want:
# rows = soup.select('table[class="report"] tr[onmouseover]') 

rows = soup.select('table.report tr[onmouseover]')

# --- block 5 ---
for r in rows:
    date, flag = r.find('td', class_= "time"), r.find('td', class_= "flag")
    info = [i.get_text() if i else i for i in [date, flag]]
    if any([i is not None for i in info]): print(info) 
    # [ only prints if there are any non-null values ]

# --- block 6 ---
for r in rows: 
    info = selectForList(r, ['td.time', 'td.flag'], printList=True)
    if any([i is not None for i in info]): print(info)

# --- block 7 ---
infList = [selectForList(r, {
    'time': 'td.time', 'flag': 'td.flag', ## add selectors for any info you want 
}) for r in soup.select('table.report tr[onmouseover]')]
infList = [d for d in infoList if [v for v in d.values() if v is not None]]

# --- block 8 ---
for r in rows: 
    info = [(td.get_text(),''.join(td.get('style','').split())) for td in r.select('td')]
    info = [txt.strip() for txt, styl in r.select('td') if 'display:none' not in styl]
    # info = [i if i else 0 for i in info] # fill blanks with zeroes intead of ''
    if any(info):  print(info) ## or write to CSV
