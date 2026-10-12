# Code from my Stack Overflow answer https://stackoverflow.com/a/74334353 (posted 2022-11-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# link = 'http://agence-prd.ansm.sante.fr/php/ecodex/frames.php?specid=61350428&typedoc=R&ref=R0390743.htm' # your link
linkStart = '/'.join(link.split('/')[:-1])
refParam = link.split('?', 1)[-1].split('ref=',1)[-1].split('&')[0].split('.')[0]
link = f'{linkStart}/rcp/{refParam}.htm' # my link

req = requests.get(link)
soup = BeautifulSoup(req.content)
# rest of your code

# --- block 2 ---
pTexts = '\n'.join([p.text for p in soup.findAll('p')])
print(pTexts)
