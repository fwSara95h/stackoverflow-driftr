---
title: "Ignore / skip tags when prettifying with BeautifulSoup"
site: stackoverflow
question_id: 73011981
answer_id: 74987578
url: https://stackoverflow.com/a/74987578
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-02T22:30:42Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74987578/revisions
accepted: false
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 80f686c973e310ed47632cdcfa386b191141df9f9c8603bd664c7c8d7f1dc1ef
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74987578>, 2023-01-02; score 1. Text as retrieved 2026-10-12.

As far as I can tell, bs4 doesn't allow for skipping particular tags; but you could write your own parser ([like here](https://stackoverflow.com/a/56683309/6146136)) and include or allow exceptions, or use [regex](https://www.w3schools.com/python/python_regex.asp) to replace the tags you don't want to parse.

First, list the tags you want to skip parsing

```python
skipTags = ['svg']
# skipTags = ['svg', 'script', 'style'] ## list all the tag names to skip
```

---

If you don't care about preserving the the tags, you could just get rid of them entirely.

```python
# import re
# from bs4 import BeautifulSoup
for n in skipTags: messy = re.sub(f'<{n}\s*.*\s*>\s*.*\s*</{n}>', '', messy)
pretty = BeautifulSoup(markup=messy, features='html.parser').prettify()
```

---

If you want to preserver the tags, then replace them with comments and then replace the comment after prettifying. [**This can be significantly slower than just getting rid of them.**]

```python
# import re
# from bs4 import BeautifulSoup
cReps = []

for n in skipTags: 
    rcpat = re.compile(f'<{n}\s*.*\s*>\s*.*\s*</{n}>')
    cReps += [m.span() for m in rcpat.finditer(messy)]
for cri, (sPos, ePos) in list(enumerate(cReps))[::-1]:
    repCmt, orig = f'<!--do_not_parse__placeholder_{cri}-->', messy[sPos:ePos]
    messy = messy[:sPos] + repCmt + messy[ePos:]
    cReps[cri] = (repCmt, orig)

pretty = BeautifulSoup(markup=messy, features='html.parser').prettify()
for repCmt, orig in cReps:
    pretty = pretty.replace(repCmt, orig, 1)

print('<!--messy-subbed-->', messy, '\n<!--pretty-->', pretty, sep='\n')
```

Printed output of the last statement above, with the sample HTML in your question looks like:

```html
<!--messy-subbed-->
<html>  <head>
   <title>
   
       Some title</title>
    </head> <body>
<!--do_not_parse__placeholder_0-->
</body> </html>


<!--pretty-->
<html>
 <head>
  <title>
   Some title
  </title>
 </head>
 <body>
  <svg>Don't parse and prettify this!</svg>
 </body>
</html>
```

---

**Note that** I don't know if either method will actually improve performance, especially when you consider how many more times it will be through the HTML string/s. You might want to look into https://thehftguy.com/2020/07/28/making-beautifulsoup-parsing-10-times-faster/

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[questiondude](https://stackoverflow.com/users/2031993)** (2023-03-08): Thanks very much! I apologize for not replying sooner. You have several good ideas. Perhaps the most efficient would be a custom parser. I copied the code from the link you gave and did some timing experiments. It seems the custom parser is 20x slower than the normal BS4 parser and `prettify` function. Obviously this depends on the custom parser, but in this case it is very simple, so perhaps BS4 uses a fast C implementation, while the custom parser is in Python (?) I have upvoted your answer, but am leaving the question open in case someone has a better solution in the future. Thanks again!
- **[questiondude](https://stackoverflow.com/users/2031993)** (2023-03-08): Furthermore, it seems that what I really need is the opposite of the `parse_only` argument to the `BeautifulSoup` class. Something like a `parse_except` argument. That would be an elegant and probably also quite efficient solution. Perhaps that will get added some day.
- **me** (2023-03-08): @questiondude I actually didn't know about the `parse_only` argument (looks rather handy, thanks!). Have you considered using that? You could list all the tag names in the [w3schools HTML reference](https://www.w3schools.com/TAGS/default.asp), or collect all the names in some of these files with something like `tagsList = set(d.name for d in soup.descendants if d.name)` [and then remove the ones you don't want]....or does that sound too risky in terms of data loss?
