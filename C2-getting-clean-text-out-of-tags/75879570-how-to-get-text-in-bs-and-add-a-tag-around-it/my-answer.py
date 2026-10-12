# Code from my Stack Overflow answer https://stackoverflow.com/a/75883946 (posted 2023-03-30), extracted verbatim; may need the question's context to run.

# --- block 1 ---
xStr = '    <p>\n    lorem ipsum dolor <hi>a</hi>met.\n    Thing_A, <thing>Thing_B</thing>, Thing_C\n    </p>' 

thing_tag = 'thing' # 'rs' # 
things = ['Thing_A', 'Thing_B', 'Thing_C']

p_snip = BeautifulSoup(xStr, 'lxml').p

# --- block 2 ---
def wrap_str(s, name='rs', attrs=None): 
    if not isinstance(attrs, dict): 
        attrs = {'type':"org", 'ref':f"#{s.lower()}"}
    wrapped = BeautifulSoup(f'<{name}>{s}</{name}>', 'lxml').find(name)
    for k,v in attrs.items(): wrapped[k] = v
    return wrapped

for thing in things:
    thing_strs = [
        d for d in soup.descendants if isinstance(d,str) and not d.PREFIX
        and thing in d and not (d.strip()==thing and d.parent.name==thing_tag)
    ]
    for thing_str in thing_strs:
        for si, str_sect in enumerate(thing_str.split(thing)):
            # if si: thing_str.insert_before(wrap_str(thing, thing_tag)) 
            if si: thing_str.insert_before(wrap_str(thing, thing_tag, {})) 
            thing_str.insert_before(str_sect)
        thing_str.replace_with('')
