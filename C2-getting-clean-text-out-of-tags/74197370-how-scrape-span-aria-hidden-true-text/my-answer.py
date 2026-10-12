# Code from my Stack Overflow answer https://stackoverflow.com/a/74198014 (posted 2022-10-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
spanTxt1 = soup.select_one('span.t-14.t-normal span[aria-hidden="true"]')
if spanTxt1 is not None: spanTxt1 = spanTxt1.get_text(strip=True)

spanTxt2 = soup.select_one('span.t-14.t-normal span.visually-hidden')
if spanTxt2 is not None: spanTxt2 = spanTxt2.get_text(strip=True)

print(f' Text1: "{spanTxt1}" \n Text2: "{spanTxt2}" ')

# --- block 2 ---
expSel = 'div#experience ~ div.pvs-list__outer-container ul.pvs-list li'

# --- block 3 ---
c1span =  soup.select_one(expSel+' span.t-14.t-normal span')
if c1span is not None:
    print(c1span.get_text(strip=True))

# --- block 4 ---
expSelRef = {
    'Position': 'span.mr1.t-bold',  
    'Company+Type': 'span.t-14.t-normal',
    'Dates': 'span.t-14.t-normal.t-black--light', 
    'Location': 'span.t-14.t-normal.t-black--light + span'
}
for e in soup.select(expSel):
    for r in expSelRef:
        eDet = e.select_one(expSelRef[r]+' span[aria-hidden="true"]')
        if eDet is not None: 
            print(f' [ {r}: "{eDet.get_text(strip=True)}" ] ', end='')
    print()
