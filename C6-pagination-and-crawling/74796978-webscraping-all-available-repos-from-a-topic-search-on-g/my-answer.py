# Code from my Stack Overflow answer https://stackoverflow.com/a/74821773 (posted 2022-12-16), extracted verbatim; may need the question's context to run.

# --- block 1 ---
pd.DataFrame([{'name': n, 'url': u, 'about': a} for n, u, a 
               in zip(stock_names, stock_urls, stock_about)])

# --- block 2 ---
dico = []

for page in range(1, 99):

    req = requests.get(search_topics + str(page) + "&q=" + "nlp" + "&type=Repositories", headers = headers)
    soup = BeautifulSoup(req.text, "html.parser")

    # for repo in soup.find('ul', class_="repo-list").find_all('li'):
    for repo in soup.select('ul.repo-list>li:has(a.v-align-middle[href])'):
        link = repo.select_one('a.v-align-middle[href]')
        about = repo.select_one('p.mb-1') 

        dico.append({
            # 'name': re.sub(r"\/(.*)\/(.*)", "\1", link.get('href')),
            'name': ' by '.join(link.text.strip().split('/', 1)[::-1]),
            'url': "https://github.com" + link.get('href'),
            'about': about.text.strip() if about else None
        })

df = pandas.DataFrame(dico)
