---
title: "Why soup. find_all() only returning one result"
site: stackoverflow
question_id: 75279786
answer_id: 75296465
url: https://stackoverflow.com/a/75296465
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-31T11:29:43Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75296465/revisions
accepted: true
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: [selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: eb35296cf63536f53bdab124cf8c02bc8f1bba56ce6155af54b5d0e369da4729
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-31

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75296465>, 2023-01-31; **accepted**; score 0. Text as retrieved 2026-10-12.

> Why does this line
>
> ```python
> results = soup.find_all('div', class_="similar-listings-item sponsored-listing") 
> ```
>
> return only the 1st element?

I'm getting  [2 elements][1], but maybe you're only *seeing* the last result because  the *`info=...print(info)`* lines are *after* the loop instead of **inside** it. Indent them to print every the **result** from inside the loop.

---

If your issue is that you want *all* the listings, you should note that **only the [sponsored listings][2]** have the *`sponsored-listing`* class. To get all the listings, you can try using 

```python
results = soup.find_all('div', {'class': "similar-listings-item"}) ## OR
# results = soup.select('div.similar-listings-item')
``` 

<sub>[Use `soup.select('div.similar-listings-item:not(.sponsored-listing)')` if you only want *un*sponsored listings. Check out how to use [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) for more details.]</sub>

---

> I want to extract list of lists from the (variable)

which variable? If you want list of all the `Title`, `location`, `Price` for each `result`, initiate an empty list [like `infoList`] before the loop, then indent `info=...` to include it in the list, and [append](https://www.programiz.com/python-programming/methods/list/append) `info` to `infoList` at the end of the loop (but still **in** the loop). Something like

```python
infoList = []
for result in results:
    Title = result.find('div', class_= "similar-listings-info").text.replace('\n','')
    location = result.find( class_= "listings-location").text.replace('\n','')
    Price = result.find('div', class_= "similar-listings-price").text.replace('\n','')

    info = (Title, location, Price) # this is a tuple btw, so 
    # infoList.append(info) # --> list of tuples
    infoList.append([Title, location, Price]) # --> list of lists
    # print(info) # will print for every result
print(info) # will print ONLY the LAST result
```

---

Btw, it's not very safe to chain `.find` and `.text` like that. If `.find` doesn't find any thing, then an [error will be raised](https://stackoverflow.com/q/75276178/6146136) when trying to get `.text`. To be more cautious, you should check that find returned something first.

<sub>You could use my [`selectForList`](https://pastebin.com/ZnZ7xM6u) function like *`infoList = [selectForList(result, ['div.similar-listings-info', 'p.listings-location', 'div.similar-listings-price']) for result in results]`* or [since you want to remove the `\n`s and also if you don't want to use CSS selectors] use a variation of it:</sub>

```python
def get_min_text(containerTag, elName, classAttr, defaultVal=None):
    el = containerTag.find(elName, class_=classAttr)
    if el is None: return defaultVal
    return ' '.join(el.get_text(' ').split()) # split+join minimizes whitespace

results = soup.find_all('div', {'class': "similar-listings-item"}) 
infoList = [[get_min_text(result, *c[:3]) for c in [
    ('div', 'similar-listings-info'), # Title
    ('p', 'listings-location'), # Location
    ('div', 'similar-listings-price') # Price
]] for result in results]
```

[![op][3]][3]


  [1]: https://i.sstatic.net/Kx4e7.png
  [2]: https://i.sstatic.net/5GeKh.png
  [3]: https://i.sstatic.net/QZH04.png
