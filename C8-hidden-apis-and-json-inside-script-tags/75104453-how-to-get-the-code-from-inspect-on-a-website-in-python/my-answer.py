# Code from my Stack Overflow answer https://stackoverflow.com/a/75115221 (posted 2023-01-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# from urllib.parse import urlsplit, parse_qsl
apiUrl = 'https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery112309834864079678796_1673633495739&sortColumns=SECURITY_CODE%2CTRADE_DATE&sortTypes=1%2C-1&pageSize=50&pageNumber=1&reportName=RPT_DAILYBILLBOARD_DETAILSNEW&columns=SECURITY_CODE%2CSECUCODE%2CSECURITY_NAME_ABBR%2CTRADE_DATE%2CEXPLAIN%2CCLOSE_PRICE%2CCHANGE_RATE%2CBILLBOARD_NET_AMT%2CBILLBOARD_BUY_AMT%2CBILLBOARD_SELL_AMT%2CBILLBOARD_DEAL_AMT%2CACCUM_AMOUNT%2CDEAL_NET_RATIO%2CDEAL_AMOUNT_RATIO%2CTURNOVERRATE%2CFREE_MARKET_CAP%2CEXPLANATION%2CD1_CLOSE_ADJCHRATE%2CD2_CLOSE_ADJCHRATE%2CD5_CLOSE_ADJCHRATE%2CD10_CLOSE_ADJCHRATE%2CSECURITY_TYPE_CODE&source=WEB&client=WEB&filter=(TRADE_DATE%3C%3D%272023-01-13%27)(TRADE_DATE%3E%3D%272023-01-13%27)'
dict(parse_qsl(urlsplit(url).query))

# --- block 2 ---
{'callback': 'jQuery112309834864079678796_1673633495739',
 'sortColumns': 'SECURITY_CODE,TRADE_DATE',
 'sortTypes': '1,-1',
 'pageSize': '50',
 'pageNumber': '1',
 'reportName': 'RPT_DAILYBILLBOARD_DETAILSNEW',
 'columns': 'SECURITY_CODE,SECUCODE,SECURITY_NAME_ABBR,TRADE_DATE,EXPLAIN,CLOSE_PRICE,CHANGE_RATE,BILLBOARD_NET_AMT,BILLBOARD_BUY_AMT,BILLBOARD_SELL_AMT,BILLBOARD_DEAL_AMT,ACCUM_AMOUNT,DEAL_NET_RATIO,DEAL_AMOUNT_RATIO,TURNOVERRATE,FREE_MARKET_CAP,EXPLANATION,D1_CLOSE_ADJCHRATE,D2_CLOSE_ADJCHRATE,D5_CLOSE_ADJCHRATE,D10_CLOSE_ADJCHRATE,SECURITY_TYPE_CODE',
 'source': 'WEB',
 'client': 'WEB',
 'filter': "(TRADE_DATE<='2023-01-13')(TRADE_DATE>='2023-01-13')"}

# --- block 3 ---
start, end, pgSize, pgNum = '2023-01-13', '2023-01-13', 50, 1
auQstr = 'sortColumns=SECURITY_CODE%2CTRADE_DATE&sortTypes=1%2C-1'
auQstr += f'&pageSize={pgSize}&pageNumber={pgNum}' ## max pageSize seems to be 500
auQstr += '&reportName=RPT_DAILYBILLBOARD_DETAILSNEW&columns=SECURITY_CODE%2CSECUCODE%2CSECURITY_NAME_ABBR%2CTRADE_DATE%2CEXPLAIN%2CCLOSE_PRICE%2CCHANGE_RATE%2CBILLBOARD_NET_AMT%2CBILLBOARD_BUY_AMT%2CBILLBOARD_SELL_AMT%2CBILLBOARD_DEAL_AMT%2CACCUM_AMOUNT%2CDEAL_NET_RATIO%2CDEAL_AMOUNT_RATIO%2CTURNOVERRATE%2CFREE_MARKET_CAP%2CEXPLANATION%2CD1_CLOSE_ADJCHRATE%2CD2_CLOSE_ADJCHRATE%2CD5_CLOSE_ADJCHRATE%2CD10_CLOSE_ADJCHRATE%2CSECURITY_TYPE_CODE&source=WEB&client=WEB'
auQstr += f'&filter=(TRADE_DATE%3C%3D%27{end}%27)(TRADE_DATE%3E%3D%27{start}%27)'
apiUrl = f'https://datacenter-web.eastmoney.com/api/data/v1/get?{auQstr}'

# --- block 4 ---
# import requests, json, pandas

apiReq = requests.get(apiUrl)
# print(apiReq.status_code, apiReq.reason, 'from', apiReq.url)
# apiReq.raise_for_status()

jDict = {}
try: jDict = json.loads(apiReq.text.strip().strip('jQuery_(0123456789);'))
except: print('failed to extract JSON from', apiReq.text)
rDict =  jDict.get('result') if hasattr(jDict.get('result', {}), 'get') else {}
# for k, v in jDict.items(): print(f'{k}:', type(v) if hasattr(v, 'pop') else v)
# for k, v in rDict.items(): print(f'result_{k}:', type(v) if hasattr(v, 'pop') else v)
