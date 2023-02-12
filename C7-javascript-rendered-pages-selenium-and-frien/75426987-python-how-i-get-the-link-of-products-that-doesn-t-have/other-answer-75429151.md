---
title: "Python | How i get the link of products that doesn't have href with selenium"
site: stackoverflow
question_id: 75426987
answer_id: 75429151
url: https://stackoverflow.com/a/75429151
author: "Alexander Yanque"
author_url: https://stackoverflow.com/users/21106808
posted: 2023-02-12T18:11:49Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2f1f43df033429b79a202c04de75d4b5938fdbfc3e80e66894f5612c7a10cb6d
role: another answer on the same question, kept as context; not my work
---

# Answer by [Alexander Yanque](https://stackoverflow.com/users/21106808) — 2023-02-12

Posted on Stack Overflow, <https://stackoverflow.com/a/75429151>, 2023-02-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can use wallapop's api to get this data. There are many ways to handle these data, I suggest using the the [Scrapy][1] framework. Here is the code to get the item urls (as well as saving item's data as a json file) using  Scrapy:

    import json
    import scrapy
    
    
    class WallapopSpider(scrapy.Spider):
        name = "wallapop"
        search_url = "https://api.wallapop.com/api/v3/general/search?keywords={keywords}&latitude={latitude}&longitude={longitude}&start={start}&items_count={items_count}&filters_source=search_box&order_by={order_by}"
        item_url = "https://api.wallapop.com/api/v3/items/"
    
        def start_requests(self):
            meta = {
                "keywords": "monitor",
                "latitude": 39.46895,
                "longitude": -0.37686,
                "start": 0,
                "items_count": 40,
                "order_by": "most_relevance",
            }
            yield scrapy.Request(
                url=self.search_url.format(**meta), callback=self.parse_search
            )
    
        def parse_search(self, response):
            # parsing the response into a dict
            dict_data = json.loads(response.text)
            # iterating over the search results
            for item in dict_data["search_objects"]:
                yield scrapy.Request(
                    url=self.item_url + item["id"], callback=self.parse_item
                )
    
        def parse_item(self, response):
            # parsing the response into a dict
            item_data = json.loads(response.text)
            print(item_data["share_url"])
            print(item_data["description"])
            # saving the item data on a json file
            with open(f"{item_data['id']}.json", "w") as f:
                json.dump(item_data, f)

I found both API endpoints by inspecting the network traffic on the browser dev tools. I'm using Valencia's latitude and longitude's values and "monitor" as keyword. The required parameters to run the query are keywords, latitude and longitude.

I can also suggest running the crawler on a spider management solution like [estela][2].


  [1]: https://scrapy.org/
  [2]: https://estela.bitmaker.la/docs/
