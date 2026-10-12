# Code from my Stack Overflow answer https://stackoverflow.com/a/75028807 (posted 2023-01-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
link_panel = soup.find("ul", {"class": "links"})
links = [l.a for l in link_panel.find_all('li') if l.a and not l.a.li]

# --- block 2 ---
# link_panel is no longer necessary
links = soup.select('ul.links li>a:not(:has(li))')

# --- block 3 ---
links = soup.find_all(
    lambda l: l.name == 'a' and l.parent.name == 'li' 
    and l.find_parent("ul", {"class": "links"}) and not l.find('li')
)

# --- block 4 ---
docNames = [l.get_text() for l in links]

# --- block 5 ---
> ['Despacho Homologatório',  'DOU Resultado de Julgamento', 'Termo de Ajudicação',  
>  'Ata da sessão publica',  'Proposta de preço adequada CSR',  
>  'Documentos de Habilitação CSR',  'Análise da proposta e Doc. de habilitação',  
>  'Resposta a 1ª diligencia - CSR',  '1ª Diligência - CSR',  '1ª Errata',  
>  'Anexo da 1ª Errata',  'Instrução para acesso ao processo administrativo',  
>  'Edital 0286/2022-15',  'DOU aviso de licitação'] 
>

# --- block 6 ---
# pgUrl = "https://www1.dnit.gov.br/editais/consulta/resumo.asp?NUMIDEdital=9109"
linkDocs = [{
    'name':l.get_text(' ').strip(), 'filename':l.get('href','').split('/')[-1],
    'link':urllib.parse.urljoin(pgUrl, l.get('href')) if l.get('href') else ''
} for l in soup.select('ul.links li>a:not(:has(li))')]# links]

# --- block 7 ---
> [{'name': 'Despacho Homologatório', 'filename': 'outros_edital0286_22-15_10.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_10.pdf'},
>  {'name': 'DOU Resultado de Julgamento', 'filename': 'outros_edital0286_22-15_9.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_9.pdf'},
>  {'name': 'Termo de Ajudicação', 'filename': 'outros_edital0286_22-15_8.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_8.pdf'},
>  {'name': 'Ata da sessão publica', 'filename': 'Ata_edital0286_22-15_0.pdf', 'link': 'https://www1.dnit.gov.br/anexo/Ata/Ata_edital0286_22-15_0.pdf'},
>  {'name': 'Proposta de preço adequada CSR', 'filename': 'outros_edital0286_22-15_7.zip', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_7.zip'},
>  {'name': 'Documentos de Habilitação CSR', 'filename': 'outros_edital0286_22-15_6.zip', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_6.zip'},
>  {'name': 'Análise da proposta e Doc. de habilitação', 'filename': 'outros_edital0286_22-15_5.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_5.pdf'},
>  {'name': 'Resposta a 1ª diligencia - CSR', 'filename': 'outros_edital0286_22-15_4.zip', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_4.zip'},
>  {'name': '1ª Diligência - CSR', 'filename': 'outros_edital0286_22-15_3.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_3.pdf'},
>  {'name': '1ª Errata', 'filename': 'Errata_edital0286_22-15_0.pdf', 'link': 'https://www1.dnit.gov.br/anexo/Errata/Errata_edital0286_22-15_0.pdf'},
>  {'name': 'Anexo da 1ª Errata', 'filename': 'outros_edital0286_22-15_2.zip', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_2.zip'},
>  {'name': 'Instrução para acesso ao processo administrativo', 'filename': 'outros_edital0286_22-15_1.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_1.pdf'},
>  {'name': 'Edital 0286/2022-15', 'filename': 'Edital_edital0286_22-15_0.zip', 'link': 'https://www1.dnit.gov.br/anexo/Edital/Edital_edital0286_22-15_0.zip'},
>  {'name': 'DOU aviso de licitação', 'filename': 'outros_edital0286_22-15_0.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_0.pdf'}]
>

# --- block 8 ---
> page = urlopen("https://www1.dnit.gov.br/editais/consulta/resumo.asp?NUMIDEdital=9109")
> html = page.read().decode("utf-8") 
> soup = BeautifulSoup(html, "lxml")
>
