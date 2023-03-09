---
title: "Debugging and Solving Software Problems - Google X Coursera course week 4 qwiklabs"
site: stackoverflow
question_id: 75688060
url: https://stackoverflow.com/q/75688060
asked: 2023-03-09T17:26:38Z
asked_by: "Jaidon Lee"
asked_by_url: https://stackoverflow.com/users/20084599
last_edited: 2023-03-09T17:58:47Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, dictionary, sorting, optimization]
score: 0
views_at_snapshot: 1996
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fe0dd4a73f4af16417f8eb73518322c7be8a1b130fe28c1bbceb90fb89297ccf
---

# Debugging and Solving Software Problems - Google X Coursera course week 4 qwiklabs

Asked by [Jaidon Lee](https://stackoverflow.com/users/20084599) on Stack Overflow, <https://stackoverflow.com/q/75688060>, 2023-03-09, last edited 2023-03-09 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

How do I optimise this script with the recommendations given in the instructions?

> This is a pretty challenging task that you have to complete by modifying the `get_same_or_newer()` function.
Here are few hints to fix this issue:
>
> * Download the file only once from the URL.
> * Pre-process it so that the same calculation doesn't need to be done over and over again. This can be done in two ways. You can choose any one of them:
> 
>   1. To create a dictionary with the start dates and then use the data in the dictionary instead of the complicated calculation.
>   2. To sort the data by `start_date` and then go date by date.

    
```PY
#!/usr/bin/env python3

import csv
import datetime
import requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def get_start_date():
    """Interactively get the start date to query for."""


    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()


    return datetime.datetime(year, month, day)


def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""


    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []


    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines


def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])


    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in reader: 
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')


        # If this date is smaller than the one we're looking for,
        # we skip this row
        if row_date < start_date:
            continue


        # If this date is smaller than the current minimum,
        # we pick it as the new minimum, resetting the list of
        # employees at the minimal date.
        if row_date < min_date:
            min_date = row_date
            min_date_employees = []


        # If this date is the same as the current minimum,
        # we add the employee in this row to the list of
        # employees at the minimal date.
        if row_date == min_date:
            min_date_employees.append("{} {}".format(row[0], row[1]))


    return min_date, min_date_employees


def list_newer(start_date):
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))


        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)


def main():
    start_date = get_start_date()
    list_newer(start_date)


if __name__ == "__main__":
    main()
```

I have removed the line 43 in `get_same_or_newer` :
*`data = get_file_lines(FILE_URL)`* so that the url isn't requested in every single iteration of the loop and this has reduced the time it took by half, but I have not optimised completely with the recommendations given.
