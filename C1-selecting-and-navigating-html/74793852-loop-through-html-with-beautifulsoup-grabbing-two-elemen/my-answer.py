# Code from my Stack Overflow answer https://stackoverflow.com/a/74799439 (posted 2022-12-14), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for hr in soup.find_all('hr'):
    title = hr.find_next("li").b.text
    text = hr.find_next("li").contents[-1].strip(" .\n")

# --- block 2 ---
liList = [li for li in set([
    hr.find_next("li") for hr in soup.select('hr')
]) if li.b] # remove risk of error when getting title
for li in liList:
    title = li.b.text
    text = li.contents[-1].strip(" .\n")

# --- block 3 ---
text = [t for t in li.contents if isinstance(t, str)]
text = (text[-1] if text else '').strip(" .")

# --- block 4 ---
soup = BeautifulSoup(page.content, "html.parser")

with open("test1.txt", "w") as file:
    liList = [li for li in set([
        hr.find_next("li") for hr in soup.select('hr')
    ]) if li.b] # remove risk of error when getting title
    for li in liList:
        title = li.b.text
        text = [getattr(
            c, 'text', c if isinstance(c, str) else ''
        ) for c in li.contents]
        text = (text[-1] if text else '').strip(" .")
        file.write("Today in #Space #History- "+title+" "+text.strip()+"\n")
