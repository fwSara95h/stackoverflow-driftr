---
title: "BeautifulSoup - Scrape product and product variants and export it to csv"
site: stackoverflow
question_id: 74511414
url: https://stackoverflow.com/q/74511414
asked: 2022-11-20T19:48:08Z
asked_by: "X-somtheing"
asked_by_url: https://stackoverflow.com/users/18183763
last_edited: 2022-11-21T09:47:33Z
tags: [python, python-3.x, csv, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 288
answer_count: 1
accepted_answer_id: 74514110
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 00f00bd76a3e62dd6022a176c734701db472d0e70948c8239594bb71c4e28e1e
---

# BeautifulSoup - Scrape product and product variants and export it to csv

Asked by [X-somtheing](https://stackoverflow.com/users/18183763) on Stack Overflow, <https://stackoverflow.com/q/74511414>, 2022-11-20, last edited 2022-11-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape this [website][1] products listing what I am trying to achieve here is grab all the info per product for example: product_name, price and their variants info as well like 10kg, 20kg, 3kg and their prices accordingly. I have search the html they don't provide all the info I am looking for but under script tag they have a json residing which could be useful. Here is the json script tag:

    </script><script type="text/x-magento-init">
            {
                "[data-role=swatch-option-111105]": {
                    "Magento_Swatches/js/swatch-renderer": {
                        "selectorProduct": ".product-item-details",
                        "onlySwatches": true,
                        "enableControlLabel": false,
                        "numberToShow": 16,
                        "jsonConfig": {"attributes":{"1299":{"id":"1299","code":"size","label":"Size","options":[{"id":"6651","label":"10kg","products":["116724"]},{"id":"6780","label":"20kg","products":["108981"]},{"id":"6234","label":"3kg","products":["108987"]}],"position":"0"}},"template":"$<%- data.price %>","currencyFormat":"$%s","optionPrices":{"108987":{"baseOldPrice":{"amount":49.990908090909},"oldPrice":{"amount":54.99},"basePrice":{"amount":42.718180818182},"finalPrice":{"amount":46.99},"tierPrices":[],"msrpPrice":{"amount":0}},"108981":{"baseOldPrice":{"amount":172.71818081818},"oldPrice":{"amount":189.99},"basePrice":{"amount":128.17272627273},"finalPrice":{"amount":140.99},"tierPrices":[],"msrpPrice":{"amount":0}},"116724":{"baseOldPrice":{"amount":120.899999},"oldPrice":{"amount":132.99},"basePrice":{"amount":102.71818081818},"finalPrice":{"amount":112.99},"tierPrices":[],"msrpPrice":{"amount":0}}},"priceFormat":{"pattern":"$%s","precision":2,"requiredPrecision":2,"decimalSymbol":".","groupSymbol":",","groupLength":3,"integerRequired":false},"prices":{"baseOldPrice":{"amount":49.990908090909},"oldPrice":{"amount":54.99},"basePrice":{"amount":172.71818081818},"finalPrice":{"amount":189.99}},"productId":"111105","chooseText":"Choose an Option...","images":[],"index":{"108987":{"1299":"6234"},"108981":{"1299":"6780"},"116724":{"1299":"6651"}},"preSelectedGallery":[],"channel":"website","salesChannelCode":"base","sku":{"108987":"127956","108981":"127960","116724":"501600"},"labels":{"108987":{"sales_flag_label":"Great low price"},"108981":{"sales_flag_label":"Great low price"},"116724":{"sales_flag_label":"Great low price"}},"hasEndDate":{"108987":false,"108981":false,"116724":false},"dynamic":{"name":{"108987":{"value":"Black Hawk Fish And Potato Adult Dog Food - 3kg"},"108981":{"value":"Black Hawk Fish And Potato Adult Dog Food - 20kg"},"116724":{"value":"Black Hawk Fish & Potato Dog Food 10kg"}},"sku":{"108987":{"value":"127956"},"108981":{"value":"127960"},"116724":{"value":"501600"}},"gtin":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"marketing_offer_short":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"advice_care":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"product_category":{"108987":{"value":"Dry Food"},"108981":{"value":"Dry Food"},"116724":{"value":"Dry Food"}},"benefits":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"feeding_guide":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"health_condition_dietary":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"brand_filter":{"108987":{"value":"Black Hawk"},"108981":{"value":"Black Hawk"},"116724":{"value":"Black Hawk"}},"ingredients":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"activity_level":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"size":{"108987":{"value":"3kg"},"108981":{"value":"20kg"},"116724":{"value":"10kg"}},"food_type":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"health_benefits":{"108987":{"value":"Total Wellbeing"},"108981":{"value":"Total Wellbeing"},"116724":{"value":"Total Wellbeing"}},"life_stage":{"108987":{"value":"Adult"},"108981":{"value":"Adult"},"116724":{"value":"Adult"}},"flavour":{"108987":{"value":"Fish"},"108981":{"value":"Fish"},"116724":{"value":"Fish"}},"nutritional_info":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"breed":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"nutritional_info_table":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"australia_made":{"108987":{"value":"No"},"108981":{"value":"No"},"116724":{"value":"No"}},"nutrition_grade":{"108987":{"value":"Premium"},"108981":{"value":"Premium"},"116724":{"value":"Premium"}},"lifestyle":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"weight_control":{"108987":{"value":"No"},"108981":{"value":"No"},"116724":{"value":"No"}},"frequent_feeder_price":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}},"size_swatches":{"108987":{"value":""},"108981":{"value":""},"116724":{"value":""}}}},
                        "jsonSwatchConfig": {"1299":{"6651":{"type":"0","value":null,"label":"10kg"},"6780":{"type":"0","value":null,"label":"20kg"},"6234":{"type":"0","value":null,"label":"3kg"},"additional_data":"{\"update_product_preview_image\":\"1\",\"use_product_image_for_swatch\":0,\"text_swatch_as_multiple_select\":\"1\",\"swatch_input_type\":\"text\"}"}},
                        "mediaCallback": "https\u003A\u002F\u002Fwww.petbarn.com.au\u002Fswatches\u002Fajax\u002Fmedia\u002F",
                        "jsonSwatchImageSizeConfig": {"swatchImage":{"width":30,"height":20},"swatchThumb":{"height":90,"width":110}},
                        "showTooltip": 1                }
                }
            }
        </script>

I have manage to parse that script tag and turned that into python dictionary via json.loads() but couldn't figure out the best way to extract info and export it to csv. here is my code so far:

    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    import json
    
    from datetime import datetime
    from datetime import date
    
    now = datetime.now()
    today = date.today()
    
    
    class PetBarnProdScraper:
    
        all_info = []
    
        def fetch(self, url):
            print(f"HTTP GET request to URL: {url}", end="")
            res = requests.get(url)
            print(f" | Status Code: {res.status_code}")
    
            return res
    
        def parse(self, response):
            soup = BeautifulSoup(response.text, "html.parser")
            product_urls = [a.get("href") for a in soup.select("a.product-item-link")]
            product_ids = [
                pid.get("id").split("-")[-1] for pid in soup.select("div.product-item-info")
            ]
            titles = [
                a.text.replace("\n", "").strip() for a in soup.select("a.product-item-link")
            ]
            old_price = [
                p.select_one("span.price").text for p in soup.select("span.old-price")
            ]
            ratings = [r.get("title") for r in soup.select("div.rating-result")]
            no_of_reviews = [review.text for review in soup.select("a.action.view")]
            data = (
                soup.select('script[type="text/x-magento-init"]')[3]
                .text.replace("\n", "")
                .strip()
            )
            data_json = json.loads(data)
            data_j = json.loads(
                data_json["*"]["Overdose_AdobeAnalytics/js/view/datalayer"]["datalayer"][0]
            )
    
            for idx in range(len(titles)):
                try:
                    ratings_count = ratings[idx]
                    reviews_count = no_of_reviews[idx]
                    last_price = old_price[idx]
                except:
                    ratings_count = "N/A"
                    reviews_count = "N/A"
                    last_price = "N/A"
                d = {
                    "Scraped_Date": now.strftime("%m/%d/%Y, %H:%M:%S").split(",")[0],
                    "Scraped_Time": now.strftime("%m/%d/%Y, %H:%M:%S").split(",")[1],
                    "product_name": titles[idx],
                    "price": data_j["PLP"]["products"][idx]["productPrice"],
                    "old_price": last_price,
                    "ratings": ratings_count,
                    "number_of_reviews": reviews_count,
                    "productSKU": data_j["PLP"]["products"][idx]["productSKU"],
                    "productSize": data_j["PLP"]["products"][idx]["productSize"],
                    "priceWithoutTax": data_j["PLP"]["products"][idx][
                        "productPriceLessTax"
                    ],
                    "lifeStage": data_j["PLP"]["products"][idx]["lifeStage"],
                }
    
                for prod_id in product_ids:
                    details = soup.select_one(
                        f"script:-soup-contains('[data-role=swatch-option-{prod_id}]')"
                    )
                    labels = []
                    if details:
                        json_details = json.loads(details.text.replace("\n", "").strip())
                        json_endpoint = json_details[f"[data-role=swatch-option-{prod_id}]"]
                        label_option_list = json_endpoint[
                            "Magento_Swatches/js/swatch-renderer"
                        ]["jsonConfig"]["attributes"]["1299"]["options"]
                        for lab in label_option_list:
                            labels.append(lab["label"])
    
                            d["label_options"] = labels
                print(d)
                self.all_info.append(d)
    
        def to_csv(self):
            df = pd.DataFrame(self.all_info).fillna("")
    
            df.to_csv(f"{today}_petbarn.csv", index=False)
    
            print('Stored results to "petbarn.csv"')
    
        def run(self):
            for i in range(1, 2):  # total_number of pages
                url = f"https://www.petbarn.com.au/dogs/dog-food/dry-dog-food?p={i}"
    
                response = self.fetch(url)
    
                self.parse(response)
    
            self.to_csv()
    
    
    if __name__ == "__main__":
        scraper = PetBarnProdScraper()
        scraper.run()

every time I run that code the label_options column has always the same values which is the last one I am guessing. here is the output I am getting:

    

    Scraped_Date,Scraped_Time,product_name,price,old_price,ratings,number_of_reviews,productSKU,productSize,priceWithoutTax,lifeStage,label_options
    11/21/2022, 00:31:47,Black Hawk Fish And Potato Adult Dog Food,189.99,N/A,N/A,N/A,black-hawk-fish-&-potato-adult-dog-food,,172.72,Adult,"['10kg', '20kg', '3kg']"
    11/21/2022, 00:31:47,SavourLife Ancient Grains Lean Chicken Adult Dog Food,159.99,N/A,N/A,N/A,savourlife-ancient-grains-lean-chicken-adult-dog-food,,145.45,Adult,"['10kg', '20kg', '3kg']"

Expected output:

    Scraped_Date,Scraped_Time,product_name,price,old_price,ratings,number_of_reviews,productSKU,productSize,priceWithoutTax,lifeStage,label_options
    11/21/2022, 00:31:47,Black Hawk Fish And Potato Adult Dog Food,189.99,N/A,N/A,N/A,black-hawk-fish-&-potato-adult-dog-food,,172.72,Adult,10kg
    11/21/2022, 00:31:47,Black Hawk Fish And Potato Adult Dog Food,189.99,N/A,N/A,N/A,black-hawk-fish-&-potato-adult-dog-food,,172.72,Adult,20kg
    11/21/2022, 00:31:47,Black Hawk Fish And Potato Adult Dog Food,189.99,N/A,N/A,N/A,black-hawk-fish-&-potato-adult-dog-food,,172.72,Adult,3kg
    11/21/2022, 00:31:47,SavourLife Ancient Grains Lean Chicken Adult Dog Food,159.99,N/A,N/A,N/A,savourlife-ancient-grains-lean-chicken-adult-dog-food,,145.45,Adult,3kg
    11/21/2022, 00:31:47,SavourLife Ancient Grains Lean Chicken Adult Dog Food,159.99,N/A,N/A,N/A,savourlife-ancient-grains-lean-chicken-adult-dog-food,,145.45,Adult,20kg

Can anyone help me figure out the best way to get the expected output? Thanks!

UPDATE:
Updated the code based on Driftr95' answer:

    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    import json
    import csv
    from datetime import datetime
    from datetime import date
    
    now = datetime.now()
    today = date.today()
    
    
    class PetBarnProdScraper:
    
        all_info = []
    
        def fetch(self, url):
            print(f"HTTP GET request to URL: {url}", end="")
            res = requests.get(url)
            print(f" | Status Code: {res.status_code}")
    
            return res
    
        def parse(self, response):
            soup = BeautifulSoup(response.text, "html.parser")
            product_urls = [a.get("href") for a in soup.select("a.product-item-link")]
            product_ids = [
                pid.get("id").split("-")[-1] for pid in soup.select("div.product-item-info")
            ]
            titles = [
                a.text.replace("\n", "").strip() for a in soup.select("a.product-item-link")
            ]
            old_price = [
                p.select_one("span.price").text for p in soup.select("span.old-price")
            ]
            ratings = [r.get("title") for r in soup.select("div.rating-result")]
            no_of_reviews = [review.text for review in soup.select("a.action.view")]
            data = (
                soup.select('script[type="text/x-magento-init"]')[3]
                .text.replace("\n", "")
                .strip()
            )
            data_json = json.loads(data)
            data_j = json.loads(
                data_json["*"]["Overdose_AdobeAnalytics/js/view/datalayer"]["datalayer"][0]
            )
    
            for idx in range(len(titles)):
                try:
                    ratings_count = ratings[idx]
                    reviews_count = no_of_reviews[idx]
                    last_price = old_price[idx]
                except:
                    ratings_count = "N/A"
                    reviews_count = "N/A"
                    last_price = "N/A"
                d = {
                    "Scraped_Date": now.strftime("%m/%d/%Y, %H:%M:%S").split(",")[0],
                    "Scraped_Time": now.strftime("%m/%d/%Y, %H:%M:%S").split(",")[1],
                    "product_name": titles[idx],
                    "price": data_j["PLP"]["products"][idx]["productPrice"],
                    "old_price": last_price,
                    "ratings": ratings_count,
                    "number_of_reviews": reviews_count,
                    "productSKU": data_j["PLP"]["products"][idx]["productSKU"],
                    "productSize": data_j["PLP"]["products"][idx]["productSize"],
                    "priceWithoutTax": data_j["PLP"]["products"][idx][
                        "productPriceLessTax"
                    ],
                    "lifeStage": data_j["PLP"]["products"][idx]["lifeStage"],
                }
    
                for prod_id in product_ids:
                    details = soup.select_one(
                        f"script:-soup-contains('[data-role=swatch-option-{prod_id}]')"
                    )
                    if details:
                        json_details = json.loads(details.text.replace("\n", "").strip())
                        dataJC = json_details[f"[data-role=swatch-option-{prod_id}]"][
                            "Magento_Swatches/js/swatch-renderer"
                        ]["jsonConfig"]
                        productId = dataJC["productId"]
                        jcInfs = [
                            {
                                "productId": productId,
                                "optionKey": k,
                                "sku": "?",
                                "index": v["1299"] if "1299" in v else None,
                            }
                            for k, v in dataJC["index"].items()
                        ]
                        orInfs = [
                            ("optionPrices", "amount", "reverseNest"),
                            ("dynamic", "value", "nest1"),
                            ("labels", "", "reverseNest"),
                            ("hasEndDate", "", "noNesting"),
                        ]
                        relevInfs = []
                        for kk, vk, nt in orInfs:
                            if kk not in dataJC:
                                continue
                            if nt == "noNesting":
                                relevInfs += [(kk, vk, dataJC[kk])]
                                continue
                            if nt == "nest1":
                                relevInfs += [(kk, vk, vd) for kk, vd in dataJC[kk].items()]
                                continue
                            if nt != "reverseNest":
                                ## can put a default action here
                                continue
                            ## nt == 'reverseNest'
                            orInf = {}
                            for pk, po in dataJC[kk].items():
                                for kpo, vpo in po.items():
                                    if kpo not in orInf:
                                        orInf[kpo] = {}
                                    orInf[kpo][pk] = vpo
    
                            relevInfs += [(kk, vk, vi) for kk, vi in orInf.items()]
    
                        for i, j in enumerate(jcInfs):
                            for kk, vk, vd in relevInfs:
                                if j["optionKey"] not in vd:
                                    continue
                                relevInf = vd[j["optionKey"]]
                                if type(relevInf) != dict:
                                    j[kk] = relevInf
                                elif vk in relevInf and relevInf[vk]:
                                    j[kk] = relevInf[vk]
                            # combine with main variation
                            jcInfs[i] = {
                                k: v
                                for k, v in (
                                    list(d.items())
                                    + [(jk, jv) for jk, jv in j.items() if jk not in d]
                                )
                            }
                        for j in jcInfs:
                            self.all_info.append(j)
                self.all_info.append(d)
    
        def to_csv(self):
    
            df = pd.DataFrame(self.all_info).fillna("")
    
            df.to_csv(f"{today}_petbarn.csv", index=False)
    
            print('Stored results to "petbarn.csv"')
    
        def run(self):
            for i in range(1, 2):  # total_number of pages
                url = f"https://www.petbarn.com.au/dogs/dog-food/dry-dog-food?p={i}"
    
                response = self.fetch(url)
    
                self.parse(response)
    
            self.to_csv()
    
    
    if __name__ == "__main__":
        scraper = PetBarnProdScraper()
        scraper.run()


the code and output matches the expectation but not paired up instead product_name rows keep repeating itself where on the other hand name column have just 3 rows so it'd be great to have those rows intact with each other.
Here is the output:

    Scraped_Date,Scraped_Time,product_name,price,old_price,ratings,number_of_reviews,productSKU,productSize,priceWithoutTax,lifeStage,productId,optionKey,sku,index,baseOldPrice,oldPrice,basePrice,finalPrice,tierPrices,name,product_category,brand_filter,size,health_benefits,life_stage,flavour,australia_made,nutrition_grade,weight_control,on_sale,hasEndDate,breed,new,marketing_offer_short,sales_flag_label,activity_level
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,111105,108987,127956,6234,49.990908090909,54.99,42.718180818182,46.99,[],Black Hawk Fish And Potato Adult Dog Food - 3kg,Dry Food,Black Hawk,3kg,Total Wellbeing,Adult,Fish,No,Premium,No,Sale,True,,,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,111105,108981,127960,6780,172.71818081818,189.99,128.17272627273,140.99,[],Black Hawk Fish And Potato Adult Dog Food - 20kg,Dry Food,Black Hawk,20kg,Total Wellbeing,Adult,Fish,No,Premium,No,Sale,True,,,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,111105,116724,501600,6651,120.899999,132.99,102.71818081818,112.99,[],Black Hawk Fish & Potato Dog Food 10kg,Dry Food,Black Hawk,10kg,Total Wellbeing,Adult,Fish,No,Premium,No,Sale,True,,,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,145209,143157,140846,6234,41.809089909091,45.99,41.809089909091,45.99,[],SavourLife Ancient Grains Lean Chicken Adult Dog Food 3kg,Dry Food,SavourLife Ancient Grains,3kg,Weight Management,Adult,Chicken,No,Essential,Yes,Sale,False,All,New,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,145209,143163,140847,6780,145.44545354545,159.99,99.090908090909,109.0,[],SavourLife Ancient Grains Lean Chicken Adult Dog Food 20kg,Dry Food,SavourLife Ancient Grains,20kg,Weight Management,Adult,Chicken,No,Essential,Yes,,False,All,New,Only $109,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,144663,142980,141739,6234,48.172726272727,52.99,39.990908090909,43.99,[],Black Hawk Chicken & Rice Medium Puppy Food 3kg,Dry Food,Black Hawk,3kg,Healthy Development,Puppy,Chicken,No,Premium,No,Sale,True,Medium,,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,144663,142983,141740,6651,114.53636263636,125.99,101.80908990909,111.99,[],Black Hawk Chicken & Rice Medium Puppy Food 10kg,Dry Food,Black Hawk,10kg,,Puppy,Chicken,No,Premium,No,Sale,True,Medium,,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,144663,142959,141741,6780,169.99090809091,186.99,135.99090809091,149.59,[],Black Hawk Chicken & Rice Medium Puppy Food 20kg,Dry Food,Black Hawk,20kg,,Puppy,Chicken,No,Premium,No,Sale,True,Medium,,20% off,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,144600,144351,141490,7815,36.354544454545,39.99,30.899999,33.99,[],ProBalance Care Joint Care Adult Dog Dry Food 2.5kg,Dry Food,ProBalance,2.5kg,Hip and Joint Support,Adult,,No,Superior,No,,False,,,,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,144600,144009,141491,17823,117.26363536364,128.99,93.809089909091,103.19,[],ProBalance Care Joint Care Adult Dog Dry Food 12kg,Dry Food,ProBalance,12kg,Hip and Joint Support,Adult,,No,Superior,No,,False,,,20% off,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,113391,63624,30318,6687,173.62727172727,190.99,115.03636263636,126.54,[],Royal Canin Maxi Puppy Dog Food 15kg,Dry Food,ROYAL CANIN,15kg,Growth Support,Puppy,Chicken,No,Superior,No,,False,"Giant, Large",,,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,113391,63111,29321,84219,64.536362636364,70.99,51.809089909091,56.99,[],Royal Canin Maxi Puppy Dog Food 4kg,Dry Food,ROYAL CANIN,4kg,Growth Support,Puppy,Chicken,No,Superior,No,,False,Large,,Buy 2 for $106.49,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,113391,123852,140248,8373,20.899999,22.99,17.763635363636,19.54,[],Royal Canin Maxi Breed Puppy Food 1kg,Dry Food,ROYAL CANIN,1kg,Healthy Development,Puppy,Chicken,No,Superior,No,,False,Large,,Buy 2 for $34.49,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,145119,143145,140840,7815,45.445453545455,49.99,45.445453545455,49.99,[],SavourLife Grain Free Sensitive OFish Adult Dog Food 2.5kg,Dry Food,SavourLife,2.5kg,"Grain Free, Sensitive Skin, Sensitive Stomach",Adult,Fish,No,Superior,No,Sale,False,All,New,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,145119,143148,140841,6651,113.62727172727,124.99,113.62727172727,124.99,[],SavourLife Grain Free Sensitive OFish Adult Dog Food 10kg,Dry Food,SavourLife,10kg,"Grain Free, Sensitive Skin, Sensitive Stomach",Adult,Fish,No,Superior,No,Sale,False,All,New,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,144657,142974,141735,6651,114.53636263636,125.99,99.990908090909,109.99,[],Black Hawk Lamb & Rice Large Puppy Food 10kg,Dry Food,Black Hawk,10kg,Healthy Development,Puppy,Lamb,No,Premium,No,Sale,True,Large,,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,144657,142953,141736,6780,169.99090809091,186.99,135.99090809091,149.59,[],Black Hawk Lamb & Rice Large Puppy Food 20kg,Dry Food,Black Hawk,20kg,,Puppy,Lamb,No,Premium,No,Sale,True,Large,,20% off,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,112734,62448,29328,6234,49.081817181818,53.99,36.118180818182,39.73,[],Royal Canin Labrador Dog Food 3kg,Dry Food,ROYAL CANIN,3kg,,"Adult, Senior",Chicken,No,Superior,No,,False,Labrador Retriever,,,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,112734,62985,30327,17823,148.17272627273,162.99,92.718180818182,101.99,[],Royal Canin Labrador Dog Food 12kg,Dry Food,ROYAL CANIN,12kg,,"Adult, Senior",Chicken,No,Superior,No,,False,Labrador Retriever,,,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,172479,128169,140460,8514,45.445453545455,49.99,40.899999,44.99,[],Acana Light & Fit Dry Dog Food 2kg,Dry Food,Acana,2kg,Weight Management,Adult,Chicken,No,Superior,No,,False,,,,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,172479,128175,140469,292890,159.08181718182,174.99,149.99090809091,164.99,[],Acana Light & Fit Dry Dog Food 11.3kg,Dry Food,Acana,11.3kg,Weight Management,Adult,Chicken,No,Superior,No,,False,,,,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,145083,143316,140842,7815,43.627271727273,47.99,43.627271727273,47.99,[],SavourLife Grain Free Chicken 7+ Senior Dog Food 2.5kg,Dry Food,SavourLife,2.5kg,"Ageing, Grain Free",Senior,Chicken,No,Superior,No,Sale,False,All,New,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,145083,143322,140843,6651,109.08181718182,119.99,109.08181718182,119.99,[],SavourLife Grain Free Chicken 7+ Senior Dog Food 10kg,Dry Food,SavourLife,10kg,"Ageing, Grain Free",Senior,Chicken,No,Superior,No,Sale,False,All,New,,,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,144618,144387,141488,7815,38.172726272727,41.99,32.445453545455,35.69,[],ProBalance Care Sensitive Skin Adult Dog Dry Food 2.5kg,Dry Food,ProBalance,2.5kg,Sensitive Skin,Adult,,No,Superior,No,,False,,,,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,144618,144021,141489,17823,118.17272627273,129.99,94.536362636364,103.99,[],ProBalance Care Sensitive Skin Adult Dog Dry Food 12kg,Dry Food,ProBalance,12kg,Sensitive Skin,Adult,,No,Superior,No,,False,,,20% off,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,172476,128235,140423,8514,54.536362636364,59.99,51.809089909091,56.99,[],Orijen Six Fish Dry Dog Food 2kg,Dry Food,Orijen,2kg,Grain Free,Adult,Fish,No,Superior,No,,False,,,,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,172476,128214,140431,2825802,190.899999,209.99,181.80908990909,199.99,[],Orijen Six Fish Dry Dog Food 11.4kg,Dry Food,Orijen,11.4kg,Grain Free,Adult,Fish,No,Superior,No,,False,,,,Great low price,
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,115260,109329,127959,6780,156.35454445455,171.99,119.99090809091,131.99,[],Black Hawk Lamb And Rice Adult Dog Food - 20kg,Dry Food,Black Hawk,20kg,,Adult,Lamb,No,Premium,No,Sale,True,,,,,High Activity
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,115260,109323,127955,6234,46.354544454545,50.99,28.172726272727,30.99,[],Black Hawk Lamb And Rice Adult Dog Food - 3kg,Dry Food,Black Hawk,3kg,,Adult,Lamb,No,Premium,No,Sale,True,,,3kg bags for $30.99,,High Activity
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,115260,109317,501601,6651,110.899999,121.99,93.627271727273,102.99,[],Black Hawk Lamb & Rice Adult Dog Food 10kg,Dry Food,Black Hawk,10kg,,Adult,Lamb,No,Premium,No,Sale,True,,,,,High Activity
    11/21/2022, 14:34:56,Advance Oodles Puppy Food 2.5kg,40.77,$47.99,100%,1,143138,,37.06,Puppy,,,,,,,,,,,,,,,,,,,,,,,,,,

  [1]: https://www.petbarn.com.au/dogs/dog-food/dry-dog-food
