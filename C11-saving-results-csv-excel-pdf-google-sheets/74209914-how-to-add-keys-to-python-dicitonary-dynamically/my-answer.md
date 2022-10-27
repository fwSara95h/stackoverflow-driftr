---
title: "How to Add keys to python dicitonary dynamically?"
site: stackoverflow
question_id: 74209914
answer_id: 74218507
url: https://stackoverflow.com/a/74218507
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-27T07:49:05Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74218507/revisions
accepted: true
score: 0
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: abda24f5a019aacf5639de40a6a8ab9377123c0a60baeefad87b52c9d5ab47bc
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74218507>, 2022-10-27; **accepted**; score 0. Text as retrieved 2026-10-12.

You need to pass as `fieldnames` *all* the keys any item in `self.results` might have. The error should go away if you just add that into your `to_csv` function
```python
def to_csv(self):  
        fNames = list(set([k for r in self.results for k in r.keys()]))
        fNames.sort(key=lambda r: (
            -1*(int(r.replace('lowest_price_', ''))+1) if 'lowest_price_' in r else 0, r
        ), reverse=True)

        with open('ziwi_pets_2.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fNames)
            writer.writeheader()

            for row in self.results:
                writer.writerow(row)

            print('Stored results to "ziwi_pets_2.csv"')
```
(The `sort` statement is optional - it's just to make sure the columns are in a certain order.)

<hr>

As for this bit

> I expected something like this

the `for idx, price in enumerate(detail_1)` in the `parse` function is appending a new line *for every lowest_price_idx value* of each `detail`. To get get them all in one line, change the outer loop to
```python
            for detail in other_details:
                result_i = {
                        'title': titles[index],
                        'lowest_prices': lowest_prices,
                        'store_names': store_names[index],
                        'shipping_prices': shipping_prices[index],
                        'price_per_100_kg': price_per_100_kg,
                    }

                detail_1 = [pr.text.strip() for pr in detail.find_all('span', {'class': 'sp-price'})]
                for idx, price in enumerate(detail_1):
                    result_i[f'lowest_price_{idx}'] = detail_1[idx] 

                self.results.append(result_i)
``` 

Then, your csv output will go from
[![csv before editing loop][1]][1]
to
[![csv after editing loop][2]][2]

and you json would look, as expected
```json
{
    "title": "Ziwi Peak Dog Air-Dried Free Range Chicken Recipe 1Kg",
    "lowest_prices": "$57.75",
    "store_names": "Woofers World",
    "shipping_prices": "+$9.95 shipping",
    "price_per_100_kg": "$5.78 per 100g",
    "lowest_price_0": "$3.87",
    "lowest_price_1": "$4.49",
    "lowest_price_2": "$5.09",
    "lowest_price_3": "$5.95",
    "lowest_price_4": "$5.99"
}
```
(printed using `print(json.dumps([r for r in scraper.results if len(r) == 10][0], indent=4))`)

  [1]: https://i.sstatic.net/GNH1A.png
  [2]: https://i.sstatic.net/6Y4y4.png
