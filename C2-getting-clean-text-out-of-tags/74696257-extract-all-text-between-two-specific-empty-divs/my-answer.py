# Code from my Stack Overflow answer https://stackoverflow.com/a/74703790 (posted 2022-12-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
from bs4 import BeautifulSoup
pasted_html = '''many<divs></divs>and other tags<div class="start"></div><div>bla bla bla</div><div class="start"></div><div><i><a><span><p>Text I want</p></span></a></i></div><div><p>Text I want</p><p>Text I want</p></div><div class="end"></div><div>bla bla bla</div><div class="end"></div>many<divs></divs>and other tags'''
soup = BeautifulSoup(pasted_html, 'html5lib')

# --- block 2 ---
s, e = 'div.start', 'div.end' 
mTags = soup.select(f'{s}:not(:has(~ {s})) ~ *:not({e}):not({e} ~ *):has(~ {e})')

# --- block 3 ---
mTags = soup.find_all(
    lambda t: t.find_previous_sibling('div', {'class': 'start'}) and
    not t.find_next_sibling('div', {'class': 'start'}) and
    t.find_next_sibling('div', {'class': 'end'}) and
    not t.find_previous_sibling('div', {'class': 'end'})
)

# --- block 4 ---
mText = ' '.join([t.get_text(' ').strip() for t in mTags])
# mText = "Text I want Text I want     Text I want"

# --- block 5 ---
mText = BeautifulSoup(
    '\n'.join([t.prettify().strip() for t in mTags])
).get_text(' ').strip()
# mText = "Text I want\n     \n \n \n \n \n \n \n  Text I want\n  \n \n  Text I want"

# --- block 6 ---
mText = ' '.join(w for w in mText.split() if w)
