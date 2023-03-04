---
title: "Beautiful Soup - Get all text, and preserve link html?"
site: stackoverflow
question_id: 75633334
url: https://stackoverflow.com/q/75633334
asked: 2023-03-04T02:43:32Z
asked_by: "VV75"
asked_by_url: https://stackoverflow.com/users/853113
last_edited: 2023-03-05T01:23:27Z
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 1045
answer_count: 1
accepted_answer_id: 75645726
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b770ba034c57472db787bb9297f018f0b3312d5f87f4324e4bb26f1801c84f6c
---

# Beautiful Soup - Get all text, and preserve link html?

Asked by [VV75](https://stackoverflow.com/users/853113) on Stack Overflow, <https://stackoverflow.com/q/75633334>, 2023-03-04, last edited 2023-03-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am parsing multiple HTML pages using beautiful soup. Most of the scenarios work great. I want to include text along with the URL for links.

The current syntax is:
```
            soup = MyBeautifulSoup(''.join(body), 'html.parser')
            body_text = self.remove_newlines(soup.get_text())
```




I found an online recommendation to override the _all_strings function:
```
class MyBeautifulSoup(BeautifulSoup):
    def _all_strings(self, strip=False, types=(NavigableString, CData)):
        for descendant in self.descendants:
            # return "a" string representation if we encounter it

            if isinstance(descendant, Tag) and descendant.name == 'a':
                yield str('<{}> '.format(descendant.get('href', '')))

            # skip an inner text node inside "a"
            if isinstance(descendant, NavigableString) and descendant.parent.name == 'a':
                continue

            # default behavior
            if (
                (types is None and not isinstance(descendant, NavigableString))
                or
                    (types is not None and type(descendant) not in types)):
                continue

            if strip:
                descendant = descendant.strip()
                if len(descendant) == 0:
                    continue
            yield descendant

```
However, this gives a runtime error:
```
in _all_strings
    (types is not None and type(descendant) not in types)):
TypeError: argument of type 'object' is not iterable
```

Is there a way around this error?

Thanks!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-03-04): did you call `_all_strings` with any arguments? Please include the code where you called `_all_strings`, and also where you created the `MyBeautifulSoup` object you called it on. (That said, you could try changing *`and type(descendant) not in types`* to **`and not isinstance(descendant, types)`**.)
- **[VV75](https://stackoverflow.com/users/853113)** (2023-03-05): My apologies, I had a typo that I just fixed. The code to create soup is:             soup = MyBeautifulSoup(''.join(body), 'html.parser')   and the function gets called when you call               body_text = self.remove_newlines(soup.get_text())  With your recommended change, I get the same error.   File "convert.py", line 36, in _all_strings     (types is not None and type(descendant) not in types)): TypeError: argument of type 'object' is not iterable  For what it is worth, I printed types, and here is the output. types:  <class 'object'> <object object at 0x7fc79a4223b0>
- **me** (2023-03-05): I see the issue now. [I've answered with my suggested solutions.] But are you sure about the *`if....descendant.parent.name == 'a': continue`* part? Why do you want to get rid of the hyperlink text? And also, that only gets rid of the text that isn't nested inside another tag inside the `a` tag...are you ok with keeping strings from nested tags? It might make bits of partially-formatted hyper-linked text disappear and leave behind nonsensical sentences....
