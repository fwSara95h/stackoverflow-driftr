# Code from my Stack Overflow answer https://stackoverflow.com/a/74187673 (posted 2022-10-24), extracted verbatim; may need the question's context to run.

# --- block 1 ---
soup = BeautifulSoup(response.content, "html.parser")

# --- block 2 ---
scrapingant_api = 'https://api.scrapingant.com/v2/general'
scrapingant_key = 'YOUR_API_TOKEN' # paste here
url_to_Scrape = 'https://www.idealista.com/inmueble/97795476/'
url = f'{scrapingant_api}?url={url_to_Scrape}&x-api-key={scrapingant_key}'
r = requests.get(url)

soup = BeautifulSoup(r.text)
inm = soup.find(class_="main-info__title-main").text
print(inm) # prints "Ático en venta en plaza del Ayuntamiento, 6"

# --- block 3 ---
# def linkToSoup_selenium .... # paste function into your code

soup = linkToSoup_selenium('https://www.idealista.com/inmueble/97795476/')
inm = soup.find(class_="main-info__title-main").text
print(inm) # prints "Ático en venta en plaza del Ayuntamiento, 6"
