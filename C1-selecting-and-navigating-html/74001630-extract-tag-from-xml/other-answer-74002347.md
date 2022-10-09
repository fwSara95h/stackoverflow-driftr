---
title: "Extract Tag from XML"
site: stackoverflow
question_id: 74001630
answer_id: 74002347
url: https://stackoverflow.com/a/74002347
author: "HedgeHog"
author_url: https://stackoverflow.com/users/14460824
posted: 2022-10-09T05:31:37Z
last_edited: 2022-10-09T05:36:57Z
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f7bf832a71191e10a50e51a572704cafb3cc286ec85674cfb5be1e5d9b9e1568
role: another answer on the same question, kept as context; not my work
---

# Answer by [HedgeHog](https://stackoverflow.com/users/14460824) — 2022-10-09

Posted on Stack Overflow, <https://stackoverflow.com/a/74002347>, 2022-10-09, last edited 2022-10-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Try to check the response of your example first, it is JSON not XML so no `BeautifulSoup` needed here, simply iterate the data list to pick your fact_sheets:

    for plan in Data.json()['data']:
        print(plan['fact_sheet'])

Out:

    https://rates.cleanskyenergy.com:8443/rates/DownloadDoc?path=a70e9298-5537-481a-985c-c7a005b2e4f3.html&id_plan=223344
    https://texpo-prod-api.eroms.works/api/v1/document/ViewProductDocument?type=efl&rateCode=SRCPLF24PTC&lang=en
    https://www.txu.com/Handlers/PDFGenerator.ashx?comProdId=TCXSIMVL1212AR&lang=en&formType=EnergyFactsLabel&custClass=3&tdsp=AEPTCC
    https://signup.myvaluepower.com/Home/EFL?productId=32653&Promo=16410
    https://docs.cloud.flagshippower.com/EFL?term=36&duns=007924772&product=galleon&lang=en&code=FPSPTC2
    ...

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[TaxAssassin](https://stackoverflow.com/users/20194598)** (2022-10-09): Wow, thank you so much! I researched the differences between JSON and XML after your comment and I can that although the header states it is in XML format the data is actually in JSON. Thank you again!
