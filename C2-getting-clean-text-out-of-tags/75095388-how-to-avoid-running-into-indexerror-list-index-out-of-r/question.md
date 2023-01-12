---
title: "How to avoid running into IndexError: list index out of range error if an element is nonexistent while parsing xml with BeautifulSoup in python"
site: stackoverflow
question_id: 75095388
url: https://stackoverflow.com/q/75095388
asked: 2023-01-12T11:07:40Z
asked_by: "tachyon"
asked_by_url: https://stackoverflow.com/users/9122160
last_edited: 2023-01-13T07:33:32Z
tags: [python, dictionary, beautifulsoup, xml-parsing, outofrangeexception]
score: -2
views_at_snapshot: 315
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d24dee272f67de29cb9c60a5068d448a283edba361f6d119b27a0bf406b86e04
---

# How to avoid running into IndexError: list index out of range error if an element is nonexistent while parsing xml with BeautifulSoup in python

Asked by [tachyon](https://stackoverflow.com/users/9122160) on Stack Overflow, <https://stackoverflow.com/q/75095388>, 2023-01-12, last edited 2023-01-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have the following code to parse from an xml file to produce a pandas dataframe. The XML file looks like this:

```
<?xml version="1.0" encoding="UTF-8"?>
<Entries>
 <EntrySynopsisDetail_1_0>
        <EntryID>262148</EntryID>
        <EntryTitle>Establishment of the Graduate Internship Program</EntryTitle>
        <CategoryOfEntry>ENG</CategoryOfEntry>
</EntrySynopsisDetail_1_0>
<EntrySynopsisDetail_1_0>
<EntryID>2667654</EntryID>
        <EntryTitle>Call for Mobility Program</EntryTitle>
        <CategoryOfEntry>ENG</CategoryOfEntry>
        <CategoryOfEntry>MAT</CategoryOfEntry>
 </EntrySynopsisDetail_1_0>
</Entries>
``` 
And my code is below:
```
from bs4 import BeautifulSoup
import pandas as pd 

fd = open("file_120123.xml",'r')
data = fd.read()

Bs_data = BeautifulSoup(data,'xml')

ID = Bs_data.find_all('EntryID')
Title = Bs_data.find_all('EntryTitle')
try: 
   Cat = Bs_data.find_all('CategoryOfEntry')
except IndexError:
   Cat = ''

CatDict = {
    "ENG":"English",
    "MAT" :"Mathematics"
}

dataDf = []
for i in range(0,len(ID)):
      if (Cat[i] == CatDict):
        Cat[i] == CatDict.get(Cat[i])
       
      rows = [ID[i].get_text(), Title[i].get_text(), Cat[i])
      dataDf.append(rows)
    
df = pd.DataFrame(dataDf, columns =['ID', 'Title', 'Category'], dtype=float)
df.to_csv('120123.csv')
```


As you see, the code reads a xml file called 'file_120123.xml' using BeautifulSoup library, and calls each of the elements present in the file. Now one of the elements is a key and I have created a *dictionary* listing all possible keys. Not all *parents* have that element. I want to compare the extracted key with the ones in the dictionary and replace that with the value corresponding to that key. 

With this code, I get the error ```IndexError: list index out of range``` on ```Cat[i]``` on ```if (Cat[i] == CatDict):``` line. Any insights on how to resolve this?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[jackal](https://stackoverflow.com/users/17580381)** (2023-01-12): Yes. Don't try to use subscripts that are out of bounds
- **[Jack Fleeting](https://stackoverflow.com/users/9448090)** (2023-01-12): It's not a good idea to parse xml w/ BS; try either lxml or pandas.read_xml(). Also, please edit your question and add a short, representative sample of your xml as well as your expected output.
- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-01-12): Please edit your question and put there a sample of the XML and what information you're trying to get.
- **[tachyon](https://stackoverflow.com/users/9122160)** (2023-01-13): @JackFleeting I have added the XML details. Could you explain why BS is not a good idea to parse XML? I saw some examples showing that BS can also handle poorly structured XML.
- **[Jack Fleeting](https://stackoverflow.com/users/9448090)** (2023-01-13): See response in my answer below.
