---
title: "Convert two dictionary to influx writing measurement fields in python"
site: stackoverflow
question_id: 75559962
answer_id: 75572930
url: https://stackoverflow.com/a/75572930
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-26T15:13:26Z
last_edited: 2023-02-27T15:24:56Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75572930/revisions
accepted: true
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0b6984b1dc062b976d909aa3150c304954abe7d1fd6916837a2d615b1794d5c7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75572930>, 2023-02-26, last edited 2023-02-27; **accepted**; score 0. Text as retrieved 2026-10-12.

If your dictionaries were name `assets` and `maturity`

```py
assets = {'BTC': {'030323': 562.7, '170323': 9.900000000000002, '250223': 64.60000000000004, '290923': 17.6, '100323': 53.90000000000002, '310323': 27.4, '260223': 15.499999999999996, '300623': 33.7, '280423': 30.0, '291223': 28.6, '260523': 1.0999999999999999},
          'ETH': {'030323': 562.7, '170323': 9.900000000000002, '250223': 64.60000000000004, '290923': 17.6, '100323': 53.90000000000002, '310323': 27.4, '260223': 15.499999999999996, '300623': 33.7, '280423': 30.0, '291223': 28.6, '260523': 1.0999999999999999}}
maturity = {'250223': ['daily'], '260223': ['bidaily'], '030323': ['weekly'], '100323': ['biweekly'], '170323': ['triweekly'], '310323': ['monthly', 'quarterly'], '280423': ['bimonthly'], '260523': ['trimonthly'], '300623': ['biquarterly'], '290923': ['triquarterly'], '291223': ['yearly']}
```

and if you used [flattened list comprehension](https://www.programiz.com/python-programming/examples/flatten-nested-list) as below

```py
# unlist_single = lambda l: l[0] if getattr(l, '__len__', int)()==1 else l
measurements = [{
    'measurement': 'measurement_name',
    'tags': {'asset': asset, 'maturity_date': mdate, 
             'Expiry': ', '.join(maturity.get(mdate, []))},
    'fields': {'Amount': amount},
    'time': int(time.time()*1000)
} for asset, md_amt in assets.items() for mdate, amount in md_amt.items()] 
```

<sup>[you can also use *`unlist_single(maturity.get(mdate))`* for `Expiry` if you want multiple values to be stored as lists - like <kbd>`['monthly', 'quarterly']`</kbd> instead of *`'monthly, quarterly'`*]</sup>

then `measurements` should return

>```python
> [{'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '030323', 'Expiry': 'weekly'},
>   'fields': {'Amount': 562.7},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '170323', 'Expiry': 'triweekly'},
>   'fields': {'Amount': 9.900000000000002},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '250223', 'Expiry': 'daily'},
>   'fields': {'Amount': 64.60000000000004},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '290923', 'Expiry': 'triquarterly'},
>   'fields': {'Amount': 17.6},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '100323', 'Expiry': 'biweekly'},
>   'fields': {'Amount': 53.90000000000002},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '310323', 'Expiry': 'monthly, quarterly'},
>   'fields': {'Amount': 27.4},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '260223', 'Expiry': 'bidaily'},
>   'fields': {'Amount': 15.499999999999996},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '300623', 'Expiry': 'biquarterly'},
>   'fields': {'Amount': 33.7},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '280423', 'Expiry': 'bimonthly'},
>   'fields': {'Amount': 30.0},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '291223', 'Expiry': 'yearly'},
>   'fields': {'Amount': 28.6},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'BTC', 'maturity_date': '260523', 'Expiry': 'trimonthly'},
>   'fields': {'Amount': 1.0999999999999999},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '030323', 'Expiry': 'weekly'},
>   'fields': {'Amount': 562.7},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '170323', 'Expiry': 'triweekly'},
>   'fields': {'Amount': 9.900000000000002},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '250223', 'Expiry': 'daily'},
>   'fields': {'Amount': 64.60000000000004},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '290923', 'Expiry': 'triquarterly'},
>   'fields': {'Amount': 17.6},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '100323', 'Expiry': 'biweekly'},
>   'fields': {'Amount': 53.90000000000002},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '310323', 'Expiry': 'monthly, quarterly'},
>   'fields': {'Amount': 27.4},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '260223', 'Expiry': 'bidaily'},
>   'fields': {'Amount': 15.499999999999996},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '300623', 'Expiry': 'biquarterly'},
>   'fields': {'Amount': 33.7},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '280423', 'Expiry': 'bimonthly'},
>   'fields': {'Amount': 30.0},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '291223', 'Expiry': 'yearly'},
>   'fields': {'Amount': 28.6},
>   'time': 1677421469057},
>  {'measurement': 'measurement_name',
>   'tags': {'asset': 'ETH', 'maturity_date': '260523', 'Expiry': 'trimonthly'},
>   'fields': {'Amount': 1.0999999999999999},
>   'time': 1677421469057}]
>```
