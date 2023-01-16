---
title: "bse result data scraping from bse site"
site: stackoverflow
question_id: 73414578
answer_id: 75129525
url: https://stackoverflow.com/a/75129525
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-16T01:24:24Z
last_edited: 2024-02-19T18:26:12Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75129525/revisions
accepted: true
score: 3
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-hidden-api-json
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0d22aa6b349d97008c93dc33e4e3ae74681be5cd761d52b1aef0cc3740e5fe71
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75129525>, 2023-01-16, last edited 2024-02-19; **accepted**; score 3. Text as retrieved 2026-10-12.

I assume that you're trying to get the data from [this table][5]; if you [preview][6] the source code (in the [network logs](https://support.happyfox.com/kb/article/882-accessing-the-browser-console-and-network-logs/)), or [check the text contents][4] of `div_list`, you might notice that the source code (which is all that `requests.get` fetches) only contains a *template* for the table, which is later filled in with [data loaded][7] via [an API][8].

---

You could simply set the dates in the `apiUrl` <sub>[go to [sample link](https://api.bseindia.com/BseIndiaAPI/api/AnnGetData/w?pageno=2&strCat=-1&strPrevDate=20230113&strScrip=&strSearch=P&strToDate=20230115&strType=C)]</sub> and call [`pd.DataFrame(requests.get(apiUrl).json()['Table'])`][1], but you will get only the first 50 rows [at maximum] this way.

---

To get more than the first 50 rows, you can wrap it in a recursive function:

```python
# from datetime import date, timedelta
# import requests
def bseindia_apiScraper(searchDate=None, qParams={}, prevData=None, depth=0):
    def cleanDate(sd):
        if not isinstance(sd, date):
            sd = str(sd).strip()
            try: sd  = date.fromisoformat(f'{sd[:4]}-{sd[4:6]}-{sd[6:]}')
            except: sd = date.today()
        return sd.isoformat().replace('-', '')
    
    isv = qParams.get('printMsgs', False)
    maxDepth = qParams.get('maxDepth', 998)
    prevData = prevData if prevData else []
    curPg = int(qParams.get('pageno', 1))
    curData, totalRows, totalPgs, t1Data = [], 0, 0, 'N/A'

    daysDict = {'week': 7, 'month': 30, 'year': 365}
    searchDate = searchDate if searchDate else date.today()  
    if searchDate in daysDict: searchDate = daysDict[searchDate]
    if isinstance(searchDate, int) and searchDate > 0:
        prevDate = date.today() - timedelta(days=searchDate)
        qParams['strPrevDate'] = cleanDate(prevDate)
        qParams['strToDate'] = cleanDate(date.today()) 
    searchDate = cleanDate(searchDate) 

    qDefaults = {
        'pageno': 1, 'strCat': -1, 'strPrevDate': searchDate, 'strScrip': '', 
        'strSearch': 'P', 'strToDate': searchDate, 'strType': 'C'
    }
    qStr = [(k, qParams.get(k, v)) for k, v in qDefaults.items()]
    qStr = '&'.join([f'{qk}={qv}' for qk, qv in qStr])
    apiUrl = f'https://api.bseindia.com/BseIndiaAPI/api/AnnGetData/w?{qStr}'

    apiResp = requests.get(apiUrl, headers={'user-agent': 'Mozilla/5.0'}) 
    rMsg = f'{apiResp.status_code} {apiResp.reason} from {apiResp.url}'
    try:
        jData = apiResp.json()
        if not isinstance(jData.get('Table'), list): apiResp.raise_for_status()
        curData, t1Data = jData.get('Table', []), jData.get('Table1')
        if curData: totalPgs = curData[0].get('TotalPageCnt', 0) 
        status, msg = 'success', f'[page {curPg} of {totalPgs}] ' 
        msg += f'collected [{len(prevData)}+]{len(curData)} rows of data'
    except Exception as e:
        status, msg = 'error', f'{type(e)} {e}'    
    if isv: print(f'[{depth}][{status}] {rMsg}\n{msg} from {apiUrl}')

    # retry same page [if request failed] or get next page #
    nextPg = None
    if depth < maxDepth: 
        if status == 'success' and curPg < totalPgs: nextPg = curPg + 1
        if status == 'error' and apiResp.status_code != 200:
            nextPg = curPg + int(len(curData) > 0)
    if nextPg:
        qParams['pageno'] = nextPg
        return bseindia_apiScraper(
            searchDate=searchDate, qParams=qParams, 
            prevData=prevData[:]+curData[:], depth=depth+1)
    
    ## return collected data ##
    if isinstance(t1Data,list) and len(t1Data)==1: t1Data = t1Data[0] 
    return {
        'data': prevData[:]+curData[:], 'Table1': t1Data, 'status': status, 
        'msg': msg, 'latest_call': apiUrl, 'latest_rStatus': rMsg, 
        'depth': depth, 'maxDepth': maxDepth, 'qParams': qParams
    }
```

(This also allows you to parametrize it and to add in some error-handling as well.) To just get that day's data, you could simply call [`bseindia_apiScraper()`][3] <sub>[or [`pd.DataFrame(bseindia_apiScraper()['data'])`][2] to get it as a DataFrame].</sub>

---

You can also form the XBRL and attachment links from the collected data.

```python
# import pandas as pd
weekScrape = bseindia_apiScraper('week')#, {'printMsgs':True})
weekDf = pandas.DataFrame(weekScrape['data'])

xbrRoot = 'https://www.bseindia.com/Msource/90D/CorpXbrlGen.aspx'
scripcodes = pandas.Series([str(s) for s in weekDf['SCRIP_CD']])
weekDf['XBR_link'] = f'{xbrRoot}?Bsenewid=' + weekDf['NEWSID'] 
weekDf['XBR_link'] = weekDf['XBR_link'] + '&Scripcode=' + scripcodes

flRoot = 'https://www.bseindia.com/xml-data/corpfiling/AttachLive/'
weekDf['ATTACHMENT_link'] = flRoot + weekDf['ATTACHMENTNAME'] 

# weekDf.to_csv('bseindia.csv', index=False)
```

Below is a sample of `weekDf` [see [bseindia.csv](https://docs.google.com/spreadsheets/d/1dRFUewghMtMpAt7PqzbQxgdMERlYWCs4lMdVXvfXSc4/edit?usp=sharing) for all rows]:

|   index | NEWSID                               |   SCRIP_CD | XML_NAME                                        | NEWSSUB                                                                                                                                | DT_TM                   | NEWS_DT                 |   CRITICALNEWS | ANNOUNCEMENT_TYPE   | QUARTER_ID   | FILESTATUS   | ATTACHMENTNAME                           | MORE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | HEADLINE                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | CATEGORYNAME   |   OLD |   RN |   PDFFLAG | NSURL                                                                                   | SLONGNAME                   |   AGENDA_ID |   TotalPageCnt | News_submission_dt   | DissemDT                | TimeDiff   |   Fld_Attachsize | XBR_link                                                                                                             | ATTACHMENT_link                                                                                  |
|--------:|:-------------------------------------|-----------:|:------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|:------------------------|:------------------------|---------------:|:--------------------|:-------------|:-------------|:-----------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|------:|-----:|----------:|:----------------------------------------------------------------------------------------|:----------------------------|------------:|---------------:|:---------------------|:------------------------|:-----------|-----------------:|:---------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
|       0 | 57cf0c81-22b1-43c9-a704-841209ecb822 |     531155 | ANN_531155_57CF0C81-22B1-43C9-A704-841209ECB822 | EPSOM PROPERTIES LTD. - 531155 - Compliances-Certificate under Reg. 74 (5) of SEBI (DP) Regulations, 2018                              | 2023-01-15T23:48:25.81  | 2023-01-15T23:48:25.81  |              0 | A                   | None         | N            | f4d985ab-3468-4caf-bf15-13568f5984d7.pdf |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Certificate under Regulation 74 (5) of SEBI (Depositories and Participants) Regulations, 2018 for the quarter ended 31st December, 2022                                                                                                                                                                                                                                                                                                                                    | Company Update |     1 |    1 |         0 | https://www.bseindia.com/stock-share-price/epsom-properties-ltd/epsompro/531155/        | EPSOM PROPERTIES LTD.       |         212 |             97 | 2023-01-15T23:48:25  | 2023-01-15T23:48:25.81  | 00:00:00   |      2.24986e+06 | https://www.bseindia.com/Msource/90D/CorpXbrlGen.aspx?Bsenewid=57cf0c81-22b1-43c9-a704-841209ecb822&Scripcode=531155 | https://www.bseindia.com/xml-data/corpfiling/AttachLive/f4d985ab-3468-4caf-bf15-13568f5984d7.pdf |
|       3 | f81472c4-2181-47ce-a238-fc3f61b52110 |     534920 | ANN_534920_F81472C4-2181-47CE-A238-FC3F61B52110 | COVIDH TECHNOLOGIES LIMITED - 534920 - Compliances-Certificate under Reg. 74 (5) of SEBI (DP) Regulations, 2018                        | 2023-01-15T22:59:36.63  | 2023-01-15T22:59:36.63  |              0 | A                   | None         | N            | 4579b99a-507a-40a7-b28f-7f3e56f7ce3f.pdf | This is to certify that the details of securities dematerialized/rematerialized during the quarter ended 31st December 2022, as required under Regulation 74(5) of SEBI (Depositories and Participants) Regulations, 2018, have been furnished to all the stock exchanges where the shares of the Company are listed. The letter confirming this from our RTA - Aarthi Consultants Private Limited is enclosed for your reference.<br>Further, the certificates of securities which were dematerialized, are listed on the Stock Exchanges<br>where earlier issued securities of the Company were listed.                                                                                                                                                                                                                                                                                                                                                                                                                        | This is to certify that the details of securities dematerialized/rematerialized during the quarter ended 31st December 2022, as required under Regulation 74(5) of SEBI (Depositories and Participants) Regulations, 2018, have been furnished to all the stock exchanges where the shares of the Company are listed. The letter confirming this from our RTA - Aarthi Consultants Private Limited is enclosed for your reference.<br>Further, the certificates of ....    | Company Update |     1 |    1 |         0 | https://www.bseindia.com/stock-share-price/covidh-technologies-limited/covidh/534920/   | COVIDH TECHNOLOGIES LIMITED |         212 |             97 | 2023-01-15T22:59:36  | 2023-01-15T22:59:36.63  | 00:00:00   | 503494           | https://www.bseindia.com/Msource/90D/CorpXbrlGen.aspx?Bsenewid=f81472c4-2181-47ce-a238-fc3f61b52110&Scripcode=534920 | https://www.bseindia.com/xml-data/corpfiling/AttachLive/4579b99a-507a-40a7-b28f-7f3e56f7ce3f.pdf |
|    1203 | 64b9f0db-1978-4038-9f48-c8c473a69a8b |     542383 | ANN_542383_64B9F0DB-1978-4038-9F48-C8C473A69A8B | Ritco Logistics Ltd - 542383 - Intimation Of Grant Of 72,500 More Stock Options Under 'PRAGATI KI AUR' Employee Stock Option Plan 2022 | 2023-01-12T22:51:37.047 | 2023-01-12T22:51:37.047 |              0 | A                   | None         | N            | d3e8f813-56d4-46dd-a2e6-53cac2da5951.pdf | Pursuant to SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015, we wish to inform you that Nomination and Remuneration Committee of the Company at their meeting held on 11th January, 2023 has approved the grant of 72,500 (Seventy Two Thousand and Five Hundred only) Stock Options (each option exercisable into one equity share) in addition to 3,40,500 Stock Options already granted under 'PRAGATI KI AUR' Employee Stock Option Plan 2022.<br>The outstanding as on date total up to 4,13,000 Stock Options.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Pursuant to SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015, we wish to inform you that Nomination and Remuneration Committee of the Company at their meeting held on 11th January, 2023 has approved the grant of 72,500 (Seventy Two Thousand and Five Hundred only) Stock Options (each option exercisable into one equity share) in addition to 3,40,500 Stock Options already granted under 'PRAGATI KI AUR' Employee Stock Option Plan .... | Company Update |     1 |    1 |         1 | https://www.bseindia.com/stock-share-price/ritco-logistics-ltd/ritco/542383/            | Ritco Logistics Ltd         |           1 |             97 | 2023-01-12T22:51:36  | 2023-01-12T22:51:37.047 | 00:00:01   | 180688           | https://www.bseindia.com/Msource/90D/CorpXbrlGen.aspx?Bsenewid=64b9f0db-1978-4038-9f48-c8c473a69a8b&Scripcode=542383 | https://www.bseindia.com/xml-data/corpfiling/AttachLive/d3e8f813-56d4-46dd-a2e6-53cac2da5951.pdf |
|    2403 | 2c593191-f244-42cb-bb53-dc598acd647f |     543443 | ANN_543443_2C593191-F244-42CB-BB53-DC598ACD647F | Ascensive Educare Ltd - 543443 - Announcement under Regulation 30 (LODR)-Preferential Issue                                            | 2023-01-11T16:22:16.39  | 2023-01-11T16:22:16.39  |              0 | A                   | None         | N            | 5b0b9251-c71a-4471-9429-0e7ca11dc156.pdf |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Board of Directors of the Company in their meeting held today i.e. Wednesday, 11th January, 2023 which commenced at 01.00 PM and concluded at 04.00 PM have, inter alia considered and approved the agendas mentioned in the outcome attached herewith.                                                                                                                                                                                                                    | Company Update |     1 |    1 |         1 | https://www.bseindia.com/stock-share-price/ascensive-educare-ltd/ascensive/543443/      | Ascensive Educare Ltd       |         140 |             97 | 2023-01-11T16:22:16  | 2023-01-11T16:22:16.39  | 00:00:00   | 875339           | https://www.bseindia.com/Msource/90D/CorpXbrlGen.aspx?Bsenewid=2c593191-f244-42cb-bb53-dc598acd647f&Scripcode=543443 | https://www.bseindia.com/xml-data/corpfiling/AttachLive/5b0b9251-c71a-4471-9429-0e7ca11dc156.pdf |
|    3603 | 111f83be-bdeb-411c-afe4-14c1cc4f49c4 |     539659 | ANN_539659_111F83BE-BDEB-411C-AFE4-14C1CC4F49C4 | Vidli Restaurants Ltd - 539659 - Board Meeting Outcome for Outcome Of The Meeting Of The Board Of Directors.                           | 2023-01-10T12:11:12.027 | 2023-01-10T12:11:12.027 |              0 | A                   | None         | N            | b9e1b95b-ff7d-4818-a73d-3b9b287d0f83.pdf | The Board of Directors of the Company has, at its meeting held today, inter alia:<br>i. considered and approved the appointment of Ms. Bhakti Khanna as Company Secretary and Compliance Officer of the Company with effect from 10th January, 2023.<br>ii. considered and approved the appointment of Mr. Ravindra Shinde as Chief Financial Officer of the Company with effect from 10th January, 2023.<br>iii. authorized Ms. Bhakti Khanna, Secretary of the Company (Phone: 74000 58768; Email: cs@kamatsindia.com) and Mr. Ravindra Shinde, Chief Financial Officer (Phone: 74000 18878; Email: cfo@kamatsindia.com) of the Company for the purpose of determining materiality of an event or information for the purpose of making disclosures of same to stock exchange, in addition to Dr. Vidhi V. Kamat, Managing Director of the Company.<br>A brief profile of Ms. Bhakti Khanna and Mr. Ravindra Shinde is enclosed.<br>The Meeting of the Board of Directors commenced at 11.15 a.m. and concluded at 12.00 noon. | The Board of Directors of the Company has, at its meeting held today, inter alia:<br>i. considered and approved the appointment of Ms. Bhakti Khanna as Company Secretary and Compliance Officer of the Company with effect from 10th January, 2023.<br>ii. considered and approved the appointment of Mr. Ravindra Shinde as Chief Financial Officer of the Company with effect from 10th January, 2023.<br>iii. authorized Ms. Bhakti Khanna, Secretary of the ....      | None           |     1 |    1 |         1 | https://www.bseindia.com/stock-share-price/vidli-restaurants-ltd/vidli/539659/          | Vidli Restaurants Ltd       |         223 |             97 | 2023-01-10T12:11:10  | 2023-01-10T12:11:12.027 | 00:00:02   | 486788           | https://www.bseindia.com/Msource/90D/CorpXbrlGen.aspx?Bsenewid=111f83be-bdeb-411c-afe4-14c1cc4f49c4&Scripcode=539659 | https://www.bseindia.com/xml-data/corpfiling/AttachLive/b9e1b95b-ff7d-4818-a73d-3b9b287d0f83.pdf |
|    4803 | b28063fe-e3eb-41fa-adc4-20d4c0019812 |     542650 | ANN_542650_B28063FE-E3EB-41FA-ADC4-20D4C0019812 | Metropolis Healthcare Ltd - 542650 - Announcement under Regulation 30 (LODR)-Allotment of ESOP / ESPS                                  | 2023-01-08T00:38:03.643 | 2023-01-08T00:38:03.643 |              0 | A                   | None         | N            | d2556f4c-ba4a-4903-b6dd-232b5cd4f068.pdf | The Nomination and Remuneration Committee of the Board of the Directors of the Company vide circular resolution dated January 07, 2023 have approved the allotment of 4,372 (Four Thousand Three Hundred and Seventy-Two) Equity shares of Rs.2/- (Rupees Two Only) each at an exercise price of Rs. 2/- (Rupees Two Only) each aggregating to Rs. 8,744 (Rupees Eight Thousand Seven Hundred and Forty-Four Only) against the Restrictive Stock Units ('RSU') vested in and exercised by the employees of the Company under the MHL- Restrictive Stock Unit Plan, 2020.                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The Nomination and Remuneration Committee of the Board of the Directors of the Company vide circular resolution dated January 07, 2023 have approved the allotment of 4,372 (Four Thousand Three Hundred and Seventy-Two) Equity shares of Rs.2/- (Rupees Two Only) each at an exercise price of Rs. 2/- (Rupees Two Only) each aggregating to Rs. 8,744 (Rupees Eight Thousand Seven Hundred and Forty-Four Only) against the Restrictive Stock Units ('RSU') vested .... | Company Update |     1 |    1 |         1 | https://www.bseindia.com/stock-share-price/metropolis-healthcare-ltd/metropolis/542650/ | Metropolis Healthcare Ltd   |         115 |             97 | 2023-01-08T00:38:03  | 2023-01-08T00:38:03.643 | 00:00:00   | 768882           | https://www.bseindia.com/Msource/90D/CorpXbrlGen.aspx?Bsenewid=b28063fe-e3eb-41fa-adc4-20d4c0019812&Scripcode=542650 | https://www.bseindia.com/xml-data/corpfiling/AttachLive/d2556f4c-ba4a-4903-b6dd-232b5cd4f068.pdf |


---

### EDIT:

It seems that they have increased the security or something so you might have to add more headers - something like:

```py
headers = {
    'authority': 'api.bseindia.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,ms;q=0.8,ar;q=0.7',
    'origin': 'https://www.bseindia.com',
    'referer': 'https://www.bseindia.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}
```



  [1]: https://i.sstatic.net/dLUAq.png
  [2]: https://i.sstatic.net/KJDD1.png
  [3]: https://i.sstatic.net/7O4Kc.png
  [4]: https://i.sstatic.net/FCQGB.png
  [5]: https://i.sstatic.net/rAQt2.png
  [6]: https://i.sstatic.net/xIs3t.png
  [7]: https://i.sstatic.net/Uy1IB.png
  [8]: https://i.sstatic.net/jGN78.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Soham Jain](https://stackoverflow.com/users/8924786)** (2024-02-18): Tried Running this. But the apiUrl = f'https://api.bseindia.com/BseIndiaAPI/api/AnnGetData/w?{qStr}' gets redirected to https://www.bseindia.com/members/showinterest.aspx. Any workaround on this?
- **me** (2024-02-19): @SohamJain adding more headers *might* help. You could try the ones from the edit I've added at the bottom
