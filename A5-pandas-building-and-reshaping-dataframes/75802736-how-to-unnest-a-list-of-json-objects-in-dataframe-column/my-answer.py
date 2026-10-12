# Code from my Stack Overflow answer https://stackoverflow.com/a/75808253 (posted 2023-03-22), extracted verbatim; may need the question's context to run.
# import ast
data = {'tax_info': [[], [{'price': '1.26', 'rate': 0.06, 'title': 'Idaho State Tax', 'price_set': {'shop_money': {'amount': '1.26', 'currency_code': 'USD'}, 'presentment_money': {'amount': '1.26', 'currency_code': 'USD'}}, 'channel_liable': False}], [{'price': '1.98', 'rate': 0.0625, 'title': 'Illinois State Tax', 'price_set': {'shop_money': {'amount': '1.98', 'currency_code': 'USD'}, 'presentment_money': {'amount': '1.98', 'currency_code': 'USD'}}, 'channel_liable': False}, {'price': '0.39', 'rate': 0.0125, 'title': 'Chicago City Tax', 'price_set': {'shop_money': {'amount': '0.39', 'currency_code': 'USD'}, 'presentment_money': {'amount': '0.39', 'currency_code': 'USD'}}, 'channel_liable': False}, {'price': '0.87', 'rate': 0.0275, 'title': 'Cook County Tax', 'price_set': {'shop_money': {'amount': '0.87', 'currency_code': 'USD'}, 'presentment_money': {'amount': '0.87', 'currency_code': 'USD'}}, 'channel_liable': False}]]}

data['tax_info'] = [ast.literal_eval(s) for s in data['tax_info']] 
df = pd.json_normalize(data, ['tax_info', []])

# in one statement, and without altering data:
# pd.json_normalize({**data, 'tax_info': [ast.literal_eval(s) for s in data['tax_info']]}, ['tax_info', []])
