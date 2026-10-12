# Code from my Stack Overflow answer https://stackoverflow.com/a/75962227 (posted 2023-04-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def calculate_capital(row, from_df):
    if row.name==0: return row
    prev_row = from_df.loc[row.name-1]
    if row['TRADE'] != -1: # BUY order: set POSITION for buy order
        row['POSITION'] = row['CAPITAL']//row['<Open>']
        row['GAIN'] = 0
        row['GAIN_C'] = prev_row['GAIN_C']
    if row['TRADE'] == -1: # SELL order: recalculate Capital, gain, gain_c
        row['POSITION'] = 0
        row['DIFF'] = row['<Close>'] - prev_row['<Open>']            
        row['GAIN'] = row['DIFF'] * prev_row['POSITION']
        row['GAIN_C'] = prev_row['GAIN_C'] + row['GAIN']
        row['CAPITAL'] = prev_row['CAPITAL'] + row['GAIN']
    return row

# --- block 2 ---
df_trades = pd.DataFrame([l.split() for l in '''
  7.17   1.0  100000.00   13947.0      0.00      0.00   NaN
  7.20  -1.0  100418.41       0.0    418.41    418.41  0.03
  7.19   1.0  100418.41   13966.0      0.00    418.41   NaN
  8.96  -1.0  125138.23       0.0  24719.82  25138.23  1.77
  8.99   1.0  125138.23   13919.0      0.00  25138.23   NaN
'''.splitlines() if l.strip()], columns='''
  <Open> TRADE    CAPITAL  POSITION      GAIN    GAIN_C  DIFF
'''.split())
df_trades = df_trades.assign(**{'<Close>': 8})[[
    '<Open>','<Close>', 'TRADE','CAPITAL','POSITION', 'GAIN','GAIN_C','DIFF'
]].applymap(float)

# --- block 3 ---
def calculate_new_row(row):
    if row.name==0: return row
    if row['TRADE'] != -1: # BUY order: set POSITION for buy order
        row['POSITION'] = row['CAPITAL']//row['<Open>']
        row['GAIN'] = 0
        row['GAIN_C'] = row['GAIN_C_prev']
    if row['TRADE'] == -1: # SELL order: recalculate Capital, gain, gain_c
        row['POSITION'] = 0
        row['DIFF'] = row['<Close>'] - row['<Open>_prev']            
        row['GAIN'] = row['DIFF'] * row['POSITION_prev']
        row['GAIN_C'] = row['GAIN_C_prev'] + row['GAIN']
        row['CAPITAL'] = row['CAPITAL_prev'] + row['GAIN']
    return row

# --- block 4 ---
df_trades = df_trades.join(
    df_trades.shift(), rsuffix='_prev').apply(
        calculate_new_row, axis=1)[df_trades.columns]
