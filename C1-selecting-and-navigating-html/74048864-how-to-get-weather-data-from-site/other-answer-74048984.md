---
title: "How to get weather data from site?"
site: stackoverflow
question_id: 74048864
answer_id: 74048984
url: https://stackoverflow.com/a/74048984
author: "Cezar Peixeiro"
author_url: https://stackoverflow.com/users/20143178
posted: 2022-10-12T23:30:51Z
last_edited: 2022-10-20T03:44:15Z
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 948deefaa4febfddd1d6e95f14ad8ed68152db366acb6daf6934f5e61a626d2b
role: another answer on the same question, kept as context; not my work
---

# Answer by [Cezar Peixeiro](https://stackoverflow.com/users/20143178) — 2022-10-12

Posted on Stack Overflow, <https://stackoverflow.com/a/74048984>, 2022-10-12, last edited 2022-10-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The best approach is to use BeautifulSoup to parse the page.

This is what you want:

    import requests
    from bs4 import BeautifulSoup

    resp = requests.get("https://weather.gc.ca/city/pages/ab-52_metric_e.html").content

    soup = BeautifulSoup(resp, "html.parser")

    all_dt = soup.find_all("dt")

    #if you want more metrics, just add it to the list
    metrics = ["Dew point:","Wind:","Pressure:","Condition:","Tendency:","Temperature:", "Humidity:", "Visibility:"]

    data = {}

    for metric in metrics:
      data[metric] = []

    for elem in all_dt:
      if elem.text in metrics:
        value = elem.next_sibling.next_sibling
        data[elem.text].append(value.text.strip("\n") if  value != None else "No Data")

    print(data)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[laisp-lostlamb](https://stackoverflow.com/users/20162704)** (2022-10-19): Hi, above code does work, would like to access the following sibling elements,       Condition: Partly Cloudy Pressure: 102.0 kPa Tendency: Falling Temperature: 23.3°C Dew point: -5.7°C Humidity: 14% Wind: S 10 km/h Visibility: 24 km
- **[Cezar Peixeiro](https://stackoverflow.com/users/20143178)** (2022-10-20): I will edit the answer with a more flexible code. If it resolver your question, please accept it.
- **[laisp-lostlamb](https://stackoverflow.com/users/20162704)** (2022-10-20): {'Dew point:': ['-1.9°C', '-1.9°C', '-1.9°C'], 'Wind:': ['N 27  gust 39 km/h', 'N 27  gust 39 km/h', 'N 27  gust 39 km/h'], 'Pressure:': ['101.0 kPa', '101.0 kPa', '101.0 kPa'], 'Condition:': ['Mostly Cloudy', 'Mostly Cloudy'], 'Tendency:': ['Falling', 'Falling'], 'Temperature:': ['15.9°C', '15.9°C', '15.9°C'], 'Humidity:': ['29%', '29%', '29%'], 'Visibility:': ['19 km', '19 km', '19 km']} Hi this does work, just the items appear 3 times, I believe this is because the text does appear 3 times as td when viewed as inspecting the source element.
