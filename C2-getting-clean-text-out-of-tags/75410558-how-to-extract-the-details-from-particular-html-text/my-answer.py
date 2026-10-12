# Code from my Stack Overflow answer https://stackoverflow.com/a/75411642 (posted 2023-02-10), extracted verbatim; may need the question's context to run.

# --- block 1 ---
soup = BeautifulSoup(html_content, 'html.parser')
form_data = soup.find("div",{"id":"formContents"})
if form_data:
    section_data = soup.find_all("div",{"class":"sectionDiv expanded"})
    for datas in section_data:
        labels = datas.find_all("label",{"class":"fieldLabel"})
        for item in labels: 
            print(item.text) ## label
            for nxtTable in item.find_next_siblings('table'):
                print('\n'.join([td.text for td in nxtTable.find_all("td")]))
                break ## [ only takes the first table ]

# --- block 2 ---
> Address
> 
> 
> 1183
> Pelham Wood Dr, Rock Hill, SC 29732
> 
> 
>

# --- block 3 ---
soup = BeautifulSoup(html_content, 'html.parser')

section_sel = 'div#formContents div.sectionDiv.expanded'
label_sel = 'label.fieldLabel'
for datas in soup.select(f'{section_sel}:has({label_sel}+table td)'):
    labels = datas.select(f'{label_sel}:has(+table td)')
    labels = [' '.join(l.get_text(' ').split()) for l in labels]
    entity_data = [' '.join([
        ' '.join(td.get_text(' ').split()) for td in ed.select('td')
    ]) for ed in datas.select(f'{label_sel}+table:has(td)')]
    # data_dict = dict(zip(labels, entity_data))
    for l, ed in zip(labels, entity_data): print(f'{l}: {ed}')

# --- block 4 ---
> Address: 1183 Pelham Wood Dr, Rock Hill, SC 29732
>
