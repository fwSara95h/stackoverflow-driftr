---
title: "Why am I getting a python RecursionError"
site: stackoverflow
question_id: 74978098
url: https://stackoverflow.com/q/74978098
asked: 2023-01-01T23:52:21Z
asked_by: "Carter James"
asked_by_url: https://stackoverflow.com/users/20487614
last_edited: 2023-01-02T00:10:37Z
tags: [python, python-3.x, web-scraping, recursion, iteration]
score: -2
views_at_snapshot: 963
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b1eea8f4a87a6714fafd0b9d078bdfc5780187bb1e876fe28b39bfe16cc88120
---

# Why am I getting a python RecursionError

Asked by [Carter James](https://stackoverflow.com/users/20487614) on Stack Overflow, <https://stackoverflow.com/q/74978098>, 2023-01-01, last edited 2023-01-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am creating a web scraper to go over almost 400k records. Basically, it works like this, I have a CSV of part numbers that need to be searched on this site. The site has an exposed API so I am able to skip the frontend and make a direct request to the site after logging in. I created one function called GetPdcResults() which takes in a list of parts and a start number. The start argument is for if the scraper stops for any reason I can start it back up at the same point it left off on the parts list. Then the main loop of the scraper which enumerates over each part in the list builds a payload for that part and requests the information. Some error handling for if I have a network error or a cookie error which only happens when my user's session has expired. Then it calls the CleanPdcResults() function. This cleans the response returned from the site and saves the relevant information to a CSV for exporting. 

To my understanding recursion is when a function calls itself repeatedly and there is a limit to this in python and is more resource intensive. Iteration is when you use a loop to repeat a set of actions.

I think I want iteration in my app, not recursion because currently I a, getting this error I have never seen before. 
```
RecursionError: maximum recursion depth exceeded while calling a Python object
```
I'm assuming because there is recursion happening in my functions instead of iteration but I can't seem to point it out. The only time a function is calling itself is when there is a cookie error and the GetPdcResults() function is called again but that wouldn't be called so many times that a Limit is reached.

Can someone help me find where recursion is happening in my scrapper and how I can convert it to iteration to stop this error?? Any help is appreciated!

```
def GetPdcResults(parts, start=0):
    logger = PartsLogger()
    logger.log_cookie(headers['cookie'])
    logger.log_num_parts(parts)
    
    for (i, part) in tqdm(enumerate(parts[start:], start), total=len(parts[start:])):
        if part == nan:
            break
        logger.log_cur_part(i, part)
        payload = "{\"catalogId\":\"2\",\"locatorService\":\"Panda\""
        payload += f',"partNumber":"{part}", "cacheKey":"{part}_2_en-US_7497fea0-4fb6-4b28-b0e8-62e3e4204cc5"{"}"}'
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except requests.exceptions.RequestException as e:
            print('\n[-] Request Error')
            print(e)
            logger.log_error(str(e), part=part)
        if response.status_code == 401:
            logger.log_error('[-] Cookie Error', part=part)
            print('\n[-] Cookie Error')
            GetPdcResults(parts, start=i)
            break
        CleanPdcResults(response.json(), i, part, logger)

def CleanPdcResults(resp, index, part, logger):
    try:
        pdc_results = resp['d']['PdcResults']
        pdc92 = {} 
        for pdc in pdc_results:
            if '92' in pdc['LocationName']:
                pdc92.update(pdc)
                break
        if(bool(pdc92)):
            foundPart = [{'':index, 'Part':part, 'Qty':pdc92['Quantity']}]
            df = pd.DataFrame(foundPart)
            if not exists('Parts.csv'):
                df.to_csv('Parts.csv', index=False)            
            df.to_csv('Parts.csv', mode='a', index=False, header=False)
        else:
            print('\n[-] Part Not Found')
    except Exception as e:
        logger.log_error(str(e), part=part, response=resp)    
```

```
Traceback (most recent call last):
  File "c:\Users\carte\OneDrive\Documents\GrayTeck\Chad S\CleanPartsCSV.py", line 30, in run
    GetPdcResults(partsList, start=startIndex)
  File "c:\Users\carte\OneDrive\Documents\GrayTeck\Chad S\GetPDCRes.py", line 57, in GetPdcResults
    GetPdcResults(parts, start=i)
  File "c:\Users\carte\OneDrive\Documents\GrayTeck\Chad S\GetPDCRes.py", line 57, in GetPdcResults
    GetPdcResults(parts, start=i)
  File "c:\Users\carte\OneDrive\Documents\GrayTeck\Chad S\GetPDCRes.py", line 57, in GetPdcResults
    GetPdcResults(parts, start=i)
  [Previous line repeated 973 more times]
  File "c:\Users\carte\OneDrive\Documents\GrayTeck\Chad S\GetPDCRes.py", line 48, in GetPdcResults
    response = requests.request("POST", url, headers=headers, data=payload)
  File "C:\Python310\lib\site-packages\requests\api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Python310\lib\site-packages\requests\sessions.py", line 529, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Python310\lib\site-packages\requests\sessions.py", line 645, in send
    r = adapter.send(request, **kwargs)
  File "C:\Python310\lib\site-packages\requests\adapters.py", line 440, in send
    resp = conn.urlopen(
  File "C:\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Python310\lib\site-packages\urllib3\connectionpool.py", line 449, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "C:\Python310\lib\site-packages\urllib3\connectionpool.py", line 444, in _make_request
    httplib_response = conn.getresponse()
  File "C:\Python310\lib\http\client.py", line 1374, in getresponse
    response.begin()
  File "C:\Python310\lib\http\client.py", line 337, in begin
    self.headers = self.msg = parse_headers(self.fp)
  File "C:\Python310\lib\http\client.py", line 236, in parse_headers
    return email.parser.Parser(_class=_class).parsestr(hstring)
  File "C:\Python310\lib\email\parser.py", line 67, in parsestr
    return self.parse(StringIO(text), headersonly=headersonly)
  File "C:\Python310\lib\email\parser.py", line 56, in parse
    feedparser.feed(data)
  File "C:\Python310\lib\email\feedparser.py", line 176, in feed
    self._call_parse()
  File "C:\Python310\lib\email\feedparser.py", line 180, in _call_parse
    self._parse()
  File "C:\Python310\lib\email\feedparser.py", line 295, in _parsegen
    if self._cur.get_content_maintype() == 'message':
  File "C:\Python310\lib\email\message.py", line 594, in get_content_maintype
    ctype = self.get_content_type()
  File "C:\Python310\lib\email\message.py", line 578, in get_content_type
    value = self.get('content-type', missing)
  File "C:\Python310\lib\email\message.py", line 471, in get
    return self.policy.header_fetch_parse(k, v)
  File "C:\Python310\lib\email\_policybase.py", line 316, in header_fetch_parse
    return self._sanitize_header(name, value)
  File "C:\Python310\lib\email\_policybase.py", line 287, in _sanitize_header
    if _has_surrogates(value):
  File "C:\Python310\lib\email\utils.py", line 57, in _has_surrogates
    s.encode()
RecursionError: maximum recursion depth exceeded while calling a Python object
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-01-01): You're making us guess where the error is.  Please edit the question and add the whole error traceback message.
- **[Scott Hunter](https://stackoverflow.com/users/535275)** (2023-01-01): What evidence do you have that the recursion isn't going too deep?
- **[Tim Roberts](https://stackoverflow.com/users/1883316)** (2023-01-02): 401 is "unauthorized".  It's not a cookie error.  And if you get that error on item #0, then `i` will still be 0 when you call `GetPdcResults` again, so you'll make the exact same call  again and again and again and again.
- **[John Coleman](https://stackoverflow.com/users/4996248)** (2023-01-02): `401` is an authentication error. Apparently you are trying to scrape from a site for which you lack credentials (or aren't providing the credentials in the right way). If `GetPdcResults` fails because of an authentication problem, how is calling it again supposed to fix that problem? The full traceback shows that you had run into the `401` error 977 times before crashing.
- **[Carter James](https://stackoverflow.com/users/20487614)** (2023-01-02): @JohnColeman Ok I see I missed something in the traceback it was calling the GetPdcResutls() too many times see my update
- **[John Coleman](https://stackoverflow.com/users/4996248)** (2023-01-02): Probably the best solution is to find a way to make your requests properly authenticated. You have to do something to address the 401 problem. I don't have experience with this (the only web-scraping I have done is with public bioinformatics sites). Perhaps [this question](https://stackoverflow.com/q/26745462/4996248) will help.
