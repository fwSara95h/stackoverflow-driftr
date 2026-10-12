# Code from my Stack Overflow answer https://stackoverflow.com/a/74159271 (posted 2022-10-21), extracted verbatim; may need the question's context to run.

# --- block 1 ---
table = soup.find(
    'span', {'id': 'By_market_capitalization'}
).find_parent('h2').find_next_sibling('table')

# --- block 2 ---
table = soup.select_one('h2:has(span#By_market_capitalization) ~ table')

# --- block 3 ---
colwidth = [10, 50, 30] # set column widths

for r in table.select('tr'):
  cells = [
      (c.text.strip()[:cw], cw) for c, cw 
      in zip(r.select('td,th'), colwidth)
  ]
  bottomBorder = ''
  if r.find('th'):
    bottomBorder = ' | '.join(['+'*c for c in colwidth])
    bottomBorder = f'\n| {bottomBorder} |'
  cells = ' | '.join([
      ("{0:^"+str(cw)+"}").format(c) for c, cw in cells
  ])
  print(f'| {cells} |{bottomBorder}')
