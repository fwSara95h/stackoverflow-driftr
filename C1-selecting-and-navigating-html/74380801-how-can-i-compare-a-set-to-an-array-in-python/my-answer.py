# Code from my Stack Overflow answer https://stackoverflow.com/a/74384000 (posted 2022-11-10), extracted verbatim; may need the question's context to run.
prev_links = [r[2] for r in sh.get_all_values()]
ar = []

# (I prefer to define constants outside loop) 
abs_url = "https://www.ig.com" 
h_selector = 'h3[class="article-category-section-title"]'
link_selector = f'{h_selector} a[class="primary js_target"][href]'

for url in urls:
    my_url = requests.get(url)
    html = my_url.content
    soup = BeautifulSoup(html, "html.parser")

    date_today = str(datetime.date.today())
    for arLink in soup.select(link_selector):
        rel_url = arLink.get("href")
        full_url = urllib.parse.urljoin(abs_url, rel_url)
        article = str(full_url.replace("https://",""))
        if article in prev_links: 
            continue # skip if already added

        title = arLink.text.strip()
        pub_date = rel_url[-6:]
        pub_date = f"{pub_date[4:6]} {pub_date[2:4]} {pub_date[0:2]}"

        ar.append([date_today, title, article, pub_date]) # no need for str() - they're all strings already
        prev_links.append(article) # maintain list of already-added-urls

if ar != []:
    sh.append_rows(ar, value_input_option="USER_ENTERED")
