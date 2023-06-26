---
title: "how to web scrape a multipage from internet"
site: stackoverflow
question_id: 76558962
answer_id: 76559505
url: https://stackoverflow.com/a/76559505
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-26T18:58:09Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76559505/revisions
accepted: false
score: 1
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-hidden-api-json
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 17d963cc11d7e4ca17dddb1cd8f6082c7419fbf71dc89aaee43c5f411672ced5
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76559505>, 2023-06-26; score 1. Text as retrieved 2026-10-12.

Using [selenium](https://medium.com/ymedialabs-innovation/2f8ad15efe25) and then  [`pandas.read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html) would probably be easiest. `read_html` won't be enough by itself and replicating the POST request (with [`requests`](https://pypi.org/project/requests/)) for generating the next page looks rather complicated.

[![network tab][1]][1]

from copying that to [https://curlconverter.com/](https://curlconverter.com/):

```py
import requests
import pandas as pd

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,ms;q=0.8,ar;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.quantalys.com',
    'Referer': 'https://www.quantalys.com/Recherche?Values.lstIdProduits=1&Values.bExcludeUncommercialized=true&Values.bETF=true&start=300',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'draw': '3',
    'columns[0][name]': 'ID_Produit',
    'columns[1][name]': 'cTypeFinancialItem',
    'columns[2][name]': 'cClasseFinancialItem',
    'columns[3][name]': 'sTypeFinancialObject',
    'columns[4][name]': 'checkbox',
    'columns[5][name]': 'sNom',
    'columns[6][name]': 'sURL',
    'columns[7][name]': 'sNomManager',
    'columns[8][name]': 'sNomTypeFinancialObject',
    'columns[9][name]': 'sGroupeCat_Specific_Dynamic',
    'columns[10][name]': 'sGroupeCat_rng1',
    'columns[11][name]': 'sCodeISIN',
    'columns[12][name]': 'nVL',
    'columns[13][name]': 'sCurrency',
    'columns[14][name]': 'nStarRating',
    'columns[15][name]': 'nScore',
    'columns[16][name]': 'nRetYTD',
    'columns[17][name]': 'nRet1a',
    'columns[18][name]': 'nRet3a',
    'columns[19][name]': 'nRet5a',
    'columns[20][name]': 'nRet1c',
    'columns[21][name]': 'nRet3c',
    'columns[22][name]': 'nRet1j',
    'columns[23][name]': 'nRet1m',
    'columns[24][name]': 'nRet3m',
    'columns[25][name]': 'nRet6m',
    'columns[26][name]': 'nRet5c',
    'columns[27][name]': 'nRet8c',
    'columns[28][name]': 'nVolat1a',
    'columns[29][name]': 'nVolat3a',
    'columns[30][name]': 'nVolat5a',
    'columns[31][name]': 'nSharpe1a',
    'columns[32][name]': 'nSharpe3a',
    'columns[33][name]': 'nSharpe5a',
    'columns[34][name]': 'nPerteMax1a',
    'columns[35][name]': 'nPerteMax3a',
    'columns[36][name]': 'nPerteMax5a',
    'columns[37][name]': 'nSortino1a',
    'columns[38][name]': 'nSortino3a',
    'columns[39][name]': 'nSortino5a',
    'columns[40][name]': 'nIr1A',
    'columns[41][name]': 'nIr3A',
    'columns[42][name]': 'nIr5A',
    'columns[43][name]': 'nMinInvest',
    'columns[44][name]': 'nFraisGestion',
    'columns[45][name]': 'nFraisEntree',
    'columns[46][name]': 'nFraisSortie',
    'columns[47][name]': 'dtRet',
    'columns[48][name]': 'dtRetMonth',
    'columns[49][name]': 'bFerme',
    'columns[50][name]': 'nIntensiteESG',
    'columns[51][name]': 'nActifEur',
    'columns[52][name]': 'nActifDiffEUR1m',
    'columns[53][name]': 'nActifDiffEUR3m',
    'columns[54][name]': 'nActifDiffEUR6m',
    'columns[55][name]': 'nActifDiffEUR1A',
    'columns[56][name]': 'nActifCompartimentEUR',
    'columns[57][name]': 'nActifCompartimentDiffEUR1m',
    'columns[58][name]': 'nActifCompartimentDiffEUR3m',
    'columns[59][name]': 'nActifCompartimentDiffEUR6m',
    'columns[60][name]': 'nActifCompartimentDiffEUR1A',
    'columns[61][name]': 'nCollecteCompartiment1m',
    'columns[62][name]': 'nCollecteCompartiment3m',
    'columns[63][name]': 'nCollecteCompartiment6m',
    'columns[64][name]': 'nCollecteCompartimentYTD',
    'columns[65][name]': 'nCollecteCompartiment1A',
    'columns[66][name]': 'nCollecteCompartiment3A',
    'columns[67][name]': 'nCollecteRet1m',
    'columns[68][name]': 'nCollecteRet3m',
    'columns[69][name]': 'nCollecteRet6m',
    'columns[70][name]': 'nCollecteRetYTD',
    'columns[71][name]': 'nCollecteRet1A',
    'columns[72][name]': 'nCollecteRet3A',
    'columns[73][name]': 'nCollecteCompartimentRet1m',
    'columns[74][name]': 'nCollecteCompartimentRet3m',
    'columns[75][name]': 'nCollecteCompartimentRet6m',
    'columns[76][name]': 'nCollecteCompartimentRetYTD',
    'columns[77][name]': 'nCollecteCompartimentRet1A',
    'columns[78][name]': 'nCollecteCompartimentRet3A',
    'columns[79][name]': 'isESG',
    'columns[80][name]': 'sArticleSFDR',
    'columns[81][name]': 'nIntensiteISR',
    'columns[82][name]': 'nESG_Environnement',
    'columns[83][name]': 'nESG_Social',
    'columns[84][name]': 'nESG_Gouvernance',
    'columns[85][name]': 'nNbLabels',
    'columns[86][name]': 'sProspectusUrl',
    'columns[87][name]': 'sUrlMainDocument',
    'columns[88][name]': 'isMainDocumentAccessible',
    'order[0][column]': '5',
    'order[0][dir]': 'asc',
    'start': '10',
    'length': '10',
    'search[value]': '',
    'search[regex]': 'false',
    'nbMaxCompare': '5',
    'Values.sNomOrISIN': '',
    'chkTypeProduits': '1',
    'Values.bETF': 'true',
    'Values.isTypeProduitV2': 'true',
    'Values.sDevise': '',
    'Values.nAge': '',
    'Values.sDomicile': '',
    'Values.nTypeFonds': '',
    'Values.nTypeInvestisseur': '',
    'Values.nDistribution': '',
    'Values.nAMF': '',
    'Values.bExcludeUncommercialized': 'true',
    'Values.perfAnnu.dateIndex': '0',
    'Values.perfAnnu.signe': 'ge',
    'Values.perfAnnu.value': '',
    'Values.perfCumulee.sDate': '0',
    'Values.perfCumulee.signe': 'ge',
    'Values.perfCumulee.value': '',
    'Values.superfAnnu.dateIndex': '0',
    'Values.superfAnnu.signe': 'le',
    'Values.superfAnnu.value': '',
    'Values.sharpe.dateIndex': '0',
    'Values.sharpe.signe': 'ge',
    'Values.sharpe.value': '',
    'Values.volat.dateIndex': '0',
    'Values.volat.signe': 'le',
    'Values.volat.value': '',
    'Values.perteMax.dateIndex': '0',
    'Values.perteMax.signe': 'le',
    'Values.perteMax.value': '',
    'Values.beta.dateIndex': '0',
    'Values.beta.signe': 'le',
    'Values.beta.value': '',
    'Values.ecartSuivi.dateIndex': '0',
    'Values.ecartSuivi.signe': 'le',
    'Values.ecartSuivi.value': '',
    'Values.IR.dateIndex': '0',
    'Values.IR.signe': 'le',
    'Values.IR.value': '',
    'Values.sortino.dateIndex': '0',
    'Values.sortino.signe': 'le',
    'Values.sortino.value': '',
    'Values.ratioOmega.dateIndex': '0',
    'Values.ratioOmega.signe': 'le',
    'Values.ratioOmega.value': '',
    'Values.betaHaussier.dateIndex': '0',
    'Values.betaHaussier.signe': 'le',
    'Values.betaHaussier.value': '',
    'Values.betaBaissier.dateIndex': '0',
    'Values.betaBaissier.signe': 'le',
    'Values.betaBaissier.value': '',
    'Values.upCaptureRatio.dateIndex': '0',
    'Values.upCaptureRatio.signe': 'le',
    'Values.upCaptureRatio.value': '',
    'Values.downCaptureRatio.dateIndex': '0',
    'Values.downCaptureRatio.signe': 'le',
    'Values.downCaptureRatio.value': '',
    'Values.DSR.dateIndex': '0',
    'Values.DSR.signe': 'le',
    'Values.DSR.value': '',
    'Values.var95.dateIndex': '0',
    'Values.var95.signe': 'le',
    'Values.var95.value': '',
    'Values.var99.dateIndex': '0',
    'Values.var99.signe': 'le',
    'Values.var99.value': '',
    'Values.skewness.dateIndex': '0',
    'Values.skewness.signe': 'le',
    'Values.skewness.value': '',
    'Values.kurtosis.dateIndex': '0',
    'Values.kurtosis.signe': 'le',
    'Values.kurtosis.value': '',
    'Values.fraisSouscription.Signe': 'le',
    'Values.fraisSouscription.Value': '',
    'Values.fraisRachat.Signe': 'le',
    'Values.fraisRachat.Value': '',
    'Values.fraisGestion.Signe': 'le',
    'Values.fraisGestion.Value': '',
    'Values.fraisCourants.Signe': 'le',
    'Values.fraisCourants.Value': '',
    'Values.ESG.isEnvironnement': '',
    'Values.ESG.isSocial': '',
    'Values.ESG.isGouvernance': '',
    'Values.isIntersectionContrats': 'false',
    'Values.lstIdProduits[]': '1',
    'lstIdProduits[]': '1',
    'sNomOrISIN': '',
    'Values.isForProposition': 'false',
}

response = requests.post('https://www.quantalys.com/Recherche/Data', headers=headers, data=data)

df_pg2 = pd.DataFrame(response.json()['data'])
```

[![opdf][2]][2]
[![opdf2][3]][3]

You can change the page number by setting `data['start']` - 0 for page 1, 10 for page 2, 20 for page 3, and so on.... So, you can loop through the different pages [until `response.json()['data']` is empty, meaning there are no more pages] and collect a list of DataFrames that you can then [`concat`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html) together into one DataFrame.


  [1]: https://i.sstatic.net/QDqhu.png
  [2]: https://i.sstatic.net/Jlxgk.png
  [3]: https://i.sstatic.net/1g2MW.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[jacques](https://stackoverflow.com/users/22134741)** (2023-06-26): where is data['start'] ? I can not find it in your code.
- **me** (2023-06-26): Before the command `response = requests.post('https://www.quantalys.com/Recherche/Data', headers=headers, data=data)`, the `data` dictionary is defined, and in that dictionary there's a `'start'` key, paired to value `'10'` (for page 2) in this case
- **[jacques](https://stackoverflow.com/users/22134741)** (2023-06-27): what is  https://curlconverter.com/ ??? I do not know this site. What is his purpose ?
- **me** (2023-06-30): It helps you turn requests from your [network logs](https://support.happyfox.com/kb/article/882-accessing-the-browser-console-and-network-logs/) into code so you can replicate how your browser loads certain data
