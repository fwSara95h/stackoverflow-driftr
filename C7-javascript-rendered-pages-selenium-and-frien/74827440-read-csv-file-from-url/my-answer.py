# Code from my Stack Overflow answer https://stackoverflow.com/a/74827588 (posted 2022-12-16), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# driver.get(start_urls) # NOT like this
for sUrl in start_urls:
    driver.get(sUrl)
    ### SCRAPE AS NEEDED ###

# --- block 2 ---
suLen = len(start_urls)
for si, sUrl in enumerate(start_urls):
    print(f'[{si} of {suLen}] reading {sUrl}')
    driver.get(sUrl)
    ### SCRAPE AS NEEDED ###

# --- block 3 ---
with open("data.csv") as file:
    start_urls=[line.strip() for line in file]  

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

suLen = len(start_urls)
for si, sUrl in enumerate(start_urls):
    print(f'[{si} of {suLen}] reading {sUrl}')
    driver.get(sUrl)
    ### SCRAPE AS NEEDED ###
