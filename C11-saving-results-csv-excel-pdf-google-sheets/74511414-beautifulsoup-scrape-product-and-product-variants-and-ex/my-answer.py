# Code from my Stack Overflow answer https://stackoverflow.com/a/74514110 (posted 2022-11-21), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for lab in label_option_list:
    labels.append(lab["label"])

d["label_options"] = labels

# --- block 2 ---
dataj = json.loads(pasted_jstr)
dataJC = dataj['[data-role=swatch-option-111105]']['Magento_Swatches/js/swatch-renderer']['jsonConfig']

# from io import StringIO
csvStr = '''
Scraped_Date,Scraped_Time,product_name,price,old_price,ratings,number_of_reviews,productSKU,productSize,priceWithoutTax,lifeStage,label_options
11/21/2022, 00:31:47,Black Hawk Fish And Potato Adult Dog Food,189.99,N/A,N/A,N/A,black-hawk-fish-&-potato-adult-dog-food,,172.72,Adult,"['10kg', '20kg', '3kg']"
'''.split('\n')
d = dict(zip(csvStr[1].split(',')[:-1], csvStr[2].split(',')))

# --- block 3 ---
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

# --- block 4 ---
| Scraped_Date   | Scraped_Time   | product_name                              |   price | old_price   | ratings   | number_of_reviews   | productSKU                              | productSize   |   priceWithoutTax | lifeStage   |   productId |   optionKey |    sku |   index |   baseOldPrice |   oldPrice |   basePrice |   finalPrice | tierPrices   | name                                             | product_category   | brand_filter   | size   | health_benefits   | life_stage   | flavour   | australia_made   | nutrition_grade   | weight_control   | sales_flag_label   | hasEndDate   |
|:---------------|:---------------|:------------------------------------------|--------:|:------------|:----------|:--------------------|:----------------------------------------|:--------------|------------------:|:------------|------------:|------------:|-------:|--------:|---------------:|-----------:|------------:|-------------:|:-------------|:-------------------------------------------------|:-------------------|:---------------|:-------|:------------------|:-------------|:----------|:-----------------|:------------------|:-----------------|:-------------------|:-------------|
| 11/21/2022     | 00:31:47       | Black Hawk Fish And Potato Adult Dog Food |  189.99 | N/A         | N/A       | N/A                 | black-hawk-fish-&-potato-adult-dog-food |               |            172.72 | Adult       |      111105 |      108987 | 127956 |    6234 |        49.9909 |      54.99 |     42.7182 |        46.99 | []           | Black Hawk Fish And Potato Adult Dog Food - 3kg  | Dry Food           | Black Hawk     | 3kg    | Total Wellbeing   | Adult        | Fish      | No               | Premium           | No               | Great low price    | False        |
| 11/21/2022     | 00:31:47       | Black Hawk Fish And Potato Adult Dog Food |  189.99 | N/A         | N/A       | N/A                 | black-hawk-fish-&-potato-adult-dog-food |               |            172.72 | Adult       |      111105 |      108981 | 127960 |    6780 |       172.718  |     189.99 |    128.173  |       140.99 | []           | Black Hawk Fish And Potato Adult Dog Food - 20kg | Dry Food           | Black Hawk     | 20kg   | Total Wellbeing   | Adult        | Fish      | No               | Premium           | No               | Great low price    | False        |
| 11/21/2022     | 00:31:47       | Black Hawk Fish And Potato Adult Dog Food |  189.99 | N/A         | N/A       | N/A                 | black-hawk-fish-&-potato-adult-dog-food |               |            172.72 | Adult       |      111105 |      116724 | 501600 |    6651 |       120.9    |     132.99 |    102.718  |       112.99 | []           | Black Hawk Fish & Potato Dog Food 10kg           | Dry Food           | Black Hawk     | 10kg   | Total Wellbeing   | Adult        | Fish      | No               | Premium           | No               | Great low price    | False        |
