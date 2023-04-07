---
title: "Python3 AttributeError: 'NoneType' object has no attribute 'find_all'"
site: stackoverflow
question_id: 75953316
answer_id: 75955830
url: https://stackoverflow.com/a/75955830
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-07T06:01:48Z
last_edited: 2023-04-07T06:36:57Z
revisions: 4
revision_history: https://stackoverflow.com/posts/75955830/revisions
accepted: false
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5c92436f4cd98e7cdbba4b983e6a200cf09e65b4dda149c3785adac6cafa5a14
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75955830>, 2023-04-07, last edited 2023-04-07; score 0. Text as retrieved 2026-10-12.

|<kbd>[ Summary: I think the <kbd>`genres_div`</kbd> you want is a <kbd>**`ul`**</kbd> tag (NOT a *`div`*) with *`class="genres"`*. ]</kbd>|
|:-:|

<br>

> Error :
> ```py
> genre_links = genres_div.find_all('a')
>                   ^^^^^^^^^^^^^^^^^^^
> AttributeError: 'NoneType' object has no attribute 'find_all'
> ```

So that indicates that `genres_div` is returning `None`; to just avoid raising the error, you can just check for it and set `genre_links` as an empty list by default

```py
genre_links = [] if genres_div is None else genres_div.find_all('a') ## OR
# genre_links = genres_div.find_all('a') if genres_div else []
```

and that's fine if `genres_div` is only null *some* of the time, and you just want empty `path` and `text` lists in such cases.

---

However, if you want to investigate *why* `genres_div` isn't returning anything, it's likely because you're trying to find it with

> ```py
> genres_div = soup.find('div', class_='genres')
> ```

but I could not find any `div`s in the [source html](https://egghead.io/lessons/misc-chrome-devtools-elements-inspect-elements-vs-view-source) with `class_='genres'`.

The only tag I could find<sup>([view screenshot][1])</sup> with that class was a `ul` tag, which *did* contain a list of links; so you could change the line above to <kbd>`genres_div = soup.find('ul', class_='genres')`</kbd>, but I find chaining `find...` calls risky in general, and usually prefer to use [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors-through-the-css-property)<sup>(handled by [SoupSieve](https://facelessuser.github.io/soupsieve/selectors/))</sup>  like:

```py
genre_links = soup.select('ul.genres a[href]') ## OR
# genre_links = soup.select('.genres a[href]') 
## '.genres a[href]' <-- any a tags inside any tag with a "genres" class
```

If those *are* the links you want, then you can also bypass `.genres` entirely and search for them via the `title` attribute:

```py
# genre_links = soup.select(f'a[href][title^="View all posts in "]') ## OR 

title_check = lambda t: t and t.startswith("View all posts in ")
genre_links = soup.find_all('a', href=True, title=title_check)
```

<br>

---

<br>

Btw, you can also get the `path` and `text` lists with [list comprehension](https://www.programiz.com/python-programming/list-comprehension) instead of appending on loop, 

- either with two separate list comprehensions:
  ```py
  genre_links = soup.select(f'.genres a[href]')
  path, text = [a['href'] for a in genre_links], [a.text for a in genre_links]
  # path_text_pairs = list(zip(path, text))
  ```

- or as a list of tuples that you then separate by [unpacking](https://towardsdatascience.com/unpacking-operators-in-python-306ae44cd480) and  [zipping](https://www.programiz.com/python-programming/methods/built-in/zip):

  ```py
  path_text_pairs = [(a['href'], a.text) for a in soup.select('.genres a[href]')]
  path, text = [list(l) for l in zip(*path_text_pairs)] 
  ```

With either method, <kbd>`print(f'{path_text_pairs = }\n\n{path = }\n{text = }')`</kbd> should print:
> ```py
> path_text_pairs = [('/genres/action/', 'Action'), ('/genres/adventure/', 'Adventure'), ('/genres/comedy/', 'Comedy'), ('/genres/demons/', 'Demons'), ('/genres/drama/', 'Drama'), ('/genres/ecchi/', 'Ecchi'), ('/genres/fantasy/', 'Fantasy'), ('/genres/game/', 'Game'), ('/genres/harem/', 'Harem'), ('/genres/historical/', 'Historical'), ('/genres/horror/', 'Horror'), ('/genres/josei/', 'Josei'), ('/genres/magic/', 'Magic'), ('/genres/martial-arts/', 'Martial Arts'), ('/genres/mecha/', 'Mecha'), ('/genres/military/', 'Military'), ('/genres/music/', 'Music'), ('/genres/mystery/', 'Mystery'), ('/genres/psychological/', 'Psychological'), ('/genres/parody/', 'Parody'), ('/genres/police/', 'Police'), ('/genres/romance/', 'Romance'), ('/genres/samurai/', 'Samurai'), ('/genres/school/', 'School'), ('/genres/sci-fi/', 'Sci-Fi'), ('/genres/seinen/', 'Seinen'), ('/genres/shoujo/', 'Shoujo'), ('/genres/shoujo-ai/', 'Shoujo Ai'), ('/genres/shounen/', 'Shounen'), ('/genres/slice-of-life/', 'Slice of Life'), ('/genres/sports/', 'Sports'), ('/genres/space/', 'Space'), ('/genres/super-power/', 'Super Power'), ('/genres/supernatural/', 'Supernatural'), ('/genres/thriller/', 'Thriller'), ('/genres/vampire/', 'Vampire')]
> 
> path = ['/genres/action/', '/genres/adventure/', '/genres/comedy/', '/genres/demons/', '/genres/drama/', '/genres/ecchi/', '/genres/fantasy/', '/genres/game/', '/genres/harem/', '/genres/historical/', '/genres/horror/', '/genres/josei/', '/genres/magic/', '/genres/martial-arts/', '/genres/mecha/', '/genres/military/', '/genres/music/', '/genres/mystery/', '/genres/psychological/', '/genres/parody/', '/genres/police/', '/genres/romance/', '/genres/samurai/', '/genres/school/', '/genres/sci-fi/', '/genres/seinen/', '/genres/shoujo/', '/genres/shoujo-ai/', '/genres/shounen/', '/genres/slice-of-life/', '/genres/sports/', '/genres/space/', '/genres/super-power/', '/genres/supernatural/', '/genres/thriller/', '/genres/vampire/']
> text = ['Action', 'Adventure', 'Comedy', 'Demons', 'Drama', 'Ecchi', 'Fantasy', 'Game', 'Harem', 'Historical', 'Horror', 'Josei', 'Magic', 'Martial Arts', 'Mecha', 'Military', 'Music', 'Mystery', 'Psychological', 'Parody', 'Police', 'Romance', 'Samurai', 'School', 'Sci-Fi', 'Seinen', 'Shoujo', 'Shoujo Ai', 'Shounen', 'Slice of Life', 'Sports', 'Space', 'Super Power', 'Supernatural', 'Thriller', 'Vampire'] 
> ```

<br>

---

<br>

Suggested version of full working code:

```py
import requests
from bs4 import BeautifulSoup

url = 'https://otakudesu.lol/genre-list/'
soup = BeautifulSoup((r:=requests.get(url)).content, 'html.parser')
print(f'<{r.status_code} {r.reason}> from {r.url}\n') ## for debugging

genre_links = soup.select(f'.genres a[href]')
paths, texts = [a['href'] for a in genre_links], [a.text for a in genre_links]

if not genre_links: ## for debugging [ if no results ]
    dump_fp = 'x.html'
    with open(dump_fp, 'wb') as f: f.write(soup.prettify('utf-8'))
    print(f'No genre links found - saved html to {dump_fp!r}')
else: print(f'{paths = }\n{texts = }') ## print results
```

This way, if there are no results, you can open the `dump_fp` file (and inspect [with JavaScript disabled](https://developer.chrome.com/docs/devtools/javascript/disable/)) to check exactly what HTML source your code is working with [sometimes it's [not the same as what you can inspect on your browser](https://egghead.io/lessons/misc-chrome-devtools-elements-inspect-elements-vs-view-source) even if your request gets an [`OK`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses) response].



  [1]: https://i.sstatic.net/mp9SE.png
