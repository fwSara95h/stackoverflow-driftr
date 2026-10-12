# Code from my Stack Overflow answer https://stackoverflow.com/a/74973195 (posted 2023-01-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas
# PASTE EVERYTHING FROM https://pastebin.com/trKxysh6

colHead = ['Important Questions', 'Answers', 'Why This Matters:']
pandas.DataFrame(getRows_fromPdfDoc(
    pDoc='045632_2023.pdf',  startSeq=' '.join(colHead), colHint=colHead, skipRows=1
)).drop(['col_0'], axis='columns').dropna(thresh=2, axis='rows').set_axis(colHead, axis='columns')

# --- block 2 ---
csSamps = [ 'Common Medical Event', 'Services You May Need', '$30 copayment', 
            'Non-Preferred: 40% coinsurance', 'Limitations, Exceptions, & Other']
headTxt = ' '.join(csSamps[:2] + ['What You Will Pay'] + csSamps[-1:])
rList = getRows_fromPdfDoc('045632_2023.pdf', headTxt, csSamps, 2)

# --- block 3 ---
prev_c1 = ''
for ri, r in enumerate(rList):
    if r['col_1']: prev_c1 = r['col_1']
    else: rList[ri]['col_1'] = prev_c1
