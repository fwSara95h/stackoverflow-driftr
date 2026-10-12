# Code from my Stack Overflow answer https://stackoverflow.com/a/75305011 (posted 2023-02-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>         span = soup.find('span', {'class': 'next-games-date'})
>         a_tags = span.findAll('a')
>

# --- block 2 ---
>     a_tags = span.findAll('a')
> AttributeError: 'NoneType' object has no attribute 'findAll'
>

# --- block 3 ---
if return_urls:
    a_cont = soup.find('div', {'class': 'tabs'})
    if a_cont is None: a_tags = [] # check for None to be safe
    else: a_tags =  a_cont.find_all('a', {'class':'h-8', 'href':True}) 
    urls = [
        'https://www.oddsportal.com'+a_tag['href'] for a_tag in a_tags
        if not a_tag['href'].startswith('#') # sections in current page 
        and 'active-item-calendar' not in a_tag['class'] # current page
    ]

# --- block 4 ---
if return_urls:
    a_sel = 'div.tabs a.h-8:not([href^="#"]):not(.active-item-calendar)'
    urls = ['https://www.oddsportal.com'+a['href'] 
            for a in soup.select(a_sel)]
