---
title: "How to parse XML for elements preceding a certain tag?"
site: stackoverflow
question_id: 75870697
answer_id: 75872121
url: https://stackoverflow.com/a/75872121
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-29T00:34:46Z
last_edited: 2023-03-29T23:01:56Z
revisions: 3
revision_history: https://stackoverflow.com/posts/75872121/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 95de58e689a26fd8e8f69627c3cfa05e82e71f6a712903de95255508fb49c857
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-29

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75872121>, 2023-03-29, last edited 2023-03-29; score 0. Text as retrieved 2026-10-12.

`find` always only returns the first of the corresponding `find_all` [or `None`], and `find_all` returns a ResultSet [which is a sub-class of list].

So, you need to loop through that ResultSet and get the `.previous_element` of each result with either a `for`-loop or [list comprehension](https://www.programiz.com/python-programming/list-comprehension).

---

#### List Comprehension

```py
[x.previous_element for x in soup.find_all("xref", attrs={'ref-type': 'bibr'})]
```

should return the list

>```py
> [
>     'This could be due to two nonmutually exclusive possibilities: first, the HB3 DNA sequence for these genes may be substantially rearranged or completely deleted relative to the reference strain, 3D7; second, only a few of these genes may be selectively expressed, as has been proposed (',
>     '). To identify regions of genomic variability between 3D7 and HB3, we performed microarray-based comparative genomic hybridization (CGH) analysis. Array-based CGH has been performed with human cDNA and bacterial artificial chromosome-based microarrays to characterize DNA copy-number changes associated with tumorigenesis (',
>     '; '
> ]
>```

and

```py
''.join([x.previous_element for x in soup.find_all("xref", attrs={'ref-type': 'bibr'})])
```

would join that list into a single string:

> *"This could be due to two nonmutually exclusive possibilities: first, the HB3 DNA sequence for these genes may be substantially rearranged or completely deleted relative to the reference strain, 3D7; second, only a few of these genes may be selectively expressed, as has been proposed (). To identify regions of genomic variability between 3D7 and HB3, we performed microarray-based comparative genomic hybridization (CGH) analysis. Array-based CGH has been performed with human cDNA and bacterial artificial chromosome-based microarrays to characterize DNA copy-number changes associated with tumorigenesis (; "*

---

#### `for` Loop

If you wanted the texts grouped with the relevant `xref`s, you could use something like

```py
cited_texts = [{}]
for section in soup.select(':has(>xref[ref-type="bibr"])'):
    prev_xref = True
    for c in section.contents:
        cTxt = c.strip() if isinstance(c,str) else c.get_text(' ',strip=True)
        if not (c.name=='xref' or cTxt.strip(';().')): continue 
        if c.name=='xref': 
            xref = f"[{c.get('rid', '?rid')}] {cTxt}" # c # cTxt #
            refsList = cited_texts[-1].setdefault('references', tuple())
            cited_texts[-1]['references'] = (*refsList, xref)
            prev_xref = True
            continue
        
        if prev_xref and cited_texts[-1]: cited_texts.append({})
        prev_xref = False
        cited_text = cited_texts[-1].setdefault('text', '')
        cited_texts[-1]['text'] = (cited_text+' '+cTxt).strip().strip(';().').strip()
```

and after that, `cited_texts` should return

>```py
> [
>   {
>     'text': 'This could be due to two nonmutually exclusive possibilities: first, the HB3 DNA sequence for these genes may be substantially rearranged or completely deleted relative to the reference strain, 3D7; second, only a few of these genes may be selectively expressed, as has been proposed',
>     'references': ('[pbio-0000005-Deitsch1] Deitsch et al. 2001',)
>   },
>   {
>     'text': 'To identify regions of genomic variability between 3D7 and HB3, we performed microarray-based comparative genomic hybridization (CGH) analysis. Array-based CGH has been performed with human cDNA and bacterial artificial chromosome-based microarrays to characterize DNA copy-number changes associated with tumorigenesis',
>     'references': ('[pbio-0000005-Gray1] Gray and Collins 2000', '[pbio-0000005-Pollack2] Pollack et al. 2002')
>   }
> ]
>```

You could also convert it to a single dictionary with the `text`s as the keys and the `references` as the values :

```py
{c.get('text'):c.get('references') for c in cited_texts}
```

>```py
> {
>   'This could be due to two nonmutually exclusive possibilities: first, the HB3 DNA sequence for these genes may be substantially rearranged or completely deleted relative to the reference strain, 3D7; second, only a few of these genes may be selectively expressed, as has been proposed': ('[pbio-0000005-Deitsch1] Deitsch et al. 2001',),
>   'To identify regions of genomic variability between 3D7 and HB3, we performed microarray-based comparative genomic hybridization (CGH) analysis. Array-based CGH has been performed with human cDNA and bacterial artificial chromosome-based microarrays to characterize DNA copy-number changes associated with tumorigenesis': ('[pbio-0000005-Gray1] Gray and Collins 2000', '[pbio-0000005-Pollack2] Pollack et al. 2002')
> }
>```

but I find the list of dictionaries (with `text` and `references` as keys) much more readable.
