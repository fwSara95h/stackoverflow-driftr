# Code from my Stack Overflow answer https://stackoverflow.com/a/73862860 (posted 2022-09-27), extracted verbatim; may need the question's context to run.
def stripList(l: list, fromEnd='both'): 
  lInd = range(len(l))
  if fromEnd == 'right': 
    lInd = reversed(lInd) 
  for i in lInd:
    if str(l[i]).strip() != '':
      if fromEnd not in ['left', 'right']:
        return stripList(l[i:], 'right')
      return l[i:] if fromEnd == 'left' else l[:i+1] 
  return []
