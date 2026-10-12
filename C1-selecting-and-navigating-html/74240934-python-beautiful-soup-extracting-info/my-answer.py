# Code from my Stack Overflow answer https://stackoverflow.com/a/74241299 (posted 2022-10-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# t3selector = ....
t3 = soup.select_one(t3selector).get_text(strip=True)

# --- block 2 ---
t3selector = 'h3:-soup-contains("Investment") ~ * .amount'

# --- block 3 ---
t3selector = 'h3:-soup-contains("Investment") + * + p span'

# --- block 4 ---
t3 = soup.find(
    lambda tag:tag.name=="h3" and "Investment" in tag.text
).find_next_sibling("p").find("span").get_text(strip=True)

# --- block 5 ---
t3 = soup.select_one(t3selector)
if t3 is not None: t3 = t3.get_text(strip=True)
