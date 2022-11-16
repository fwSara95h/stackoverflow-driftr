---
title: "How to scrape service and corresponding price, selected by string?"
site: stackoverflow
question_id: 74422347
answer_id: 74455631
url: https://stackoverflow.com/a/74455631
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-16T05:35:14Z
last_edited: 2022-11-16T05:41:14Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74455631/revisions
accepted: true
score: 1
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dd3bb573ac2ff62afd94907adf4721cc23e8e4c59eb967a49a5697a08f83c83d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74455631>, 2022-11-16, last edited 2022-11-16; **accepted**; score 1. Text as retrieved 2026-10-12.

<sub>[I got `soup` simply with `url='https://optimdent.pl/cennik/'; soup=BeautifulSoup(requests.get(url).content)`.]</sub>

If you're sure that the `td` cells have classes `column-1` and `column-2` respectively, you can get the first cell [if it *contains* `strServiceVersion`] of each row with such cells (and no other cells) with
```python
tcrSel1 = 'tr:has(td.column-1~td.column-2):not(:has(td~td~td))' 
tcrSel2 = f'td.column-1:first-child:-soup-contains("{strServiceVersion}")' 
arrDataCell = soup.select(f'{tcrSel1} {tcrSel2}')
```
(NB: You'll probably need to have [`html5lib`](https://pypi.org/project/html5lib/) installed to be able use [pseudo-classes](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/) like `-soup-contains`.)

It's pretty much the same as
```python
arrDataCell = soup.find_all(
    lambda t: t.name == 'td' and 'column-1' in t.get('class', []) 
    and strServiceVersion in t.get_text() #and t.get_text()==strServiceVersion 
    and t.find_parent('tr') and t == t.find_parent('tr').td 
    and len(t.find_next_siblings('td', {'class': 'column-2'})) == 1
)
```
it's longer, but using `find`+`lambda` lets you specify exact (full) text, and even use regex if you want.

(Btw, for this particular site, your `soup.find_all('td', text=strServiceVersion)` is probably also fine, but I couldn't know before how many tables/rows might contain the same text but have different structure.)

---
---

With either version,
```python
dictList = [{
  'column-1': a1.get_text(strip=True), 'column-2': a2.get_text(strip=True) 
} for a1,a2 in [a.parent.find_all('td', recursive=False) for a in arrDataCell]]
```
should give you this list of dictionaries:
```lang-none
[
   {'column-1': 'Wybielanie zębów w gabinecie preparatem Prevdent', 'column-2': '1600'} ,
   {'column-1': 'Aparat stały (za jeden łuk): zamki metalowe | zamki ICONIX | zamki ceramiczne', 'column-2': '2500 | 2900 | 3500'} ,
   {'column-1': 'Wizyta kontrolna w trakcie noszenia aparatu: 1 łuk | 2 łuki', 'column-2': '240 | 280'} ,
   {'column-1': 'Leczenie aparatem INVISALIGN (przeźroczyste nakładki): diagnostyka | pakiet Standard | pakiet Full', 'column-2': '2000 | 11000 | 18000'} ,
]
```

---

OR, to get a single dictionary,
```python
adcDict = {
    a1.get_text(' ', strip=True): a2.get_text(' ', strip=True) for 
    a1,a2 in [a.parent.find_all('td', recursive=False) for a in arrDataCell]
}
```
```lang-none
{
 'Wybielanie zębów w gabinecie preparatem Prevdent': '1600',
 'Aparat stały (za jeden łuk): zamki metalowe | zamki ICONIX | zamki ceramiczne': '2500 | 2900 | 3500',
 'Wizyta kontrolna w trakcie noszenia aparatu: 1 łuk | 2 łuki': '240 | 280',
 'Leczenie aparatem INVISALIGN (przeźroczyste nakładki): diagnostyka | pakiet Standard | pakiet Full': '2000 | 11000 | 18000'
}
```

---
---

Results will look a bit different with [`read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html), since it will grab the whole table instead of specific rows (and you can't specify the `td` class or cells per row).
```python
# dfList = pandas.read_html(url, match=strServiceVersion) # OR
# dfList = pandas.read_html('\n'.join([str(a.find_parent('table')) for a in arrDataCell])) # OR
# dfList = pandas.read_html('<table>\n'+'\n'.join([str(a.find_parent('tr'))+'\n</table>' for a in arrDataCell])) # OR
dfList = pandas.read_html(str(soup), match=strServiceVersion)
dictList = []
for df in dfList: dictList += df.to_dict('records')
```
(It looks like merged columns are split and duplicated...)
```lang-none
[
   {0: 'Licówka porcelanowa', 1: '2000'} ,
   {0: 'Dbamy o każdy szczegół wykonywanej pracy, aby przyszłe uzupełnienie w największym stopniu odzwierciedlało naturalny, piękny zdrowy uśmiech. Przed przystąpieniem do pracy wykonujemy waxup, dzięki któremu możemy zwizualizować i ocenić przyszłe efekty leczenia. Współpracujemy z uznanymi pracowniami dentystycznymi bazującymi na najnowszych materiałach oraz technologiach.', 1: 'Dbamy o każdy szczegół wykonywanej pracy, aby przyszłe uzupełnienie w największym stopniu odzwierciedlało naturalny, piękny zdrowy uśmiech. Przed przystąpieniem do pracy wykonujemy waxup, dzięki któremu możemy zwizualizować i ocenić przyszłe efekty leczenia. Współpracujemy z uznanymi pracowniami dentystycznymi bazującymi na najnowszych materiałach oraz technologiach.'} ,
   {0: 'Bonding zębów metodą Flow-Injection (za ząb)', 1: '450'} ,
   {0: 'Dzięki bogatemu doświadczeniu i wiedzy naszych specjalistów, jesteśmy w stanie przywrócić naturalny i piękny uśmiech, którym możesz dzielić się z innymi. Często przed wykonaniem odbudowy wykonujemy wizualizację w jamie ustnej, dzięki czemu możesz ocenić efekt przed ostateczną realizacją. Bonding wykonujemy techniką Flow-Injection, która jest zdecydowanie dokładniejsza niż tzw. odbudowa z ręki.', 1: 'Dzięki bogatemu doświadczeniu i wiedzy naszych specjalistów, jesteśmy w stanie przywrócić naturalny i piękny uśmiech, którym możesz dzielić się z innymi. Często przed wykonaniem odbudowy wykonujemy wizualizację w jamie ustnej, dzięki czemu możesz ocenić efekt przed ostateczną realizacją. Bonding wykonujemy techniką Flow-Injection, która jest zdecydowanie dokładniejsza niż tzw. odbudowa z ręki.'} ,
   {0: 'Wybielanie zębów w gabinecie preparatem Prevdent', 1: '1600'} ,
   {0: 'Metoda wybielania preparatem Prevdent jest w 100% bezpieczna i pozwala uzyskać naturalny efekt estetyczny. Cała procedura wykonywana jest w gabinecie stomatologicznym w trakcie jednej wizyty, która trwa około 2 godzin.', 1: 'Metoda wybielania preparatem Prevdent jest w 100% bezpieczna i pozwala uzyskać naturalny efekt estetyczny. Cała procedura wykonywana jest w gabinecie stomatologicznym w trakcie jednej wizyty, która trwa około 2 godzin.'} ,
   {0: 'Wybielanie nakładkowe (szyny + 4 strzykawki Opalescence)', 1: '950'} ,
   {0: 'Metoda nakładkowa polega na trójwymiarowym zeskanowaniu zębów pacjenta, a następnie przygotowaniu specjalnych, indywidualnych szyn, do których nakłada się żel wybielający Opalescence. Procedura wymaga 2 wizyt w odstępie paru dni (skan wewnątrzustny oraz oddanie nakładek). Efekt wybielania jest po około 7-10 dniach noszenia nakładek.', 1: 'Metoda nakładkowa polega na trójwymiarowym zeskanowaniu zębów pacjenta, a następnie przygotowaniu specjalnych, indywidualnych szyn, do których nakłada się żel wybielający Opalescence. Procedura wymaga 2 wizyt w odstępie paru dni (skan wewnątrzustny oraz oddanie nakładek). Efekt wybielania jest po około 7-10 dniach noszenia nakładek.'} ,
   {0: 'Zabiegi z zakresu ortodoncji wykonuje lek. dent. Karolina Różycka-Popadiak (właściciel OptimDent). W trakcie leczenia wykorzystujemy światowe standardy i rozwiązania. Każdy przypadek jest inny dlatego leczenie rozpoczynamy od wnikliwej analizy klinicznej, starając się dobrać jak najodpowiedniejszy sposób leczenia.', 1: 'Zabiegi z zakresu ortodoncji wykonuje lek. dent. Karolina Różycka-Popadiak (właściciel OptimDent). W trakcie leczenia wykorzystujemy światowe standardy i rozwiązania. Każdy przypadek jest inny dlatego leczenie rozpoczynamy od wnikliwej analizy klinicznej, starając się dobrać jak najodpowiedniejszy sposób leczenia.'} ,
   {0: 'Aparat stały (za jeden łuk): zamki metalowe | zamki ICONIX | zamki ceramiczne', 1: '2500 | 2900 | 3500'} ,
   {0: 'Wizyta kontrolna w trakcie noszenia aparatu: 1 łuk | 2 łuki', 1: '240 | 280'} ,
   {0: 'Leczenie aparatem INVISALIGN (przeźroczyste nakładki): diagnostyka | pakiet Standard | pakiet Full', 1: '2000 | 11000 | 18000'} ,
   {0: 'Posiadamy najnowocześniejszy aparat rentgenowski. Aby wykonać zdjęcie nie musisz się umawiać, cała procedura trwa kilka minut, a wynik jest dostępny tuż po wykonaniu zdjęcia w wersji cyfrowej lub na kliszy.', 1: 'Posiadamy najnowocześniejszy aparat rentgenowski. Aby wykonać zdjęcie nie musisz się umawiać, cała procedura trwa kilka minut, a wynik jest dostępny tuż po wykonaniu zdjęcia w wersji cyfrowej lub na kliszy.'} ,
   {0: 'Pantomogram (zdjęcie 2D wszystkich zębów)', 1: '90'} ,
   {0: 'Cefalometria (zdjęcie boczne 2D używane głównie w ortodoncji)', 1: '90'} ,
   {0: 'Tomografia komputerowa: odcinka | szczęki lub żuchwy | całość', 1: '140 | 250 | 350'} ,
   {0: 'Pakiet Pantomogram + Cefalometria', 1: '150'} ,
]
```

---

Although, you could filter down to rows with numbers in the second column with something like 
```python
dictList = [d for d in dictList if d[1].split(' | ')[0].isdigit()]
```
```lang-none
[
   {0: 'Licówka porcelanowa', 1: '2000'} ,
   {0: 'Bonding zębów metodą Flow-Injection (za ząb)', 1: '450'} ,
   {0: 'Wybielanie zębów w gabinecie preparatem Prevdent', 1: '1600'} ,
   {0: 'Wybielanie nakładkowe (szyny + 4 strzykawki Opalescence)', 1: '950'} ,
   {0: 'Aparat stały (za jeden łuk): zamki metalowe | zamki ICONIX | zamki ceramiczne', 1: '2500 | 2900 | 3500'} ,
   {0: 'Wizyta kontrolna w trakcie noszenia aparatu: 1 łuk | 2 łuki', 1: '240 | 280'} ,
   {0: 'Leczenie aparatem INVISALIGN (przeźroczyste nakładki): diagnostyka | pakiet Standard | pakiet Full', 1: '2000 | 11000 | 18000'} ,
   {0: 'Pantomogram (zdjęcie 2D wszystkich zębów)', 1: '90'} ,
   {0: 'Cefalometria (zdjęcie boczne 2D używane głównie w ortodoncji)', 1: '90'} ,
   {0: 'Tomografia komputerowa: odcinka | szczęki lub żuchwy | całość', 1: '140 | 250 | 350'} ,
   {0: 'Pakiet Pantomogram + Cefalometria', 1: '150'} ,
]
```
