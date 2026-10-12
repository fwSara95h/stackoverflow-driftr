# Code from my Stack Overflow answer https://stackoverflow.com/a/74277990 (posted 2022-11-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
print(souped.find(class_="propertyItem_13").get_text('\n').strip())

# --- block 2 ---
print(html_to_text(souped.find(class_="propertyItem_13"))[1])
