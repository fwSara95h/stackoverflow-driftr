---
title: "BeautifulSoup - Scrape product and product variants and export it to csv"
site: stackoverflow
question_id: 74511414
answer_id: 74514110
url: https://stackoverflow.com/a/74514110
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-21T04:01:51Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74514110/revisions
accepted: true
score: 1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 159496796a5cf79d53631ebefbbc49e6f9b41a92fe08a3aa80335a2b24059af1
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74514110>, 2022-11-21; **accepted**; score 1. Text as retrieved 2026-10-12.

> every time I run that code the label_options column has always the same values which is the last one I am guessing

Are you sure that they don't just all happen to have the same set of options? It *shouldn't* be repeating since you're clearing the list with `labels = []` in the loop - although you can just append `label_options` *outside* the `for lab...` loop: 
```python
                    for lab in label_option_list:
                        labels.append(lab["label"])

                    d["label_options"] = labels
```
instead of updating it for every label in `label_option_list`.

---
---

Anyway, I think your main issue is on the part where you want separate rows for each variant, and I *can* help a bit there. 
> Can anyone help me figure out the best way to get the expected output

I don't know if this is the *best* way, but this how I would get the maximum amount of information from the JSON in the script:

---

For this example, I copied the JSON inside the `script` tag from the html snippet in your question (to a variable `pasted_jstr`) as well as some of your output to set `d` and `dataJC` with 
```python
dataj = json.loads(pasted_jstr)
dataJC = dataj['[data-role=swatch-option-111105]']['Magento_Swatches/js/swatch-renderer']['jsonConfig']

# from io import StringIO
csvStr = '''
Scraped_Date,Scraped_Time,product_name,price,old_price,ratings,number_of_reviews,productSKU,productSize,priceWithoutTax,lifeStage,label_options
11/21/2022, 00:31:47,Black Hawk Fish And Potato Adult Dog Food,189.99,N/A,N/A,N/A,black-hawk-fish-&-potato-adult-dog-food,,172.72,Adult,"['10kg', '20kg', '3kg']"
'''.split('\n')
d = dict(zip(csvStr[1].split(',')[:-1], csvStr[2].split(',')))
```

---
and then
```python
productId = dataJC['productId']
jcInfs = [{
    'productId': productId, 'optionKey': k, 'sku': '?',
    'index': v['1299'] if '1299' in v else None
} for k, v in dataJC['index'].items()] 
orInfs = [
    ('optionPrices', 'amount', 'reverseNest'), 
    ('dynamic', 'value', 'nest1'),
    ('labels', '', 'reverseNest'),
    ('hasEndDate', '', 'noNesting')
]
relevInfs = []
for kk, vk, nt in orInfs:
    if kk not in dataJC: continue
    if nt == 'noNesting':
        relevInfs += [(kk, vk, dataJC[kk])]
        continue
    
    if nt == 'nest1':
        relevInfs += [(kk, vk, vd) for kk, vd in dataJC[kk].items()]
        continue
    
    if nt != 'reverseNest':
        ## can put a default action here
        continue
    
    ## nt == 'reverseNest'
    orInf = {}
    for pk, po in dataJC[kk].items():
        for kpo, vpo in po.items():
            if kpo not in orInf: orInf[kpo] = {}
            orInf[kpo][pk] = vpo
    relevInfs += [(kk, vk, vi) for kk, vi in orInf.items()]
    
for i, j in enumerate(jcInfs):
    for kk, vk, vd in relevInfs:
        if j['optionKey'] not in vd: continue
        relevInf = vd[j['optionKey']]
        if type(relevInf) != dict: j[kk] = relevInf
        elif vk in relevInf and relevInf[vk]: j[kk] = relevInf[vk]
    
    # combine with main variation
    jcInfs[i] = {k:v for k, v in (list(d.items()) + [
        (jk, jv) for jk, jv in j.items() if jk not in d
    ])}
```
You can set `orInfs` somewhere outside the loops and add in any keys [with which you want to get info from the json], and you can also add the actions for new formats/`nt` ("nesting type") into the `for kk, vk, nt in orInfs` loop. (You can also separate the loop out into its own function...)

<sub>I was able to print the table below with `print(pd.DataFrame(jcInfs).to_markdown(index=False))`</sub>
```lang-none
| Scraped_Date   | Scraped_Time   | product_name                              |   price | old_price   | ratings   | number_of_reviews   | productSKU                              | productSize   |   priceWithoutTax | lifeStage   |   productId |   optionKey |    sku |   index |   baseOldPrice |   oldPrice |   basePrice |   finalPrice | tierPrices   | name                                             | product_category   | brand_filter   | size   | health_benefits   | life_stage   | flavour   | australia_made   | nutrition_grade   | weight_control   | sales_flag_label   | hasEndDate   |
|:---------------|:---------------|:------------------------------------------|--------:|:------------|:----------|:--------------------|:----------------------------------------|:--------------|------------------:|:------------|------------:|------------:|-------:|--------:|---------------:|-----------:|------------:|-------------:|:-------------|:-------------------------------------------------|:-------------------|:---------------|:-------|:------------------|:-------------|:----------|:-----------------|:------------------|:-----------------|:-------------------|:-------------|
| 11/21/2022     | 00:31:47       | Black Hawk Fish And Potato Adult Dog Food |  189.99 | N/A         | N/A       | N/A                 | black-hawk-fish-&-potato-adult-dog-food |               |            172.72 | Adult       |      111105 |      108987 | 127956 |    6234 |        49.9909 |      54.99 |     42.7182 |        46.99 | []           | Black Hawk Fish And Potato Adult Dog Food - 3kg  | Dry Food           | Black Hawk     | 3kg    | Total Wellbeing   | Adult        | Fish      | No               | Premium           | No               | Great low price    | False        |
| 11/21/2022     | 00:31:47       | Black Hawk Fish And Potato Adult Dog Food |  189.99 | N/A         | N/A       | N/A                 | black-hawk-fish-&-potato-adult-dog-food |               |            172.72 | Adult       |      111105 |      108981 | 127960 |    6780 |       172.718  |     189.99 |    128.173  |       140.99 | []           | Black Hawk Fish And Potato Adult Dog Food - 20kg | Dry Food           | Black Hawk     | 20kg   | Total Wellbeing   | Adult        | Fish      | No               | Premium           | No               | Great low price    | False        |
| 11/21/2022     | 00:31:47       | Black Hawk Fish And Potato Adult Dog Food |  189.99 | N/A         | N/A       | N/A                 | black-hawk-fish-&-potato-adult-dog-food |               |            172.72 | Adult       |      111105 |      116724 | 501600 |    6651 |       120.9    |     132.99 |    102.718  |       112.99 | []           | Black Hawk Fish & Potato Dog Food 10kg           | Dry Food           | Black Hawk     | 10kg   | Total Wellbeing   | Adult        | Fish      | No               | Premium           | No               | Great low price    | False        |
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[X-somtheing](https://stackoverflow.com/users/18183763)** (2022-11-21): @Drfitr95 I tried your approach and it matches the expected output but it is only fetching one single product not all of them. I have update the question with the code I tried with your approach. Can you please look into this? Thank you!
- **me** (2022-11-21): @X-somtheing sorry I forgot to mention the last part of incorporating my solution into your code. You still need to add to `all_info`, but `jcInfs` is the like the new `d` - it's multiple rows though, so you can add instead of appending; where you had `self.all_info.append(d)`, you should now have **`self.all_info += jcInfs`** (*although you can also do `for j in jcInfs: self.all_info.append(j)` instead*). I hope it works now. Please let me know
- **me** (2022-11-21): @X-somtheing Btw, you can still save with `pd.DataFrame(self.all_info).fillna("").to_csv(f"{today}_petbarn.csv", index=False)` but it should be *outside* of all the loops, at the end of `parse()` - or even in just save *`scraper.all_info`* at the end of *`__main__`*. It's just important to remember that `jcInfs` only contains *all the variants of **one** product*, and `all_info` is what should have all the products [with the current code at least]
- **[X-somtheing](https://stackoverflow.com/users/18183763)** (2022-11-21): Great! Thank you so much for the explanation. There is still one issue with main dixtionary `d` and primary dictionary `jcInfs` they are not intacted with each othe for example `product_name` rows keeps repeating where `name` rows which is coming from `jcInfs` only have 3 rows. And I am looking to have `product_name` rows repeat per variation. Any chance we can achieve that?
- **[X-somtheing](https://stackoverflow.com/users/18183763)** (2022-11-21): I have updated the code above with `for j in jcInfs: self.all_info.append(j)`
- **[X-somtheing](https://stackoverflow.com/users/18183763)** (2022-11-21): I figured it out why product_name rows were repeating I forgot I was running it under the loop `for idx in range(len(titles)):` removed the loop and it is working fine but now question is how to get those products which do not have variations it will be better to have a separate question for this.
- **me** (2022-11-21): @X-somtheing `self.all_info.append(d)` should take care of the ones without variants - [here's a version with my corrections](https://pastebin.com/eH2wmF7X) (all my changes are marked with `#!#`; as it is, the products with variants will have one extra row from `d` as it is before adding variants, but the version without the extra row is in comment)
- **me** (2022-11-21): @X-somtheing If you're interested, I also had [some suggested changes](https://pastebin.com/pN3GGzEe) beyond the corrections; the way you're doing it is actually a bit dangerous - it will raise an exception if any of the html elements are missing, and also, they might not line up perfectly, especially the ratings, reviews and lastprice, so it's better to find the container element (from which you're already getting `product_ids`), and then search for each product detail within that container element
- **me** (2022-11-21): ( If you want to discuss further, we can [continue this discussion in chat](https://chat.stackoverflow.com/rooms/249784/discussion-between-driftr95-and-x-somtheing). )
- **[X-somtheing](https://stackoverflow.com/users/18183763)** (2022-11-21): Amazing! I really like your suggestions in my code and I am going to keep that one it is really cool and beyond my expectations. Appreciate your efforts and thank you so much for putting your time into this really appreciated!
- **[X-somtheing](https://stackoverflow.com/users/18183763)** (2023-01-20): I have a another question regarding scraping this website https://stackoverflow.com/questions/75190026/beautifulsoup-scrape-product-and-product-price-per-variants-json-parsing-and-e . Please if you have some time can you take a look at it?
