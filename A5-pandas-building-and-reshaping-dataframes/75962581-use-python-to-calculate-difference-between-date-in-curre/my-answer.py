# Code from my Stack Overflow answer https://stackoverflow.com/a/75962918 (posted 2023-04-08), extracted verbatim; may need the question's context to run.
# df = pd.read_html('https://stackoverflow.com/questions/75962581')[0]
# df[['Online','Offline']] = df[['Online','Offline']].applymap(pd.to_datetime)

offline_days = df['Online'] - df['Offline'].shift(1)
df['Offline Days'] = offline_days.where(df['Kiosk']==df['Kiosk'].shift(1))
# df['Offline Days'] = offline_days.where(lambda td: td>pd.Timedelta(0))
