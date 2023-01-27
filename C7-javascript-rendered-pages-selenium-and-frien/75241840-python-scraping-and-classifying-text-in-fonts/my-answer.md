---
title: "Python - Scraping and classifying text in \"fonts\""
site: stackoverflow
question_id: 75241840
answer_id: 75259313
url: https://stackoverflow.com/a/75259313
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-27T14:16:01Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75259313/revisions
accepted: true
score: 2
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 45263e2d359dbe46f0861d1dadc73745db788b4520f129aaca2acab51b2c4bce
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75259313>, 2023-01-27; **accepted**; score 2. Text as retrieved 2026-10-12.

**Note:** instead of using selenium, I simply fetched and parsed with `soup = BeautifulSoup(requests.get(url).content, "html.parser")`; as far as I an tell, the required section is not dynamic, so it shouldn't cause any issues.

---

> would you have any idea about how to look for pairs of `<br>`

Since they represent empty lines, you could try simply splitting the text [in that cell][1] by `\n\n\n`

```python 
blockText = soup.select_one('td:has(font)').get_text(' ')
blockText = blockText.replace('-'*10, '\n\n\n') # pad "underlined" lines
blockSections = [sect.strip() for sect in '\n'.join([
    l.strip('-').strip() for l in blockText.splitlines()
]).split('\n\n\n') if sect.strip()]
```

Although, if you looked at [`blockSections`][2], you might notice that some headers [`ROSTER` and `MEMBERS`] get stuck to the end of the previous section - probably because their formatting means that an extra `<br>` is not needed to distinguish them from their adjacent sections. [I added the `.replace('-'*10, '\n\n\n')` line so that at least they're separated from the *next* section.]

Another risk is that I don't know if all versions and parsers will parse `<br><br>` to text as 3 line breaks - some omit `br` space entirely from text, and others might add extra space based on spaces between tags in the source html.

---

It's easier to split if you loop through the `<br>`s and pad them with something more distinctive to split by; the [`.insert...`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#insert-before-and-insert-after) methods are useful here. (This method also has the advantage of being able to target bolded lined as well.)

```python
blockSoup = soup.select_one('td:has(font)')
for br2 in blockSoup.select('br+br, font:has(br)'): 
    br2.insert_after(BeautifulSoup(f'<p>{"="*80}</p>').p)
    br2.insert_before(BeautifulSoup(f'<p>{"="*80}</p>').p)
blockSections = [
    sect.strip().strip('-').strip() for sect in 
    blockSoup.get_text(' ').split("="*80) if sect.strip()
]
```

This time, `blockSections` looks something like

> ```python
> ['Membership Roster - ACE\n AIDS CLINICAL STUDIES AND EPIDEMIOLOGY STUDY SECTION\n Center For Scientific Review\n (Terms end 6/30 of the designated year)\n ROSTER',
>  'CHAIRPERSON',
>  'SCHACKER, TIMOTHY\n W\n , MD,\n (14)\n PROFESSOR\n DEPARTMENT OF MEDICINE\n UNIVERSITY OF MINNESOTA\n MINNEAPOLIS,\n MN\n 55455',
>  'MEMBERS',
>  'ANDERSON, JEAN\n R\n , MD,\n (14)\n PROFESSOR\n DEPARTMENT OF GYNECOLOGY AND OBSTETRICS\n JOHNS HOPKINS UNIVERSITY\n BALTIMORE,\n MD 21287',
>  'BALASUBRAMANYAM, ASHOK\n , MD,\n (14)\n PROFESSOR\n DEPARTMENT OF MEDICINE AND\n MOLECULAR AND CELLULAR BIOLOGY\n DIVISION OF DIABETES, ENDOCRINOLOGY AND METABOLISM\n BAYLOR COLLEGE OF MEDICINE\n HOUSTON,\n TX 77030',
>  'BLATTNER, WILLIAM\n ALBERT\n , MD,\n (15)\n PROFESSOR AND ASSOCIATE DIRECTOR\n DEPARTMENT OF MEDICNE\n INSTITUTE OF HUMAN VIROLOGY\n UNIVERSITY OF MARYLAND, BALTIMORE\n BALTIMORE,\n MD 21201',
>  'CHEN, YING\n QING\n , PHD,\n (15)\n PROFESSOR\n PROGRAM IN BIOSTATISTICS AND BIOMATHEMATICS\n FRED HUTCHINSON CANCER RESEARCH CENTER\n SEATTLE,\n WA 981091024',
>  'COTTON, DEBORAH\n , MD,\n (13)\n PROFESSOR\n SECTION OF INFECTIOUS DISEASES\n DEPARTMENT OF MEDICINE\n BOSTON UNIVERSITY\n BOSTON,\n MA 02118',
>  'DANIELS, MICHAEL\n J\n , SCD,\n (16)\n PROFESSOR\n DEPARTMENT OF BIOSTATISTICS\n UNIVERSITY OF TEXAS AT AUSTIN\n AUSTIN,\n TX 78712',
>  'FOULKES, ANDREA\n SARAH\n , SCD,\n (14)\n ASSOCIATE PROFESSOR\n DEPARTMENT OF BIOSTATISTICS\n UNIVERSITY OF MASSACHUSETTS\n AMHERST,\n MA 01003',
>  'HEROLD, BETSY\n C\n , MD,\n (16)\n PROFESSOR\n DEPARTMENT OF PEDIATRICS\n ALBERT EINSTEIN COLLEGE OF MEDICINE\n BRONX,\n NY 10461',
>  'JUSTICE, AMY\n CAROLINE\n , MD, PHD,\n (16)\n PROFESSOR\n DEPARTMENT OF PEDIATRICS\n YALE UNIVERSITY\n NEW HAVEN,\n CT 06520',
>  'KATZENSTEIN, DAVID\n ALLENBERG\n , MD,\n (13)\n PROFESSOR\n DIVISION OF INFECTIOUS DISEASES\n STANFORD UNIVERSITY SCHOOL OF MEDICINE\n STANFORD,\n CA 94305',
>  'MARGOLIS, DAVID\n M\n , MD,\n (14)\n PROFESSOR\n DEPARTMENT OF MEDICINE\n UNIVERSITY OF NORTH CAROLINA, CHAPEL HILL\n CHAPEL HILL,\n NC 27599',
>  'MONTANER, LUIS\n J\n , DVM, PHD,\n (13)\n PROFESSOR\n DEPARTMENT OF IMMUNOLOGY\n THE WISTAR INSTITUTE\n PHILADELPHIA,\n PA 19104',
>  'MONTANO, MONTY\n A\n , PHD,\n (15)\n RESEARCH SCIENTIST\n DEPARTMENT OF IMMUNOLOGY AND\n INFECTIOUS DISEASES\n BOSTON UNIVERSITY\n BOSTON,\n MA 02115',
>  'PAGE, KIMBERLY\n , PHD, MPH,\n (16)\n PROFESSOR\n DIVISION OF PREVENTIVE MEDICINE AND PUBLIC HEALTH\n AND GLOBAL HEALTH SCIENCES\n DEPARTMENT OF EPIDEMIOLOGY AND BIOSTATICTICS\n UNIVERSITY OF CALIFORNIA, SAN FRANCISCO\n UNIVERSITY OF CALIFORNIA, SAN FRANCISCO\n SAN FRANCISCO,\n CA 94105',
>  'SHIKUMA, CECILIA\n M\n , MD,\n (15)\n PROFESSOR\n DEPARTMENT OF MEDICINE\n HAWAII AIDS CLINICAL RESEARCH PROGRAM\n UNIVERSITY OF HAWAII\n HONOLULU,\n HI 96816',
>  'WOOD, CHARLES\n , PHD,\n (13)\n PROFESSOR\n UNIVERSITY OF NEBRASKA\n LINCOLN,\n NE 68588']
> ```

---

> create a table with the columns NAME, TITLE, LOCATION

There may be a more elegant solution, but I feel like the simplest way would be to just loop the siblings of the headers and keep count of consecutive `br`s.

```python
doubleBr = soup.select('br')[:2] # [ so the last person also gets added ]
personsList = []
for f in soup.select('td>font>font:has(b br)'):
    role, lCur,pCur,brCt = f.get_text(' ').strip('-').strip(), [],[],0 
    for lf in f.find_next_siblings(['font','br'])+doubleBr:
        brCt = brCt+1 if lf.name == 'br' else 0 
        if pCur and (brCt>1 or lf.b):
            pDets = {'role': role, 'name': '?'} # initiate

            if len(pCur)>1: pDets['title'] = pCur[1]
            pDets['name'], pCur = pCur[0], pCur[2:]
            
            dList = pCur[:-2] 
            pDets['departments'] = dList[0] if len(dList)==1 else dList

            if len(pCur)>1: pDets['institute'] = pCur[-2]
            if pCur: pDets['location'] = pCur[-1]

            personsList.append(pDets)      
            pCur, lCur, brCt = [], [], 0 # clear
        if lf.b: break # rached next section
        if lf.name == 'font': # [split and join to minimize whitespace]
            lCur.append(' '.join(lf.get_text(' ').split())) # add to line
        if brCt and lCur: pCur, lCur = pCur+[' '.join(lCur)], [] # newline 
```

Since [`personsList`][3] is a list of dictionaries, it can be tabulated as simply as  `pandas.DataFrame(personsList)` to get a DataFrame that looks like:

| role        | name                              | title                            | departments                                                                                                                                                                    | institute                                 | location                |
|:------------|:----------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------|:------------------------|
| CHAIRPERSON | SCHACKER, TIMOTHY W , MD          | PROFESSOR                        | DEPARTMENT OF MEDICINE                                                                                                                                                         | UNIVERSITY OF MINNESOTA                   | MINNEAPOLIS, MN 55455   |
| MEMBERS     | ANDERSON, JEAN R , MD             | PROFESSOR                        | DEPARTMENT OF GYNECOLOGY AND OBSTETRICS                                                                                                                                        | JOHNS HOPKINS UNIVERSITY                  | BALTIMORE, MD 21287     |
| MEMBERS     | BALASUBRAMANYAM, ASHOK , MD       | PROFESSOR                        | ['DEPARTMENT OF MEDICINE AND', 'MOLECULAR AND CELLULAR BIOLOGY', 'DIVISION OF DIABETES, ENDOCRINOLOGY AND METABOLISM']                                                         | BAYLOR COLLEGE OF MEDICINE                | HOUSTON, TX 77030       |
| MEMBERS     | BLATTNER, WILLIAM ALBERT , MD     | PROFESSOR AND ASSOCIATE DIRECTOR | ['DEPARTMENT OF MEDICNE', 'INSTITUTE OF HUMAN VIROLOGY']                                                                                                                       | UNIVERSITY OF MARYLAND, BALTIMORE         | BALTIMORE, MD 21201     |
| MEMBERS     | CHEN, YING QING , PHD             | PROFESSOR                        | PROGRAM IN BIOSTATISTICS AND BIOMATHEMATICS                                                                                                                                    | FRED HUTCHINSON CANCER RESEARCH CENTER    | SEATTLE, WA 981091024   |
| MEMBERS     | COTTON, DEBORAH , MD              | PROFESSOR                        | ['SECTION OF INFECTIOUS DISEASES', 'DEPARTMENT OF MEDICINE']                                                                                                                   | BOSTON UNIVERSITY                         | BOSTON, MA 02118        |
| MEMBERS     | DANIELS, MICHAEL J , SCD          | PROFESSOR                        | DEPARTMENT OF BIOSTATISTICS                                                                                                                                                    | UNIVERSITY OF TEXAS AT AUSTIN             | AUSTIN, TX 78712        |
| MEMBERS     | FOULKES, ANDREA SARAH , SCD       | ASSOCIATE PROFESSOR              | DEPARTMENT OF BIOSTATISTICS                                                                                                                                                    | UNIVERSITY OF MASSACHUSETTS               | AMHERST, MA 01003       |
| MEMBERS     | HEROLD, BETSY C , MD              | PROFESSOR                        | DEPARTMENT OF PEDIATRICS                                                                                                                                                       | ALBERT EINSTEIN COLLEGE OF MEDICINE       | BRONX, NY 10461         |
| MEMBERS     | JUSTICE, AMY CAROLINE , MD, PHD   | PROFESSOR                        | DEPARTMENT OF PEDIATRICS                                                                                                                                                       | YALE UNIVERSITY                           | NEW HAVEN, CT 06520     |
| MEMBERS     | KATZENSTEIN, DAVID ALLENBERG , MD | PROFESSOR                        | DIVISION OF INFECTIOUS DISEASES                                                                                                                                                | STANFORD UNIVERSITY SCHOOL OF MEDICINE    | STANFORD, CA 94305      |
| MEMBERS     | MARGOLIS, DAVID M , MD            | PROFESSOR                        | DEPARTMENT OF MEDICINE                                                                                                                                                         | UNIVERSITY OF NORTH CAROLINA, CHAPEL HILL | CHAPEL HILL, NC 27599   |
| MEMBERS     | MONTANER, LUIS J , DVM, PHD       | PROFESSOR                        | DEPARTMENT OF IMMUNOLOGY                                                                                                                                                       | THE WISTAR INSTITUTE                      | PHILADELPHIA, PA 19104  |
| MEMBERS     | MONTANO, MONTY A , PHD            | RESEARCH SCIENTIST               | ['DEPARTMENT OF IMMUNOLOGY AND', 'INFECTIOUS DISEASES']                                                                                                                        | BOSTON UNIVERSITY                         | BOSTON, MA 02115        |
| MEMBERS     | PAGE, KIMBERLY , PHD, MPH         | PROFESSOR                        | ['DIVISION OF PREVENTIVE MEDICINE AND PUBLIC HEALTH', 'AND GLOBAL HEALTH SCIENCES', 'DEPARTMENT OF EPIDEMIOLOGY AND BIOSTATICTICS', 'UNIVERSITY OF CALIFORNIA, SAN FRANCISCO'] | UNIVERSITY OF CALIFORNIA, SAN FRANCISCO   | SAN FRANCISCO, CA 94105 |
| MEMBERS     | SHIKUMA, CECILIA M , MD           | PROFESSOR                        | ['DEPARTMENT OF MEDICINE', 'HAWAII AIDS CLINICAL RESEARCH PROGRAM']                                                                                                            | UNIVERSITY OF HAWAII                      | HONOLULU, HI 96816      |
| MEMBERS     | WOOD, CHARLES , PHD               | PROFESSOR                        | []                                                                                                                                                                             | UNIVERSITY OF NEBRASKA                    | LINCOLN, NE 68588       |

---

[ Btw, if the *`.select('br+br, font:has(br)')`* and *`.select('td>font>font:has(b br)')`* parts are unfamiliar to you, you can look up [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) and [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php). [Combinators](https://facelessuser.github.io/soupsieve/selectors/combinators/) [like `>`/`+`/`,`]  and [pseudo-classes](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/) [like `:has`] allow us to get very specific with out targets. ]


  [1]: https://i.sstatic.net/SxuBl.png
  [2]: https://i.sstatic.net/AI8Vv.png
  [3]: https://i.sstatic.net/QyZ9B.png
