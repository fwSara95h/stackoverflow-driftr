# Code from my Stack Overflow answer https://stackoverflow.com/a/74132169 (posted 2022-10-19), extracted verbatim; may need the question's context to run.

# --- block 1 ---
[s.text for s in soup.select('td *[name^="dei:EntityAddress"]')]

# --- block 2 ---
print(', '.join([
    s.get_text(strip=True) for s in 
    soup.select('p>span *[name^="dei:EntityAddress"]')
    if 'ZipCode' not in s.get('name') # excludes zipcode
]))

# --- block 3 ---
addrsCell = soup.find(attrs={'name':'dei:EntityAddressAddressLine1'})
if addrsCell and addrsCell.find_parent('td'): # is not None
  print(' '.join([
      s.text for s in addrsCell.find_parent('td').select('p')]))
