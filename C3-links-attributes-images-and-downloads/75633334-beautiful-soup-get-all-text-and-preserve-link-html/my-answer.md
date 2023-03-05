---
title: "Beautiful Soup - Get all text, and preserve link html?"
site: stackoverflow
question_id: 75633334
answer_id: 75645726
url: https://stackoverflow.com/a/75645726
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-05T22:24:47Z
last_edited: 2023-03-05T22:34:42Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75645726/revisions
accepted: true
score: 1
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: [get_text_plus]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 31be2b1866a4f2500bc6c44064a76a84bc31ca32b5251b9cad7746a905f41e6d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75645726>, 2023-03-05, last edited 2023-03-05; **accepted**; score 1. Text as retrieved 2026-10-12.

> *try changing `and type(descendant) not in types` to **`and not isinstance(descendant, types)`***

> With your recommended change, I get the same error
> ```
> in _all_strings
>     (types is not None and type(descendant) not in types)):
> TypeError: argument of type 'object' is not iterable
> ```

But the error should be different after changing - the line mentioned in the error traceback (*`types is not None and type(descendant) not in types)`*) is the very line I suggested changing...

Anyway, I looked into it a bit more, and my suggested change just raises a different kind of error; the main issue is caused by `get_text` calling `_all_strings` with `types=default`; it seems that `default` has no meaning in this new subclass (that's why you're seeing *`<class 'object'> ....`*).

---

You could check `types` at the beginning and ensure it's either a class or a tuple of classes at the beginning of the function:

```py
class MyBeautifulSoup(BeautifulSoup):
    def _all_strings(self, strip=False, types=(NavigableString, CData)):
        # verify types [ADDED]
        if hasattr(types,'__iter__'):
            types = tuple([t for t in types if isinstance(t,type)])
        if types is None: types = NavigableString
        if not types or not isinstance(types, (type, tuple)):
            types = (NavigableString, CData)

        for descendant in self.descendants:
            # return "a" string representation if we encounter it

            if isinstance(descendant, Tag) and descendant.name == 'a':
                yield str('<{}> '.format(descendant.get('href', '')))

            # skip an inner text node inside "a"
            if isinstance(descendant,NavigableString) and descendant.parent.name == 'a':
                continue
            
            if not isinstance(descendant, types): continue # default behavior [EDITED]

            if strip:
                descendant = descendant.strip()
                if len(descendant) == 0:
                    continue
            yield descendant
```

---

However, not using `default` as `types` also means that JavaScript and CSS are no longer excluded. So [personally] I would prefer to just write the new class with two entirely new methods and use those:

```py
# from urllib.parse import urljoin

class MyBeautifulSoup(BeautifulSoup):
    def _all_strings_plus(  self, strip=True, types=NavigableString, 
                            aRef={'a': lambda a: f"<{a.get('href', '')}>"}, 
                            skipTags=['script', 'style']    ):
        # verify types
        if hasattr(types,'__iter__') and not isinstance(types,type):
            types = tuple([t for t in types if isinstance(t, type)])
        if not (types and isinstance(types,(type,tuple))): types = NavigableString
        
        # skip text in tags included in aRef
        # skipTags += list(aRef.keys())
        
        for descendant in self.descendants:
            # yield extra strings according to aRef
            if isinstance(descendant, Tag) and descendant.name in aRef:
                extraStr = aRef[descendant.name](descendant)
                if isinstance(extraStr, str): yield extraStr

            # skip text nodes DIRECTLY inside a Tag in aRef
            # if descendant.parent.name in aRef: continue

            # skip ALL text nodes inside skipTags 
            if skipTags and descendant.find_parent(skipTags): continue

            # default behavior
            if not isinstance(descendant, types): continue

            if strip:
                descendant = descendant.strip()
                if len(descendant) == 0: continue
            yield descendant
    
    def get_text_plus(self, separator=" ", srcUrl=None, **aspArgs):
        if srcUrl and isinstance(srcUrl, str):
            def hrefStr(aTag):
                href = aTag.get('href')
                if not (href is None or href.startswith('javascript:')):
                    return f"<{urljoin(srcUrl, href)}>"
            aspArgs.setdefault('aRef', {})
            aspArgs['aRef']['a'] = hrefStr
        
        return separator.join(self._all_strings_plus(**aspArgs)) 
```

This also lets you specify the source URL [like <kbd>`soup.get_text(srcUrl='https://example.com/')`</kbd>] so that [relative paths](https://www.coffeecup.com/help/articles/absolute-vs-relative-pathslinks/) can be converted to full links, and JavaScript links can be ignored (remove the *`or href.startswith('javascript:')`* part of the condition if you don't care about omitting those).

Btw, I've commented out the parts for omitting strings from `a` tags [or, rather, any tags included in `aRef`], but you can uncomment them according to what you want; although, if you uncomment the *`skipTags += list(aRef.keys())`* line, then the *`if descendant.parent.name in aRef: continue`* line becomes redundant.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[VV75](https://stackoverflow.com/users/853113)** (2023-03-07): Worked great! I can't thank you enough for spending time on this issue! To answer your earlier questions, I am not trying to skip the Link text. I wanted to get both (text and the link).
- **me** (2023-03-07): @VV75 glad it works! [Yeah, the `continue` after *`# skip an inner text node inside "a"`* would have skipped some text. It made me wonder if you meant to add something to format that text differently before yielding it but forgot...]
