# Code from my Stack Overflow answer https://stackoverflow.com/a/75351812 (posted 2023-02-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def groupItems(dictList, itemsFrom, groupBy, saveTo=None):
    ik, gk, colsDict = itemsFrom, groupBy, {}
    groups = {str(d.get(gk)): d.get(gk) for d in dictList} 
    itemsList = [ [d.get(ik) for d in dictList if str(d.get(gk))==g] 
                  for g in groups   ]

    maxRows = max(len(li) for li in itemsList) if groups else 0
    for gi, (g, li) in enumerate(zip(groups.keys(), itemsList), 1):
        colsDict[f'Group {gi}'] = [groups[g]] + [None]*(maxRows-1)
        colsDict[f'Group {gi} Items'] = li + [None]*(maxRows-len(li))

    rdf = pandas.DataFrame(colsDict)
    if saveTo and isinstance(saveTo, str):
        print('Saving', maxRows, 'rows for', len(groups),'groups to', saveTo)
        rdf.to_csv(saveTo, index=False)
    return rdf

# --- block 2 ---
def groupItems(dictList, itemsFrom, groupBy, saveTo=None):
    ik, gk = itemsFrom, groupBy
    groups = {str(d.get(gk)): d.get(gk) for d in dictList} 
    itemsList = [ [d.get(ik) for d in dictList if str(d.get(gk))==g] 
                  for g in groups   ]

    maxRows = max(len(li) for li in itemsList) if groups else 0

    colsDict = {f'Group {gi}': [groups[g]] + [None] + (
        [f'Group {gi} Items'] + li + [None]*(maxRows-len(li))
    ) for gi, (g, li) in enumerate(zip(groups.keys(), itemsList), 1)}
    rdf = pandas.DataFrame(colsDict) 

    if saveTo and isinstance(saveTo, str):
        print('Saving', maxRows+4, 'rows for', len(groups),'groups to', saveTo)
        rdf.to_csv(saveTo, index=False)
    return rdf
