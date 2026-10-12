# Code from my Stack Overflow answer https://stackoverflow.com/a/74455631 (posted 2022-11-16), extracted verbatim; may need the question's context to run.

# --- block 1 ---
tcrSel1 = 'tr:has(td.column-1~td.column-2):not(:has(td~td~td))' 
tcrSel2 = f'td.column-1:first-child:-soup-contains("{strServiceVersion}")' 
arrDataCell = soup.select(f'{tcrSel1} {tcrSel2}')

# --- block 2 ---
arrDataCell = soup.find_all(
    lambda t: t.name == 'td' and 'column-1' in t.get('class', []) 
    and strServiceVersion in t.get_text() #and t.get_text()==strServiceVersion 
    and t.find_parent('tr') and t == t.find_parent('tr').td 
    and len(t.find_next_siblings('td', {'class': 'column-2'})) == 1
)

# --- block 3 ---
dictList = [{
  'column-1': a1.get_text(strip=True), 'column-2': a2.get_text(strip=True) 
} for a1,a2 in [a.parent.find_all('td', recursive=False) for a in arrDataCell]]

# --- block 4 ---
adcDict = {
    a1.get_text(' ', strip=True): a2.get_text(' ', strip=True) for 
    a1,a2 in [a.parent.find_all('td', recursive=False) for a in arrDataCell]
}

# --- block 5 ---
# dfList = pandas.read_html(url, match=strServiceVersion) # OR
# dfList = pandas.read_html('\n'.join([str(a.find_parent('table')) for a in arrDataCell])) # OR
# dfList = pandas.read_html('<table>\n'+'\n'.join([str(a.find_parent('tr'))+'\n</table>' for a in arrDataCell])) # OR
dfList = pandas.read_html(str(soup), match=strServiceVersion)
dictList = []
for df in dfList: dictList += df.to_dict('records')

# --- block 6 ---
dictList = [d for d in dictList if d[1].split(' | ')[0].isdigit()]
