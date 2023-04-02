---
title: "Create dictionary through text file"
site: stackoverflow
question_id: 75914200
answer_id: 75914393
url: https://stackoverflow.com/a/75914393
author: "cards"
author_url: https://stackoverflow.com/users/16462878
posted: 2023-04-02T20:14:25Z
last_edited: 2023-04-02T20:19:53Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8a3b67011998112327f5bd22bb4b68e78115136033c49563884526e6531af815
role: another answer on the same question, kept as context; not my work
---

# Answer by [cards](https://stackoverflow.com/users/16462878) — 2023-04-02

Posted on Stack Overflow, <https://stackoverflow.com/a/75914393>, 2023-04-02, last edited 2023-04-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Use [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader). By giving the right data _delimiter_ you get back a iteraror of dictionaries... and if the 1st line are given the columns' name they will be the keys. 

```
# ########################################
# this is used just to mimic a file object
from io import StringIO

data = """Year,Country,Coach,Captain
1930,Uruguay,Alberto Suppici,Jose Nasazzi
1934,Italy,Vittorio Pozzo,Gianpiero Combi
1938,Italy,Vittorio Pozzo,Giuseppe Meazza
1950,Uruguay,Juan Lopez,Obdulio Varela
1954,Germany,Sepp Herberger,Fritz Walter
1958,Brazil,Vicente Feola,Hilderaldo Bellini
1962,Brazil,Aymore Moreira,Mauro Ramos
1966,England,Alf Ramsey,Bobby Moore
1970,Brazil,Mario Zagallo,Carlos Alberto
1974,Germany,Helmut Schon,Franz Beckenbauer
1978,Argentina,Cesar Luis Menotti,Daniel Passarella
1982,Italy,Enzo Bearzot,Dino Zoff
1986,Argentina,Carlos Bilardo,Diego Maradona
1990,Germany,Franz Beckenbauer,Lothar Matth�us
1994,Brazil,Carlos Alberto Parreira,Dunga
1998,France,Aime Jacquet,Didier Deschamps
2002,Brazil,Luiz Felipe Scolari,Cafu
2006,Italy,Marcello Lippi,Fabio Cannavaro
2010,Spain,Vicente del Bosque,Iker Casillas
2014,Germany,Joachim Low,Philipp Lahm"""

f = StringIO(data)
# ################

import csv
from collections import defaultdict


# main part
dd = defaultdict(dict)
r = csv.DictReader(f, delimiter=',')
for line in r:
    if line['Country'] in dd:
        dd[line['Country']]['Wins'] += 1
    else:
        dd[line['Country']]['Wins'] = 1

    dd[line['Country']].setdefault("Years", []).append(line['Year'])


# alphabetic order 
dd_ordered = {c: dd[c] for c in sorted(dd)}

# check output
print(*dd_ordered.items(), sep='\n')
```
