---
title: "Create dictionary through text file"
site: stackoverflow
question_id: 75914200
answer_id: 75914432
url: https://stackoverflow.com/a/75914432
author: "Milly Stack"
author_url: https://stackoverflow.com/users/17755651
posted: 2023-04-02T20:23:15Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f5ebc0988f4e0943e12c568aaf12496eb7d25792633233d7e7b781a67b6d7f54
role: another answer on the same question, kept as context; not my work
---

# Answer by [Milly Stack](https://stackoverflow.com/users/17755651) — 2023-04-02

Posted on Stack Overflow, <https://stackoverflow.com/a/75914432>, 2023-04-02; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

If you don't want to format the table by yourself, it's best to use one of the many python libraries available. Also, the best approach is maybe to use the `pandas` library which allows you to easily sort the data and group it by country. 

If you're not looking to use any libraries, the solution below should help you. It creates a dictionary to save the country details which is then used to format the table at the end using a loop. You might want to update the formatting of the table.



```python
from collections import defaultdict
def main():
    inFile = [
        "Year,Country,Coach,Captain",
        "1930,Uruguay,Alberto Suppici,Jose Nasazzi",
        "1934,Italy,Vittorio Pozzo,Gianpiero Combi",
        "1938,Italy,Vittorio Pozzo,Giuseppe Meazza",
        "1950,Uruguay,Juan Lopez,Obdulio Varela",
        "1954,Germany,Sepp Herberger,Fritz Walter",
        "1958,Brazil,Vicente Feola,Hilderaldo Bellini",
        "1962,Brazil,Aymore Moreira,Mauro Ramos",
        "1966,England,Alf Ramsey,Bobby Moore",
        "1970,Brazil,Mario Zagallo,Carlos Alberto",
        "1974,Germany,Helmut Schon,Franz Beckenbauer",
        "1978,Argentina,Cesar Luis Menotti,Daniel Passarella",
        "1982,Italy,Enzo Bearzot,Dino Zoff",
        "1986,Argentina,Carlos Bilardo,Diego Maradona",
        "1990,Germany,Franz Beckenbauer,Lothar Matthus",
        "1994,Brazil,Carlos Alberto Parreira,Dunga",
        "1998,France,Aime Jacquet,Didier Deschamps",
        "2002,Brazil,Luiz Felipe Scolari,Cafu",
        "2006,Italy,Marcello Lippi,Fabio Cannavaro",
        "2010,Spain,Vicente del Bosque,Iker Casillas",
        "2014,Germany,Joachim Low,Philipp Lahm"
    ]
    champions = createDict(inFile)
    printChamps(champions)
    

def createDict(file):
    winners = defaultdict(str)
    try:
        for line in file:
            year, country, coach, captain = (line.strip()).split(",")
            if(year == "Year"): ## ignoring the first line
                continue
            if(winners.get(country) is None): 
                winners[country] = {
                    'wins': 1,
                    'years': [year],
                    'captains': [captain],
                    'coaches': [coach]
                }
            else: 
                winners[country]['wins'] += 1
                winners[country]['years'].append(year)
                winners[country]['coaches'].append(coach)
                winners[country]['captains'].append(captain)
        return (winners)
    except Exception as e:
        print(e)    

def printChamps(unsorted_dict):
    print("-------------------------------------------------------------------------|")
    print(f"{'Country':10} | {'Wins':5} | {'Year':5} | {'Captain':20} | {'Coach':20} |")
    print("-------------------------------------------------------------------------|")
    sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda x: x[1]['wins'], reverse=True))
    for key in sorted_dict:
        print ("%-10s | %5i | %-5s | %-20s | %-20s |" % (key, sorted_dict[key]['wins'], ", ".join(sorted_dict[key]['years']), ", ".join(sorted_dict[key]['captains']), ", ".join(sorted_dict[key]['coaches'])))
        print("-------------------------------------------------------------------------|")
    print("-------------------------------------------------------------------------|")
if __name__ == '__main__':
    main()
```


Output
```
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Country    | Wins  | Year                         | Captain                                                       | Coach                                                                                      |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Brazil     |     5 | 1958, 1962, 1970, 1994, 2002 | Hilderaldo Bellini, Mauro Ramos, Carlos Alberto, Dunga, Cafu  | Vicente Feola, Aymore Moreira, Mario Zagallo, Carlos Alberto Parreira, Luiz Felipe Scolari |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Italy      |     4 | 1934, 1938, 1982, 2006       | Gianpiero Combi, Giuseppe Meazza, Dino Zoff, Fabio Cannavaro  | Vittorio Pozzo, Vittorio Pozzo, Enzo Bearzot, Marcello Lippi                               |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Germany    |     4 | 1954, 1974, 1990, 2014       | Fritz Walter, Franz Beckenbauer, Lothar Matthus, Philipp Lahm | Sepp Herberger, Helmut Schon, Franz Beckenbauer, Joachim Low                               |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Uruguay    |     2 | 1930, 1950                   | Jose Nasazzi, Obdulio Varela                                  | Alberto Suppici, Juan Lopez                                                                |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Argentina  |     2 | 1978, 1986                   | Daniel Passarella, Diego Maradona                             | Cesar Luis Menotti, Carlos Bilardo                                                         |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
England    |     1 | 1966                         | Bobby Moore                                                   | Alf Ramsey                                                                                 |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
France     |     1 | 1998                         | Didier Deschamps                                              | Aime Jacquet                                                                               |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Spain      |     1 | 2010                         | Iker Casillas                                                 | Vicente del Bosque                                                                         |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
```
