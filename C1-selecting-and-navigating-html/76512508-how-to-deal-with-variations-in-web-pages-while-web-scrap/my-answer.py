# Code from my Stack Overflow answer https://stackoverflow.com/a/76544401 (posted 2023-06-24), extracted verbatim; may need the question's context to run.

# --- block 1 ---
MRP = soup.select_one('span:is(.a-price.a-text-price.a-size-base, .a-price.a-text-price) span')
MRP = MRP.text if MRP else ''

# --- block 2 ---
MRP = soup.select_one('span.a-price.a-text-price span')
MRP = MRP.text if MRP else ''
