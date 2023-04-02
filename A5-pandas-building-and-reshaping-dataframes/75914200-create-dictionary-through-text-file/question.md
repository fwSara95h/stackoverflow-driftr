---
title: "Create dictionary through text file"
site: stackoverflow
question_id: 75914200
url: https://stackoverflow.com/q/75914200
asked: 2023-04-02T19:31:08Z
asked_by: "Yeonari"
asked_by_url: https://stackoverflow.com/users/20369514
last_edited: 2023-04-02T19:38:33Z
tags: [python, dictionary, file]
score: 0
views_at_snapshot: 128
answer_count: 4
accepted_answer_id: 75914432
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 573611e7443a639c6580119d93e96728abd93bebdd9e59a1724744adea8b31da
---

# Create dictionary through text file

Asked by [Yeonari](https://stackoverflow.com/users/20369514) on Stack Overflow, <https://stackoverflow.com/q/75914200>, 2023-04-02, last edited 2023-04-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

In a lab for class we are to read from a text file containing line by line world cup winners with their country name, year, captain, and coach. We are expected to make a dictionary using the country name as keys.

I was trying to make a dictionary in a dictionary originally. With the country name being the key, then under that key having a key/value pair for wins, years, captain, coach.
    
```
def main():
    inFile = open('world_cup_champions.txt', 'r')
    champions = createDict(inFile)
    printChamps(champions)
    

def createDict(file):
    dict = {}
    try:
        for line in file:
            line = (line.strip()).split(",")
            dict[line[1]] = {}
            dict['Wins'] = 0
            for word in line:
                if (word == dict[line[1]]):
                    dict['Wins'] += 1
                    dict['Year(s)'] = line[0]
                    dict['Captain'] = line[2]
                    dict['Coach'] = line[3]
        return (dict)
    except Exception as e:
        print(e)    

def printChamps(unsorted_dict):
    print(f"{'Country':10} {'Wins':5} {'Year':32} {'Captain':72} {'Coach':30}\n")
    sorted_dict = dict(sorted(unsorted_dict.items()))  
    for key in sorted_dict:
        print ("%-10s | %2i | %-30s | %-70s | %-50s" % (key, sorted_dict[key]['Wins'], sorted_dict[key]['Year(s)'], sorted_dict[key]['Captain'], sorted_dict[key]['Coach']))


if __name__ == '__main__':
    main()
```
This is what I had as of now but I got confused on making the dictionary within createDict. Here is what the text file looks like:
```
Year,Country,Coach,Captain
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
2014,Germany,Joachim Low,Philipp Lahm
```

I want to print in a format that lists the country's name, how many wins they have, with the years that they have won.

This is the expected output:
[![enter image description here][1]][1]


  [1]: https://i.sstatic.net/3Iv2d.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[B Remmelzwaal](https://stackoverflow.com/users/17200348)** (2023-04-02): Unrelated: try not to name variables as built-ins, such as `dict`. This overrides them, and won't allow you to call a `dict()` constructor anymore as it would try to call the dictionary variable you created. Good to remember that if an IDE or the code blocks here highlight your variable name, it is not a good variable name.
- **[shaik moeed](https://stackoverflow.com/users/8353711)** (2023-04-02): What is the expected output should look like? What is the current output look like? Add more details to your question which makes easy to get help from SO.
- **[Yeonari](https://stackoverflow.com/users/20369514)** (2023-04-02): @BRemmelzwaal Yeah I saw a lot about that online I completely forgot to switch that variable name over haha.
- **[Yeonari](https://stackoverflow.com/users/20369514)** (2023-04-02): @shaikmoeed I added an image for the expected output.
- **[cards](https://stackoverflow.com/users/16462878)** (2023-04-02): it seems that  [`csv`](https://docs.python.org/3/library/csv.html) could be useful
