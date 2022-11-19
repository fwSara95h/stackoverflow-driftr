---
title: "Extract content from a page that renders it with javascript using Beautifulsoup"
site: stackoverflow
question_id: 74497235
answer_id: 74498302
url: https://stackoverflow.com/a/74498302
author: "Barry the Platipus"
author_url: https://stackoverflow.com/users/19475185
posted: 2022-11-19T07:41:35Z
last_edited: 2022-11-19T08:08:16Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d9bccc02fe5c28a3cee7c2466baddd8a50419124b84e8ae0d32c49a1ed030630
role: another answer on the same question, kept as context; not my work
---

# Answer by [Barry the Platipus](https://stackoverflow.com/users/19475185) — 2022-11-19

Posted on Stack Overflow, <https://stackoverflow.com/a/74498302>, 2022-11-19, last edited 2022-11-19. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Hoping that OP's next questions will contain a [minimal, reproducible example](https://stackoverflow.com/help/minimal-reproducible-example), here is one way of getting some data from that page using Requests and BeautifulSoup:

    from bs4 import BeautifulSoup as bs
    import requests
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
    }
    
    r = requests.get('https://statusinvest.com.br/acoes/petr4', headers=headers)
    soup = bs(r.text, 'html.parser')
    valor_atual = soup.select_one('h3:-soup-contains("Valor atual")').find_next('strong').text
    min_52_semanas = soup.select_one('h3:-soup-contains("Min. 52 semanas")').find_next('strong').text
    print('Valor atual:', valor_atual)
    print('Min. 52 semanas:', min_52_semanas)
    
    ### and now some values hydrated in page by Javascript, from an API endpoint:
    
    api_url = 'https://statusinvest.com.br/acao/payoutresult?code=petr4&companyid=408&type=0'
    api_headers = {
        'referer': 'https://statusinvest.com.br/acoes/petr4',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
    }
    r = requests.get(api_url, headers=api_headers)
    print(r.json())

Result in terminal:

    Valor atual: 26,54
    Min. 52 semanas: 15,85
    {'actual': 124.12623323305537, 'avg': 83.32096287339556, 'avgDifference': 48.97359434223362, 'minValue': 26.353309862919502, 'minValueRank': 2019, 'maxValue': 144.51093035368598, 'maxValueRank': 2020, 'actual_F': '124,13%', 'avg_F': '83,32%', 'avgDifference_F': '48,97% acima da média', 'minValue_F': '26,35%', 'minValueRank_F': '2019', 'maxValue_F': '144,51%', 'maxValueRank_F': '2020', 'chart': {'categoryUnique': True, 'category': ['2018', '2019', '2020', '2021', '2022'], 'series': {'percentual': [{'value': 27.189302754606462, 'value_F': '27,19%'}, {'value': 26.353309862919502, 'value_F': '26,35%'}, {'value': 144.51093035368598, 'value_F': '144,51%'}, {'value': 94.42503816271046, 'value_F': '94,43%'}, {'value': 124.12623323305537, 'value_F': '124,13%'}], 'proventos': [{'value': 7009130357.11, 'value_F': 'R$ 7.009.130.357,11', 'valueSmall_F': '7,01 B'}, {'value': 10577427979.68, 'value_F': 'R$ 10.577.427.979,68', 'valueSmall_F': '10,58 B'}, {'value': 10271836929.54, 'value_F': 'R$ 10.271.836.929,54', 'valueSmall_F': '10,27 B'}, {'value': 100721299707.4, 'value_F': 'R$ 100.721.299.707,40', 'valueSmall_F': '100,72 B'}, {'value': 179966901777.61, 'value_F': 'R$ 179.966.901.777,61', 'valueSmall_F': '179,97 B'}], 'lucroLiquido': [{'value': 25779000000.0, 'value_F': 'R$ 25.779.000.000,00', 'valueSmall_F': '25,78 B'}, {'value': 40137000000.0, 'value_F': 'R$ 40.137.000.000,00', 'valueSmall_F': '40,14 B'}, {'value': 7108000000.0, 'value_F': 'R$ 7.108.000.000,00', 'valueSmall_F': '7,11 B'}, {'value': 106668000000.0, 'value_F': 'R$ 106.668.000.000,00', 'valueSmall_F': '106,67 B'}, {'value': 144987000000.0, 'value_F': 'R$ 144.987.000.000,00', 'valueSmall_F': '144,99 B'}]}}}

BeautifulSoup documentation can be found here: https://beautiful-soup-4.readthedocs.io/en/latest/

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Álan Gabriel](https://stackoverflow.com/users/19396132)** (2022-11-19): I apologize, for being my first post here I got distracted and forgot to do the correct "formatting"
