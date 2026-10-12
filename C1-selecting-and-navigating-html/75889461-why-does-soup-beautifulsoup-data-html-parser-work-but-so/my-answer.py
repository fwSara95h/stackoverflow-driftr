# Code from my Stack Overflow answer https://stackoverflow.com/a/75895103 (posted 2023-03-31), extracted verbatim; may need the question's context to run.

# --- block 1 ---
with open(url, encoding="utf8") as f:
    data = f.read()

# --- block 2 ---
# soup = BeautifulSoup(open(url, encoding="utf8"), "html.parser") ## less safe
with open(url, encoding="utf8") as f: soup = BeautifulSoup(f, "html.parser")
