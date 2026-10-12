# Code from my Stack Overflow answer https://stackoverflow.com/a/75121512 (posted 2023-01-14), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> r= requests.get(url, headers) 
>

# --- block 2 ---
> page = requests.get('https://www.google.com/search?q=RaindropsKeepFallinonMyHead+lyrcis&')
> soup = BeautifulSoup(page.content, 'html.parser').find_all('div',jsname="WbKHeb") 
> print(soup) 
>

# --- block 3 ---
title = 'Raindrops Keep Fallin on My Head'
url = f'https://www.google.com/search?q={title.replace(" ", "+")}+lyrics'
r = requests.get(url)
print('[', r.status_code, r.reason, 'from', r.url, f']\n{"-"*85}\n')
# r.raise_for_status()

lcSel = 'div:has(>span:has(>span):has(~span>span))~div div'
print(('\n\n'+'-'*80+'\n\n').join([el.get_text(' ').strip() + (
    f' ( {el.a.get("href")} )' if el.a else ''
) for el in [soup.select_one(s) for s in [
    f'{lcSel} span>div:has(a)', 
    f'{lcSel} span:has(>div a)+span', 
    f'{lcSel}:not(:has(span))'
]]]))
