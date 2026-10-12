# Code from my Stack Overflow answer https://stackoverflow.com/a/75283560 (posted 2023-01-30), extracted verbatim; may need the question's context to run.

# --- block 1 ---
container = soup.find_all('div', {'data-testid': 'component-agentCard'})

# --- block 2 ---
for con in soup.find_all('div', {'data-testid': 'component-agentCard'}):
    print({kk: t.get_text(' ').strip() if t else None for kk, t in [
        (k ,con.find('div', {'class':f'agent-{k}'})) for k in ['name', 'phone']
    ]})

# --- block 3 ---
> {'name': 'Christopher Marti', 'phone': '(830) 660-1004'}
> {'name': 'Matthew Guzman', 'phone': '(281) 650-0533'}
> {'name': 'Adam Olsen', 'phone': '(936) 689-9123'}
> {'name': 'Cyndi Kornegay', 'phone': '(713) 952-6767'}
> {'name': 'The Gayden Team Team', 'phone': '(832) 692-2000'}
> {'name': 'Christy Buck', 'phone': '(832) 264-8934'}
> {'name': 'Tammy Fruge', 'phone': '(281) 709-5124'}
> {'name': 'Todd Spencer', 'phone': '(512) 665-3747'}
> {'name': 'JOHN PRELL, Broker', 'phone': '(214) 696-4663'}
> {'name': 'Rene Sorola', 'phone': '(832) 816-4673'}
> {'name': 'Wendy Cline Team', 'phone': '(281) 858-3451'}
> {'name': 'Andrea Kitzmann', 'phone': '(979) 217-1722'}
> {'name': 'Tammie Bell', 'phone': '(979) 292-6163'}
> {'name': 'Mike Seder', 'phone': '(713) 806-6796'}
> {'name': 'Scott Laird Team', 'phone': '(281) 339-1800'}
> {'name': 'Cari Goeke Team', 'phone': '(979) 530-2714'}
> {'name': 'Travis Edmunds', 'phone': '(281) 363-2500'}
> {'name': 'Libby Mitchell Team', 'phone': '(409) 718-1933'}
> {'name': 'Robbie Jansky', 'phone': '(361) 293-8759'}
> {'name': 'Ronnie Matthews Team', 'phone': '(281) 440-7900'}
>
