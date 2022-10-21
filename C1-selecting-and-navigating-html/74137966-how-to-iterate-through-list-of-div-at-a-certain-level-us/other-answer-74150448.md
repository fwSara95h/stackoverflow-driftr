---
title: "How to iterate through list of div at a certain level using BeautifulSoup?"
site: stackoverflow
question_id: 74137966
answer_id: 74150448
url: https://stackoverflow.com/a/74150448
author: "HedgeHog"
author_url: https://stackoverflow.com/users/14460824
posted: 2022-10-21T07:56:45Z
last_edited: 2022-10-21T08:21:11Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 035392134e0280b2404eb5ad01d119fa65568d196f3b7a30dcc1bf694eedc689
role: another answer on the same question, kept as context; not my work
---

# Answer by [HedgeHog](https://stackoverflow.com/users/14460824) — 2022-10-21

Posted on Stack Overflow, <https://stackoverflow.com/a/74150448>, 2022-10-21, last edited 2022-10-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Just in addition to simplify the selection a bit - You could use all `<a>` that has a `<h3>` as container for your iterations:

    soup.select('a:has(h3)')


#### Example

Uses `cookies={'CONSENT':'YES+'}` cause it is necessary from my location to set, but could be ignored from yours.

    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    
    url = 'https://www.google.com/search?num=250&q=Apple+innovation%20performance&oq=Apple+innovation%20performance%3D1600&source=lnt&tbs=cdr:1,cd_min:1/1/2018,cd_max:12/31/2018&tbm=nws&hl=en-US'
    response = requests.get(url,headers = {'User-Agent': 'Mozilla/5.0'}, cookies={'CONSENT':'YES+'})
    
    data = []
    
    soup = BeautifulSoup(response.text)
    for e in soup.select('a:has(h3)'):
        data.append({
            'title': e.h3.get_text(),
            'date': e.span.get_text(),
            'excerpt':e.br.previous,
            'site': e.h3.find_next_sibling('div').get_text() if e.h3.find_next_sibling('div') else None,
            'url': e.get('href').strip('/url?q=')
        })
    pd.DataFrame(data)


#### Output

|    | title                                                                | date         | excerpt                                                                                                                                        | site               | url                                                                                                                                                                                                         |
|---:|:---------------------------------------------------------------------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | Apple iPhone 14: Premium Smartphone with Innovation Issues           | 4 days ago   | The Apple iPhone 14 performs very well in our review and achieves top scores primarily in the performance, display, and camera categories.     | NotebookCheck.net  | https://www.notebookcheck.net/Apple-iPhone-14-Premium-Smartphone-with-Innovation-Issues.661772.0.html&sa=U&ved=2ahUKEwicrvmP7PD6AhVPDuwKHQqAA5IQxfQBegQIBxAC&usg=AOvVaw3iLsrux3Epc_tFQbj7MUh1               |
|  1 | Improvement over innovation: are Apple's latest products a letdown?  | 16 hours ago | Improvement over innovation: are Apple's latest products a letdown? ... for those willing to pay more for Pro models, improved performance.    | The Oxford Student | https://www.oxfordstudent.com/2022/10/20/improvement-over-innovation-are-apples-latest-products-a-letdown/&sa=U&ved=2ahUKEwicrvmP7PD6AhVPDuwKHQqAA5IQxfQBegQIYxAC&usg=AOvVaw1gwOjOUJox68KMeiPj_CR8          |
|  2 | Apple iPad Pro: New generation with M2 chip, Wi-Fi 6E and more       | 2 days ago   | A 10-core GPU with up to 35 percent faster graphics performance ... Otherwise, the innovations of the new Apple iPad Pro are in the details.   | Basic Tutorials    | https://basic-tutorials.com/news/apple-ipad-pro-new-generation-with-m2-chip-wi-fi-6e-and-more/&sa=U&ved=2ahUKEwicrvmP7PD6AhVPDuwKHQqAA5IQxfQBegQIYhAC&usg=AOvVaw07b023WuvT4kB1XoO2-yla                      |
|  3 | Apple ditched Intel and never looked back — are other laptop ...     | 15 hours ago | Called the M1 chip, Apple stuffed it inside a Mac Mini, ... products with the most extraordinary performance, most innovative technology,...   | Laptop Mag         | https://www.laptopmag.com/features/apple-ditched-intel-and-never-looked-back-are-other-laptop-makers-doing-the-same&sa=U&ved=2ahUKEwicrvmP7PD6AhVPDuwKHQqAA5IQxfQBegQIYRAC&usg=AOvVaw3IjNFjvFz_B3B3Xzu767gh |
|  4 | Chinese supply chain able to cope with impact of potential Apple ... | 1 day ago    | One of Apple's manufacturers in China has been instructed to immediately ... assessment of the iPhone 14 series' performance in the Chinese... | Global Times       | https://www.globaltimes.cn/page/202210/1277497.shtml&sa=U&ved=2ahUKEwicrvmP7PD6AhVPDuwKHQqAA5IQxfQBegQIXhAC&usg=AOvVaw2dUujWfIkidI1-TpdWsqvh                                                                |

...
