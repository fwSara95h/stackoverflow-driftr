# Code from my Stack Overflow answer https://stackoverflow.com/a/74331712 (posted 2022-11-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
selectors = [
    'span.badge.badge-secondary.ng-star-inserted',                                             #badge 
    'span.font-weight-bold span.ng-star-inserted:has(span[translate])',                        #issue 
    'span.font-weight-bold span.ng-star-inserted:last-child',                                  #date 
    'span.font-weight-bold ~ span.ng-star-inserted:-soup-contains(", ")',                      #publisher 
    'span.font-weight-bold ~ span.ng-star-inserted:-soup-contains(", ") + span.ng-star-inserted:-soup-contains(", ")', #city 
    'span.font-weight-bold ~ span.ng-star-inserted:-soup-contains(":")',                       #page 
]

# --- block 2 ---
desired_list = [None if s[0] is None else (
    s[0].get_text(' ', strip=True)[2:] if '-soup-contains' in s[1] 
    else s[0].get_text(' ', strip=True)
) for s in [(soup.select_one(sel), sel) for sel in selectors]]

# --- block 3 ---
soup = BeautifulSoup(html, "html5lib") # html_1, html_2, html_3
