# Code from my Stack Overflow answer https://stackoverflow.com/a/76431395 (posted 2023-06-08), extracted verbatim; may need the question's context to run.
for repo in soup.findAll('li', attrs={'class': 'repo-list-item'}):
    rep = repo.find('a', attrs={'href': True, 'class':'v-align-middle'})
    descp = repo.find('p', attrs={'class': 'mb-1'})
    dt = repo.find('relative-time', attrs={'datetime': True}) 

    date.append(dt['datetime']) 
    rep_link.append(rep['href'])
    description.append(None if descp is None else descp.text.strip()) 
    ## not all repos have description
