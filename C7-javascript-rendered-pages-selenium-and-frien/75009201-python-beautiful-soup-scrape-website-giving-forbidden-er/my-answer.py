# Code from my Stack Overflow answer https://stackoverflow.com/a/75013193 (posted 2023-01-05), extracted verbatim; may need the question's context to run.
### PASTE FOR linkToSoup_scrapingAnt FROM https://pastebin.com/5ibz2F6p 
### OR PASTE FOR linkToSoup_selenium FROM https://pastebin.com/VLZ2vPYK 

roorUrl = 'https://ae.indeed.com'
for current_page in range(1, 3):
        page_url = f'https://ae.indeed.com/jobs?q=&l=UAE&start={current_page}'
        print(page_url)

        # r = s.get(f'https://ae.indeed.com/jobs?q=&l=UAE&start={current_page}')  
        # soup = BeautifulSoup(r.text, 'html.parser')
        ## INSTEAD:

        # pgSoup = linkToSoup_scrapingAnt(page_url, isv=True, returnErr=False) # OR
        pgSoup = linkToSoup_selenium(page_url, isv=True, returnErr=False)
        if not pgSoup: continue

        links = [a.get('href') for a in pgSoup.select('a[id^="job_"][href]')]
        for link in links: 
             if link[:1] == '/': link = f'{roorUrl}{link}'
             # soup = linkToSoup_scrapingAnt(link, isv=True, returnErr=False) # OR
             soup = linkToSoup_selenium(link, isv=True, returnErr=False) 
             if not soup: continue

             ####### EXTRACT DATA #######
             # try...soup.select_one....text.strip()...except...
             # links_list.append(....) # print(f'done ....') # t.sleep(1)

# df = pd.DataFrame....df.to_csv....
