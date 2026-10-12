# Code from my Stack Overflow answer https://stackoverflow.com/a/75677851 (posted 2023-03-08), extracted verbatim; may need the question's context to run.

# --- block 1 ---
term_map = {
    'FLOORS': ('FLOOR', 'FLR', 'TF', 'FT'),
    'WALLS': ('WALL', 'WL', 'TW'),
    'CARPET': ('CAR', 'CPT'),
    'KITCHEN BACKSPLASH': ('KBS', 'BACKSPLASH'),
    'FIREPLACE': ('FIRE', 'FP', 'FRP'),
    'WOOD': ('WOOD', 'WD'),
    'VINYL': ('VINYL', 'LVP', 'VP'),
    'PREWALK': ('PREWALK', 'PW'),
    'TILE': ('TILE',),
    'FINE TUNE': ('FINE', 'F/T')
}

def get_kw(fullStr, ref_map=term_map):
    if fullStr in ref_map or not isinstance(fullStr, str): return fullStr
    for kw, lk in ref_map.items():
        # if re.match('|'.join(lk), fullStr): return fullStr
        for k in lk:
            if k in fullStr: return kw
    return fullStr

df['Job Type'] = df['Job Type'].apply(get_kw)

# --- block 2 ---
# term_map = ... ## [ same as above ]
term_map_inv = {k: kw for kw, lk in term_map.items() for k in lk}

df['Job Type'] = df['Job Type'].str.extract(
    f'({"|".join(term_map_inv)})', expand=False
).map(term_map_inv).fillna(df['Job Type'])

# --- block 3 ---
def get_kw(fullStr, ref_map=term_map_inv, reg_pat = '|'.join(term_map_inv)):
    if isinstance(fullStr, str): 
        if (rsearch:=re.search(reg_pat, fullStr)): 
            return term_map_inv.get(rsearch.group(0), fullStr)
    return fullStr
