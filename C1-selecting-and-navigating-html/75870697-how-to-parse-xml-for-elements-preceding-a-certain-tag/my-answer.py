# Code from my Stack Overflow answer https://stackoverflow.com/a/75872121 (posted 2023-03-29), extracted verbatim; may need the question's context to run.

# --- block 1 ---
[x.previous_element for x in soup.find_all("xref", attrs={'ref-type': 'bibr'})]

# --- block 2 ---
> [
>     'This could be due to two nonmutually exclusive possibilities: first, the HB3 DNA sequence for these genes may be substantially rearranged or completely deleted relative to the reference strain, 3D7; second, only a few of these genes may be selectively expressed, as has been proposed (',
>     '). To identify regions of genomic variability between 3D7 and HB3, we performed microarray-based comparative genomic hybridization (CGH) analysis. Array-based CGH has been performed with human cDNA and bacterial artificial chromosome-based microarrays to characterize DNA copy-number changes associated with tumorigenesis (',
>     '; '
> ]
>

# --- block 3 ---
''.join([x.previous_element for x in soup.find_all("xref", attrs={'ref-type': 'bibr'})])

# --- block 4 ---
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

# --- block 5 ---
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
>

# --- block 6 ---
{c.get('text'):c.get('references') for c in cited_texts}

# --- block 7 ---
> {
>   'This could be due to two nonmutually exclusive possibilities: first, the HB3 DNA sequence for these genes may be substantially rearranged or completely deleted relative to the reference strain, 3D7; second, only a few of these genes may be selectively expressed, as has been proposed': ('[pbio-0000005-Deitsch1] Deitsch et al. 2001',),
>   'To identify regions of genomic variability between 3D7 and HB3, we performed microarray-based comparative genomic hybridization (CGH) analysis. Array-based CGH has been performed with human cDNA and bacterial artificial chromosome-based microarrays to characterize DNA copy-number changes associated with tumorigenesis': ('[pbio-0000005-Gray1] Gray and Collins 2000', '[pbio-0000005-Pollack2] Pollack et al. 2002')
> }
>
