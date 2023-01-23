---
title: "Get full text below h2 tag with BeautifulSoup"
site: stackoverflow
question_id: 75204624
answer_id: 75206102
url: https://stackoverflow.com/a/75206102
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-23T06:03:33Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75206102/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f229b0e420c6c0a208cd855d31f7b122f27d55f807ee53760d8fbee4973667d7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-23

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75206102>, 2023-01-23; score 0. Text as retrieved 2026-10-12.

I think in this case, [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) would be very useful.

To get [all the section headers][1], you can use the selector `h2:has(span.mw-headline[id])`; and to get a specific header by the `id` attribute value (`hId` below) of the `span` nested within, you can use the selector `hSel` below.

```python
hId = 'Personalidad' # for example
hSel = f'h2:has(span.mw-headline[id="{hId}"])'
```

Then, to get all the tags *after* that header, you can use `f'{hSel}~*'`, but you also need to filter out the tags after the *next* header to only get tags in that section, so the full selector would be 

```python
sSel = f'{hSel}~*:not({hSel}~h2~*):not(h2)'
```

<sup>[`:not({hSel}~h2~*)` filters out the tags after the next header, and **`:not(h2)`** filters out the next header tag itself.]</sup>

---

Making use of this, the function below returns a dictionary containing section header, text and html.

```python
def get_wikiSection(header, wSoup, sec1Header='? Abstract ?'):
    sSel = 'h2:has(span.mw-headline[id])'
    sSel = f'*:has(~{sSel}):not({sSel}~*)'
    if not header: hId = hSel = None # [first section has no header]
    elif isinstance(header, str):
        hId, hSel = header, f'h2:has(span.mw-headline[id="{header}"])'
        header = wSoup.select_one(hSel)
        if not header: return {'errorMsg': f'Not found: {hSel}'} 
    else: hId = header.select_one('span.mw-headline[id]')['id'] 
    ## header SHOULD BE: None/hId/a tag containing span.mw-headline[id] ##

    if hId: 
        hSel = f'h2:has(span.mw-headline[id="{hId}"])'
        sSel = f'{hSel}~*:not({hSel}~h2~*):not(h2)'
        header = header.get_text(' ').strip()
    else: header = sec1Header
    
    sect = wSoup.select(sSel)
    sText = '\n'.join([s.get_text(' ').strip() for s in sect])
    sHtml = '\n'.join([''.join(s.prettify().splitlines()) for s in sect])
    if not sect: sText = sHtml = None
    return {'headerId': hId, 'sectionHeader': header, 
            'sectionText': sText, 'sectionHtml': sHtml}
```

For example, [`get_wikiSection('Personalidad', soup)`][2] will return

> ```python
> {
>  'headerId': 'Personalidad',
>  'sectionHeader': 'Personalidad',
>  'sectionText': 'Jotaro describió a Star Platinum como un ser muy violento. Suele ser silencioso, excepto cuando lanza golpes,  gritando  "ORA ORA ORA" en voz alta, bastante rápido y repetidamente. Con una cara relativamente humana ha demostrado tener expresiones tales como fruncir el ceño y sonreír.\nStar Platinum demuestra un tipo de interés en la auto-conservación, como se ve cuando detiene una bala que Jotaro dispara experimentalmente en su propia cabeza, protege a un Jotaro incapacitado de los ataques de  DIO  durante los efectos de su  The World , y lo revive de cerca de la muerte directamente hacia latir su corazón (Sin embargo, considerando el papel pionero de Star Platinum en la serie, esta capacidad puede hablar principalmente de cualidades metafísicas o subconscientes genéricas para los usuarios de Stand).\nEn el manga original, Star Platinum desde el principio se ve con una sonrisa amplia y desconcertante. Más tarde, Star Platinum gana el rostro estoico de Jotaro, cualquier sonrisa futura va a advertir a la persona que se dirige a un gran dolor inminente.\nStar Platinum lleva el nombre de la carta del Tarot  La Estrella , que simboliza el optimismo, el discernimiento y la esperanza.',
>  'sectionHtml': '<p> Jotaro describió a Star Platinum como un ser muy violento. Suele ser silencioso, excepto cuando lanza golpes, <a href="/es/wiki/Grito_de_Stand" title="Grito de Stand">  gritando </a> "ORA ORA ORA" en voz alta, bastante rápido y repetidamente. Con una cara relativamente humana ha demostrado tener expresiones tales como fruncir el ceño y sonreír.</p>\n<p> Star Platinum demuestra un tipo de interés en la auto-conservación, como se ve cuando detiene una bala que Jotaro dispara experimentalmente en su propia cabeza, protege a un Jotaro incapacitado de los ataques de <a href="/es/wiki/Dio_Brando" title="Dio Brando">  DIO </a> durante los efectos de su <a href="/es/wiki/The_World" title="The World">  The World </a> , y lo revive de cerca de la muerte directamente hacia latir su corazón (Sin embargo, considerando el papel pionero de Star Platinum en la serie, esta capacidad puede hablar principalmente de cualidades metafísicas o subconscientes genéricas para los usuarios de Stand).</p>\n<p> En el manga original, Star Platinum desde el principio se ve con una sonrisa amplia y desconcertante. Más tarde, Star Platinum gana el rostro estoico de Jotaro, cualquier sonrisa futura va a advertir a la persona que se dirige a un gran dolor inminente.</p>\n<p> Star Platinum lleva el nombre de la carta del Tarot <a class="extiw" href="http://en.wikipedia.org/wiki/es:La_Estrella_(Tarot)" title="wikipedia:es:La Estrella (Tarot)">  La Estrella </a> , que simboliza el optimismo, el discernimiento y la esperanza.</p>'
> }
> ```

---

If you want all the sections:

```python
h2Tags = soup.select('h2:has(span.mw-headline[id])')
wikiSections = [get_wikiSection(h, soup) for h in [None]+h2Tags]
```

**<sup>The resulting list of dictionaries can also be converted to a pandas DataFrame as simply as [`pd.DataFrame(wikiSections)`][3].</sup>**


  [1]: https://i.sstatic.net/73HyJ.png
  [2]: https://i.sstatic.net/6Y0Uj.png
  [3]: https://i.sstatic.net/uvtPK.png
