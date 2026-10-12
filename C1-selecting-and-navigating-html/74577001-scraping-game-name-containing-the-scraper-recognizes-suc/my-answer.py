# Code from my Stack Overflow answer https://stackoverflow.com/a/74587510 (posted 2022-11-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def deCFEmail(encTag):
    if not (encTag.get('data-cfemail') or encTag.select('*[data-cfemail]')):
        encTag.append(f'[! no "data-cfemail" attribute !]')
    else:
        fp = encTag.get('data-cfemail', None)
        if fp is None:
            fp = encTag.select_one('*[data-cfemail]').get('data-cfemail')
        try:
            r = int(fp[:2],16)
            encTag.string = ''.join([chr(int(fp[i:i+2], 16) ^ r) for i in range(2, len(fp), 2)]) 
        except Exception as e:
            encTag.append(f'! failed to decode "{e}"')
    return encTag

# --- block 2 ---
for i, h in enumerate(header): 
    if h.get_text()=='[email\xa0protected]': 
        header[i] = deCFEmail(h)

# --- block 3 ---
[<a href="https://www.mobygames.com/game/amperst">Ampers@t</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/amperst/forums">Discuss</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/sheet/review_game/amperst/">Review</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/amperst/add-to-want-list">+ Want</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/amperst/add-to-have-list">+ Have</a>,
 <a class="btn btn-xs btn-mobysuccess" href="https://www.mobygames.com/game/amperst/contribute">Contribute</a>]
