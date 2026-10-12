# Code from my Stack Overflow answer https://stackoverflow.com/a/75010441 (posted 2023-01-04), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> name_element = soup.find('span', {'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
>

# --- block 2 ---
>     display_name = name_element.text
>

# --- block 3 ---
name_element = soup.select_one('div[data-testid="UserName"] span>span')

# --- block 4 ---
# name_element = soup.find('div', {'data-testid': 'UserName'}).span.span ## too many weak points
name_element = soup.find(lambda t: t.name == t.parent.name == 'span' and t.find_parent('div', {'data-testid': 'UserName'}))

# --- block 5 ---
# imports ## PASTE FROM https://pastebin.com/kEC9gPC8
# def linkToSoup_selenium... ## PASTE FROM https://pastebin.com/kEC9gPC8
# def selectForList... ## PASTE FROM https://pastebin.com/ZnZ7xM6u 

## JUST FOR REDUCING WHITESPACE - not important for extracting information ##
def miniStr(o): return ' '.join(w for w in str(o).split() if w)

profileUrls = ['https://twitter.com/twitterID', 'https://twitter.com/jokowi', 'https://twitter.com/sep_colin']

# ptSel = 'article[data-testid="tweet"]:has(div[data-testid="socialContext"])'
# ptuaSel = 'div[data-testid="User-Names"]>div>div>div>a'
selectors = {
    'og_url': ('meta[property="og\:url"][content]', 'content'),
    'name_span': 'div[data-testid="UserName"] span>span',
    'name_div': 'div[data-testid="UserName"]',
    # 'handle': 'div[data-testid="UserName"]>div>div>div+div',
    'description': 'div[data-testid="UserDescription"]',
    # 'location': 'span[data-testid="UserLocation"]>span',
    # 'url_href': ('a[data-testid="UserUrl"][href]', 'href'),
    # 'url_text': 'a[data-testid="UserUrl"]>span',
    # 'birthday': 'span[data-testid="UserBirthdate"]',
    # 'joined': 'span[data-testid="UserJoinDate"]>span',
    # 'following': 'div[data-testid="UserName"]~div>div>a[href$="\/following"]',
    # 'followers': 'div[data-testid="UserName"]~div>div>a[href$="\/followers"]',
    # 'pinnedTweet_uname': f'{ptSel} div[data-testid="User-Names"] span>span',
    # 'pinnedTweet_handl': f'{ptSel} {ptuaSel}:not([aria-label])',
    # 'pinnedTweet_pDate': (f'{ptSel} {ptuaSel}[aria-label]', 'aria-label'),
    # 'pinnedTweet_text': f'{ptSel} div[data-testid="tweetText"]',
}


def scrapeTwitterProfile(profileUrl, selRef=selectors):
    soup = linkToSoup_selenium(profileUrl, ecx=[
        'div[data-testid="UserDescription"]'  # wait for user description to load
        # 'article[data-testid="tweet"]'  # wait for tweets to load
    ], tmout=3, by_method='css', returnErr=True)
    if not isinstance(soup, str): return selectForList(soup, selRef)
    return {'Error': f'failed to scrape {profileUrl} - {soup}'}

# --- block 6 ---
tuDets = [scrapeTwitterProfile(url) for url in profileUrls]
for url, d in zip(profileUrls, tuDets):
    print('\nFrom', url)
    for k, v in d.items(): print(f'\t{k}: {miniStr(v)}')

# --- block 7 ---
# import snscrape.modules.twitter as sns_twitter
# def miniStr(o): return ' '.join(w for w in str(o).split() if w)

# profileIDs = [url.split('twitter.com/', 1)[-1].split('/')[0] for url in profileUrls]
profileIDs = ['twitterID', 'jokowi', 'sep_colin']
keysList = ['username', 'id', 'displayname', 'description', 'url']

for pid in profileIDs:
    tusRes, defVal = sns_twitter.TwitterUserScraper(pid).entity, 'no such attribute'
    print('\nfor ID', pid)
    for k in keysList: print('\t', k, ':', miniStr(getattr(tusRes, k, defVal)))

# --- block 8 ---
print('\n'.join(f'{a}: {miniStr(v)}' for a, v in [
    (n, getattr(tusRes, n)) for n in dir(tusRes)
] if not (a[:1] == '_' or callable(v))))
