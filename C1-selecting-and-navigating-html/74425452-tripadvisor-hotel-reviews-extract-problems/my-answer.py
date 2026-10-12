# Code from my Stack Overflow answer https://stackoverflow.com/a/74426247 (posted 2022-11-14), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for t in soup.find_all(lambda t: t.name=='div' and t.get('data-test-target')):
    if t.find(lambda c: c.name=='div' and c.get('data-reviewid')): print(t.text)

# --- block 2 ---
print((f'\n\n{"-"*130}\n\n').join([f'[Review ID: {i}] --> [{u}]\n{r}' for i, u, r in [(
    rev.get("data-reviewid"), rev.parent.div.get_text(" "), rev.get_text("\n", strip=True) 
) for rev in soup.select('div[data-test-target] > div[data-reviewid]')]]))
