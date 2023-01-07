---
title: "Python Beautifulsoup4 all parser not working?"
site: stackoverflow
question_id: 75037029
answer_id: 75038864
url: https://stackoverflow.com/a/75038864
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-07T07:53:17Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75038864/revisions
accepted: true
score: 0
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-json-in-script
helpers_referenced: [findObj_inJS, getNestedVal]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a607ac52f1ec50cf54b29ccb97a0a7c01763a5962c2281b09523b7b17e9ce3e8
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75038864>, 2023-01-07; **accepted**; score 0. Text as retrieved 2026-10-12.

I don't think there's anything wrong with your parser.

Some notes about my tests:
- `i = 19` when I ran my tests
- so `url` was formed as <sub> https://www.aliexpress.com/af/Air-Purifiers.html?spm=a2g0o.productlist.10000020initiative_id=SB_20230106091400&dida=y&origin=n </sub>
- but when I ran *`print(f'{page.status_code} {page.reason} from {page.url}')`* to check the response, the output indicated a redirect somewhere
  > 200 OK from <sub> https://www.aliexpress.com/wholesale?SearchText=Air%2BPurifiers&spm=a2g0o.productlist.10000020initiative_id%3DSB_20230106091400&origin=n&dida=y </sub>
- I also ran *`with open('x.html', 'wb') as f: f.write(page.content)`*, but when I open "x.html" on my browser, it [looked like this](https://i.sstatic.net/eVhCL.png) even though the [products show up](https://i.sstatic.net/1CBZf.png) (with the classes used in your code too) when I rendered it with [`IPython.display.HTML`](https://ianlondon.github.io/blog/render_html_in_ipython_notebook/#rendering-the-selected-html-in-the-notebook)

This indicates that the elements you're targeting are **rendered with JavaScript**, and that's why they're not found.

---

The data you want seems to be [in one of the `script` tags](https://i.sstatic.net/w1Tac.png) though. I could target that tag with 

```python
scriptTag = soup.select_one('meta[name="aplus-auto-exp"]~script')
```

and if any other parser was not used, the JavaScript code could probably be gotten simply with *`jScript = scriptTag.get_text()`*, but with `html5lib` parser I had to stringify and strip the tag name:

```python
jScript = scriptTag.prettify().strip()
jScript = jScript.strip('<script').split('>', 1)[-1].strip('</script>').strip()
```

---

And then I extracted the list of products with **[`findObj_inJS`](https://pastebin.com/UVcLniSG)**, which uses [slimit](https://slimit.readthedocs.io/en/latest/) to parse JavaScript:

```python
itemList = findObj_inJS(jScript, '"itemList"')['content']
```

`itemList` contained 60 items. The first 2 items are prettified as JSON below:

```json
[
    {
        "itemType": "productV3",
        "productType": "natural",
        "nativeCardType": "nt_srp_cell_g",
        "itemCardType": "manhattan",
        "productId": "3256804896450950",
        "lunchTime": "2022-12-20 00:00:00",
        "image": {
            "imgUrl": "//ae01.alicdn.com/kf/S39f71cffe79a4a6981083f57128103c9d/Anti-Gravity-Humidifier-Diffuser-Water-Drop-Falling-Remote-Control-Mini-Mist-Maker-Humidifier-Air-Purifiers-Droplets.jpg_220x220xz.jpg",
            "imgWidth": 220,
            "imgHeight": 220,
            "imgType": "0"
        },
        "title": {
            "seoTitle": "Anti Gravity Humidifier Diffuser Water Drop Falling Remote Control Mini Mist Maker Humidifier Air Purifiers Droplets Upflow USB",
            "displayTitle": "Anti Gravity Humidifier Diffuser Water Drop Falling Remote Control Mini Mist Maker Humidifier Air Purifiers Droplets Upflow USB",
            "shortTitle": false
        },
        "prices": {
            "skuId": "12000031580241123",
            "pricesStyle": "default",
            "builderType": "skuCoupon",
            "currencySymbol": "US $",
            "prefix": "Sale price:",
            "salePrice": {
                "discount": -1,
                "minPriceDiscount": 50,
                "priceType": "sale_price",
                "currencyCode": "USD",
                "minPrice": 26,
                "minPriceType": 2,
                "formattedPrice": "US $26.00"
            },
            "taxRate": "0"
        },
        "sellingPoints": [
            {
                "sellingPointTagId": "m0000063",
                "tagStyleType": "default",
                "tagContent": {
                    "displayTagType": "text",
                    "tagText": "Extra 1% off with coins",
                    "tagStyle": {
                        "color": "#FD384F",
                        "position": "2"
                    }
                },
                "source": "flexiCoin_new_atm"
            },
            {
                "sellingPointTagId": "m0000064",
                "tagStyleType": "default",
                "tagContent": {
                    "displayTagType": "text",
                    "tagText": "Free Shipping",
                    "tagStyle": {
                        "color": "#009966",
                        "position": "4"
                    }
                },
                "source": "Free_Shipping_atm"
            }
        ],
        "store": {
            "storeId": 1102377281,
            "aliMemberId": 2668032633,
            "storeName": "Yousmile Life Store",
            "storeUrl": "//www.aliexpress.com/store/1102377281"
        },
        "trace": {
            "pdpParams": {
                "pdp_cdi": "%7B%22traceId%22%3A%22212243c016730635978473504d06bf%22%2C%22itemId%22%3A%223256804896450950%22%2C%22fromPage%22%3A%22search%22%2C%22skuId%22%3A%2212000031580241123%22%2C%22shipFrom%22%3A%22US%22%2C%22order%22%3A%220%22%2C%22star%22%3A%22%22%2C%22freeShip%22%3A%22true%22%7D",
                "pdp_npi": "2%40dis%21USD%2152.0%2126.0%21%21%21%21%21%40212243c016730635978473504d06bf%2112000031580241123%21sea",
                "pdp_perf": "main_img=%2F%2Fae01.alicdn.com%2Fkf%2FS39f71cffe79a4a6981083f57128103c9d.jpg",
                "pdp_ext_f": "%7B%22sku_id%22%3A%2212000031580241123%22%7D"
            },
            "exposure": {
                "displayCategoryId": "",
                "postCategoryId": "625",
                "selling_point": "m0000063,m0000064",
                "algo_exp_id": "77f9a225-26b3-4384-990c-3f411893324d-0"
            },
            "click": {
                "algo_pvid": "77f9a225-26b3-4384-990c-3f411893324d",
                "haveSellingPoint": "true"
            },
            "detailPage": {
                "algo_pvid": "77f9a225-26b3-4384-990c-3f411893324d",
                "algo_exp_id": "77f9a225-26b3-4384-990c-3f411893324d-0"
            },
            "custom": {},
            "utLogMap": {
                "original_price_type": "offer",
                "formatted_price": "US $26.00",
                "csp": "26.0,1",
                "x_object_type": "productV3",
                "algo_pvid": "77f9a225-26b3-4384-990c-3f411893324d",
                "hit_19_forbidden": false,
                "is_detail_next": "1",
                "model_ctr": 0.06788578629493713,
                "sku_id": "12000031580241123",
                "mixrank_success": "false",
                "custom_group": 3,
                "sku_ic_tags": "[]",
                "is_adult_certified": false,
                "mixrank_enable": "false",
                "ump_atmospheres": "none",
                "oip": "52.0,0",
                "selling_point": "m0000063,m0000064",
                "original_price_strategy": "sku_opt",
                "x_object_id": "1005005082765702"
            }
        }
    },
    {
        "itemType": "productV3",
        "productType": "natural",
        "nativeCardType": "nt_srp_cell_g",
        "itemCardType": "manhattan",
        "productId": "3256803823899352",
        "lunchTime": "2022-03-09 00:00:00",
        "image": {
            "imgUrl": "//ae01.alicdn.com/kf/S5d14059b4d364bf5a41d2c08a5d6e735y/Portable-Air-Purifier-Anion-Air-Purification-Xiomi-Air-Freshener-Ionizer-Cleaner-Dust-Cigarette-Smoke-Remover-Toilet.jpg_220x220xz.jpg",
            "imgWidth": 220,
            "imgHeight": 220,
            "imgType": "0"
        },
        "title": {
            "seoTitle": "Portable Air Purifier Anion Air Purification Xiomi Air Freshener Ionizer Cleaner Dust Cigarette Smoke Remover Toilet Deodorant",
            "displayTitle": "Portable Air Purifier Anion Air Purification Xiomi Air Freshener Ionizer Cleaner Dust Cigarette Smoke Remover Toilet Deodorant",
            "shortTitle": false
        },
        "prices": {
            "skuId": "12000027730379754",
            "pricesStyle": "default",
            "builderType": "skuCoupon",
            "currencySymbol": "US $",
            "prefix": "Sale price:",
            "originalPrice": {
                "priceType": "original_price",
                "currencyCode": "USD",
                "minPrice": 20.8,
                "minPriceType": 1,
                "formattedPrice": "US $20.80"
            },
            "salePrice": {
                "discount": -1,
                "minPriceDiscount": 95,
                "priceType": "sale_price",
                "currencyCode": "USD",
                "minPrice": 0.99,
                "minPriceType": 2,
                "formattedPrice": "US $0.99"
            },
            "taxRate": "0"
        },
        "sellingPoints": [
            {
                "sellingPointTagId": "m0000040",
                "tagStyleType": "default",
                "tagContent": {
                    "displayTagType": "image",
                    "tagImgUrl": "https://ae01.alicdn.com/kf/S8cbad032762b405b8ebd8f30bca4bc83u/338x64.png",
                    "tagImgWidth": 338,
                    "tagImgHeight": 64,
                    "tagStyle": {
                        "color": "#FD384F",
                        "position": "1"
                    }
                },
                "source": "new_user_platform_allowance_atm"
            },
            {
                "sellingPointTagId": "m0000064",
                "tagStyleType": "default",
                "tagContent": {
                    "displayTagType": "text",
                    "tagText": "Free Shipping",
                    "tagStyle": {
                        "color": "#009966",
                        "position": "4"
                    }
                },
                "source": "Free_Shipping_atm"
            },
            {
                "sellingPointTagId": "1000013764",
                "tagStyleType": "default",
                "tagContent": {
                    "displayTagType": "text",
                    "tagText": "Free Return",
                    "tagStyle": {
                        "color": "#009966",
                        "position": "4"
                    }
                },
                "source": "Free_return_atm"
            }
        ],
        "evaluation": {
            "starRating": 4.4,
            "starUrl": "https://ae01.alicdn.com/kf/S567d6bf538214abf95c1e5825c7e6a05t/48x48.png",
            "starWidth": 48,
            "starHeight": 48
        },
        "trade": {
            "tradeDesc": "1340 sold"
        },
        "store": {
            "storeId": 1101982761,
            "aliMemberId": 2657161543,
            "storeName": "BOYALIGE Official Store",
            "storeUrl": "//www.aliexpress.com/store/1101982761"
        },
        "trace": {
            "pdpParams": {
                "pdp_cdi": "%7B%22traceId%22%3A%22212243c016730635978473504d06bf%22%2C%22itemId%22%3A%223256803823899352%22%2C%22fromPage%22%3A%22search%22%2C%22skuId%22%3A%2212000027730379754%22%2C%22shipFrom%22%3A%22CN%22%2C%22order%22%3A%221340%22%2C%22star%22%3A%224.4%22%2C%22freeShip%22%3A%22true%22%2C%22shipSellingPoint%22%3A%22freeReturn%22%7D",
                "pdp_npi": "2%40dis%21USD%2120.8%210.99%21%21%21%21%21%40212243c016730635978473504d06bf%2112000027730379754%21sea",
                "pdp_perf": "main_img=%2F%2Fae01.alicdn.com%2Fkf%2FS5d14059b4d364bf5a41d2c08a5d6e735y.jpg",
                "pdp_ext_f": "%7B%22sku_id%22%3A%2212000027730379754%22%7D"
            },
            "exposure": {
                "displayCategoryId": "",
                "postCategoryId": "613",
                "selling_point": "m0000040,m0000064,1000013764",
                "algo_exp_id": "77f9a225-26b3-4384-990c-3f411893324d-1"
            },
            "click": {
                "algo_pvid": "77f9a225-26b3-4384-990c-3f411893324d",
                "haveSellingPoint": "true"
            },
            "detailPage": {
                "algo_pvid": "77f9a225-26b3-4384-990c-3f411893324d",
                "algo_exp_id": "77f9a225-26b3-4384-990c-3f411893324d-1"
            },
            "custom": {},
            "utLogMap": {
                "original_price_type": "offer",
                "formatted_price": "US $0.99",
                "csp": "0.99,1",
                "x_object_type": "productV3",
                "algo_pvid": "77f9a225-26b3-4384-990c-3f411893324d",
                "hit_19_forbidden": false,
                "is_detail_next": "1",
                "model_ctr": 0.21320748329162598,
                "sku_id": "12000027730379754",
                "mixrank_success": "false",
                "custom_group": 3,
                "sku_ic_tags": "[]",
                "is_adult_certified": false,
                "mixrank_enable": "false",
                "ump_atmospheres": "new_user_platform_allowance,none",
                "oip": "20.8,1",
                "selling_point": "m0000040,m0000064,1000013764",
                "original_price_strategy": "sku_opt",
                "x_object_id": "1005004010214104"
            }
        },
        "config": {
            "prices": {
                "color": "#FD384F"
            }
        }
    }
]
```

---

You could write a function to reduce it to only the information you want, something like:

```python
def reduceProductInfo(origInf): 
    try: prodId = origInf['productId']
    except: return {'errorMsg': 'productId expected', 'orig': origInf}
    pDets = {
        'id': prodId, 'link': f'https://www.aliexpress.com/item/{prodId}.html'
    }
    try: pDets['title'] = origInf["title"]["displayTitle"]
    except Exception as e: pDets['title'] = f'!{type(e)} - {e}!'
    try: pDets['salePrice'] = origInf["prices"]["salePrice"]["formattedPrice"]
    except Exception as e: pDets['salePrice'] = f'!{type(e)} - {e}!'
    try: pDets['imageLink'] = origInf["image"]["imgUrl"]
    except Exception as e: pDets['imageLink'] = f'!{type(e)} - {e}!'
    if pDets['imageLink'][:2] == '//': 
        pDets['imageLink'] = f"https:{pDets['imageLink']}"
    return pDets
```

and then just reduce the whole list with

```python
productList = [reduceProductInfo(item) for item in itemList]
```

the first 5 items of `productList` would [look like this](https://i.sstatic.net/Gh5Jb.png).

If you want to go with this approach, you might want to check out my [`getNestedVal`](https://pastebin.com/NRxKRJPn) function as well - it's rather useful for quickly figuring out the sequence of keys and indices needed to get a nested value.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[OFENROHR100](https://stackoverflow.com/users/15020314)** (2023-01-07): Your solution definitly works (Thank You! )but currently there seems to be a problem with slimit.     import slimit   File "/home/opc/.local/lib/python3.9/site-packages/slimit/__init__.py", line 2                                                                                                                                                             7, in <module>     from minifier import minify ModuleNotFoundError: No module named 'minifier'  This is the newest version.
- **me** (2023-01-07): @OFENROHR100 did you just `pip install slimit` (that works ok for me so far) or `pip install git+https://github.com/rspivak/slimit.git#egg=slimit`? whichever you used, maybe you could uninstall and try the other one? beyond that, I don't really know - tbh this is something I've been rather afraid of for a while since many of my scrapers depend on this function and I've been too lazy to learn another js parser and rewrite it....
- **me** (2023-01-07): If slimit can't be used, I guess you could just go with good old fashioned string manipulation - I'm not very good at it so I can't think of anything more elegant than `itemList = json.loads(jScript.split('window._dida_config_._init_data_', 1)[-1].strip('=').strip(';').strip()[1:-1].strip().strip('data').strip(':').strip())['data']['root']['fields']['mods']['itemList']['content']` and it's quite risky since it could stop working with very minor changes, but it [should give the same results](https://i.sstatic.net/47e1R.png)
