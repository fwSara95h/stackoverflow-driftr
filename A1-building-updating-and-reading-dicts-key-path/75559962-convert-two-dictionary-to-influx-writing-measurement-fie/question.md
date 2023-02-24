---
title: "Convert two dictionary to influx writing measurement fields in python"
site: stackoverflow
question_id: 75559962
url: https://stackoverflow.com/q/75559962
asked: 2023-02-24T18:04:19Z
asked_by: "Madan"
asked_by_url: https://stackoverflow.com/users/16488519
last_edited: never
tags: [python, json, dictionary, hashmap, influxdb]
score: 1
views_at_snapshot: 98
answer_count: 1
accepted_answer_id: 75572930
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ca4faca8fddfd0383f99900e4a0600230791b8fe35394bb9c1efbb14d62d5b68
---

# Convert two dictionary to influx writing measurement fields in python

Asked by [Madan](https://stackoverflow.com/users/16488519) on Stack Overflow, <https://stackoverflow.com/q/75559962>, 2023-02-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a dictionary like

    {'BTC': {'030323': 562.7,
      '170323': 9.900000000000002,
      '250223': 64.60000000000004,
      '290923': 17.6,
      '100323': 53.90000000000002,
      '310323': 27.4,
      '260223': 15.499999999999996,
      '300623': 33.7,
      '280423': 30.0,
      '291223': 28.6,
      '260523': 1.0999999999999999},
     'ETH': {'030323': 562.7,
      '170323': 9.900000000000002,
      '250223': 64.60000000000004,
      '290923': 17.6,
      '100323': 53.90000000000002,
      '310323': 27.4,
      '260223': 15.499999999999996,
      '300623': 33.7,
      '280423': 30.0,
      '291223': 28.6,
      '260523': 1.0999999999999999}}

and other dictionary like

    {'250223': ['daily'],
     '260223': ['bidaily'],
     '030323': ['weekly'],
     '100323': ['biweekly'],
     '170323': ['triweekly'],
     '310323': ['monthly', 'quarterly'],
     '280423': ['bimonthly'],
     '260523': ['trimonthly'],
     '300623': ['biquarterly'],
     '290923': ['triquarterly'],
     '291223': ['yearly']}

I need data structure to insert it into influx db.

Example:

    {'measurement': 'measurement_name',
            'tags': {
                    'asset': 'BTC', 
                    'maturity_date': 030323, 
                    'Expiry' - 'weekly'
                },
            'fields': {
                'Amount' - '562.7' 
                },
            'time': int(time.time()*1000),
            }
Confused with the data format on how to do it for all the values, is there any mapping that would be helpful.
