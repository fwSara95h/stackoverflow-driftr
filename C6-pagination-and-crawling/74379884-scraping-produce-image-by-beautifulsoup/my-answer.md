---
title: "Scraping Produce image by BeautifulSoup"
site: stackoverflow
question_id: 74379884
answer_id: 74391645
url: https://stackoverflow.com/a/74391645
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-10T15:40:45Z
last_edited: 2022-11-16T09:33:36Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74391645/revisions
accepted: false
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: [selenium fetch]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 52fafb506647ca3571465e5ebd14d37438d92cd617f846266c790c8de4bd47ad
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74391645>, 2022-11-10, last edited 2022-11-16; score 0. Text as retrieved 2026-10-12.

For me, the following [selector](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) works:
```python
product_image = Product_Details.select(".swiper-wrapper .lazyload-wrapper div")
print(product_image)
```
For the first 3 products, it prints
```html
[<div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر جولدن وود EDP 100مل - v1666705361/N39185122A_1" aria-hidden="true" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1666705361/N39185122A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر جولدن وود EDP 100مل - v1618317832/N39185122A_2" aria-hidden="true" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1618317832/N39185122A_2.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر جولدن وود EDP 100مل - v1618317832/N39185122A_3" aria-hidden="true" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1618317832/N39185122A_3.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر جولدن وود EDP 100مل - v1617954175/N39185122A_5" aria-hidden="true" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1617954175/N39185122A_5.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر جولدن وود EDP 100مل - v1617954175/N39185122A_4" aria-hidden="true" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1617954175/N39185122A_4.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="v1666705361/N39185122A_1" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_400/v1666705361/N39185122A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="v1618317832/N39185122A_2" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_400/v1618317832/N39185122A_2.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="v1618317832/N39185122A_3" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_400/v1618317832/N39185122A_3.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="v1617954175/N39185122A_5" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_400/v1617954175/N39185122A_5.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="v1617954175/N39185122A_4" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_400/v1617954175/N39185122A_4.jpg"/></div>]
[<div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر سايلنسز EDP 100مل - v1562242787/N11201003A_1" aria-hidden="true" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1562242787/N11201003A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر سايلنسز EDP 100مل - v1562243187/N11201003A_2" aria-hidden="true" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1562243187/N11201003A_2.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="v1562242787/N11201003A_1" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_400/v1562242787/N11201003A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="v1562243187/N11201003A_2" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_400/v1562243187/N11201003A_2.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر سايلنسز EDP 100مل" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1562242787/N11201003A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="مزيل عرق فريشلي فري ببكرة دوارة برائحة الجريب فروت والليتشي 50مل" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1654077085/N42721327A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر سايلنسز EDP 100مل" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1562242787/N11201003A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="مزيل عرق فريشلي فري ببكرة دوارة برائحة الجريب فروت والليتشي 50مل" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1654077085/N42721327A_1.jpg"/></div>]
[<div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر رويال أمبر EDP 100مل - v1515389873/N11202278A_1" aria-hidden="true" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1515389873/N11202278A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر رويال أمبر EDP 100مل - v1515389757/N11202278A_2" aria-hidden="true" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1515389757/N11202278A_2.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر رويال أمبر EDP 100مل - v1560784604/N11202278A_3" aria-hidden="true" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1560784604/N11202278A_3.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="v1515389873/N11202278A_1" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_400/v1515389873/N11202278A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="v1515389757/N11202278A_2" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_400/v1515389757/N11202278A_2.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="v1560784604/N11202278A_3" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_400/v1560784604/N11202278A_3.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر رويال أمبر EDP 100مل" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1515389873/N11202278A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر بيور بلوم EDP 100مل" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1572605693/N31750079A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر رويال أمبر EDP 100مل" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1515389873/N11202278A_1.jpg"/></div>, <div class="sc-8cbb8e24-2 eDXUdi"><img alt="عطر بيور بلوم EDP 100مل" class="sc-b51db3f-1 iCVkuj" src="https://f.nooncdn.com/products/tr:n-t_80/v1572605693/N31750079A_1.jpg"/></div>]
```
but then, even `.find_all("div", class_="sc-8cbb8e24-2 eDXUdi")` gives me the same results. Also, wouldn't getting the `img` tags be more useful? (You can select them with `.swiper-wrapper img`.)

<hr>

Are you sure you're fetching the right html? Your headers didn't work for me, and I wasn't able to write a working request at all, so I actually [used selenium](https://pastebin.com/E3sCEr9r) to get the html. If interested, take a look at my [edited version of your code](https://pastebin.com/hkAU1Hm1). I replaced your for-loop with reusable functions [after some adjustments] that I use in some of my crawlers, and the output looks like
```json
[
    {
        "page_number": 1,
        "page_link": "https://www.noon.com/egypt-ar/beauty-and-health/beauty/eg-nov22-clearance-2/?limit=50&page=1",
        "products_count": 182,
        "products": [
                {
                "product_id": "N39185122A",
                "product_brand": "إس. تي. ديبون",
                "product_name": "عطر جولدن وود EDP 100مل",
                "product_price_text": "رقم الموديل : 16904A قبل : 1298.00 جنيه الآن : 975.00 جنيه يشمل ضريبة القيمة المضافة وفّرت : 323.00 جنيه خصم 24٪",
                "current_price": "975.00",
                "product_link": "https://www.noon.com/egypt-ar/golden-wood-edp-100ml/N39185122A/p/?o=d55236b5f16d3c9d",
                "imageLinks_list": ["https://f.nooncdn.com/products/tr:n-t_80/v1666705361/N39185122A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1618317832/N39185122A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1618317832/N39185122A_3.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1617954175/N39185122A_5.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1617954175/N39185122A_4.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1666705361/N39185122A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1618317832/N39185122A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1618317832/N39185122A_3.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1617954175/N39185122A_5.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1617954175/N39185122A_4.jpg"]
            },
            {
                "product_id": "N11201003A",
                "product_brand": "جاكومو باريس",
                "product_name": "عطر سايلنسز EDP 100مل",
                "product_price_text": "4.3 12 تقييمات قبل : 811.00 جنيه الآن : 675.00 جنيه يشمل ضريبة القيمة المضافة وفّرت : 136.00 جنيه خصم 16٪",
                "current_price": "675.00",
                "product_link": "https://www.noon.com/egypt-ar/silences-edp-100ml/N11201003A/p/?o=b886ef68a4cc3e4c",
                "imageLinks_list": ["https://f.nooncdn.com/products/tr:n-t_80/v1562242787/N11201003A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1562243187/N11201003A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1562242787/N11201003A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1562243187/N11201003A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1562242787/N11201003A_1.jpg", "https://z.nooncdn.com/s/app/com/noon/icons/checkbox-square_checked_v2.svg", "https://z.nooncdn.com/s/app/com/noon/images/fulfilment_express_v2-ar.svg", "https://f.nooncdn.com/products/tr:n-t_80/v1654077085/N42721327A_1.jpg", "https://z.nooncdn.com/s/app/com/noon/icons/checkbox-square_checked_v2.svg", "https://z.nooncdn.com/s/app/com/noon/images/fulfilment_express_v2-ar.svg", "https://f.nooncdn.com/products/tr:n-t_80/v1562242787/N11201003A_1.jpg", "https://z.nooncdn.com/s/app/com/noon/icons/checkbox-square_checked_v2.svg", "https://z.nooncdn.com/s/app/com/noon/images/fulfilment_express_v2-ar.svg", "https://f.nooncdn.com/products/tr:n-t_80/v1654077085/N42721327A_1.jpg", "https://z.nooncdn.com/s/app/com/noon/icons/checkbox-square_checked_v2.svg", "https://z.nooncdn.com/s/app/com/noon/images/fulfilment_express_v2-ar.svg"]
            }
        ]
    },
    {
        "page_number": 2,
        "page_link": "https://www.noon.com/egypt-ar/beauty-and-health/beauty/eg-nov22-clearance-2/?limit=50&page=2",
        "products_count": 182,
        "products": [
                {
                "product_id": "N42677090A",
                "product_brand": "جاكومو",
                "product_name": "طَقم هدايا مكون من أو دي بارفان وبخاخ مناسب للسفر من قطعتين 100مل",
                "product_price_text": "رقم الموديل : 3392865093684 قبل : 1241.00 جنيه الآن : 679.00 جنيه يشمل ضريبة القيمة المضافة وفّرت : 562.00 جنيه خصم 45٪",
                "current_price": "679.00",
                "product_link": "https://www.noon.com/egypt-ar/2-piece-eau-de-parfum-and-travel-spray-gift-set-100ml/N42677090A/p/?o=d8dc699010d8086b",
                "imageLinks_list": ["https://f.nooncdn.com/products/tr:n-t_80/v1608984530/N42677090A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1608984530/N42677090A_1.jpg"]
            },
            {
                "product_id": "N11200698A",
                "product_brand": "لانفن باريس",
                "product_name": "ماء تواليت إكلا داربيج للرجال 100مل",
                "product_price_text": "5.0 2 تقييمات قبل : 1365.00 جنيه الآن : 687.00 جنيه يشمل ضريبة القيمة المضافة وفّرت : 678.00 جنيه خصم 49٪",
                "current_price": "687.00",
                "product_link": "https://www.noon.com/egypt-ar/eclat-d-arpege-pour-homme-edt-100ml/N11200698A/p/?o=c5824e03ee50f26a",
                "imageLinks_list": ["https://f.nooncdn.com/products/tr:n-t_80/v1544679664/N11200698A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1544679664/N11200698A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1544679665/N11200698A_3.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1544679664/N11200698A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1544679664/N11200698A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1544679665/N11200698A_3.jpg"]
            }
        ]
    },
    {
        "page_number": 3,
        "page_link": "https://www.noon.com/egypt-ar/beauty-and-health/beauty/eg-nov22-clearance-2/?limit=50&page=3",
        "products_count": 182,
        "products": [
                {
                "product_id": "N39185122A",
                "product_brand": "إس. تي. ديبون",
                "product_name": "عطر جولدن وود EDP 100مل",
                "product_price_text": "رقم الموديل : 16904A قبل : 1298.00 جنيه الآن : 975.00 جنيه يشمل ضريبة القيمة المضافة وفّرت : 323.00 جنيه خصم 24٪",
                "current_price": "975.00",
                "product_link": "https://www.noon.com/egypt-ar/golden-wood-edp-100ml/N39185122A/p/?o=d55236b5f16d3c9d",
                "imageLinks_list": ["https://f.nooncdn.com/products/tr:n-t_80/v1666705361/N39185122A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1618317832/N39185122A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1618317832/N39185122A_3.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1617954175/N39185122A_5.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1617954175/N39185122A_4.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1666705361/N39185122A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1618317832/N39185122A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1618317832/N39185122A_3.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1617954175/N39185122A_5.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1617954175/N39185122A_4.jpg"]
            },
            {
                "product_id": "N11202278A",
                "product_brand": "إس. تي. ديبون",
                "product_name": "عطر رويال أمبر EDP 100مل",
                "product_price_text": "4.7 9 تقييمات قبل : 1899.00 جنيه الآن : 699.00 جنيه يشمل ضريبة القيمة المضافة وفّرت : 1200.00 جنيه خصم 63٪",
                "current_price": "699.00",
                "product_link": "https://www.noon.com/egypt-ar/royal-amber-edp-100ml/N11202278A/p/?o=dd94cf4150e7d47c",
                "imageLinks_list": ["https://f.nooncdn.com/products/tr:n-t_80/v1515389873/N11202278A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1515389757/N11202278A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1560784604/N11202278A_3.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1515389873/N11202278A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1515389757/N11202278A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1560784604/N11202278A_3.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1515389873/N11202278A_1.jpg", "https://z.nooncdn.com/s/app/com/noon/icons/checkbox-square_checked_v2.svg", "https://z.nooncdn.com/s/app/com/noon/images/fulfilment_express_v2-ar.svg", "https://f.nooncdn.com/products/tr:n-t_80/v1572605693/N31750079A_1.jpg", "https://z.nooncdn.com/s/app/com/noon/icons/checkbox-square_checked_v2.svg", "https://z.nooncdn.com/s/app/com/noon/images/fulfilment_express_v2-ar.svg", "https://f.nooncdn.com/products/tr:n-t_80/v1515389873/N11202278A_1.jpg", "https://z.nooncdn.com/s/app/com/noon/icons/checkbox-square_checked_v2.svg", "https://z.nooncdn.com/s/app/com/noon/images/fulfilment_express_v2-ar.svg", "https://f.nooncdn.com/products/tr:n-t_80/v1572605693/N31750079A_1.jpg", "https://z.nooncdn.com/s/app/com/noon/icons/checkbox-square_checked_v2.svg", "https://z.nooncdn.com/s/app/com/noon/images/fulfilment_express_v2-ar.svg"]
            }
        ]
    },
    {
        "page_number": 4,
        "page_link": "https://www.noon.com/egypt-ar/beauty-and-health/beauty/eg-nov22-clearance-2/?limit=50&page=4",
        "products_count": 182,
        "products": [
                {
                "product_id": "N31126667A",
                "product_brand": "فيكتور أند رولف",
                "product_name": "ماء عطر فلاور بومب ميدنايبت 100مل",
                "product_price_text": "رقم الموديل : 10507A 4.5 2 تقييمات قبل : 2999.00 جنيه الآن : 2395.00 جنيه يشمل ضريبة القيمة المضافة وفّرت : 604.00 جنيه خصم 20٪",
                "current_price": "2395.00",
                "product_link": "https://www.noon.com/egypt-ar/flowerbomb-midnight-edp-100ml/N31126667A/p/?o=e34956fccd70220b",
                "imageLinks_list": ["https://f.nooncdn.com/products/tr:n-t_80/v1572005046/N31126667A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_80/v1572005047/N31126667A_2.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1572005046/N31126667A_1.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1572005047/N31126667A_2.jpg"]
            },
            {
                "product_id": "N42264463A",
                "product_brand": "كييلز",
                "product_name": "محلول تصحيح لعلاج البقع الداكنة بوضوح 30مل",
                "product_price_text": "رقم الموديل : 3605970202637 5.0 تقييم عميل واحد قبل : 2678.57 جنيه الآن : 1715.00 جنيه يشمل ضريبة القيمة المضافة وفّرت : 963.57 جنيه خصم 35٪",
                "current_price": "1715.00",
                "product_link": "https://www.noon.com/egypt-ar/clearly-corrective-dark-spot-solution-30ml/N42264463A/p/?o=bba8c04cdb7cce0e",
                "imageLinks_list": ["https://f.nooncdn.com/products/tr:n-t_80/v1605337673/N42264463A_5.jpg", "https://f.nooncdn.com/products/tr:n-t_400/v1605337673/N42264463A_5.jpg"]
            }
        ]
    }
]
```
(only 2 products from each page included)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Ashraf](https://stackoverflow.com/users/20329031)** (2022-11-11): I am grateful for the answer. For my code I tried your suggestion but I still get strange result.  https://prnt.sc/ZJcb4ylPb7r7  For selenium :  I'm still a beginner, but I can't understand how the code works. I feel frustrated I don't know what's wrong.
- **[Ashraf](https://stackoverflow.com/users/20329031)** (2022-11-11): I tried selenium but get this Error: https://prnt.sc/ON9CV16st20d
- **me** (2022-11-11): @Ashraf for the error, you need to first download [linkToSoup_selenium.py](https://gist.githubusercontent.com/Driftr95/cbae6710c134df708f44ade8503f6638/raw/05d5d7f8c332ad929d8b7a1d32a4804a9c07c859/linkToSoup_selenium.py) from the link in the comment and put it in the same folder (or remove the `import` line and paste everything from "linkToSoup_selenium.py" there); the strange result is possibly because the fetched html doesn't have the fully loaded page (which would also explain why the `.find...` by class didn't work for you)
- **me** (2022-11-11): @Ashraf if you decide to give [linkToSoup_selenium.py](https://gist.githubusercontent.com/Driftr95/cbae6710c134df708f44ade8503f6638/raw/05d5d7f8c332ad929d8b7a1d32a4804a9c07c859/linkToSoup_selenium.py) another try, please read the comments in the file first
- **[Ashraf](https://stackoverflow.com/users/20329031)** (2022-11-11): i'm appreciated. but last link not working   https://prnt.sc/PVGMveKgtBqB
- **[Ashraf](https://stackoverflow.com/users/20329031)** (2022-11-11): https://gist.githubusercontent.com/Driftr95/cbae6710c134df708f44ade8503f6638/raw/05d5d7f8c332ad929d8b7a1d32a4804a9c07c859/linkToSoup_selenium.py
- **me** (2022-11-11): @Ashraf sorry! it just happened in the last hour - I've contacted support  but idk how long it will take....you could copy an older version of `linkToSoup_selenium` from https://stackoverflow.com/a/74105681/6146136  (it should work fine for your case since you don't really need to click/load multiple elements before scraping, which is what the additions in the current version are for)
- **[Ashraf](https://stackoverflow.com/users/20329031)** (2022-11-16): Hi Dear I using Selenium With BS4 , and it seems it working now  i got that: https://prnt.sc/hKigLu2iraLS it has images links , Thanks A lot  for helping
