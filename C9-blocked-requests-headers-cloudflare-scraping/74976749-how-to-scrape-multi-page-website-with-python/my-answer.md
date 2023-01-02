---
title: "How to scrape multi page website with python?"
site: stackoverflow
question_id: 74976749
answer_id: 74979203
url: https://stackoverflow.com/a/74979203
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-02T05:24:30Z
last_edited: 2023-01-02T05:30:33Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74979203/revisions
accepted: false
score: 0
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1bb8fc94297971cf010de4f129061c8fedd66965fc9bed12cb51d62a926f9bbd
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74979203>, 2023-01-02, last edited 2023-01-02; score 0. Text as retrieved 2026-10-12.

The site uses [this API](https://haexpeditions.com/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=1084&target_action=get-all-data&default_sorting=old_first&ninja_table_public_nonce=2491a56a39&chunk_number=0) to [fetch the table data](https://i.sstatic.net/TC4R3.png), so you could request it from there.

<sub>(I used [`cloudscraper`](https://pypi.org/project/cloudscraper/) because it's easier than trying to figure out how to set the right set of [`requests` headers](https://requests.readthedocs.io/en/latest/user/quickstart/#custom-headers) to avoid getting a [406 error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/406) response; and using the `try..except...print` approach (instead of just doing *`tableData = [dict(...) for row in api_req.json()]`* directly) helps understand what went wrong in case of error [without actually raising any errors that might break the program execution.])</sub>

```python
# import cloudscraper
api_url = 'https://haexpeditions.com/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=1084&target_action=get-all-data&default_sorting=old_first&ninja_table_public_nonce=2491a56a39&chunk_number=0'
api_req = cloudscraper.create_scraper().get(api_url)

try: jData, jdMsg = api_req.json(), f'- {len(api_req.json())} rows from'
except Exception as e: jData, jdMsg = [], f'failed to get data - {e} \nfrom'
print(api_req.status_code, api_req.reason, jdMsg, api_req.url)

tableData = [dict([(k, v) for k, v in row['value'].items()] + [
    (f'{k}_options', v) for k, v in row['options'].items()
]) for row in jData]
```

At this point `tableData` is a [list of dictionaries](https://i.sstatic.net/yDuL7.png) but you can [build a DataFrame from it](https://i.sstatic.net/qIRpd.png) with [`pandas`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) and save it to a CSV file with [`.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html).

```python
# import pandas
pandas.DataFrame(tableData).set_index('number').to_csv('list_of_mount_everest_climbers.csv')
```

---

The API URL can be either copied from the [browser network logs](https://support.happyfox.com/kb/article/882-accessing-the-browser-console-and-network-logs/) or extracted from [the `script` tag containing it](https://i.sstatic.net/kZoaV.png) in the source HTML of the page.

The shorter way would be to just split the HTML string:

```python
# import cloudscraper
pg_url = 'https://haexpeditions.com/advice/list-of-mount-everest-climbers/'
pg_req = cloudscraper.create_scraper().get(pg_url)
api_url = pg_req.text.split('"data_request_url":"', 1)[-1].split('"')[0]
api_url = api_url.replace('\\', '')
print(pg_req.status_code,pg_req.reason,'from',pg_req.url,'\napi_url:',api_url)
```

However, it's a little risky in case `"data_request_url":"` appears in any other context in the HTML aside from the one that we want. So, another way would be to parse with [`bs4`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start) and [`json`](https://docs.python.org/3/library/json.html).

```python
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
```

(I would consider the second method more reliable even though it's a bit longer.)
