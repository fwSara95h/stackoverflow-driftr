# Code from my Stack Overflow answer https://stackoverflow.com/a/74778935 (posted 2022-12-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
sampleHtml = '''
<p>
  <span class="icon-water icon"></span>
  Some text...
  <span class="icon-steel icon"></span>
  some more text.
</p>
<p>
  Para 2 text...
  <span class="icon-fire icon">span text</span>
  more Para 2 text.
</p>
'''
soup = BeautifulSoup(sampleHtml)

# --- block 2 ---
for p in soup.find_all('p'):
    for s in p.select('span.icon[class*="icon-"]'):
        ci = [c for c in s.get('class') if 'icon-' in c][0]
        s.string = f" {{{ci.replace('icon-', '')}}} " ## STRING METHOD 
        # s.replace_with(f" {{{ci.replace('icon-', '')}}} ") ## REPLACE METHOD 
    print(p.get_text(' ', strip=True))

print('\n\n########################### NEW SOUP ###########################\n')
print(soup)

# --- block 3 ---
for p in soup.find_all('p'):
    for s in p.select('span.icon[class*="icon-"]'):
        ci = [c for c in s.get('class') if 'icon-' in c][0]
        # s.insert_before(f" {{{ci.replace('icon-', '')}}} ")
        # s.insert_after(f" {{{ci.replace('icon-', '')}}} ")
        # s.insert(0, f" {{{ci.replace('icon-', '')}}} ")
        s.append(f" {{{ci.replace('icon-', '')}}} ")
    print(p.get_text(' ', strip=True))

print('\n\n########################### NEW SOUP ###########################\n')
print(soup)

# --- block 4 ---
def icon_or_str(pdesc):
    if 'NavigableString' in str(type(pdesc)): return str(pdesc)
    if getattr(pdesc, 'name') != 'span': return ''
    pdc = pdesc.get('class', []) 
    pci = [c for c in pdc if 'icon-' in c]
    if not (pci and 'icon' in pdc) : return ''
    return f" {{{pci[0].replace('icon-', '')}}} "

# --- block 5 ---
for p in soup.find_all('p'):
    pTxt = ' '.join([icon_or_str(d) for d in p.descendants]) 
    print(' '.join(w for w in pTxt.split() if w)) 
    ## [remove excess whitespace by splitting and re-joining "words"]
