# Code from my Stack Overflow answer https://stackoverflow.com/a/74818698 (posted 2022-12-15), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# teams = soup.find_all('a', class_= 'tnmscn')
rows = soup.find_all('div', {'class': 'rcnt'})
# for team in teams:
for r in rows:
    hometeam = r.find('span',class_= 'homeTeam').text
    #### AND SO ON ####

# --- block 2 ---
>     location = team.find('name address', 'content').text
>

# --- block 3 ---
>     predictedscore = team.select_one('div', class_='ex_sc tabonly')
>

# --- block 4 ---
# def selectForList.... # PASTE FROM https://pastebin.com/ZnZ7xM6u

rData = [selectForList(r, [
  'span.homeTeam', 'span.awayTeam', # home/away teams
  'span.forepr', 'div.ex_sc.tabonly', # pred/correct scores
  'span.date_bah', # date [location below]
  ('span[itemprop="location"]>meta[itemprop="name address"][content]', 'content'), 
  'div.prwth.tabonly>span.wnums', # temperature
]) for r in soup.select('div.rcnt')]

# --- block 5 ---
for r in rData: 
    print(f'# {r[0]} vs {r[1]}: {r[3] if r[3] else "score_unknown"}', 
          f'[pred: {r[2]}] on {r[4]} (at {r[5]})', 
          f'[{("temp: "+r[6]) if r[6] else "no_weather_data"}]')

### PRINTED OUTPUT BELOW ###

# Argentina vs France: 2 - 2 [pred: X] on 18/12/2022 16:00 (at Lusail Iconic Stadium) [temp: 21°]
# Croatia vs Morocco: 0 - 0 [pred: X] on 17/12/2022 16:00 (at Khalifa International Stadium) [temp: 22°]
# Argentina vs Croatia: 1 - 1 [pred: X] on 13/12/2022 20:00 (at Lusail Iconic Stadium) [temp: 22°]
# France vs Morocco: 3 - 1 [pred: 1] on 14/12/2022 20:00 (at Al Bayt Stadium) [temp: 22°]
# Juventus W vs Zurich (W): score_unknown [pred: 1] on 15/12/2022 18:45 (at Allianz Stadium) [no_weather_data]
# SL Benfica (W) vs Barcelona (W): score_unknown [pred: 2] on 15/12/2022 21:00 (at Caixa Futebol Campus) [no_weather_data]

# --- block 6 ---
selRef = {'home_team': 'span.homeTeam', 'away_team': 'span.awayTeam', 'pred-y_n': ('div[class^="predict"]:has(>span.forepr)', 'class'), 'pred': 'span.forepr', 'correct_score': 'div.ex_sc.tabonly', 'date': 'span.date_bah', 'location': ('span[itemprop="location"]>meta[itemprop="name address"][content]', 'content'), 'temperature': 'div.prwth.tabonly>span.wnums', 'weather_icon': ('div.prwth.tabonly>img.wthc[src]', 'src')}

rdList = [dict(zip(
    selRef.keys(), selectForList(r, selRef.values()) #, printList=' ')
)) for r in soup.select('div.rcnt')]

# --- block 7 ---
wiRef = {'w-32': 'sunny', 'w-31': 'clear', 'w-30':'cloudy-day', 'w-29':'cloudy-night', 'w-20': 'fog', 'w-12': 'rainy-day', 'w-11': 'rainy-night'}

for ri, w in ([(i, r['weather_icon']) for i, r in enumerate(rdList) if r['weather_icon']]):
    rdList[ri]['weather_icon'] = f'https://www.forebet.com{w}' # replace with full link
    w = w.split('/')[-1].split('.png')[0].strip()
    rdList[ri]['weather'] = wiRef[w] if w in wiRef else f'{w}.png'

# import pandas
pandas.DataFrame(rdList).to_csv('wcPreds.csv', index=False)
