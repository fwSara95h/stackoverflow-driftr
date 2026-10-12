# Code from my Stack Overflow answer https://stackoverflow.com/a/75051095 (posted 2023-01-08), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> officials = soup.findAll("table",{"id":"property-history"})
>

# --- block 2 ---
officials = soup.find_all("div", {"id":"property-history"})
