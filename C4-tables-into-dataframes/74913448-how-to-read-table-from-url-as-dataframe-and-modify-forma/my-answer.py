# Code from my Stack Overflow answer https://stackoverflow.com/a/74915155 (posted 2022-12-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas
khdf = pandas.read_html('https://www.timeanddate.com/holidays/kenya/2022')[0]

# --- block 2 ---
khdf = khdf.set_axis(
    ['Date', 'Day', 'Name', 'Type'], axis='columns'
).dropna(axis='rows', how='all')

# --- block 3 ---
# from dateutil.parser import parse as duParse
y = 2022
khdf['Date'] = [duParse(f'{y} {d}').strftime('%d.%m.%Y') for d in khdf['Date']]

# --- block 4 ---
daysDict = {'Monday': 'Poniedziałek', 'Tuesday': 'Wtorek', 'Wednesday': 'Środa', 'Thursday': 'Czwartek', 'Friday': 'Piątek', 'Saturday': 'Sobota', 'Sunday': 'Niedziela'}
khdf['Day'] = [daysDict[d] if d in daysDict else d for d in khdf['Day']]

# --- block 5 ---
# !pip install googletrans==3.1.0a0
# from googletrans import Translator
translator = Translator()
for c in ['Day', 'Name', 'Type']:
    khdf[c] = [translator.translate(d, src='en', dest='pl').text for d in khdf[c]]

# --- block 6 ---
import pandas
from dateutil.parser import parse as duParse

daysDict = {'Monday': 'Poniedziałek', 'Tuesday': 'Wtorek', 'Wednesday': 'Środa', 'Thursday': 'Czwartek', 'Friday': 'Piątek', 'Saturday': 'Sobota', 'Sunday': 'Niedziela'}

def try_dup(dStr, yr):
    try: return duParse(f'{yr} {dStr}').strftime('%d.%m.%Y') 
    except: return None

# --- block 7 ---
startYear, endYear = 2010, 2030
countryList = ['kenya', 'tonga', 'belgium']

# --- block 8 ---
dfList = []
for country in countryList:
    for y in range(startYear, endYear+1):
        try: 
            cyUrl = f'https://www.timeanddate.com/holidays/{country}/{y}'
            cydf = pandas.read_html(cyUrl)[0]

            cydf = cydf.drop(# only the first 4 columns are kept
                [c for c in cydf.columns[4:]], axis='columns'
            ).set_axis(['Date', 'Day', 'Name', 'Type'], axis='columns')
            cydf['Date'] = [try_dup(d, y) for d in cydf['Date']] # parse+format date
            cydf['Country'] = country.capitalize() # add+fill a column with country name

            dfList.append(cydf.dropna(axis='rows', subset=['Date'])) # only add rows with Date
            # print('', end=f'\r{len(dfList[-1])} holidays scraped from {cyUrl}')
        # except: continue ## skip without printing error
        except Exception as e: 
            print('\n', type(e), e, '- failed to scrape from', cyUrl)
# print('\n\n', len(dfList), 'dataframes with', sum([len(d) for d in dfList]),'holidays scraped overall')

# --- block 9 ---
acydf = pandas.concat(dfList, ignore_index=True)
acydf['Day'] = [daysDict[d] if d in daysDict else d for d in acydf['Day']] # translate days
acydf = acydf[['Country', 'Date', 'Day', 'Name', 'Type']] # rearrange columns
