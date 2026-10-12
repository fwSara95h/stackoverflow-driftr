# Code from my Stack Overflow answer https://stackoverflow.com/a/75259313 (posted 2023-01-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
blockText = soup.select_one('td:has(font)').get_text(' ')
blockText = blockText.replace('-'*10, '\n\n\n') # pad "underlined" lines
blockSections = [sect.strip() for sect in '\n'.join([
    l.strip('-').strip() for l in blockText.splitlines()
]).split('\n\n\n') if sect.strip()]

# --- block 2 ---
blockSoup = soup.select_one('td:has(font)')
for br2 in blockSoup.select('br+br, font:has(br)'): 
    br2.insert_after(BeautifulSoup(f'<p>{"="*80}</p>').p)
    br2.insert_before(BeautifulSoup(f'<p>{"="*80}</p>').p)
blockSections = [
    sect.strip().strip('-').strip() for sect in 
    blockSoup.get_text(' ').split("="*80) if sect.strip()
]

# --- block 3 ---
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
>

# --- block 4 ---
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
