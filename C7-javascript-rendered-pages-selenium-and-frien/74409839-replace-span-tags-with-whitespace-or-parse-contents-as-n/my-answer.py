# Code from my Stack Overflow answer https://stackoverflow.com/a/74410700 (posted 2022-11-12), extracted verbatim; may need the question's context to run.

# --- block 1 ---
table = pd.read_html(driver.page_source)[0] # , flavor='lxml')[0] # default

# --- block 2 ---
table = pd.read_html(driver.page_source.replace('</', '&nbsp;</'))

# --- block 3 ---
tableSoup = soup.find('table')
tableHeaders = [
    h.get_text(' ', strip=True)
    for h in tableSoup.select('thead tr th')
]
tableData = [{h: c.get_text(' ', strip=True) for h, c in zip(
    tableHeaders, [cell for cell in r.select('td')]
)} for r in tableSoup.select('tbody tr')]
table = pd.DataFrame(tableData)
