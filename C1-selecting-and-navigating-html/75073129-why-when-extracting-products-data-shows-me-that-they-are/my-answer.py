# Code from my Stack Overflow answer https://stackoverflow.com/a/75074128 (posted 2023-01-10), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>     for i in range(len(brand)):
>         brands.append(brand[i].text)
>         filelist = ([titles, brands, prices, rates, rate_starts, productlink])
>         exported = zip_longest(*filelist)
>         with open('oo.csv', 'w' , encoding ='utf-8-sig' , newline='') as filecsv:
>             wr = csv.writer(filecsv)
>             wr.writerow(['title','brands','price','offer','rate','rate_starts','productlink'])
>             wr.writerows(exported)
>

# --- block 2 ---
>         except: title='non'
>

# --- block 3 ---
>         except: price = 'non'
>

# --- block 4 ---
>         except: offer='non'
>

# --- block 5 ---
>         except: rate = 'non'
>

# --- block 6 ---
>         except: rate_start = 'non'
>

# --- block 7 ---
>     brand = productlist.find_all('h3', class_='brand-product mb-1')
>     for i in range(len(brand)):
>         brands.append(brand[i].text)
>

# --- block 8 ---
# for link in productlink:
    # r = requests.get(link , headers=headers)
    # soup = BeautifulSoup(r.content,'lxml')

    # brand = soup.find(lambda t: t.name=='a' and t.parent.name=='h2')`)
    brand = soup.select_one('h2>a')
    brands.append(brand.text.strip() if brand else 'non')
