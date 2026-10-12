# Code from my Stack Overflow answer https://stackoverflow.com/a/73957068 (posted 2022-10-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
expAnchor = soup.find(id="experience")
if expAnchor: #to avoid error, in case expAnchor = None
    expContainer = expAnchor.find_next('div', {"class": "pvs-list__outer-container"})

# --- block 2 ---
expContainer = soup.select_one('#experience ~ div.pvs-list__outer-container')
