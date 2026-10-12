# Code from my Stack Overflow answer https://stackoverflow.com/a/74333634 (posted 2022-11-06), extracted verbatim; may need the question's context to run.
import pandas as pd
import re
url_link = 'https://www.taneps.go.tz/epps/viewAllAwardedContracts.do?d-3998960-p={}&selectedItem=viewAllAwardedContracts.do'
LIST = []
for number in range(1,5379):
  url = url_link.format(number)
  r = requests.get(url) # getting page -> html in r.text
  dframe = pandas.read_html(r.text, header=None)[0] 
  LIST.append(dframe)
Result_df = pd.concat(LIST)
Result_df.to_csv('Taneps_contracts.csv')
