# Code from my Stack Overflow answer https://stackoverflow.com/a/73874480 (posted 2022-09-27), extracted verbatim; may need the question's context to run.
#from selenium import webdriver

def linkSoup(l):  
    # I downloaded and saved 'chromedriver.exe' to the same folder as this .py file
    driverD = webdriver.Chrome('chromedriver.exe')
    driverD.get(l)
    lSoup = BeautifulSoup(driverD.page_source, 'html.parser')
    driverD.close()
    del driverD
    return lSoup 


soup = linkSoup('https://inmotion.dhl/en/formula-1/fastest-pit-stop-award')

table = soup.find("table", class_="f1-award-table")
table_body = table.find('tbody')

rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    print(cols)
