# Code from my Stack Overflow answer https://stackoverflow.com/a/75852976 (posted 2023-03-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
import request
import pandas as pd

cur_tab = 'JPY' # 'MostViewed' # 'USD' # 'EUR' #
api_endpt = f'https://markets.businessinsider.com/ajax/ExchangeRate_PopularListData' 
api_data = requests.get(f'{api_endpt}?currency={cur_tab}').json()
df = pd.DataFrame(api_data['ExchangeRates'])

# --- block 2 ---
import request
import pandas as pd

cur_tabs = ['MostViewed', 'USD', 'EUR', 'JPY']
api_endpt = 'https://markets.businessinsider.com/ajax/ExchangeRate_PopularListData'

dfList = [pd.DataFrame(
    requests.get(f'{api_endpt}?currency={cur_tab}').json()['ExchangeRates']
) for cur_tab in cur_tabs] 
df = pd.concat(dfList, keys=cur_tabs)
