---
title: "How to get weather data from site?"
site: stackoverflow
question_id: 74048864
url: https://stackoverflow.com/q/74048864
asked: 2022-10-12T23:10:49Z
asked_by: "laisp-lostlamb"
asked_by_url: https://stackoverflow.com/users/20162704
last_edited: never
tags: [python, html, lxml]
score: 0
views_at_snapshot: 421
answer_count: 2
accepted_answer_id: 74135961
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ce837eea6a7554857b4b9db59afa6f0b05449acc1b8394019a6614bc7028b407
---

# How to get weather data from site?

Asked by [laisp-lostlamb](https://stackoverflow.com/users/20162704) on Stack Overflow, <https://stackoverflow.com/q/74048864>, 2022-10-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm not able to get the Dew_Point and Wind Data from the site https://weather.gc.ca/city/pages/ab-52_metric_e.html

import requests
from lxml import html

```
        # Get the html page
        resp=requests.get("https://weather.gc.ca/city/pages/ab-52_metric_e.html")
        # Build html tree
        html_tree=html.fromstring(resp.text)

        #Dew_point=html_tree.xpath("//dd[@class='mrgn-bttm-0 wxo-metric-hide'][(parent::dl[@class='dl-horizontal wxo-conds-col2'])]//text()")[1].replace("Â", "")
        # Print Dew_point
        #print(f"Dew_point in {city_name} is {Dew_point}")  

        #Wind=html_tree.xpath("//dd[@class='longContent mrgn-bttm-0 wxo-metric-hide'][(parent::dl[@class='dl-horizontal wxo-conds-col2'])]//text()")[0].replace("Â", "")
        # Print Wind
        #print(f"Wind in {city_name} is {Wind}")  
```

Data should be in the following format:
Dew point:-2.3°C
Wind: NE 9 km/h

The direction for wind may change.

I'm not sure how to parse the following HTML code, thanks again for the help!
```
<dt>Temperature:</dt>
<dd class="mrgn-bttm-0 wxo-metric-hide">13.2°<abbr title="Celsius">C</abbr>
</dd>
<dd class="mrgn-bttm-0 wxo-imperial-hide wxo-city-hidden">55.8°
					<abbr title="Fahrenheit">F</abbr>
</dd>
<dt>Dew point:</dt>
<dd class="mrgn-bttm-0 wxo-metric-hide">-2.3°<abbr title="Celsius">C</abbr>
</dd>
<dd class="mrgn-bttm-0 wxo-imperial-hide wxo-city-hidden">27.9°<abbr title="Fahrenheit">F</abbr>
</dd>
<dt>Humidity:</dt>
<dd class="mrgn-bttm-0">34%</dd>
</dl></div>
<div class="col-sm-4"><dl class="dl-horizontal wxo-conds-col3">
<dt>Wind:</dt>
<dd class="longContent mrgn-bttm-0 wxo-metric-hide">
<abbr title="Northeast">NE</abbr> 9 <abbr title="kilometres per hour">km/h</abbr>
</dd>
<dd class="longContent mrgn-bttm-0 wxo-imperial-hide wxo-city-hidden">
<abbr title="Northeast">NE</abbr> 6 <abbr title="miles per hour">mph</abbr>
</dd>
<dt>Visibility:</dt>
<dd class="mrgn-bttm-0 wxo-metric-hide">48 <abbr title="kilometres">km</abbr>
</dd>
<dd class="mrgn-bttm-0 wxo-imperial-hide wxo-city-hidden">30 miles</dd>
</dl></div> 
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Karl Knechtel](https://stackoverflow.com/users/523612)** (2022-10-12): "I'm not sure how to parse the following HTML code, thanks again for the help!" If you mean "How do I parse the following HTML code?", then **ask that** - we want clear, [specific](https://meta.stackoverflow.com/questions/284236) questions here, [not thanks](https://meta.stackoverflow.com/questions/288160/no-thanks-damn-it), because this is **not a discussion forum**. If you do have some idea but it went wrong, then either [try to locate](https://ericlippert.com/2014/03/05/how-to-debug-small-programs/) a problem and show a [mre], or else ask specifically about *how to do that part*.
- **[Karl Knechtel](https://stackoverflow.com/users/523612)** (2022-10-12): Also: assuming that you have [already determined](https://meta.stackoverflow.com/questions/261592) that the right way to approach the problem is to download the HTML and parse it (as opposed to, say, looking for an API); you already have working code that gives you that HTML; and the *problem* is how to parse the HTML, then *ask a question about parsing the HTML*. It does not help to show us how you got the HTML, because that doesn't change how to parse it; that code is irrelevant to the question, and the title is actively misleading. Please read [ask].
- **[Karl Knechtel](https://stackoverflow.com/users/523612)** (2022-10-12): I can see  that you have some commented-out code that looks like it's intended to parse the HTML. **What happens** when you try using that? **How is that different** from what is supposed to happen? Please actually describe a concrete problem.
- **[laisp-lostlamb](https://stackoverflow.com/users/20162704)** (2022-10-14): Hi, will do that and check over the FAQ for how to ask questions, wasn't aware of it.
