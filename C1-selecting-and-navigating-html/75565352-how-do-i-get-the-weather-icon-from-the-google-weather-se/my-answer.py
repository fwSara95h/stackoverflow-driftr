# Code from my Stack Overflow answer https://stackoverflow.com/a/75567640 (posted 2023-02-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
dimg_id = 'dimg_1'
dimg_tag = soup.find('img', id=dimg_id)
print(dimg_tag)

dimg_script = soup.find('script', string=lambda s: s and "'dimg_1'" in s)
if dimg_script: 
    dimg_data = dimg_script.string.split("var s='",1)[-1].split("'",1)[0]

# --- block 2 ---
wi_src = soup.find('img', id='wob_tci', src=True)['src']
