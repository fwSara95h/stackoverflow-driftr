# Code from my Stack Overflow answer https://stackoverflow.com/a/74645871 (posted 2022-12-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
bsParser = 'html.parser' # 'xml' # 
# xTagList = [BeautifulSoup(str(x), bsParser) for x in xTagList] # should fix some formatting
wCont_xstrs = ['\n'.join([
    str(d) for d in x.descendants if hasattr(d, 'find_all') 
    and not d.find_all() and d.get_text().strip()
]) for x in xTagList]

# --- block 2 ---
wCont_xtags = [BeautifulSoup(x, bsParser) for x in wCont_xstrs]

# --- block 3 ---
wCont_xtags = [BeautifulSoup(f'<Entry>{x}</Entry>', bsParser).Entry for x in wCont_xstrs]
