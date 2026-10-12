# Code from my Stack Overflow answer https://stackoverflow.com/a/74779366 (posted 2022-12-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for test2 in soup.find_all(class_="fighter left_side"): 
    Fighter1Main += [t for t in test2.find_all(itemprop="url")]

# --- block 2 ---
for test2 in soup.select('.fighter.left_side *[itemprop="url"]:not(:has(*))'): 
    Fighter1Main.append(test2)

# --- block 3 ---
for test2 in soup.select('.fighter.left_side *[itemprop="url"]'): 
    test2.clear()
    Fighter1Main.append(test2)

# --- block 4 ---
soup = BeautifulSoup(response, "html.parser")
Fighter1Main += [BeautifulSoup(
    f'<{n}{h} itemprop="url"></{n}>', "html.parser"
).find(n) for n, h in [(
    t.name, '' if t.get("href") is None else f' href="{t.get("href")}"'
) for t in soup.select('.fighter.left_side *[itemprop="url"]')]]
