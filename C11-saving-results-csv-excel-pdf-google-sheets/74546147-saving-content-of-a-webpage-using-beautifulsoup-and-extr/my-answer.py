# Code from my Stack Overflow answer https://stackoverflow.com/a/74569002 (posted 2022-11-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
csvRows = []
for pCont in soup.find_all('pre'): 
    csvRows += [( 
        ('[About Query]', '\n'.join([
            ql[1:].strip() for ql in pb.split('\n')[2:5]
        ])) if pi == 0 else tuple(pb.split(f"\n{'#'*80}\n")[:2]) 
    ) for pi, pb in enumerate(pCont.get_text().split(f"{'#'*80}\n#  "))]
pandas.DataFrame(csvRows, columns=[
    'Result Header', 'Result Lines'
]).to_csv('Cotey_synopsc.csv', index=False)

# --- block 2 ---
aboutQuery, qresBlocks, bHeads = [], [], []
for pci, pCont in enumerate(soup.find_all('pre')):
    pBlocks = pCont.get_text().split(f"{'#'*80}\n#  ")

    aboutQuery.append({k: v for v, k in zip([pci]+[
        ql[1:].strip() for ql in pBlocks[0].split('\n')[2:5]
    ], ['qIndex', 'Query Time', 'Query', 'Query Inerval'])})

    for pbi, pb in enumerate(pBlocks[1:]):
        if f"\n{'#'*80}\n" not in pb: continue # unknown format
        bhead, blines = pb.split(f"\n{'#'*80}\n")[:2]
        bhead = bhead.strip().split(' | ')
        bHeads.append({k: v for k, v in [
            ('qIndex', pci), ('bIndex', pbi), ('from', bhead[0]), 
            ('N', ''.join(bhead[1:2])), ('W', ''.join(bhead[2:3])),
            ('m', ''.join(bhead[3:4])), ('extra', ' | '.join(bhead[4:]))
        ] if v != ''})
        for bl in blines.split('=\n')[:-1]:
            line1 = bl.split('\n')[0].strip()
            ldate = line1.split(' ')[0]
            line1 = line1.replace(ldate, '', 1)
            line2 = '\n'.join([l.strip() for l in bl.split('\n')[1:]])
            if line2 == '' and line1.endswith(' NIL'):
                line1, line2 = line1[:-4], 'NIL'
            qresBlocks.append({
                'qIndex': pci, 'bIndex': pbi, 'date?': ldate,
                'firstLine': line1, 'lastLine(/s)': f'{line2}='
            })

listsByName = [
    ('About Query', aboutQuery), 
    ('Result Blocks - Headers', bHeads), 
    ('Result Blocks - Lines', qresBlocks)
]

# --- block 3 ---
for name, nList in listsByName:
    pandas.DataFrame(nList).to_csv(f'{name}.csv', index=False)

# --- block 4 ---
with pandas.ExcelWriter('Cote_synopsc.xlsx') as w:
    for name, nList in listsByName:
        pandas.DataFrame(nList).to_excel(w, name, index=False)
