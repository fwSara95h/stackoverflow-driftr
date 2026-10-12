# Code from my Stack Overflow answer https://stackoverflow.com/a/74601446 (posted 2022-11-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
cr = [(k, v) for k, v in zip(category, rating)]
si = [i for i, (k, v) in  enumerate(cr) if k == 'Type Of Traveller']
si = [(i - 1) if i != 0 and cr[i - 1][0] == 'Aircraft' else i for i in si]
splitCr = [dict(cr[start:end]) for start, end in zip(si, (si[1:] + [len(cr)]))]

# --- block 2 ---
base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 3 # 5 # 10
page_size = 5 # 1 # 100

revList = []
avgSelRef = {
    'rating10': '.rating-10 span[itemprop="ratingValue"]',
    'header': 'div.info:has(h1[itemprop="name"])',
    'subheader': '.review-count',
    'reviewBody': '.skytrax-rating-mob img.skytrax-rating[alt]'
}
rbSel = '.body[id^="anchor"]'
revSelRef = {
    'rating10': '.rating-10 span[itemprop="ratingValue"]',
    'header': f'{rbSel} h2.text_header',
    'subheader': f'{rbSel} h3.text_sub_header',
    'reviewBody': f'{rbSel} div[itemprop="reviewBody"]'
} 

avgAdded = False
for i in range(1, pages + 1): 
    print("", end=f"Scraping page {i} of {pages} ")

    # Create URL to collect links from paginated data
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Collect HTML data from this page
    response = requests.get(url)
    if response.status_code != 200: 
        print(f' -- !ERROR: "{response.raise_for_status()}"" getting {url}')
        continue
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')

    avSoups = parsed_content.select('div.review-info')
    rvSoups = parsed_content.select(f'article[itemprop="review"]:has({rbSel})')
    if avSoups and not avgAdded: rvSoups += avSoups
    for r in rvSoups:
        isAvg = r.name == 'div'
        if isAvg:
            rDets = {'reviewId': '[Average]'} 
            selRef = avgSelRef.items()
            avgAdded = True
        else:
            revId = r.select_one(rbSel).get('id').replace('anchor', '', 1)
            selRef = revSelRef.items()
            rDets = {'reviewId': revId} 

        for k, s in selRef:
            rdt = r.select_one(s) 
            if rdt is None: continue
            if 'img' in s and s.endswith('[alt]'):
                rDets[k] = rdt.get('alt') 
            else:
                rDets[k] = ' '.join(w for w in rdt.get_text(' ').split() if w)

        rhSel = 'td.review-rating-header'
        rRows = r.select(f'tr:has({rhSel} + td:is(.stars, .review-value))')
        for rr in rRows: 
            k = rr.select_one(rhSel).get_text(' ').strip()
            k = k.replace(' For ', ' for ').replace(' & ', ' + ') # bit of cleanup
            if k.endswith('Staff Service'): k = 'Staff Service' # bit of cleanup
            if rr.select('td.stars'): 
                rDets[f'[stars] {k}'] = len(rr.select('td.stars span.star.fill'))
            else: 
                rDets[k] = rr.select_one('td.review-value').get_text().strip()

        revList = ([rDets] + revList) if isAvg else (revList + [rDets])
    print(' - ', len(rvSoups), 'reviews --->', len(revList), 'total reviews')
