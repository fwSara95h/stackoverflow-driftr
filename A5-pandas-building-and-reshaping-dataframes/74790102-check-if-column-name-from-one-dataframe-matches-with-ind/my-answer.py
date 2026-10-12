# Code from my Stack Overflow answer https://stackoverflow.com/a/74790801 (posted 2022-12-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import dateutil.parser
# from datetime import timedelta

def getProfit_atDelay(delayMins, startTime, profitDF):
    try: 
        startTime = dateutil.parser.parse(str(startTime))
        dTime = startTime - timedelta(minutes=int(str(delayMins)))
        return profitDF['Profit'].loc[dTime]
    except: return None

# --- block 2 ---
def profits_for_rates(ratesDF, profitDF):
    rStart, rMins = ratesDF.columns[1], ratesDF['Mins before time']
    return [getProfit_atDelay(t, rStart, profitDF) for t in rMins]

# --- block 3 ---
df_rates['New_column'] = profits_for_rates(df_rates, df_profit)

# --- block 4 ---
   Mins before time  2012-03-31 23:45:00  New_column
0                 0               113.10    3504.664
1                 5               112.10         NaN
2                10               113.10         NaN
3                15               113.17    1215.760
4                20               103.17         NaN
5                25               133.17         NaN
6                30               101.39     -21.480
