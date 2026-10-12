# Code from my Stack Overflow answer https://stackoverflow.com/a/74257730 (posted 2022-10-31), extracted verbatim; may need the question's context to run.

# --- block 1 ---
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# --- block 2 ---
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
