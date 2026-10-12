# Code from my Stack Overflow answer https://stackoverflow.com/a/74214171 (posted 2022-10-26), extracted verbatim; may need the question's context to run.
r = requests.get('https://www.pakwheels.com/used-cars/suzuki-cultus-2018-for-sale-in-lahore-6596122')
if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')

    hlYear = soup.select_one('span.engine-icon.year + p > a')
    if hlYear is not None:
        print(hlYear.get_text(strip=True))
