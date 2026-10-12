# Code from my Stack Overflow answer https://stackoverflow.com/a/75045322 (posted 2023-01-08), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> table = soup.find('table', {'class' : "tablesaw tablesaw-swipe"})
>

# --- block 2 ---
for t in soup.find_all('table'): 
    rows = f"[{len(t.select('tr')):>2} rows]"
    txtPrevw = ' '.join(t.get_text(' ').split())
    if len(txtPrevw) > 100: txtPrevw = txtPrevw[:97] + '...'
    print(f"> {str(t.get('class')):>20}", rows, ' --> ', txtPrevw)
