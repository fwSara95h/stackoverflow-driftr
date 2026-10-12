# Code from my Stack Overflow answer https://stackoverflow.com/a/74678043 (posted 2022-12-04), extracted verbatim; may need the question's context to run.
for li in soup.select("li:not(li li)"): 
    print(" ".join([
        d.get_text().strip() for d in li.descendants 
        if 'NavigableString' in str(type(d)) and 
        d.parent.name == 'li' and d.get_text().strip()
    ])) 
    print("--sep--")

# for the p tags after ANY of the [outermost] li tags
for p in soup.select("li:not(li li) ~ p"):  print(p.text.strip(), "\n--sep--")
