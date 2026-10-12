# Code from my Stack Overflow answer https://stackoverflow.com/a/74498329 (posted 2022-11-19), extracted verbatim; may need the question's context to run.

# --- block 1 ---
#### FIRST PASTE [or DOWNLOAD&IMPORT] FUNCTION DEF from https://pastebin.com/kEC9gPC8 ####
soup = linkToSoup_selenium(
    'https://statusinvest.com.br/acoes/petr4', 
    clickFirst='//strong[@data-item="avg_F"]' # it actually just has to scroll, not click [but I haven't added an option for that yet], 
    ecx='//strong[@data-item="avg_F"][text()!="-"]' # waits till this loads
)
if soup is not None:
    print({
        t.find_previous_sibling().get_text(' ').strip(): t.get_text(' ').strip()
        for t in soup.select('div#payout-section span.title + strong.value')
    })

# --- block 2 ---
{'MÉDIA': '83,32%', 'ATUAL': '124,13% \n ( 48,97% acima da média )', 'MENOR\xa0VALOR': '26,35% \n ( 2019 )', 'MAIOR\xa0VALOR': '144,51% \n \n( 2020 )'}

# --- block 3 ---
soup.select_one('#payout-section[data-company][data-code]').attrs

# --- block 4 ---
{'id': 'payout-section', 'data-company': '408', 'data-code': 'petr4', 'data-category': '1'}

# --- block 5 ---
payout = soup.select_one('#payout-section[data-company][data-code]')
if payout:
    compId, dCode = payout.get('data-company'), payout.get('data-code')
    apiUrl = f'https://statusinvest.com.br/acao'
    apiUrl = f'{apiUrl}/payoutresult?code={dCode}&companyid={compId}&type=0'
