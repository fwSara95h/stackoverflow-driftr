# Code from my Stack Overflow answer https://stackoverflow.com/a/75102700 (posted 2023-01-12), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def get_Hotel_Facilities(soup):
    selectors = ['div[data-testid="property-highlights"]', '#facilities', 
                 '.hp-description~div div.important_facility']
    new_list = []
    for sel in selectors:
        for sect in soup.select(sel): 
            new_list += list(sect.stripped_strings)
    return list(set(new_list)) # set <--> unique

# --- block 2 ---
for i in range(10):
    soup = BeautifulSoup(cloudscraper.create_scraper().get(url).content)
    fl = get_Hotel_Facilities(soup) if soup else []
    print(f'[{i}] {len(fl)} facilities: {", ".join(fl)}')
