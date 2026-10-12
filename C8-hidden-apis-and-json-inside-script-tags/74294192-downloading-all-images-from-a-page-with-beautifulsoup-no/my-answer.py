# Code from my Stack Overflow answer https://stackoverflow.com/a/74332271 (posted 2022-11-05), extracted verbatim; may need the question's context to run.
api_url = 'https://apis-edge-prod.tech.tvnz.co.nz/api/v1/web/play/page/categories/sci-fi-and-fantasy'
r = requests.get(api_url)
try:
    embVals = r.json()['_embedded'].values() 
except Exception as e:
    embVals = []
    print('failed to get embedded items\n', str(e))

urls = [img for images in [ [
    v['src'] for k, v in ev.items() if 
    k is not None and 'image' in k.lower() 
    and v is not None and 'src' in v
] for ev in embVals] for img in images]

# for url in urls: # should work the same
