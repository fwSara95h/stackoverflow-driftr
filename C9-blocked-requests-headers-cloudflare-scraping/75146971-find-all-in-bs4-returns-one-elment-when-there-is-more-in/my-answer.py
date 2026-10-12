# Code from my Stack Overflow answer https://stackoverflow.com/a/75154564 (posted 2023-01-18), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> r = requests.get('https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-2x-> 12g-oc/p/N82E16814137632?Description=gpu&cm_re=gpu-_-14-137-632-_-Product')
> print(f'<{r.status_code} {r.reason}> from {r.url}')
> # soup = bs(r.content , 'lxml')
>

# --- block 2 ---
the_rating = soup.select('.rating.rating-4') # shorter than 
# .find_all(lambda t: {'rating', 'rating-4'}.issubset(set(t.get('class', []))))
