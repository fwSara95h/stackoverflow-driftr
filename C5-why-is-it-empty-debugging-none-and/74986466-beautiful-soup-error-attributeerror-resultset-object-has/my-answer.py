# Code from my Stack Overflow answer https://stackoverflow.com/a/74987772 (posted 2023-01-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> s = requests.session()
>

# --- block 2 ---
>         s = soup.find_all("loc") ## the ResultSet
>

# --- block 3 ---
loc_rs = soup.find_all("loc") ## renamed var

for url in loc_rs: ## use renamed var
    loc = url.getText()

# --- block 4 ---
sess = requests.session() ## renamed var

for a,b in all_sitemaps.items():
    for urls in b:
        one_sitemap = urls
        pip_sitemap = sess.get(one_sitemap) ## use renamed var
        soup= bs4.BeautifulSoup(pip_sitemap.text,'html.parser')

# --- block 5 ---
for url in soup.find_all("loc"):
    loc = url.getText()
