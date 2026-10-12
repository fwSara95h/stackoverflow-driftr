# Code from my Stack Overflow answer https://stackoverflow.com/a/75051145 (posted 2023-01-08), extracted verbatim; may need the question's context to run.
nonceInp = soup.select_one('input[name="nonce"]')
# nonceInp = soup.find('input', {'name': 'nonce'})

if nonceInp:
    nonceVal = nonceInp['value'] 
    # nonceVal = nonceInp.attrs['value'] 
    # nonceVal = nonceInp.get('value') 
    # nonceVal = nonceInp.attrs.get('value')
else: nonceVal = None # print('could not find an input named "nonce"')
