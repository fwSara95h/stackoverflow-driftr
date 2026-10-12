# Code from my Stack Overflow answer https://stackoverflow.com/a/75919408 (posted 2023-04-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# from bs4 import BeautifulSoup
# htmlStr = response.text ## if you're fetching with a request
htmlStr = '''
<div>
    <h3>Some Section</h3>
    Some text from Section 1

    <h3> Contact </h3>
    Adresse : Address Line One <br/> Address Line Two <br/>
    Téléphone : 0X XX XX XX XX <br/> 
    Site : <a href="https://example.com/">https://example.com/</a>

    <h3>Some Other Section</h3>
    field 1 : some info 
    field 2 : __ <br/> field 3 : some other info
</div>
'''

soup = BeautifulSoup(htmlStr, 'lxml')

# --- block 2 ---
def get_section_info(section_header):
    hName, hList = section_header.name, 'h1,h2,h3,h4,h5,h6'
    hList = [h for h in hList.split(hName)[0].split(',') if h] + [hName]

    section_info, cur_key = {}, None
    for ns in section_header.next_siblings:
        if ns.name in hList: break ## stop if you reach the next section
        if not ((isinstance(ns,str) and not ns.PREFIX) or ns.name): continue ## skip

        nsStr = ' '.join((ns if isinstance(ns,str) else ns.get_text(' ')).split())
        if ':' in nsStr and not nsStr.startswith('http'): 
            cur_key, nsStr = [s.strip() for s in nsStr.split(':',1)]

        ckStr = section_info.get(cur_key, '')
        if ns.name == 'br': section_info[cur_key] = ckStr + ' \n'
        elif nsStr: section_info[cur_key] = ckStr + ' ' + nsStr

    section_info = {k:v.strip() for k,v in section_info.items()}
    return section_info[None] if [*section_info]==[None] else section_info

# --- block 3 ---
if (contact_h3 := soup.find('h3', string=lambda s: s and s.strip()=='Contact')):
    contact_info = get_section_info(contact_h3)
else: contact_info, _ = {}, print('Could not find <h3>Contact</h3>')

# --- block 4 ---
> { 'Adresse': 'Address Line One \n Address Line Two', 
>   'Téléphone': '0X XX XX XX XX', 
>   'Site': 'https://example.com/' }
>

# --- block 5 ---
{h3.text.strip(): get_section_info(h3) for h3 in soup.select('h3')}

# --- block 6 ---
> {
>   'Some Section': 'Some text from Section 1',
>   'Contact': {
>     'Adresse': 'Address Line One \n Address Line Two',
>     'Téléphone': '0X XX XX XX XX',
>     'Site': 'https://example.com/'
>   },
>   'Some Other Section': {
>     'field 1': 'some info field 2 : __', 'field 3': 'some other info'
>   }
> }
>

# --- block 7 ---
def get_textchunk(word1, word2, text):
    if not (word1 in text and word2 in text): return ''
    return text.split(word1)[-1].split(word2)[0]
    ## can refine with more conditions/string-manipulations/regex/etc

get_textchunk('Adresse :', 'Téléphone :', soup.get_text(' '))

# --- block 8 ---
def get_text_by_field(soupX, fieldName):
    fsCond = lambda s: s and ':' in s and s.split(':')[0].strip()==fieldName
    fieldStr = soupX.find(string=fsCond)
    hList, myText = [f'h{i}' for i in range(1,7)], fieldStr.split(':',1)[1]
    for ns in (fieldStr.next_siblings if fieldStr else []):
        if ns.name in hList: break ## stop when you reach the next section
        if not ((isinstance(ns,str) and not ns.PREFIX) or ns.name): continue 

        nsStr = ' '.join((ns if isinstance(ns,str) else ns.get_text(' ')).split())
        if ':' in nsStr and not nsStr.startswith('http'): break

        if ns.name == 'br': myText += ' \n'
        elif nsStr: myText += (' ' + nsStr)
    return myText.strip()

# --- block 9 ---
> 'Address Line One \n Address Line Two'
>
