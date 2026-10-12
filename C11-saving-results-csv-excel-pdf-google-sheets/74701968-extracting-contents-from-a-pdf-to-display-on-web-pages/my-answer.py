# Code from my Stack Overflow answer https://stackoverflow.com/a/74724548 (posted 2022-12-08), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def getLctrSelectors(stsh):  
    stsh = stsh.get_text() if stsh else ''

    ll_ids = list(set([
        l.replace('>li', '> li').split('> li')[0].strip() 
        for l in stsh.splitlines() if l.strip()[:1] == '#' 
        and '> li' in l.replace('>li', '> li') and 
        'counter-increment' in l.split('{')[-1].split(':')[0]
    ]))
    for i, l in enumerate(ll_ids): 
        sel = f'{l} > li > *:first-child'
        ll_ids[i] = (sel, 1)
        crl = [
            ll for ll in stsh.splitlines() if ll.strip().startswith(l)
            and 'counter-reset' in ll.split('{')[-1].split(':')[-2:][0] 
        ][:1] 
        if not crl: continue

        crl = crl[0].split('{')[-1].split('counter-reset')[-1].split(':')[-1]
        crl = [w for w in crl.split(';')[0].split() if w.isdigit()] 
        ll_ids[i] = (sel, int(crl[-1]) if crl else 1)

    return ll_ids

# --- block 2 ---
soup = BeautifulSoup(fp, "html.parser") 
for sel, ctStart in getLctrSelectors(soup.select_one('style')):
    for i, lif in enumerate(soup.select(sel)):
        lif.insert(0, f'{i + ctStart}. ')

para_counter = 1
### REST OF CODE ###
