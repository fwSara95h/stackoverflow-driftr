# Code from my Stack Overflow answer https://stackoverflow.com/a/74133843 (posted 2022-10-20), extracted verbatim; may need the question's context to run.

# --- block 1 ---
questions = soup.select('.s-post-summary.js-post-summary')

# --- block 2 ---
questions = soup.select('*[class="js-post-summary s-post-summary"]')

# --- block 3 ---
questions = soup.select('*[data-post-type-id="1"]')

# --- block 4 ---
questions = soup.select('*[id^="question-summary-"]')

# --- block 5 ---
for qLink in soup.select('*[data-post-type-id="1"] a.s-link'):
    print(qLink.get_text())

# --- block 6 ---
response = requests.get("https://stackoverflow.com/questions", timeout=5)
