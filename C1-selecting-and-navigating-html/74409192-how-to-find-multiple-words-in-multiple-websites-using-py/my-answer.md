---
title: "How to find multiple words in multiple websites using Python?"
site: stackoverflow
question_id: 74409192
answer_id: 74410285
url: https://stackoverflow.com/a/74410285
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-12T03:59:16Z
last_edited: 2022-11-12T14:17:58Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74410285/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 931c8691ed4d8c5374af14ab3ceb5e6555002cb1193a4ed93499636b6411df1a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74410285>, 2022-11-12, last edited 2022-11-12; score 0. Text as retrieved 2026-10-12.

I suggest using list comprehension (for multiple input) and [regex](https://www.w3schools.com/python/python_regex.asp) (for pattern/partial matching). Also, since you just want the text, you can use [`.stripped_strings`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#strings-and-stripped-strings) directly instead `.find_all(text...)` followed by `.strip`.
```python 
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
```
(I removed `allow_redirects=False` from the requests because the second and third sites give [301 error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301) otherwise.)

---

Now, `the_word` can have multiple strings/patterns to search for; for example, setting 
```python
the_word = ['composite',  'condensation', 'surface']
# same results as with:  
# the_word = ('composite',  'condensation', 'surface')
# the_word = {'composite',  'condensation', 'surface'}  
```
would lead to printing
```python

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
```

---

With regex, the "wildcard" character is `.` [or `.*` (zero or more chars) or `.?` (zero or one) or `.+` (one or more)], and you can also specify possible character in square brackets; so setting `the_word = 'mo.e[y!n]'` would find matches in strings containing "<i>**mo**r**e**!</i>" or "<i>**mo**m**e**n</i>t" or "<i>**mo**n**e**y</i>"
```python

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
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[nihility24](https://stackoverflow.com/users/19563980)** (2022-11-12): Wow !! Many many thanks for the comprehensive suggestion and codes ! But, when I tested it for a random door-window website,   https://tpimprovements.com/ There was error message ''' 'contains 36 matches for "door" or "window"   ['var gform;gform||(document.addeventlistener("gform_main_scripts_loaded",function(){gform.scriptsloaded=!0}),window.addeventlistener("domcontentloaded",function()................................................... '''  Why is it not showing in normal lines like before?
- **me** (2022-11-12): @nihility24 [I don't think it's an error message?] that's from the `script` tag. I think maybe we have different parser versions because that result doesn't show up for me (but I can see the tag with `soup.select('script')`); I've edited my code to use `find_all(text=True)` (like you were, but more simply) instead of `stripped_strings` because then you can filter by parent tag properties as well
