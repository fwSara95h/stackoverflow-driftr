# Code from my Stack Overflow answer https://stackoverflow.com/a/75123132 (posted 2023-01-15), extracted verbatim; may need the question's context to run.
kre = requests.get('http://pitzavod.ru/products/upakovka/')
# print(kre.status_code, kre.reason, 'from', kre.url)
kre.raise_for_status()
soup = BeautifulSoup(kre.content, 'lxml')

# table = soup.select_one('div#tab4>div.table-responsive>table')
table = soup.find('table') # soup.select_one('table')
tData = [{
    1 if 'center' in c.get('style', '') else ci: '\n'.join([
        l.strip() for l in c.get_text('\n').splitlines() if l.strip()
    ]) for ci, c in enumerate(r.select('td'))
} for r in table.select('tr')]
df = pandas.DataFrame(tData)

## combine the top 2 rows to form header ##
df.columns = ['\n'.join([
    f'{d}' for d in df[c][:2] if pandas.notna(d)
]) for c in df.columns]
df = df.drop([0,1], axis='rows').reset_index(drop=True)

# print(df.to_markdown(tablefmt="fancy_grid"))
