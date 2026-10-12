# Code from my Stack Overflow answer https://stackoverflow.com/a/76546063 (posted 2023-06-24), extracted verbatim; may need the question's context to run.
for p in reversed(soup.find_all(lambda t: t.name=='p' and 'Read our full' in t.text)): 
    if 'Read our full' in p.text:
        p.decompose()
