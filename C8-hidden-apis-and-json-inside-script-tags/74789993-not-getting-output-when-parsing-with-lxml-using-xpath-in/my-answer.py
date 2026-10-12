# Code from my Stack Overflow answer https://stackoverflow.com/a/74794006 (posted 2022-12-14), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> driver.find_element('xpath','//*[@id="1b7a3ab3-2765-4ee2-8367-c8a0e7230fa4"]/span').text
>

# --- block 2 ---
prize=driver.find_element("css selector", '*.ProductHero__content *.ProductPricing>span').text

# --- block 3 ---
xRef = {
    'www.ulta.com': '//*[@id="1b7a3ab3-2765-4ee2-8367-c8a0e7230fa4"]/span',
    'www.sephora.com': '//p[@data-comp="Price "]//span/b'
}

# for url in urls[:599]:... ################ REST OF CODE #############

# --- block 4 ---
# from urllib.parse import urlsplit

# lst, urls, xRef = ....


# for url in urls[:599]:
    # sleep...driver.get...sleep...
    try:
         uxrKey = urlsplit(url).netloc
         prize = driver.find_element('xpath', xRef[uxrKey]).text
    except:
        # pass # you'll just be repeating whatever you got in the previous loop for prize
        # [also, if this happens in the first loop, an error will be raised at lst.append([prize])]

        prize = None # 'MISSING' # '' #
################ REST OF CODE #############

# --- block 5 ---
price = soup.select('.ProductHero__content .ProductPricing>span') # for Ulta

# --- block 6 ---
price = soup.select('p[data-comp~="Price"] span>b') # for Sephora

# --- block 7 ---
# import json

############ LONGER  VERSION ##########
def getPrice_fromScript(scriptTag):
    try:
        s, sj = scriptTag.get_text(), json.loads(scriptTag.get_text())
        while s:
            sPair = s.split('"@type"', 1)[1].split(':', 1)[1].split(',', 1)
            t, s = sPair[0].strip(), sPair[1]
            try: 
                if t == '"Product"': return sj['offers']['price'] # Ulta
                elif t == '"Organization"': return sj['offers'][0]['price'] # Sephora
                # elif.... # can add more options
                # else.... # can add a default
            except: continue
    except: return None
#######################################

############ SHORTER VERSION ##########
def getPrice_fromScript(scriptTag):
    try:
        sj = json.loads(scriptTag.get_text())
        try: return sj['offers']['price'] # Ulta
        except: pass
        try: return sj['offers'][0]['price'] # Sephora
        except: pass 
        # try...except: pass # can try more options
    except: return None
#######################################

# --- block 8 ---
# from requests_html import HTMLSession # IF you use instead of requests

# def getPrice_fromScript....

for i in range(len(df)):
    response = requests.get(df['product_url'].iloc[i]) # takes too long [for me]
    # response = HTMLSession().get(df['product_url'].iloc[i]) # is faster [for me]

    ## error handing, just in case ##
    if response.status_code != 200:
        errorMsg = f'Failed to scrape [{response.status_code} {response.reason}] - '
        print(errorMsg, df['product_url'].iloc[i])
        continue # skip to next loop/url

    soup = BeautifulSoup(response.content, 'html.parser')

    pList = [p.strip() for p in [
        getPrice_fromScript(s) for s in soup.select('script[type="application/ld+json"]')[:5] # [1:2]
    ] if p and p.strip()]

    if pList: df['price'].iloc[i] = pList[0]
