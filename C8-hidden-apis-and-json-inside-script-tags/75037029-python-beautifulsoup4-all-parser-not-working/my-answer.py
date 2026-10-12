# Code from my Stack Overflow answer https://stackoverflow.com/a/75038864 (posted 2023-01-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
scriptTag = soup.select_one('meta[name="aplus-auto-exp"]~script')

# --- block 2 ---
jScript = scriptTag.prettify().strip()
jScript = jScript.strip('<script').split('>', 1)[-1].strip('</script>').strip()

# --- block 3 ---
itemList = findObj_inJS(jScript, '"itemList"')['content']

# --- block 4 ---
def reduceProductInfo(origInf): 
    try: prodId = origInf['productId']
    except: return {'errorMsg': 'productId expected', 'orig': origInf}
    pDets = {
        'id': prodId, 'link': f'https://www.aliexpress.com/item/{prodId}.html'
    }
    try: pDets['title'] = origInf["title"]["displayTitle"]
    except Exception as e: pDets['title'] = f'!{type(e)} - {e}!'
    try: pDets['salePrice'] = origInf["prices"]["salePrice"]["formattedPrice"]
    except Exception as e: pDets['salePrice'] = f'!{type(e)} - {e}!'
    try: pDets['imageLink'] = origInf["image"]["imgUrl"]
    except Exception as e: pDets['imageLink'] = f'!{type(e)} - {e}!'
    if pDets['imageLink'][:2] == '//': 
        pDets['imageLink'] = f"https:{pDets['imageLink']}"
    return pDets

# --- block 5 ---
productList = [reduceProductInfo(item) for item in itemList]
