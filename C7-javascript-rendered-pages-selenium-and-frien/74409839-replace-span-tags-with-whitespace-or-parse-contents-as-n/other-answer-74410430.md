---
title: "Replace span tags with whitespace or parse contents as new column with pandas.read_html"
site: stackoverflow
question_id: 74409839
answer_id: 74410430
url: https://stackoverflow.com/a/74410430
author: "Md. Fazlul Hoque"
author_url: https://stackoverflow.com/users/12848411
posted: 2022-11-12T04:46:37Z
last_edited: 2022-11-12T04:52:03Z
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f88ef2203f34ca99b4f945f4ce61d16a21afa98083d9c7f7a0c49a728e4570f1
role: another answer on the same question, kept as context; not my work
---

# Answer by [Md. Fazlul Hoque](https://stackoverflow.com/users/12848411) — 2022-11-12

Posted on Stack Overflow, <https://stackoverflow.com/a/74410430>, 2022-11-12, last edited 2022-11-12; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

 To separate company names and tickers or parse the span as another column aka to get overall neat and clean `ResultSet`, you can change your tool selection strategy a bit.  In this case, It would be better to `apply bs4 with pandas DataFrame` instead of pd.read_html() method.

**Full working code as an example:**

    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
    import time
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #The base url: https://www.capitoltrades.com/trades?assetType=stock&pageSize=50
    data = []
    for page in range(1, 5):
        driver.get(f'https://www.capitoltrades.com/trades?assetType=stock&pageSize=50&page={page}')
        driver.maximize_window()
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        for row in soup.select('table.q-table.trades-table > tbody tr'):
            Politician = row.select_one('[class="q-fieldset politician-name"] > a').text.strip()
            Politician_info = row.select_one('[class="q-fieldset politician-info"]').get_text(' ',strip=True)
            Traded_Issuer = row.select_one('[class="q-fieldset issuer-name"] > a').text.strip()
            Issuer_ticker =row.select_one('span[class="q-field issuer-ticker"]').text.strip()
            Published = row.select_one('[class="q-td q-column--pubDate"] .q-value').text.strip()
            Traded = row.select_one('[class="q-td q-column--txbDate"] .q-value')
            Traded = Traded.text.strip() if Traded else None
            Filed_after = row.select_one('[class="q-td q-column--reportingGap"] .q-value').text.strip()
            Owner =row.select_one('[class="svg-image owner-icon"]+span').text.strip()
            _type = row.select_one('[class="q-data-cell tx-type"]').get_text(strip=True)
            Size = row.select_one('[class="q-td q-column--value"] > div').get_text(strip=True)
            #Size = Size.text.strip() if Size else None
            Price =row.select_one('[class="q-field trade-price"]').text.strip()
    
            data.append({
                'Politician':Politician,
                'Politician_info':Politician_info,
                'Traded_Issuer':Traded_Issuer,
                'Issuer_ticker':Issuer_ticker,
                'Published':Published,
                'Traded':Traded,
                'Filed_after':Filed_after,
                'Owner':Owner,
                'Type':_type,
                'Size':Size,
                'Price':Price
    
            })
    
    
    df = pd.DataFrame(data)
    print(df)

**Output:**

 

                       Politician      Politician_info                 Traded_Issuer Issuer_ticker  ...        Owner  Type      Size   Price
    0    Debbie Wasserman Schultz    Democrat House FL  ADAMS RESOURCES & ENERGY INC         AE:US  ...        Child  sell  1K - 15K   32.27     
    1               Kathy Manning    Democrat House NC                         3M Co        MMM:US  ...       Spouse   buy  1K - 15K  108.95     
    2               Kathy Manning    Democrat House NC                 Accenture PLC        ACN:US  ...       Spouse   buy  1K - 15K  250.07     
    3               Kathy Manning    Democrat House NC                     Adobe Inc       ADBE:US  ...       Spouse  sell  1K - 15K  286.15     
    4               Kathy Manning    Democrat House NC                  Alphabet Inc      GOOGL:US  ...       Spouse   buy  1K - 15K   97.56     
    ..                        ...                  ...                           ...           ...  ...          ...   ...       ...     ...       
    195         Diana Harshbarger  Republican House TN                 CME Group Inc        CME:US  ...        Joint  sell  1K - 15K  176.26       
    196         Diana Harshbarger  Republican House TN                 CME Group Inc        CME:US  ...       Spouse  sell  1K - 15K  176.26       
    197         Diana Harshbarger  Republican House TN            The Home Depot Inc         HD:US  ...  Undisclosed  sell  1K - 15K  268.69       
    198         Diana Harshbarger  Republican House TN            The Home Depot Inc         HD:US  ...  Undisclosed  sell  1K - 15K  268.69       
    199         Diana Harshbarger  Republican House TN            The Home Depot Inc         HD:US  ...        Joint  sell  1K - 15K  268.69       
    
    [200 rows x 11 columns]
