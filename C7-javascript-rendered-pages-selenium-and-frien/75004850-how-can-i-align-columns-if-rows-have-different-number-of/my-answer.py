# Code from my Stack Overflow answer https://stackoverflow.com/a/75014335 (posted 2023-01-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
labels = cssSelect(iiaEl, 'div.field span.label')

# --- block 2 ---
'labels': ', '.join([l.text.strip() for l in labels])

# --- block 3 ---
>     initiative_item = browser.find_elements(By.CSS_SELECTOR, "initivative-item")
>     initiatives = [item.text for item in initiative_item] 
>

# --- block 4 ---
def cssSelect(el, sel): return el.find_elements(By.CSS_SELECTOR, sel)
def getDetails_iiaRow(iiaEl):
    title = cssSelect(iiaEl, 'div.search-result-title')
    labels = cssSelect(iiaEl, 'div.field span.label')
    iiarDets = {
        'title': title[0].text.strip() if title else None,
        'labels': ', '.join([l.text.strip() for l in labels])
    }

    cvSel = 'div[translate]+div:last-child'
    for c in cssSelect(iiaEl, f'div:has(>{cvSel})'):
        colName = cssSelect(c, 'div[translate]')[0].text.strip()
        iiarDets[colName] = cssSelect(c, cvSel)[0].text.strip()

    link = iiaEl.get_attribute('href')
    if link[:1] == '/':
        link = f'https://ec.europa.eu/{link}'
    iiarDets['link'] = iiaEl.get_attribute('href')

    return iiarDets

# --- block 5 ---
initiative_list = []
for i in range(0, 2):
    url = f'https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives_de?page={i}'
    browser.get(url)
    time.sleep(random.randint(5, 10))
    initiative_list += [
        getDetails_iiaRow(iia) for iia in
        cssSelect(browser, 'initivative-item>article>a ')
    ]

# --- block 6 ---
pd.DataFrame(initiative_list).to_csv('Initiativen.csv', index=False)
