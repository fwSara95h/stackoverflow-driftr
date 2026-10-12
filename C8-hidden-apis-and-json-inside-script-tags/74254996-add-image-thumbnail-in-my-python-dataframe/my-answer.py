# Code from my Stack Overflow answer https://stackoverflow.com/a/74270958 (posted 2022-11-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import json
image_url = json.loads(soup.select_one('script[type="application/ld+json"]').text)['image']

# --- block 2 ---
# import json

scCont = [s.text for s in soup.select('script[type="application/ld+json"]') if '"image"' in s.text]
if scCont:
    try:
        scCont = json.loads(scCont[0])
        if 'image' not in scCont: 
            image_url = None
            print('No image found for', i)
        else: image_url = scCont['image']
    except Exception as e: 
        image_url = None
        print('Could not parse movie info for', i, '\n', str(e))
else:
    image_url = None
    print('Could not find script with movie info for', i)

# --- block 3 ---
df_database_url['image_urls'] = images
