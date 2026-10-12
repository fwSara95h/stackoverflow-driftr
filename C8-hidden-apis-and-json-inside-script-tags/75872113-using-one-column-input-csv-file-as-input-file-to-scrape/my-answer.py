# Code from my Stack Overflow answer https://stackoverflow.com/a/75894956 (posted 2023-03-31), extracted verbatim; may need the question's context to run.

# --- block 1 ---
searchUrls=set(pd.read_csv('input_file.csv', header=None)[0])

# --- block 2 ---
for url in searchUrls: await self.Parser(session, url)

# --- block 3 ---
# soup:=BeautifulSoup(await response.text(), "lxml"))
if not (pgProg:=soup.find('div', class_='row-label')): break
### print('Now extracting:', pgProg, 'from', searchUrl) ## [OPTIONAL]
# links = soup.select("div.has-padding-content-block-30.-zb")

# --- block 4 ---
# from urllib.parse import urljoin, urlsplit, parse_qsl

# --- block 5 ---
split_url = urlsplit(searchUrl)
params = dict(parse_qsl(split_url.query) # + [('page',f'{count}')])
snpUrl = urljoin(f'{split_url.scheme}://{split_url.netloc}', split_url.path)

# --- block 6 ---
params['page'] = count
async with session.get(snpUrl, params=params) as response:

# --- block 7 ---
async with session.get(f'{searchUrl}&page={count}') as response:
