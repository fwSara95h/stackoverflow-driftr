# Code from my Stack Overflow answer https://stackoverflow.com/a/75280477 (posted 2023-01-30), extracted verbatim; may need the question's context to run.
# from urllib.parse import urljoin # [ if you use it ]

rootUrl = 'https://crmhelpcenter.gitbook.io'
nxtUrl = f'{rootUrl}/wahi-digital/getting-started/readme'
nextUrls = [nxtUrl]
# allUrls = [nxtUrl] # [ if you want to collect ]
while nxtUrl:
    resp = requests.get(nxtUrl)
    print([len(nextUrls)], resp.status_code, resp.reason, 'from', resp.url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    ### EXTRACT ANY PAGE DATA YOU WANT TO COLLECT ###
    # pgUrl = {urljoin(nxtUrl, a["href"]) for a in soup.select('a[href]')}
    # allUrls += [l for l in pgUrl if l not in allUrls]

    aNxt = [a for a in soup.find_all(
        'a', {'href': True, 'data-rnwi-handle': 'BaseCard'}
    ) if list(a.stripped_strings)[:1]==['Next']]

    # nxtUrl = urljoin(nxtUrl, aNxt[0]["href"]) if aNxt else None
    nxtUrl = f'{rootUrl}{aNxt[0]["href"]}' if aNxt else None
    nextUrls.append(nxtUrl) # the last item will [most likely] be None
# if nxtUrl is None: nextUrls = nextUrls[:-1] # remove last item if None
