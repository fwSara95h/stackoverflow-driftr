# Code from my Stack Overflow answer https://stackoverflow.com/a/75123779 (posted 2023-01-15), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def get_sku(source_product_url):
 print("bdr.sandbox")
 generated_on = datetime.datetime.now()
 print(generated_on) 
 url_data = get_url_data_from_url_request(url=source_product_url)
 soup = BeautifulSoup(url_data, "lxml")
 id_element = soup.find('span', {"itemprop": "sku"}).text
 print(id_element)
 return id_element

# --- block 2 ---
def try_get_sku(srcProdUrl):
 try: return {'source_product_url': srcProdUrl, 'sku': get_sku(srcProdUrl)}
 except Exception as e:
  errorMsg = f'{type(e)} {e}'
  print(f'failed to scrape {srcProdUrl} \n ', errorMsg)
  return {'source_product_url': srcProdUrl, 'errorMsg': errorMsg}

# --- block 3 ---
def main():
 spUrls = [
  'https://www.6pm.com/p/easy-spirit-epic-gray/product/9450972/color/11',
  ## ADD ALL URLS TO SCRAPE ##
 ]
 productsInfo = [try_get_sku(spUrls) for url in spUrls]
 # do something with productsInfo if you want to, like
 # pandas.DataFrame(productsInfo).to_csv('productsInfo.csv') # saves in csv file [import pandas]
