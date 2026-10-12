# Code from my Stack Overflow answer https://stackoverflow.com/a/75325285 (posted 2023-02-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def dict2df(seasonDict:dict):
    df = pd.DataFrame(seasonDict).T.rename_axis('Year', axis='rows')
    return df.rename(lambda n: f'Hour {n}', axis='columns')

# --- block 2 ---
def dict2df(seasonDict:dict):
    return pd.DataFrame([{'Year': yk, **{
        f'Hour {hk}': hdf for hk, hdf in yd.items()
    }} for yk, yd in seasonDict.items()]).set_index('Year')

# --- block 3 ---
seasonRef = {k:v for k,v in enumerate(['winter','spring','summer','autumn'],1)}
# seasonRef = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}

seasons_dfs = {sk: {yk: {
    hk: pd.DataFrame(
        {f'{sn[0]}_{str(yk)[-2:]}':{f'hour{hk:0>2}':f'<DataFrame>'}}
    ) for hk in range(24)
} for yk in range(2005,2019)} for sk,sn in seasonRef.items()}

# --- block 4 ---
nestedDfs = {
    seasonRef.get(s, f'[season {s}]'): dict2df(sd) 
    for s, sd in seasons_dfs.items()
}
