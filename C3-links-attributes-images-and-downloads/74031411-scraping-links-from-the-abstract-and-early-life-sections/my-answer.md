---
title: "Scraping links from the Abstract, and Early Life sections separately"
site: stackoverflow
question_id: 74031411
answer_id: 74036946
url: https://stackoverflow.com/a/74036946
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-12T05:37:42Z
last_edited: 2022-11-09T12:52:45Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74036946/revisions
accepted: true
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bd8faf268b65af3680c4ef0ddfb3e5628c56ae9dd89d3f5b04a868e92c88f8d9
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74036946>, 2022-10-12, last edited 2022-11-09; **accepted**; score 0. Text as retrieved 2026-10-12.

It's not very clear what format you want your output to be in, but the following will produce a list of dictionaries with the sections in several different formats:

First, the sections and abstract are all inside [this][1] `div`, and are not nested any further into separate elements - so this starts by [selecting](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) the whole outer element and then going through its children:

```python
content = soup.select_one('#mw-content-text > .mw-parser-output').children
splitContent = []
```

(`splitContent` is the list that will be filled up with a dictionary for each section.)

```python
for c in content:
    if c.name == 'h2' or splitContent == []:
        sectionName = 'Abstract' if splitContent == [] else c.text
        splitContent.append({
            'section': sectionName, 
            'listSoups': [], 'HTML': '', 'asText': ''
        }) 

    splitContent[-1]['listSoups'].append(c)
    splitContent[-1]['HTML'] += str(c)
    if c.name not in ['style', 'script']: 
        splitContent[-1]['asText'] += c.text
```

Each section header is wrapped as `h2`*, so every time the loop gets to a child tag that's h2, a new dictionary is started, and the child object itself is always added to `listSoups` in the *last* dictionary of the `splitContent` list.

`HTML` is saved too, so if you want a single bs4 object to be created for each section, `splitContent` can be looped through:

```python
for i in range(len(splitContent)):
    splitContent[i]['asSoup'] = BeautifulSoup(splitContent[i]['HTML'], 'html.parser')
```
Now, you [can see any of the sections in any of the formats][2] added to the dictionaries.

Note that `listSoups` is not the same as `asSoup`. `listSoups` is a *list*, and each item within is still connected to the original `soup` variable and you can view its parent, nextSibling, etc in ways that would not be possible with `asSoup`, which is a *single* object.

<br>

*Btw, using `{'class':'mw-headline'}` will give you not just the main section headers, but also the subheaders. You can actually get something like a [tree of the article structure][3] with:

```python
for h in soup.findAll('span',attrs={'class':'mw-headline'}):
    hLevel = int(h.parent.name.replace('h', ''))
    print(('\t'*(hLevel-2))+'↳', f'[{h.parent.name}] {h.text}')
```

<hr>

**Additional EDIT:**

To get a dictionary of section texts, just use

```python
sectnTexts_dict = dict([(
    sc['section'].replace(' ', '_'), # section name to key
    sc['asText'] # section text as value
) for sc in splitContent])
```
to view a truncated version, print `dict((k, v[:50]+'...') for k, v in sectnTexts_dict.items())`, which looks like
```json
{
   "Abstract": "44th President of the United States\n\"Barack\" and \"...",
   "Early_life_and_career": "Early life and career\nMain article: Early life and...",
   "Legal_career": "Legal career\nCivil Rights attorney\nHe joined Davis...",
   "Legislative_career": "Legislative career\nIllinois Senate (1997\u20132004)\nMai...",
   "Presidential_campaigns": "Presidential campaigns\n2008\nMain articles: 2008 Un...",
   "Presidency_(2009\u20132017)": "Presidency (2009\u20132017)\n First official portrait of...",
   "Cultural_and_political_image": "Cultural and political image\nMain article: Public ...",
   "Post-presidency_(2017\u2013present)": "Post-presidency (2017\u2013present)\n Obama with his the...",
   "Legacy": "Legacy\n Job growth during the presidency of Obama ...",
   "Bibliography": "Bibliography\nMain article: Bibliography of Barack ...",
   "See_also": "See also\n\n\nBiography portal\nUnited States portal\nC...",
   "References": "References\n\n^ \"Barack Hussein Obama Takes The Oath...",
   "Further_reading": "Further reading\n\nDe Zutter, Hank (December 8, 1995...",
   "External_links": "External links\nLibrary resources about  Barack Oba..."
}
```

  [1]: https://i.sstatic.net/3ys8q.png
  [2]: https://i.sstatic.net/qWmyC.png
  [3]: https://i.sstatic.net/2EUb7.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Minda](https://stackoverflow.com/users/12863170)** (2022-11-10): Thank you so much. This is very helpful. The additional thing I want to do is: dict={h2:{h3:{h4:html}}}. If you can show me that I really appreciate it. For example: dict={early life:{education:{college and research jobs: h4 html}}}
- **[Minda](https://stackoverflow.com/users/12863170)** (2022-11-10): dict={h2:{h3:{h4:h4 paragraphs html}}}
- **me** (2022-11-12): @Minda you can [do the same thing recursively for each header-type](https://pastebin.com/vsKc9Qq5) [ see also the code for some [sample tests](https://pastebin.com/LcqTjYNZ) as well as [one of the sample outputs](https://pastebin.com/3sxUbBd0) (It's with the truncated htmls because full htmls exceed the maximum allowance for size)]
