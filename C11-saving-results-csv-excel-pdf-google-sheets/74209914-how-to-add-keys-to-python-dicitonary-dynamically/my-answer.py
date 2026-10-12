# Code from my Stack Overflow answer https://stackoverflow.com/a/74218507 (posted 2022-10-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
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
