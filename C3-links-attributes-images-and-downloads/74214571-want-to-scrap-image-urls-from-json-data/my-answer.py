# Code from my Stack Overflow answer https://stackoverflow.com/a/74215563 (posted 2022-10-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
link = data['product']['response']['product']['data']['attributes']['media_map']

# --- block 2 ---
mediaMap = data['product']['response']['product']['data']['attributes']['media_map']

# --- block 3 ---
mediaAlts = [m['alt'] for m in mediaMap.values() if 'alt' in m]

# --- block 4 ---
imgAlts = [
    m['alt'] for m in mediaMap.values() if 'alt' in m 
    and 'type' in m and m['type'] == 'image'
]

# --- block 5 ---
m1srcs = list(list(mediaMap.values())[0]['src'].values())

# --- block 6 ---
m1srcs = [s for s in m1srcs if type(s) == str and s.endswith('.jpg')]

# --- block 7 ---
altJpgs = [
    src for srcs in [[
            s for s in mv['src'].values()
            if type(s) == str and s.endswith('.jpg')
        ] for mv in mediaMap.values()
        if type(mv) == dict and 'src' in mv
        and 'alt' in mv # has alt
        and 'type' in mv and mv['type'] == 'image' # has type listed as image 
    ] for src in srcs
]

# --- block 8 ---
altJpgs = []

for mv in mediaMap.values():
    if type(mv) != dict or 'src' not in mv: continue 
    if 'alt' not in mv: continue 
    if 'type' not in mv and mv['type'] != 'image': continue 

    for s in mv['src'].values():
        if type(s) == str and s.endswith('.jpg'):
            altJpgs.append(s)
