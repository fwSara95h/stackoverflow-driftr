---
title: "Beautiful Soup Parsing from a HTML Website"
site: stackoverflow
question_id: 73954775
answer_id: 74138200
url: https://stackoverflow.com/a/74138200
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-20T10:16:12Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74138200/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 79e189996f0cb1e5a33e98a0534ecf4fc82ced632449046e784319dbb194ee14
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-20

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74138200>, 2022-10-20; **accepted**; score 0. Text as retrieved 2026-10-12.

It's been a while, so maybe you've already solved some or all of the issues, but in case you haven't, I can suggest some solutions. 

(First, I saved the DataFrame as **ggDf** with `ggDf = get_gas(soup)`, so it's easier to refer to and I don't have to call `get_gas` again and again.)

<hr>

> Question: Not sure why the code splits this into different columns. GAS.2 \ this splits the data for GAS.3 onto a entirely different line.

It's a thing that pandas does - by default it will [split the table](https://stackoverflow.com/questions/66064899/how-to-stop-a-pandas-dataframe-splitting-columns-onto-separate-lines) if it's wider that 80chars; you can adjust this maximum with 
```python
pd.set_option('display.width', 1000000)

print(ggDf)
```
and now you should be able to see the table without it splitting. (Just 100 would probably enough for this table, btw.)

<hr>

> the first 3 rows need to be removed, GAS & Simple Cycle & ASSET is not information I need to display.

> ie afc = {'AB Newsprint (ANC1)': {'MC':63,'TNG': 65}, 'Bantry (ALP1)': {'MC': 7,'TNG': 6}}
>
> For the entire list of td scraped from the GAS table, into dictionary above.

Before forming the dictionary, you'd need to clean up the table a bit with
```python
# get rid of GAS-GAS.1-GAS.2-GAS.3 headers row
ggDf2 = ggDf.rename(columns=dict(
    zip(list(ggDf.columns), list(ggDf.loc[1]))))

# get rid of 0-1-2-3....n index column
ggDf2 = ggDf2.set_index('ASSET') 

# filter: only keep cells with numbers  
ggDf2 = ggDf2[ggDf2['MC'].str.isnumeric()]  
# [so Simple Cycle & ASSET lines will be gone] 
```
and at this point `ggDf2` will look like:

|ASSET|MC|TNG|DCR|
|---|---|---|---|
|AB Newsprint \(ANC1\)|63|0|0|
|Bantry \(ALP1\)|7|0|0|
|Bellshill \(BHL1\)|5|0|0|
|Carson Creek \(GEN5\)|15|12|0|
|Cloverbar \#1 \(ENC1\)|48|0|0|
|Cloverbar \#2 \(ENC2\)|101|0|0| 

I'm assuming you don't care to keep the GAS.3/DCR column since you only mention wanting MC and TNG; you can drop that column with
```python
ggDf2 = ggDf2.drop('DCR', axis=1)
```

<br>

Since the dataframe has been cleaned up, the dictionary can be formed directly with the [`to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html) function:
```python
ggDict = ggDf2.to_dict('index')
print(ggDict)
```
Output:
```python
{'AB Newsprint (ANC1)': {'MC': '63', 'TNG': '0'}, 'Bantry (ALP1)': {'MC': '7', 'TNG': '0'}, 'Bellshill (BHL1)': {'MC': '5', 'TNG': '0'}, 'Carson Creek (GEN5)': {'MC': '15', 'TNG': '12'}, 'Cloverbar #1 (ENC1)': {'MC': '48', 'TNG': '0'}, 'Cloverbar #2 (ENC2)': {'MC': '101', 'TNG': '0'}, 'Cloverbar #3 (ENC3)': {'MC': '101', 'TNG': '94'}, 'Crossfield Energy Centre #1 (CRS1)': {'MC': '48', 'TNG': '0'}, 'Crossfield Energy Centre #2 (CRS2)': {'MC': '48', 'TNG': '0'}, 'Crossfield Energy Centre #3 (CRS3)^': {'MC': '48', 'TNG': '0'}, 'Drywood (DRW1)': {'MC': '6', 'TNG': '0'}, 'H.R. Milner (HRM)': {'MC': '300', 'TNG': '0'}, 'Judy Creek (GEN6)': {'MC': '15', 'TNG': '13'}, 'Lethbridge Burdett (ME03)': {'MC': '7', 'TNG': '0'}, 'Lethbridge Coaldale (ME04)': {'MC': '6', 'TNG': '0'}, 'Lethbridge Taber (ME02)': {'MC': '8', 'TNG': '0'}, 'NPC2 JL Landry (NPC2)': {'MC': '9', 'TNG': '0'}, 'NPC3 Elmworth (NPC3)': {'MC': '9', 'TNG': '0'}, 'Northern Prairie Power Project (NPP1)': {'MC': '105', 'TNG': '70'}, 'Parkland (ALP2)': {'MC': '10', 'TNG': '0'}, 'Poplar Hill #1 (PH1)': {'MC': '48', 'TNG': '32'}, 'Rainbow #5 (RB5)': {'MC': '50', 'TNG': '0'}, 'Ralston (NAT1)': {'MC': '20', 'TNG': '0'}, 'South Edmonton Terminal (SET1)': {'MC': '20', 'TNG': '16'}, 'Valley View 1 (VVW1)': {'MC': '50', 'TNG': '0'}, 'Valley View 2 (VVW2)': {'MC': '50', 'TNG': '0'}, 'West Cadotte (WCD1)': {'MC': '20', 'TNG': '19'}, 'West Pembina (PMB1)*': {'MC': '13', 'TNG': '0'}, 'Air Liquide Scotford #1 (ALS1)': {'MC': '106', 'TNG': '56'}, 'AltaGas Harmattan (HMT1)': {'MC': '45', 'TNG': '24'}, 'Base Plant (SCR1)': {'MC': '50', 'TNG': '18'}, 'Bear Creek 1 (BCRK)': {'MC': '64', 'TNG': '57'}, 'Bear Creek 2 (BCR2)': {'MC': '36', 'TNG': '32'}, 'Blackfalds (BFD1)': {'MC': '6', 'TNG': '1'}, 'CNRL Horizon (CNR5)*': {'MC': '203', 'TNG': '181'}, 'COD1 Coaldale (COD1)': {'MC': '5', 'TNG': '5'}, 'Camrose (CRG1)*': {'MC': '10', 'TNG': '5'}, 'Caroline (SHCG)*': {'MC': '19', 'TNG': '0'}, 'Carseland Cogen (TC01)': {'MC': '95', 'TNG': '77'}, 'Christina Lake (CL01)': {'MC': '100', 'TNG': '53'}, 'Dow Hydrocarbon (DOWG)': {'MC': '326', 'TNG': '183'}, 'Edson (TLM2)': {'MC': '13', 'TNG': '9'}, 'Empress (EPS1)*': {'MC': '46', 'TNG': '0'}, 'Firebag (SCR6)': {'MC': '497', 'TNG': '403'}, 'Fort Hills (FH1)': {'MC': '199', 'TNG': '169'}, 'Foster Creek (EC04)': {'MC': '98', 'TNG': '68'}, 'Heartland Petrochemical (HRT1)': {'MC': '108', 'TNG': '96'}, 'Joffre #1 (JOF1)': {'MC': '474', 'TNG': '137'}, 'Kearl (IOR3)': {'MC': '84', 'TNG': '66'}, 'Lindbergh (PEC1)*': {'MC': '16', 'TNG': '0'}, 'MEG1 Christina Lake (MEG1)': {'MC': '202', 'TNG': '150'}, 'MacKay River (MKRC)': {'MC': '207', 'TNG': '176'}, 'Mahkeses (IOR1)': {'MC': '180', 'TNG': '152'}, 'Mulligan (MUL1)*': {'MC': '5', 'TNG': '0'}, 'Muskeg River (MKR1)': {'MC': '202', 'TNG': '165'}, 'Nabiye (IOR2)*': {'MC': '195', 'TNG': '156'}, 'Nexen Inc #2 (NX02)': {'MC': '220', 'TNG': '167'}, 'Poplar Creek (SCR5)': {'MC': '376', 'TNG': '261'}, 'Primrose #1 (PR1)': {'MC': '100', 'TNG': '74'}, 'Rainbow Lake #1 (RL1)': {'MC': '47', 'TNG': '37'}, 'Redwater Cogen (TC02)': {'MC': '92', 'TNG': '76'}, 'Saddle Hills (SDH1)': {'MC': '10', 'TNG': '6'}, 'Scotford Upgrader (APS1)': {'MC': '195', 'TNG': '148'}, 'Strathcona (IOR4)*': {'MC': '43', 'TNG': '43'}, 'Syncrude #1 (SCL1)*': {'MC': '510', 'TNG': '333'}, 'U of C Generator (UOC1)*': {'MC': '12', 'TNG': '13'}, 'University of Alberta (UOA1)*': {'MC': '39', 'TNG': '32'}, 'Cavalier (EC01)': {'MC': '120', 'TNG': '84'}, 'ENMAX Calgary Energy Centre (CAL1)': {'MC': '330', 'TNG': '201'}, 'Fort Nelson (FNG1)': {'MC': '73', 'TNG': '0'}, 'Medicine Hat #1 (CMH1)': {'MC': '299', 'TNG': '129'}, 'Nexen Inc #1 (NX01)': {'MC': '120', 'TNG': '102'}, 'Shepard (EGC1)': {'MC': '868', 'TNG': '648'}, 'Battle River #4 (BR4)': {'MC': '155', 'TNG': '29'}, 'Battle River #5 (BR5)': {'MC': '395', 'TNG': '90'}, 'Keephills #2 (KH2)': {'MC': '395', 'TNG': '67'}, 'Keephills #3 (KH3)': {'MC': '463', 'TNG': '465'}, 'Sheerness #1 (SH1)': {'MC': '400', 'TNG': '123'}, 'Sheerness #2 (SH2)': {'MC': '400', 'TNG': '135'}, 'Sundance #6 (SD6)': {'MC': '401', 'TNG': '137'}}
```

<hr>

> What I'm looking for is how do I write this information into excel?

This can also be done directly, with the [`to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html) function
```python
ggDf2.to_excel('ggDf.xlsx', header=False)
```

Without the previous cleanup, the statement would have been longer:
```python
ggDf[ggDf['GAS.1'].str.isnumeric()].drop(
    'GAS.3', axis=1).to_excel('ggDf.xlsx', header=False, index=False)
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[laisp-lostlamb](https://stackoverflow.com/users/20162704)** (2022-10-20): Hi, thank you for looking into my post related to web scrapping, I'm new to this field. No I haven't resolved this, I tested what you have suggested.
- **me** (2022-10-20): @laisp-CAD did they work?
- **[laisp-lostlamb](https://stackoverflow.com/users/20162704)** (2022-10-20): Thank you! This did indeed work, you solutions are vaild. I did not ask in this thread, so I will ignore it for this answer, but would it possible to categorize, GAS table by type? ie. Simple Cycle, Cogeneration, Combined Cycle, Gas Fired Steam? I basically needed the other tables in a seperate tab in excel , ie SUMMARY, GENERATION, INTERCHANGE tabs for it's data, with DCR info. Other than summary tab which should only have 1 column. If you have solution...that would great, if not I will try to figure it out.
