# Code from my Stack Overflow answer https://stackoverflow.com/a/73931516 (posted 2022-10-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
origString = 'Total Revenue42,965,39136,483,93920,139,65822,588,85825,067,279'

cols = origString.split(',')

rowName = cols[0][:] #copy
cols[0] = ''.join(e for e in cols[0] if e.isdigit())
rowName = rowName.replace(cols[0], '')

cols = ','.join([c if len(c) < 4 else (c[:3]+'|'+c[3:]) for c in cols])
colVals = [rowName] + cols.split('|')

# --- block 2 ---
tables = soup.find_all(class_ = 'fi-row')

print(len(tables), 'rows found:')
print('Breakdown       ||          TTM |   12/31/2021 |   12/31/2020 |   12/31/2019 |   12/31/2018')
print('-------------------------------------------------------------------------------------------')
for table in tables:
  cols = [s.text for s in table.find_all('div',{'data-test':'fin-col'})]
  rowName = table.find('span').text
  colText = ' | '.join([f'{c:>12}' for c in cols])
  nameTxt = rowName if len(rowName) < 15 else f'{rowName[:12]}...'
  print(f'{nameTxt:15} || {colText}')
