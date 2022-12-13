---
title: "Parsing inline elements of a paragraph with BeautifulSoup & Python"
site: stackoverflow
question_id: 74778497
answer_id: 74778935
url: https://stackoverflow.com/a/74778935
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-13T01:01:07Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74778935/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 23247205398b4264ade41f2675ebab72925ffd0daeb06f8d0f39e7e3528149be
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74778935>, 2022-12-13; score 0. Text as retrieved 2026-10-12.

There are several ways to accomplish this. I'll be using the following sample HTML and `soup` to demonstrate each of the methods:

```python
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
```

---

If you're sure the `span` tags will be empty, or if you want to over-write the text inside them, then you can set the [`.string`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#modifying-string) property or use the [`.replace_with`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#replace-with) method to replace the `span` tags entirely.

```python
for p in soup.find_all('p'):
    for s in p.select('span.icon[class*="icon-"]'):
        ci = [c for c in s.get('class') if 'icon-' in c][0]
        s.string = f" {{{ci.replace('icon-', '')}}} " ## STRING METHOD 
        # s.replace_with(f" {{{ci.replace('icon-', '')}}} ") ## REPLACE METHOD 
    print(p.get_text(' ', strip=True))

print('\n\n########################### NEW SOUP ###########################\n')
print(soup)
```

printed output with the first method (setting `.string`):

```html
{water} Some text... {steel} some more text.
Para 2 text... {fire} more Para 2 text.


########################### NEW SOUP ###########################

<html><body><p>
<span class="icon-water icon"> {water} </span>
  Some text...
  <span class="icon-steel icon"> {steel} </span>
  some more text.
</p>
<p>
  Para 2 text...
  <span class="icon-fire icon"> {fire} </span>
  more Para 2 text.
</p>
</body></html>
```

printed output with the replace method:

```html
{water} Some text... {steel} some more text.
Para 2 text... {fire} more Para 2 text.


########################### NEW SOUP ###########################

<html><body><p>
 {water} 
  Some text...
   {steel} 
  some more text.
</p>
<p>
  Para 2 text...
   {fire} 
  more Para 2 text.
</p>
</body></html>
```

---

If the `span` tags might contain text and you want to preserve that text, you can use one of the [`.insert`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#insert) methods or the [`.append`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#append) method

```python
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
```

printed output (with the append method):

```html
{water} Some text... {steel} some more text.
Para 2 text... span text {fire} more Para 2 text.


########################### NEW SOUP ###########################

<html><body><p>
<span class="icon-water icon"> {water} </span>
  Some text...
  <span class="icon-steel icon"> {steel} </span>
  some more text.
</p>
<p>
  Para 2 text...
  <span class="icon-fire icon">span text {fire} </span>
  more Para 2 text.
</p>
</body></html>
```

---

If you want to avoid altering `soup`, then you could define a function like

```python
def icon_or_str(pdesc):
    if 'NavigableString' in str(type(pdesc)): return str(pdesc)
    if getattr(pdesc, 'name') != 'span': return ''
    pdc = pdesc.get('class', []) 
    pci = [c for c in pdc if 'icon-' in c]
    if not (pci and 'icon' in pdc) : return ''
    return f" {{{pci[0].replace('icon-', '')}}} "
```

and then use it as below:

```python
for p in soup.find_all('p'):
    pTxt = ' '.join([icon_or_str(d) for d in p.descendants]) 
    print(' '.join(w for w in pTxt.split() if w)) 
    ## [remove excess whitespace by splitting and re-joining "words"]
```

printed output:

```lang-none
{water} Some text... {steel} some more text.
Para 2 text... {fire} span text more Para 2 text.
```

(Personally, I feel that this last method is a bit cumbersome compared to the others.)
