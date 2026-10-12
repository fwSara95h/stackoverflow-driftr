# Code from my Stack Overflow answer https://stackoverflow.com/a/74979203 (posted 2023-01-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import cloudscraper
api_url = 'https://haexpeditions.com/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=1084&target_action=get-all-data&default_sorting=old_first&ninja_table_public_nonce=2491a56a39&chunk_number=0'
api_req = cloudscraper.create_scraper().get(api_url)

try: jData, jdMsg = api_req.json(), f'- {len(api_req.json())} rows from'
except Exception as e: jData, jdMsg = [], f'failed to get data - {e} \nfrom'
print(api_req.status_code, api_req.reason, jdMsg, api_req.url)

tableData = [dict([(k, v) for k, v in row['value'].items()] + [
    (f'{k}_options', v) for k, v in row['options'].items()
]) for row in jData]

# --- block 2 ---
# import pandas
pandas.DataFrame(tableData).set_index('number').to_csv('list_of_mount_everest_climbers.csv')

# --- block 3 ---
# import cloudscraper
pg_url = 'https://haexpeditions.com/advice/list-of-mount-everest-climbers/'
pg_req = cloudscraper.create_scraper().get(pg_url)
api_url = pg_req.text.split('"data_request_url":"', 1)[-1].split('"')[0]
api_url = api_url.replace('\\', '')
print(pg_req.status_code,pg_req.reason,'from',pg_req.url,'\napi_url:',api_url)

# --- block 4 ---
# import cloudscraper
# from bs4 import BeautifulSoup
# import json

pg_url = 'https://haexpeditions.com/advice/list-of-mount-everest-climbers/'
sel = 'div.footer.footer-inverse>div.bottom-bar+script[type="text/javascript"]'
api_url = 'https://haexpeditions.com/wp-admin/admin-ajax.php...' ## will be updated

pg_req = cloudscraper.create_scraper().get(pg_url)
jScript = BeautifulSoup(pg_req.content).select_one(sel) 
try:
    sjData = json.loads(jScript.get_text().split('=',1)[-1].strip())
    api_url = sjData['init_config']['data_request_url']
    auMsg = f'\napi_url: {api_url}'
except Exception as e: auMsg = f'failed to extract API URL - {type(e)} {e}'
print(pg_req.status_code,pg_req.reason,'from',pg_req.url,'\napi_url:',auMsg)
