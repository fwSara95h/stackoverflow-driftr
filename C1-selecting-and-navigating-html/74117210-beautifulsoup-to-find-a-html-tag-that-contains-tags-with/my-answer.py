# Code from my Stack Overflow answer https://stackoverflow.com/a/74120574 (posted 2022-10-19), extracted verbatim; may need the question's context to run.

# --- block 1 ---
mtables = [s.parent for s in bs.select('*[class^="TD"][class$="3"]')]

# if you want tr only:
# mtables = [s.parent for s in bs.select('tr *[class^="TD"][class$="3"]')]

mtables = list(set(mtables)) # no duplicates

# --- block 2 ---
tagPat = '^TD.3$' 
# tagPat = '^TD.*3$' # if there might be more than one character between TD and 3
mtables = bs.find_all(
  lambda p: 
  p.name == 'tr' and # remove if you want all tags and not just tr
  p.find(
    lambda t: t.get('class') is not None and 
    len([c for c in t.get('class') if re.search('^TD.3$', c)]) > 0
    , recursive=False # prevent getting <tr><tr><td class="TDo3">someval</td></tr></tr>
  ))

# --- block 3 ---
tagPat = '^TD.3$' # '^TD.*3$' #
mtables = [
    s.parent for s in bs.find_all(class_ = re.compile(tagPat))
    if s.parent.name == 'tr' # remove if you want all tags and not just tr
]
mtables = list(set(mtables)) # no duplicates

# --- block 4 ---
for mtable in mtables: print('---\n', mtable, '\n---')
