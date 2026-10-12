# Code from my Stack Overflow answer https://stackoverflow.com/a/74334463 (posted 2022-11-06), extracted verbatim; may need the question's context to run.
# import urllib.parse

url = "https://www.taneps.go.tz/epps/viewAllAwardedContracts.do?d-3998960-p=1&selectedItem=viewAllAwardedContracts.do&T01_ps=100"

session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

i = 0 
while url:
    html = session.get(url).content
    soup = BeautifulSoup(html, "html.parser")

    #######  EXTRACT AND SAVE THE DATA YOU WANT  #######

    nxtBtn = soup.select_one('button.SearchBtn[title="Next"][href]')
    if nxtBtn:
        url = urllib.parse.urljoin(url, nxtBtn.get('href'))
        print('going to next page', url)
    else: url = None
