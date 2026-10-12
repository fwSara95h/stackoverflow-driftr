# Code from my Stack Overflow answer https://stackoverflow.com/a/75206102 (posted 2023-01-23), extracted verbatim; may need the question's context to run.

# --- block 1 ---
hId = 'Personalidad' # for example
hSel = f'h2:has(span.mw-headline[id="{hId}"])'

# --- block 2 ---
sSel = f'{hSel}~*:not({hSel}~h2~*):not(h2)'

# --- block 3 ---
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

# --- block 4 ---
> {
>  'headerId': 'Personalidad',
>  'sectionHeader': 'Personalidad',
>  'sectionText': 'Jotaro describió a Star Platinum como un ser muy violento. Suele ser silencioso, excepto cuando lanza golpes,  gritando  "ORA ORA ORA" en voz alta, bastante rápido y repetidamente. Con una cara relativamente humana ha demostrado tener expresiones tales como fruncir el ceño y sonreír.\nStar Platinum demuestra un tipo de interés en la auto-conservación, como se ve cuando detiene una bala que Jotaro dispara experimentalmente en su propia cabeza, protege a un Jotaro incapacitado de los ataques de  DIO  durante los efectos de su  The World , y lo revive de cerca de la muerte directamente hacia latir su corazón (Sin embargo, considerando el papel pionero de Star Platinum en la serie, esta capacidad puede hablar principalmente de cualidades metafísicas o subconscientes genéricas para los usuarios de Stand).\nEn el manga original, Star Platinum desde el principio se ve con una sonrisa amplia y desconcertante. Más tarde, Star Platinum gana el rostro estoico de Jotaro, cualquier sonrisa futura va a advertir a la persona que se dirige a un gran dolor inminente.\nStar Platinum lleva el nombre de la carta del Tarot  La Estrella , que simboliza el optimismo, el discernimiento y la esperanza.',
>  'sectionHtml': '<p> Jotaro describió a Star Platinum como un ser muy violento. Suele ser silencioso, excepto cuando lanza golpes, <a href="/es/wiki/Grito_de_Stand" title="Grito de Stand">  gritando </a> "ORA ORA ORA" en voz alta, bastante rápido y repetidamente. Con una cara relativamente humana ha demostrado tener expresiones tales como fruncir el ceño y sonreír.</p>\n<p> Star Platinum demuestra un tipo de interés en la auto-conservación, como se ve cuando detiene una bala que Jotaro dispara experimentalmente en su propia cabeza, protege a un Jotaro incapacitado de los ataques de <a href="/es/wiki/Dio_Brando" title="Dio Brando">  DIO </a> durante los efectos de su <a href="/es/wiki/The_World" title="The World">  The World </a> , y lo revive de cerca de la muerte directamente hacia latir su corazón (Sin embargo, considerando el papel pionero de Star Platinum en la serie, esta capacidad puede hablar principalmente de cualidades metafísicas o subconscientes genéricas para los usuarios de Stand).</p>\n<p> En el manga original, Star Platinum desde el principio se ve con una sonrisa amplia y desconcertante. Más tarde, Star Platinum gana el rostro estoico de Jotaro, cualquier sonrisa futura va a advertir a la persona que se dirige a un gran dolor inminente.</p>\n<p> Star Platinum lleva el nombre de la carta del Tarot <a class="extiw" href="http://en.wikipedia.org/wiki/es:La_Estrella_(Tarot)" title="wikipedia:es:La Estrella (Tarot)">  La Estrella </a> , que simboliza el optimismo, el discernimiento y la esperanza.</p>'
> }
>

# --- block 5 ---
h2Tags = soup.select('h2:has(span.mw-headline[id])')
wikiSections = [get_wikiSection(h, soup) for h in [None]+h2Tags]
