---
title: "want to scrap image urls from json data"
site: stackoverflow
question_id: 74214571
url: https://stackoverflow.com/q/74214571
asked: 2022-10-26T21:45:17Z
asked_by: "babar akhter"
asked_by_url: https://stackoverflow.com/users/16720394
last_edited: 2024-08-02T07:51:15Z
last_editor: "VLAZ"
last_editor_url: https://stackoverflow.com/users/3689450
tags: [python, arrays, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 199
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9d9c289fecfebfadaeacbb9ae370dd76d668f19020c91274ea9015a38074cae1
---

# want to scrap image urls from json data

Asked by [babar akhter](https://stackoverflow.com/users/16720394) on Stack Overflow, <https://stackoverflow.com/q/74214571>, 2022-10-26, last edited 2024-08-02 by [VLAZ](https://stackoverflow.com/users/3689450). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

i,m trying to scrap image urls of each product only jpg extension also with the name available in "alt" from json structure like (also mentioned below) "attributes" > "media_map" > ("b" , "c" , "d" , e which available) > "src" and then "medium" , "lg" , "xl" , "xxl"

```"attributes": {
              "a218": {
                "label": "Shape",
                "field_type": "button_select",
                "value_order": [
                  "v766",
                  "v767"
                ],
                "values": {
                  "v766": {
                    "label": "Round",
                    "value": "S6CBRO",
                    "price": 35
                  },
                  "v767": {
                    "label": "Rectangle",
                    "value": "S6CBRE",
                    "price": 35,
                    "hypotheticalPrice": 24.5
                  }
                }
              }
            },
            "inventory": {
              "stock": 0,
              "sold": 0,
              "total": 0
            },
            "optional": {},
            "media_map": {
              "b": {
                "src": {
                  "xs": "https://ctl.s6img.com/society6/img/xVx1vleu7iLcR79ZkRZKqQiSzZE/w_125/artwork/~artwork/s6-0041/a/18613683_5971445",
                  "lg": "https://ctl.s6img.com/society6/img/W-ESMqUtC_oOEUjx-1E_SyIdueI/w_550/artwork/~artwork/s6-0041/a/18613683_5971445",
                  "xl": "https://ctl.s6img.com/society6/img/z90VlaYwd8cxCqbrZ1ttAxINpaY/w_700/artwork/~artwork/s6-0041/a/18613683_5971445",
                  "xxl": null
                },
                "type": "image",
                "alt": "I'M NOT ALWAYS A BITCH (Red) Cutting Board",
                "meta": null
              },
              "c": {
                "src": {
                  "xs": "https://ctl.s6img.com/society6/img/KQJbb4jG0gBHcqQiOCivLUbKMxI/w_125/cutting-board/rectangle/lifestyle/~artwork,fw_1572,fh_2500,fx_93,fy_746,iw_1386,ih_2142/s6-0041/a/18613725_13086827/~~/im-not-always-a-bitch-red-cutting-board.jpg",
                  "lg": "https://ctl.s6img.com/society6/img/ztGrxSpA7FC1LfzM3UldiQkEi7g/w_550/cutting-board/rectangle/lifestyle/~artwork,fw_1572,fh_2500,fx_93,fy_746,iw_1386,ih_2142/s6-0041/a/18613725_13086827/~~/im-not-always-a-bitch-red-cutting-board.jpg",
                  "xl": "https://ctl.s6img.com/society6/img/PHjp9jDic2NGUrpq8k0aaxsYZr4/w_700/cutting-board/rectangle/lifestyle/~artwork,fw_1572,fh_2500,fx_93,fy_746,iw_1386,ih_2142/s6-0041/a/18613725_13086827/~~/im-not-always-a-bitch-red-cutting-board.jpg",
                  "xxl": "https://ctl.s6img.com/society6/img/m-1HhSM5CIGl6DY9ukCVxSmVDIw/w_1500/cutting-board/rectangle/lifestyle/~artwork,fw_1572,fh_2500,fx_93,fy_746,iw_1386,ih_2142/s6-0041/a/18613725_13086827/~~/im-not-always-a-bitch-red-cutting-board.jpg"```
 below is my code i,m able to access "media_map" but dnt know how to access jpg extension url

```contents = []
with open('urls.csv','r') as csvf: # Open file in read mode
    urls = csv.reader(csvf)
    for url in urls:
        contents.append(url) # Add each url to list contents
        newlist = []
        for url in contents:
            try:
                page = urlopen(url[0]).read()
                soup = BeautifulSoup(page, 'html.parser')
                scripts = soup.find_all('script')[7].text.strip()[24:]
                data = json.loads(scripts)
                link = data['product']['response']['product']['data']['attributes']['media_map']```

every product have "b" , "c" , "d" or "b" , "c" , "d" , "e" , "f"
or some products have only "b" , "c"
i,m new in scraping but stuck over there
