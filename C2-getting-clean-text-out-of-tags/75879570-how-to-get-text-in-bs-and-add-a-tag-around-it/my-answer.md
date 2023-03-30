---
title: "How to get text in BS and add a tag around it"
site: stackoverflow
question_id: 75879570
answer_id: 75883946
url: https://stackoverflow.com/a/75883946
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-30T03:45:22Z
last_edited: 2023-03-30T04:31:38Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75883946/revisions
accepted: false
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 48b5e71f93f02621e72e47943095388ce72a92242e95c2cf3a580c52eda01a03
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75883946>, 2023-03-30, last edited 2023-03-30; score 1. Text as retrieved 2026-10-12.

Not sure how efficient it would be, but you could just loop through `things`, split strings containing a substring from `things` and use [`.insert...`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#insert-before-and-insert-after) like:

```py
xStr = '    <p>\n    lorem ipsum dolor <hi>a</hi>met.\n    Thing_A, <thing>Thing_B</thing>, Thing_C\n    </p>' 

thing_tag = 'thing' # 'rs' # 
things = ['Thing_A', 'Thing_B', 'Thing_C']

p_snip = BeautifulSoup(xStr, 'lxml').p 
```

```py
def wrap_str(s, name='rs', attrs=None): 
    if not isinstance(attrs, dict): 
        attrs = {'type':"org", 'ref':f"#{s.lower()}"}
    wrapped = BeautifulSoup(f'<{name}>{s}</{name}>', 'lxml').find(name)
    for k,v in attrs.items(): wrapped[k] = v
    return wrapped

for thing in things:
    thing_strs = [
        d for d in soup.descendants if isinstance(d,str) and not d.PREFIX
        and thing in d and not (d.strip()==thing and d.parent.name==thing_tag)
    ]
    for thing_str in thing_strs:
        for si, str_sect in enumerate(thing_str.split(thing)):
            # if si: thing_str.insert_before(wrap_str(thing, thing_tag)) 
            if si: thing_str.insert_before(wrap_str(thing, thing_tag, {})) 
            thing_str.insert_before(str_sect)
        thing_str.replace_with('')
```

and after that, `p_snip` should look like your desired output: 

>```html
>     <p> 
>     lorem ipsum dolor <hi>a</hi>met. 
>     <thing>Thing_A</thing>, <thing>Thing_B</thing>, <thing>Thing_C</thing> 
>     </p>
>```

although, if you use `wrap_str` with the default `attrs` parameter like in the commented *`if si...`* line and with `thing_tag='rs'`, then `p_snip` should look like:

>```html
>     <p> 
>     lorem ipsum dolor <hi>a</hi>met. 
>     <rs ref="#thing_a" type="org">Thing_A</rs>, <thing><rs ref="#thing_b" type="org">Thing_B</rs></thing>, <rs ref="#thing_c" type="org">Thing_C</rs> 
>     </p>
>```
