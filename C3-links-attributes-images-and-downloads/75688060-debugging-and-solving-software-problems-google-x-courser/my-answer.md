---
title: "Debugging and Solving Software Problems - Google X Coursera course week 4 qwiklabs"
site: stackoverflow
question_id: 75688060
answer_id: 75695241
url: https://stackoverflow.com/a/75695241
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-10T10:56:33Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75695241/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 08242e3e32aebd0f5a284628099131628c282879fcbbff03f11f95b18079c031
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75695241>, 2023-03-10; score 0. Text as retrieved 2026-10-12.

> - *Download the file only once from the URL.* 
> - *Pre-process it so that the same calculation doesn't need to be done over and over again.*

You can either set an extra parameter `data` to `list_newer` and `get_same_or_newer` and pass the processed data every call, or you could just make `data` a global variable that can be used from any function. [**Just make sure to define it before calling any functions that use it.**]

---

> *1. To create a dictionary with the start dates and then use the data in the dictionary instead of the complicated calculation.*

This *will* reduce the search time by a lot, but only if the exact `start_date` exists in `data`, otherwise it can take just as much time as it does currently to find the next `min_date`.

```py
# FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_file_data(url):
    """Downloads, processes and returns data contained in the file at the given URL""" 

    # Download the file over the internet
    response = requests.get(url, stream=True)
    decoded_lines = [line.decode("UTF-8") for line in response.iter_lines()]

    rows = list(csv.reader(decoded_lines[1:]))
    dates = {row[3] for row in rows} ## unique dates
    getNames = lambda sdate: [f'{r[0]} {r[1]}' for r in rows if r[3]==sdate]
    return {datetime.datetime.strptime(d, '%Y-%m-%d'): getNames(d) for d in dates}
```

Now, you can rewrite `get_same_or_newer` and use it as before

```py
date_employees = get_file_data(FILE_URL)
def get_same_or_newer(start_date, data=date_employees):
    """Returns the employees that started on the given date, or the closest one."""

    ## try to access as dictionary key to immediately find exact date
    min_date, min_date_employees = start_date, data.get(start_date)

    ## no exact match ---> search for next oldest date
    if min_date_employees is None:
        newer_dates = [d for d in data if d>start_date] ## filter
        if newer_dates: 
            min_date = min(newer_dates)
            min_date_employees = data[min_date]
        else: min_date, min_date_employees = datetime.datetime.today(), []
    return min_date, min_date_employees
```

But you could also bypass it entirely in `list_newer`

```py
# date_employees = get_file_data(FILE_URL)
def list_newer(start_date, end_date=datetime.datetime.today(), data=date_employees):
    newer_dates = sorted([d for d in date_employees if start_date<=d<end_date]) # filter+sort
    for d in newer_dates: 
        print(f"Started on {d.strftime('%b %d, %Y')}: {data[d]}")
```

---

> 2. To sort the data by `start_date` and then go date by date.

This can make searching even faster [though there isn't a special advantage for exact matches like with a dictionary], because you can use [binary search](https://www.programiz.com/dsa/binary-search) on sorted data.

```py
def get_file_data(url):
    """Downloads, processes and returns data contained in the file at the given URL""" 

    # Download the file over the internet
    response = requests.get(url, stream=True)
    decoded_lines = [line.decode("UTF-8") for line in response.iter_lines()]

    rows = list(csv.reader(decoded_lines[1:]))
    return [(
        datetime.datetime.strptime(d, '%Y-%m-%d'), 
        [f'{fname} {lname}' for fname,lname,dept,sdate in rows if sdate==d]
    ) for d in sorted({row[3] for row in rows})] # sort set --> build sorted list
```

<sup>I think sets get automatically sorted, but I used the `sorted` function as well just in case.</sup>

The binary search logic is contained in the `bisect_byDate` function, which can reduce `get_same_or_newer` to a single statement. <sup>*(`data[bisect_byDate(start_date)] if start_date < data[-1][0] else....today(), []`*)</sup>

```py
date_employees = get_file_data(FILE_URL)
def bisect_byDate(start_date, data=date_employees):
    '''Find index of date (or next closest) with binary search'''
    lo, hi = 0, len(data)
    while lo < hi: 
        mid = (lo + hi) // 2
        if data[mid][0] < start_date: 
            lo = mid + 1 
        else: hi = mid
    while data[lo-1][0] >= start_date: lo -= 1
    return lo
    
def get_same_or_newer(start_date, data=date_employees):
    """Returns the employees that started on the given date, or the closest one."""

    ## first, check that the latest date isn't before start_date
    if data[-1][0] < start_date: return datetime.datetime.today(), [] 

    return data[bisect_byDate(start_date)]
```

And again, you could bypass `get_same_or_newer` entirely in `list_newer`:

```py
def list_newer(start_date, end_date=datetime.datetime.today(), data=date_employees):
    for sdate, employees in data[bisect_byDate(start_date):]: 
        if not sdate < end_date: break
        print(f"Started on {sdate.strftime('%b %d, %Y')}: {employees}")
```

---

You could combine the advantages of both methods by having the dictionary as well as a sorted list of dates. Then, you could use the dictionary to check for exact matches before using binary search on the sorted dates to find the closest key.
