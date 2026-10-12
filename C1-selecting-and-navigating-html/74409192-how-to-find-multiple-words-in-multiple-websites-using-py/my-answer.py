# Code from my Stack Overflow answer https://stackoverflow.com/a/74410285 (posted 2022-11-12), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import re # for regex

## ENSURE the_word IS A LIST OF [lowercase] STRINGS ##
if type(the_word) in [list, tuple, set]:
    the_word = [str(w).lower() for w in the_word]
else: the_word = [str(the_word).lower()]
######################################################

total_words = []
for url in url_list:
    r = requests.get(url) # , allow_redirects=False) # why block redirects?
    soup = BeautifulSoup(r.content.lower(), 'lxml')
    # words_list = [s for s in soup.stripped_strings if [w for w in the_word if re.search(w, s)]]
    words_list = [
        s.strip() for s in soup.find_all(text=True) 
        if s.parent.name not in ['script', 'style']
        and [w for w in the_word if re.search(w, s)]
    ]
    count = len(words_list)
    total_words += words_list

    print('\nUrl: {}\ncontains {} matches for {}'.format(
        url, count, ' or '.join([f'"{w}"' for w in the_word])
    ), '\n', words_list, '\n')

total_count = len(total_words)
print(f'\n{total_count} found for {the_word}\n', total_words)

# --- block 2 ---
the_word = ['composite',  'condensation', 'surface']
# same results as with:  
# the_word = ('composite',  'condensation', 'surface')
# the_word = {'composite',  'condensation', 'surface'}

# --- block 3 ---

Url: http://www.a-w-s.co.uk/
contains 1 matches for "composite" or "condensation" or "surface" 
 ['surface guarantee'] 


Url: http://www.albanywindows.co.uk
contains 6 matches for "composite" or "condensation" or "surface" 
 ['composite doors', 'composite door builder', 'composite doors', 'composite door builder', ', including improved thermal efficiency and minimised risk of interior condensation. we also offer', 'composite door'] 


Url: http://www.aimwindows.co.uk
contains 5 matches for "composite" or "condensation" or "surface" 
 ['composite doors', 'composite fire doors', 'composite doors', 'composite fire doors', 'for a closer look at the finer, technical specifics of our renovation products, our detailed brochures are readily available to download. from versatile casement windows to captivating aluminium bifold doors & ultra-secure composite doors, embrace the opportunity to pursue your home improvement aspirations with aim windows.'] 


12 found for ['composite', 'condensation', 'surface']
 ['surface guarantee', 'composite doors', 'composite door builder', 'composite doors', 'composite door builder', ', including improved thermal efficiency and minimised risk of interior condensation. we also offer', 'composite door', 'composite doors', 'composite fire doors', 'composite doors', 'composite fire doors', 'for a closer look at the finer, technical specifics of our renovation products, our detailed brochures are readily available to download. from versatile casement windows to captivating aluminium bifold doors & ultra-secure composite doors, embrace the opportunity to pursue your home improvement aspirations with aim windows.']

# --- block 4 ---

Url: http://www.a-w-s.co.uk/
contains 1 matches for "mo.e[y!n]" 
 ['we are the uk’s leading manufacturers and suppliers to the trade, with a huge range of pvcu and aluminium windows, doors, bifolds, sliding patios, heritage flush sash products, conservatories, and more!'] 


Url: http://www.albanywindows.co.uk
contains 1 matches for "mo.e[y!n]" 
 ["both being a+ rated, you can be sure that heat won't escape your home and you'll be protected against draughts. this helps you save money in the long run as you'll be spending less on your heating bills."] 


Url: http://www.aimwindows.co.uk
contains 1 matches for "mo.e[y!n]" 
 ['our showroom is temporarily closed at the moment.'] 


3 found for ['mo.e[y!n]']
 ['we are the uk’s leading manufacturers and suppliers to the trade, with a huge range of pvcu and aluminium windows, doors, bifolds, sliding patios, heritage flush sash products, conservatories, and more!', "both being a+ rated, you can be sure that heat won't escape your home and you'll be protected against draughts. this helps you save money in the long run as you'll be spending less on your heating bills.", 'our showroom is temporarily closed at the moment.']
