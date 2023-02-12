---
title: "Python | How i get the link of products that doesn't have href with selenium"
site: stackoverflow
question_id: 75426987
answer_id: 75429108
url: https://stackoverflow.com/a/75429108
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2023-02-12T18:06:01Z
last_edited: 2023-02-16T13:02:48Z
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b59ca1ada531d8331beeb05988f7865c4e0f386a3202b5375b1ed716650fcd49
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2023-02-12

Posted on Stack Overflow, <https://stackoverflow.com/a/75429108>, 2023-02-12, last edited 2023-02-16; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can use their Ajax API to download the information about the items (one of the info is the URL):

```py
import requests

api_url = "https://api.wallapop.com/api/v3/general/search"
params = {
    "keywords": "monitor",
    "filters_source": "search_box",
    "latitude": "39.46895",
    "longitude": "-0.37686",
}

data = requests.get(api_url, params=params).json()

for o in data["search_objects"]:
    print(
        "{:<30} {:<5} {}".format(
            o["title"][:30], o["price"], "https://es.wallapop.com/item/" + o["web_slug"]
        )
    )
```

Prints:

```none
Monitor Philips                50.0  https://es.wallapop.com/item/pantalla-pc-874564380
monitor de vigilancia de bebé  48.0  https://es.wallapop.com/item/monitor-de-vigilancia-de-bebe-874583928
MONITOR PC NUEVO               100.0 https://es.wallapop.com/item/monitor-pc-nuevo-874568539
Monitor LG 24"                 65.0  https://es.wallapop.com/item/monitor-lg-24-874529151
Monitor Samsung 24"            80.0  https://es.wallapop.com/item/monitor-samsung-24-874496925
monitor roto gaming msi 32     50.0  https://es.wallapop.com/item/monitor-roto-gaming-msi-32-874589740
Monitor 22 pulgadas Full HD    30.0  https://es.wallapop.com/item/monitor-22-pulgadas-full-hd-874571734
Monitor Keep Out 32" Full HD H 120.0 https://es.wallapop.com/item/monitor-keep-out-32-full-hd-hdmi-874555259
Monitor Asus 4k 60hz con caja  230.0 https://es.wallapop.com/item/monitor-asus-4k-60hz-con-caja-874575205
Monitor Keep Out XGM24P 24" Fu 85.0  https://es.wallapop.com/item/monitor-keep-out-xgm24p-24-full-hd-hdmi-874557938
MONITOR HP W2072a NEGRO        50.0  https://es.wallapop.com/item/monitor-hp-w2072a-negro-874446605
Monitor ASUS VZ249HE 23.8" Ful 119.0 https://es.wallapop.com/item/monitor-asus-vz249he-23-8-full-hd-874542630
Samsung Monitor Curvo Gaming   150.0 https://es.wallapop.com/item/samsung-monitor-curvo-gaming-874418062
Monitor Lenovo L22e-20 21,5" F 80.0  https://es.wallapop.com/item/monitor-lenovo-l22e-20-21-5-full-hd-hdmi-874560092
Monitor Acer 18.5''            20.0  https://es.wallapop.com/item/monitor-acer-18-5-874380113
se vende monitor asus          45.0  https://es.wallapop.com/item/se-vende-monitor-asus-874244944
HP 22W Monitor                 60.0  https://es.wallapop.com/item/hp-22w-monitor-874320493
MONITOR ASUS 19 NUEVO          60.0  https://es.wallapop.com/item/monitor-asus-19-nuevo-874239039
Monitor Hp                     150.0 https://es.wallapop.com/item/monitor-hp-874114954
Monitor pc                     10.0  https://es.wallapop.com/item/monitor-pc-874098257
Monitor HP negro 20 pulgadas   15.0  https://es.wallapop.com/item/monitor-hp-negro-20-pulgadas-874234251
Monitor 21.5" Full HD LED      80.0  https://es.wallapop.com/item/monitor-21-5-full-hd-led-874261942
Monitor MEDION MD 5043 OD, des 10.0  https://es.wallapop.com/item/monitor-medion-md-5043-od-despiece-874263768
Monitor LED de 24" - LG 24EA53 80.0  https://es.wallapop.com/item/monitor-led-de-24-lg-24ea53vq-p-874296411
Monitor para ordenador         10.0  https://es.wallapop.com/item/monitor-para-ordenador-873697820
Monitor HP 27o negociable      110.0 https://es.wallapop.com/item/monitor-hp-27o-negociable-874017054
Monitor Samsung                30.0  https://es.wallapop.com/item/monitor-samsung-873754031
Monitor philips                30.0  https://es.wallapop.com/item/monitor-philips-873752989
BenQ GL2460 - Monitor LED de 2 50.0  https://es.wallapop.com/item/benq-gl2460-monitor-led-de-24-full-hd-2ms-hdmi-874289910
Monitor 2 k                    100.0 https://es.wallapop.com/item/monitor-2-k-873847429
Monitores Tv Monitor Lg M197wd 29.9  https://es.wallapop.com/item/monitores-tv-monitor-lg-m197wdp-hdmi-873875385
Samsung Monitor Profesional de 150.0 https://es.wallapop.com/item/samsung-monitor-profesional-de-27-2k-874038879
Monitor hp 22xw Pavillon como  70.0  https://es.wallapop.com/item/monitor-hp-22xw-como-nuevo-874014297
Monitor 24" Benq XL2411T 144Hz 150.0 https://es.wallapop.com/item/monitor-24-benq-xl2411t-144hz-874159199
Monitor                        65.0  https://es.wallapop.com/item/monitor-873408045
Monitor benq 144hz             120.0 https://es.wallapop.com/item/monitor-benq-144hz-873858204
Monitor 21,5" Samsung          69.0  https://es.wallapop.com/item/monitor-21-5-samsung-873777001
2x monitores Asus 19.5" sin es 60.0  https://es.wallapop.com/item/2x-monitores-asus-19-5-sin-estrenar-874000367
Monitores baratos              7.0   https://es.wallapop.com/item/monitores-baratos-873394797
MONITOR HP 21'5 LCD            95.0  https://es.wallapop.com/item/monitor-hp-21-5-lcd-873879049
```

---

EDIT: To get the products from next pages you can add `start=` parameter to URL:

```py
import requests

api_url = "https://api.wallapop.com/api/v3/general/search"
params = {
    "keywords": "monitor",
    "filters_source": "search_box",
    "latitude": "39.46895",
    "longitude": "-0.37686",
    "start": 0
}


for page in range(0, 3):  # <-- increase number of pages here
    params['start'] = page * 40

    data = requests.get(api_url, params=params).json()
    for o in data["search_objects"]:
        print(
            "{:<30} {:<5} {}".format(
                o["title"][:30], o["price"], "https://es.wallapop.com/item/" + o["web_slug"]
            )
        )
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[SkyManu](https://stackoverflow.com/users/21197547)** (2023-02-13): Thank you so much, works so well, where can i learn more about this API's?
- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-02-13): @SkyManu I've found this API call in Web Developer Tools (in Firefox, but Chrome has something similar) -> Network Tab. Refresh the page and you will see the API URL there.
- **[SkyManu](https://stackoverflow.com/users/21197547)** (2023-02-16): The problem with this is that i just have the first 40 products, in my original script i could get every product of the page with selenium scrolling down. Do you know is there a way to get all products using the api?
