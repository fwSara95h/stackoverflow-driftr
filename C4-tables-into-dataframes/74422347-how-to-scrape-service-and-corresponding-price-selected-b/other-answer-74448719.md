---
title: "How to scrape service and corresponding price, selected by string?"
site: stackoverflow
question_id: 74422347
answer_id: 74448719
url: https://stackoverflow.com/a/74448719
author: "HedgeHog"
author_url: https://stackoverflow.com/users/14460824
posted: 2022-11-15T16:05:42Z
last_edited: 2022-11-15T16:51:24Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0dea239067c7be3aa7eb06afe579596729394c27b6d5feff30982e74f3a996cc
role: another answer on the same question, kept as context; not my work
---

# Answer by [HedgeHog](https://stackoverflow.com/users/14460824) — 2022-11-15

Posted on Stack Overflow, <https://stackoverflow.com/a/74448719>, 2022-11-15, last edited 2022-11-15. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Question could be improved by some details and expected result - However, to select a element by containing specific string you could go with:

    for e in soup.select('td:-soup-contains("Kompleksowe badanie")'):
        print(e.text,e.find_next_sibling('td').text)

*Note: `soup.find_all('td', text=strServiceVersion)` will only work if you have the exact matching string*

-----------------
Alternative would be to create a `dict` to filter: 

    {s.text:s.next_sibling.text for s in soup.select('td:has(+td.column-2)')}

and too deal with `|` prices:

    d = {}
    for k in soup.select('td:has(+td.column-2)'):
        v=k.next_sibling.text
        k=k.text
        if '|' in v:
            d.update(dict(zip([' '.join((k.split(':')[0], itm)) for itm in k.split(':')[-1].split(' | ')], v.split(' | '))))
        else:
            d.update({k:v})
    d

#### Example

    import requests
    from bs4 import BeautifulSoup
    
    headers = {'User-Agent':'Mozilla/5.0'}
    url = 'https://optimdent.pl/cennik/'
    
    soup = BeautifulSoup(requests.get(url, headers=headers).text)
       
    d = {}
    for k in soup.select('td:has(+td.column-2)'):
        v=k.next_sibling.text
        k=k.text
        if '|' in v:
            d.update(dict(zip([' '.join((k.split(':')[0], itm)) for itm in k.split(':')[-1].split(' | ')], v.split(' | '))))
        else:
            d.update({k:v})
    d

#### Output

A `dict` that could be filtered an manipulated:

    {'Kompleksowe badanie stomatologiczne jamy ustnej': '150',
     'Kompleksowe badanie stomatologiczne jamy ustnej poszerzone o badanie stawów skroniowo-żuchwowych': '250',
     'Konsultacja: endodontyczna | periodontologiczna | chirurgiczna | protetyczna | implantologiczna': '150',
     'Konsultacja ortodontyczna': '250',
     'Całkowite opracowanie i odbudowa ubytku zęba materiałem Estelite Asteria  małe': '330',
     'Całkowite opracowanie i odbudowa ubytku zęba materiałem Estelite Asteria średnie': '380',
     'Całkowite opracowanie i odbudowa ubytku zęba materiałem Estelite Asteria duże': '420',
     'Całkowite opracowanie i wysokoestetyczna odbudowa ubytku zęba materiałem Enamel HRI  małe': '370',
     'Całkowite opracowanie i wysokoestetyczna odbudowa ubytku zęba materiałem Enamel HRI średnie': '410',
     'Całkowite opracowanie i wysokoestetyczna odbudowa ubytku zęba materiałem Enamel HRI duże': '450',
     'Leczenie kanałowe zęba  1 kanałowego': '800',
     'Leczenie kanałowe zęba 2 kanałowego': '1000',
     'Leczenie kanałowe zęba 3 kanałowego': '1300',
     'Leczenie kanałowe zęba 4 kanałowego': '1450',...}
