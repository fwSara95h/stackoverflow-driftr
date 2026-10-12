# Code from my Stack Overflow answer https://stackoverflow.com/a/75062460 (posted 2023-01-09), extracted verbatim; may need the question's context to run.

# --- block 1 ---
response = cloudscraper.create_scraper().get(URL)

# --- block 2 ---
response = HTMLSession().get(URL)
