# Code from my Stack Overflow answer https://stackoverflow.com/a/74281335 (posted 2022-11-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
odds = [
    o.get('data-odd') if o.get('data-odd') else (
        o.select_one('*[data-odd]').get('data-odd')
        if o.select('*[data-odd]') else None
    ) for o in odds_raw
]

# --- block 2 ---
odds = [ 
    o.select_one('span[data-odd]').get('data-odd')
    if o.select('span[data-odd]') else None
    for o in odds_raw
]

# --- block 3 ---
['1.22', None, None, '1.71', None, None, None, None, '1.74', None, '3.43', None, '3.07', None, None, '2.09', None, None, None, '3.42', None, None, None, '1.40', None, None, '11.93', '1.76', None, None, '1.60', None, None, '2.06', None, None, None, None, '3.41', None, '4.60', None, None, None, '3.33', None, None, '3.13', None, '3.55', None, '2.52', None, None, '1.23', None, None, '8.85', None, None, '2.95', None, None, '2.30', None, None, None, None, '2.79', None, '3.70', None, '1.42', None, None, '2.37', None, None, '1.67', None, None, None, '4.95', None, '2.10', None, None, None, None, '1.99', None, None, '1.63', '3.81', None, None, None, '3.65', None, None, '3.35', None, None, '3.60', None, None, '3.45', None, '1.46', None, None, '1.72', None, None, '3.22', None, None, None, '3.57', None, '2.53', None, None, '2.06', None, None, None, None, '2.07', '1.63', None, None, '3.27', None, None, None, None, '2.83', '1.50', None, None, '1.12', None, None, '1.68', None, None, '1.71', None, None, None, '3.39', None, '1.43', None, None, '1.98', None, None, None, '3.47', None, None, None, '1.77', None, None, '2.46', None, '4.76', None, None, None, '3.22', '2.04', None, None, None, None, '1.78', '2.92', None, None, None, '4.79', None, '1.51', None, None, None, None, '1.33', '2.07', None, None, None, None, '2.58', None, None, None, None, None, None, None, None, None, None, None, None, '1.92', None, None, '2.65', None, None, None, '5.77', None, '2.14', None, None, '1.67', None, None, None, '5.15', None, None, '3.41', None, None, None, '3.55', '1.52', None, None, '2.15', None, None, None, None, '2.16', '1.53', None, None, None, '3.26', None, '1.28', None, None, '1.09', None, None, None, '3.54', None, None, '3.45', None, '3.32', None, None, None, '3.59', None, '5.26', None, None, None, None, '3.65', None, None, '1.45', None, '3.28', None, '1.39', None, None, None, '3.42', None, '1.74', None, None, '1.40', None, None, '1.14', None, None, '1.19', None, None, None, None, '1.96', '4.58', None, None, '6.02', None, None, None, '4.90', None, None, None, '2.91', None, None, '1.43', '2.49', None, None, None, '3.51', None, '2.65', None, None, None, None, '4.40', '1.45', None, None, None, '6.11', None, None, '3.46', None, '4.02', None, None, '1.56', None, None, '1.78', None, None, '4.39', None, None, None, '3.26', None, '1.08', None, None, None, '3.54', None, None, '3.39', None, None, '3.65', None, None, None, '4.70', None, None, '1.38', '4.01', None, None, None, None, '1.56', None, '6.10', None, '2.43', None, None, '1.58', None, None, '1.36', None, None, None, None, '1.84']

# --- block 4 ---
odds = [o for o in odds if o is not None]
