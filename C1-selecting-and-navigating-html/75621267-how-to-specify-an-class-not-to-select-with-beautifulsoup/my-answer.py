# Code from my Stack Overflow answer https://stackoverflow.com/a/75643095 (posted 2023-03-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
bs.select('[href*="str"]:not(.footer-wikiwalk-nav)')

# --- block 2 ---
bs.find_all(href=lambda h: h and "str" in h, class_= lambda c: 'footer-wikiwalk-nav' not in c.split())
