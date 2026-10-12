# Code from my Stack Overflow answer https://stackoverflow.com/a/74293587 (posted 2022-11-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
username = doc.find_all('span', attrs={'class':'lia-component-message-view-widget-author-username'})

# --- block 2 ---
all_data = []
for u, t, d, m in zip(username, time, date, article):
    if d.get_text(strip=True)[1:] == '10-25-2022': 
        all_data.append([
            u.get_text(strip=True) , 
            t.text, 
            d.get_text(strip=True),
            m.get_text(strip=True, separator='\n')
        ])

# --- block 3 ---
all_data = [[
        u.get_text(strip=True), 
        t.text, 
        d.get_text(strip=True),
        m.get_text(strip=True, separator='\n')
    ] for u, t, d, m in zip(uname, time, date, article)
    if d.get_text(strip=True)[1:] == '10-25-2022'
]
