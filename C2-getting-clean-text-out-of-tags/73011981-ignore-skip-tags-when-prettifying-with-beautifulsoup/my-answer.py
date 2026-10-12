# Code from my Stack Overflow answer https://stackoverflow.com/a/74987578 (posted 2023-01-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
skipTags = ['svg']
# skipTags = ['svg', 'script', 'style'] ## list all the tag names to skip

# --- block 2 ---
# import re
# from bs4 import BeautifulSoup
for n in skipTags: messy = re.sub(f'<{n}\s*.*\s*>\s*.*\s*</{n}>', '', messy)
pretty = BeautifulSoup(markup=messy, features='html.parser').prettify()

# --- block 3 ---
# import re
# from bs4 import BeautifulSoup
cReps = []

for n in skipTags: 
    rcpat = re.compile(f'<{n}\s*.*\s*>\s*.*\s*</{n}>')
    cReps += [m.span() for m in rcpat.finditer(messy)]
for cri, (sPos, ePos) in list(enumerate(cReps))[::-1]:
    repCmt, orig = f'<!--do_not_parse__placeholder_{cri}-->', messy[sPos:ePos]
    messy = messy[:sPos] + repCmt + messy[ePos:]
    cReps[cri] = (repCmt, orig)

pretty = BeautifulSoup(markup=messy, features='html.parser').prettify()
for repCmt, orig in cReps:
    pretty = pretty.replace(repCmt, orig, 1)

print('<!--messy-subbed-->', messy, '\n<!--pretty-->', pretty, sep='\n')
