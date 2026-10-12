# Code from my Stack Overflow answer https://stackoverflow.com/a/74643531 (posted 2022-12-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def getDECstars(starCont, mSoup, outOf=5,  isv=False):
    classList = starCont.get('class', [])
    if type(classList) != list: classList = [classList]
    classList = [str(c) for c in classList if str(c).startswith('css-')] 
    if not classList: 
        if isv: print('Stars container has no "css-" class')
        return None

    demc = classList[0].replace('css-', '', 1)
    demc_sel = f'style[data-emotion-css="{demc}"]'
    cssStyle = mSoup.select_one(demc_sel)
    if not cssStyle:
        if isv: print(f'Nothing found with selector {demc_sel}')
        return None

    cssStyle = cssStyle.get_text()
    errMsg = ''
    if '90deg,#0caa41 ' not in cssStyle: errMsg += 'No #0caa41'
    if '%' not in cssStyle.split('90deg,#0caa41 ', 1)[-1][:20]: 
        errMsg += ' No %'
    if not errMsg:
        rPerc = cssStyle.split('90deg,#0caa41 ', 1)[-1]
        rPerc = rPerc.split('%')[0]
        try:  
            rPerc = float(rPerc)
            if 0 <= rPerc <= 100:
                if type(outOf) == int and outOf > 0: rPerc = (rPerc/100)*outOf
                return float(f'{float(rPerc):.3}')
            errMsg = f'{demc_sel} --> "{rPerc}" is out of range'
        except: errMsg = f'{demc_sel} --> cannot convert to float "{rPerc}"' 
    if isv: print(f'{demc_sel} --> unexpected format {errMsg}')
    return None

# --- block 2 ---
def getDECstars(starCont, mSoup, outOf=5, isv=False):
    try:
        demc = [c for c in starCont.get('class', []) if c[:4]=='css-'][0].replace('css-', '', 1)
        demc_sel = f'style[data-emotion-css="{demc}"]'
        rPerc = float(mSoup.select_one(demc_sel).get_text().split('90deg,#0caa41 ', 1)[1].split('%')[0])
        return float(f'{(rPerc/100)*outOf if type(outOf) == int and outOf > 0 else rPerc:.3}')
    except: return None

# --- block 3 ---
pcCon = 'div.px-std:has(h2 > a.reviewLink) + div.px-std'
pcDiv = f'{pcCon} div.v2__EIReviewDetailsV2__fullWidth'
refDict = {
    'rating_num': 'span.ratingNumber',
    'emp_status': 'div:has(> div > span.ratingNumber) + span',
    'header': 'h2 > a.reviewLink',
    'subheader': 'h2:has(> a.reviewLink) + span',
    'pros': f'{pcDiv}:first-of-type > p.pb',
    'cons': f'{pcDiv}:nth-of-type(2) > p.pb'
}

subRatSel = 'div:has(> .ratingNumber) ~ aside ul > li:has(div ~ div)'
empRevs = []
for r in soup.select('li[id^="empReview_"]'):
    rDet = {'reviewId': r.get('id')}
    for sr in r.select(subRatSel):
        k = sr.select_one('div:first-of-type').get_text(' ').strip()
        sval = getDECstars(sr.select_one('div:nth-of-type(2)'), soup)
        rDet[f'[rating] {k}'] = sval

    for k, sel in refDict.items():
        sval = r.select_one(sel)
        if sval: sval = sval.get_text(' ').strip()
        rDet[k] = sval

    empRevs.append(rDet)

# --- block 4 ---
> erdf = pandas.DataFrame(empRevs).set_index('reviewId')
> erdf['pros'] = [p[:30] + '...' if len(p) > 33 else p for p in erdf['pros']]
> erdf['cons'] = [p[:30] + '...' if len(p) > 33 else p for p in erdf['cons']]
> print(erdf.to_markdown())
>
