# Code from my Stack Overflow answer https://stackoverflow.com/a/74270546 (posted 2022-11-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for row in WholeDoc.select('div[data-type="Photobook"] tbody tr[data-id]'): 
    print(row.get('data-id'))

# --- block 2 ---
dataType_tables = [{
    'type': t.get('data-type') + ' -> ' + t.get('data-subtype', 'NO_SUBTYPE'), 
    'headers': ['Data-ID'] + [
        col.get_text(strip=True) for col in t.select('th')], 
    'data': [[r.get('data-id')] + [
        col.get_text(strip=True) for col in r.select('td')
    ] for r in t.select('tr:has(td)')]
} for t in doc.select('div[data-type]')]

# --- block 3 ---
for t in doc.select('div[data-type]'): 
    titleLine = t.get('data-type').upper()
    if t.get('data-subtype'): 
        titleLine += ' --> ' + t.get('data-subtype').upper()
    print(titleLine)

    divider = ('| ' + ' | '.join([
        '+'*40 if i == 1 else ('+'*20 if i == 0 else '+'*15) 
        for i in range(len(t.select('th'))+1)
    ]) + ' |')
    print(divider)
    print('|', ' | '.join([
        f'{c[:40]:^40}' if i == 1 else 
        (f'{c[:20]:^20}' if i == 0 else f'{c[:15]:^15}') 
        for i, c in enumerate(
            ['Data-ID'] + [col.text.strip() for col in t.select('th')]
    )]), '|')
    print(divider)
    for r in t.select('tr:has(td)'):
        print('|', ' | '.join([
            f'{c:^40}' if i == 1 else (f'{c:^20}' if i == 0 else f'{c:^15}') 
            for i, c in enumerate(
                [r.get('data-id', '')] + 
                [col.text.strip() for col in r.select('td')]
        )]), '|')
    print(divider, '\n')
