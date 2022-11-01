---
title: "getting the span text from bs4"
site: stackoverflow
question_id: 74281093
answer_id: 74281335
url: https://stackoverflow.com/a/74281335
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T20:15:30Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74281335/revisions
accepted: false
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b715e3776408a1e31c9da7bbc3e32b0da25c6d3e4482b21c012fe92b22639c56
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74281335>, 2022-11-01; score 1. Text as retrieved 2026-10-12.

> The logic below does not return any values.

and yet, I see *some* values in your screenshot.

Anyway, if you mean that you want the `odd` attribute value from inner elements even if `td` itself doesn't have it, you can do this
```python
odds = [
    o.get('data-odd') if o.get('data-odd') else (
        o.select_one('*[data-odd]').get('data-odd')
        if o.select('*[data-odd]') else None
    ) for o in odds_raw
]
```
output of `print(odds)`:
```lang-none
['1.22', '6.75', '13.19', '1.71', '3.87', '4.97', '4.97', '3.72', '1.74', '2.17', '3.43', '3.41', '3.07', '3.35', '2.38', '2.09', '3.39', '3.71', '2.28', '3.42', '3.20', '7.55', '5.05', '1.40', '1.22', '6.96', '11.93', '1.76', '3.81', '4.65', '1.60', '4.00', '5.88', '2.06', '3.48', '3.66', '2.07', '3.72', '3.41', '6.81', '4.60', '1.47', '2.21', '3.43', '3.33', '2.35', '3.33', '3.13', '2.13', '3.55', '3.42', '2.52', '3.13', '3.05', '1.23', '6.68', '12.94', '8.85', '5.42', '1.34', '2.95', '3.39', '2.43', '2.30', '3.54', '3.06', '2.66', '3.21', '2.79', '4.35', '3.70', '1.83', '1.42', '4.98', '7.11', '2.37', '3.48', '2.98', '1.67', '3.90', '5.32', '1.39', '4.95', '8.17', '2.10', '3.28', '3.79', '3.95', '3.46', '1.99', '5.10', '4.23', '1.63', '3.81', '4.06', '1.87', '2.06', '3.65', '3.51', '2.96', '3.35', '2.45', '1.95', '3.60', '3.93', '2.38', '3.45', '2.98', '1.46', '4.66', '6.94', '1.72', '3.78', '4.98', '3.22', '3.44', '2.26', '3.73', '3.57', '2.01', '2.53', '3.72', '2.65', '2.06', '3.56', '3.59', '3.57', '3.56', '2.07', '1.63', '3.98', '5.53', '3.27', '3.50', '2.20', '2.57', '3.30', '2.83', '1.50', '4.28', '6.81', '1.12', '10.21', '21.18', '1.68', '3.96', '5.10', '1.71', '4.02', '4.73', '2.42', '3.39', '2.97', '1.43', '5.29', '6.58', '1.98', '3.69', '3.74', '3.17', '3.47', '2.27', '4.81', '3.71', '1.77', '2.92', '3.40', '2.46', '1.46', '4.76', '6.74', '2.33', '3.29', '3.22', '2.04', '3.35', '3.94', '4.48', '3.88', '1.78', '2.92', '3.29', '2.52', '1.41', '4.79', '7.85', '1.51', '4.54', '6.36', '9.09', '5.50', '1.33', '2.07', '3.53', '3.61', '2.78', '3.38', '2.58', '4.80', '3.55', '1.86', '4.50', '4.10', '1.80', '1.32', '6.10', '10.00', '2.38', '3.55', '3.10', '1.92', '3.56', '4.21', '2.65', '3.47', '2.67', '9.06', '5.77', '1.32', '2.14', '3.56', '3.40', '1.67', '3.99', '5.28', '7.70', '5.15', '1.39', '2.08', '3.41', '3.74', '2.18', '3.34', '3.55', '1.52', '4.52', '6.20', '2.15', '3.46', '3.46', '3.24', '3.73', '2.16', '1.53', '4.46', '6.10', '3.31', '3.26', '2.31', '1.28', '6.16', '10.14', '1.09', '11.85', '27.62', '3.27', '3.54', '2.20', '2.08', '3.45', '3.69', '3.32', '3.24', '2.31', '2.11', '3.59', '3.47', '5.26', '4.07', '1.65', '2.10', '3.45', '3.65', '6.95', '4.75', '1.45', '2.55', '3.28', '2.90', '1.39', '5.26', '7.55', '2.09', '3.42', '3.71', '1.74', '3.87', '4.74', '1.40', '5.05', '7.72', '1.14', '8.87', '18.56', '1.19', '7.51', '15.15', '3.63', '3.90', '1.96', '4.58', '4.32', '1.69', '6.02', '4.57', '1.52', '6.95', '4.90', '1.44', '2.50', '3.35', '2.91', '7.61', '4.70', '1.43', '2.49', '3.22', '3.03', '1.91', '3.51', '4.35', '2.65', '3.36', '2.73', '1.76', '4.08', '4.40', '1.45', '4.76', '7.13', '1.27', '6.11', '11.79', '2.16', '3.46', '3.44', '4.02', '3.60', '1.94', '1.56', '4.36', '5.87', '1.78', '3.61', '4.96', '4.39', '3.86', '1.81', '2.43', '3.26', '3.08', '1.08', '12.60', '31.88', '2.44', '3.54', '2.86', '2.20', '3.39', '3.41', '1.90', '3.65', '4.10', '1.78', '3.74', '4.70', '7.95', '5.24', '1.38', '4.01', '3.46', '1.99', '6.52', '4.05', '1.56', '10.45', '6.10', '1.28', '2.43', '3.34', '3.00', '1.58', '4.04', '6.19', '1.36', '5.20', '8.69', '4.58', '3.57', '1.84']
```

<hr>

Or if you wanted the `odd` attribute value from *only* the `span` tags, 
```python
odds = [ 
    o.select_one('span[data-odd]').get('data-odd')
    if o.select('span[data-odd]') else None
    for o in odds_raw
]
```
now, the output of `print(odds)` would be
```lang-none
['1.22', None, None, '1.71', None, None, None, None, '1.74', None, '3.43', None, '3.07', None, None, '2.09', None, None, None, '3.42', None, None, None, '1.40', None, None, '11.93', '1.76', None, None, '1.60', None, None, '2.06', None, None, None, None, '3.41', None, '4.60', None, None, None, '3.33', None, None, '3.13', None, '3.55', None, '2.52', None, None, '1.23', None, None, '8.85', None, None, '2.95', None, None, '2.30', None, None, None, None, '2.79', None, '3.70', None, '1.42', None, None, '2.37', None, None, '1.67', None, None, None, '4.95', None, '2.10', None, None, None, None, '1.99', None, None, '1.63', '3.81', None, None, None, '3.65', None, None, '3.35', None, None, '3.60', None, None, '3.45', None, '1.46', None, None, '1.72', None, None, '3.22', None, None, None, '3.57', None, '2.53', None, None, '2.06', None, None, None, None, '2.07', '1.63', None, None, '3.27', None, None, None, None, '2.83', '1.50', None, None, '1.12', None, None, '1.68', None, None, '1.71', None, None, None, '3.39', None, '1.43', None, None, '1.98', None, None, None, '3.47', None, None, None, '1.77', None, None, '2.46', None, '4.76', None, None, None, '3.22', '2.04', None, None, None, None, '1.78', '2.92', None, None, None, '4.79', None, '1.51', None, None, None, None, '1.33', '2.07', None, None, None, None, '2.58', None, None, None, None, None, None, None, None, None, None, None, None, '1.92', None, None, '2.65', None, None, None, '5.77', None, '2.14', None, None, '1.67', None, None, None, '5.15', None, None, '3.41', None, None, None, '3.55', '1.52', None, None, '2.15', None, None, None, None, '2.16', '1.53', None, None, None, '3.26', None, '1.28', None, None, '1.09', None, None, None, '3.54', None, None, '3.45', None, '3.32', None, None, None, '3.59', None, '5.26', None, None, None, None, '3.65', None, None, '1.45', None, '3.28', None, '1.39', None, None, None, '3.42', None, '1.74', None, None, '1.40', None, None, '1.14', None, None, '1.19', None, None, None, None, '1.96', '4.58', None, None, '6.02', None, None, None, '4.90', None, None, None, '2.91', None, None, '1.43', '2.49', None, None, None, '3.51', None, '2.65', None, None, None, None, '4.40', '1.45', None, None, None, '6.11', None, None, '3.46', None, '4.02', None, None, '1.56', None, None, '1.78', None, None, '4.39', None, None, None, '3.26', None, '1.08', None, None, None, '3.54', None, None, '3.39', None, None, '3.65', None, None, None, '4.70', None, None, '1.38', '4.01', None, None, None, None, '1.56', None, '6.10', None, '2.43', None, None, '1.58', None, None, '1.36', None, None, None, None, '1.84']
```

<hr>

If you want to filter out the `None`s, just add
```python
odds = [o for o in odds if o is not None]
```
