# Code from my Stack Overflow answer https://stackoverflow.com/a/75695241 (posted 2023-03-10), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
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

# --- block 3 ---
# date_employees = get_file_data(FILE_URL)
def list_newer(start_date, end_date=datetime.datetime.today(), data=date_employees):
    newer_dates = sorted([d for d in date_employees if start_date<=d<end_date]) # filter+sort
    for d in newer_dates: 
        print(f"Started on {d.strftime('%b %d, %Y')}: {data[d]}")

# --- block 4 ---
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

# --- block 5 ---
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

# --- block 6 ---
def list_newer(start_date, end_date=datetime.datetime.today(), data=date_employees):
    for sdate, employees in data[bisect_byDate(start_date):]: 
        if not sdate < end_date: break
        print(f"Started on {sdate.strftime('%b %d, %Y')}: {employees}")
