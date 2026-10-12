# Code from my Stack Overflow answer https://stackoverflow.com/a/75564298 (posted 2023-02-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# from requests_html import HTMLSession
# from bs4 import BeautifulSoup

url='https://www.sec.gov/Archives/edgar/data/1801762/000149315221018835/form10-12g.htm'
resp = HTMLSession().get(url)
# print(resp.status_code, resp.reason, 'from', resp.url)
soup = BeautifulSoup(resp.content)

fieldLabel = '(Exact name of registrant as specified in its charter)'
try:
    fieldVal = soup.find(
        'p', string=lambda s: s and ' '.join(s.split())==fieldLabel
    ).find_previous(  'p', string=lambda s: s and s.strip()  ).string
except Exception as e:
    print('Error finding', fieldLabel, ':', repr(e))
    fieldVal = None
print(fieldVal)

# --- block 2 ---
> WESTERN
> MAGNESIUM CORPORATION
>
