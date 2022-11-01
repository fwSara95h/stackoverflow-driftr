---
title: "Web Scraping 'Advice to management\" not printing from Glassdoor"
site: stackoverflow
question_id: 74253197
answer_id: 74275374
url: https://stackoverflow.com/a/74275374
author: "Brze"
author_url: https://stackoverflow.com/users/10848420
posted: 2022-11-01T11:42:46Z
last_edited: 2022-11-05T18:36:09Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c6f55086b4429e8e4ef6713e459da61b5a57a556ae44d721974350441290bf82
role: another answer on the same question, kept as context; not my work
---

# Answer by [Brze](https://stackoverflow.com/users/10848420) — 2022-11-01

Posted on Stack Overflow, <https://stackoverflow.com/a/74275374>, 2022-11-01, last edited 2022-11-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

To get "Advice to management" you need to click on the link "Continue reading"

Therefore, one of the possible solutions could be for example `Selenium`:
```py
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


def save_to_csv(data: list) -> None:
    with open(file='glassdoor.csv', mode='a', encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([*data])

def get_params(params: dict) -> str:
    return f"?{'&'.join([f'{k}={v}' for k, v in params.items()])}"

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
service = Service(executable_path="path/to/your/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

url = 'https://www.glassdoor.com/Reviews/Google-Engineering-Reviews-EI_IE9079.0,6_DEPT1007.htm'
# sort options
params = {
    'sort.sortType': 'RD', 
    'sort.ascending': 'false', 
    'filter.iso3Language': 'eng'
    }
# cookies needed to prevent the login window from appearing
cookies = {
    "name": "at", 
    "value": "AQuAbmAwLKGMSj7gS4VKDrlQfUrJlSdHPS5T7ui1struL_UX8_FNmWke8iuqLwd9zGs0faZ29oqiGJyiePbR0cBUIU"\
        "Pk9V2h1dGnUG9RoU7COdbZqRl47h6dfhf9t31wRW9jiHIiIdCFre1fh_28W4tg0zg6yDwjMZ3u0PRDtS_cWKkljwrdI10xZt"\
        "Pk9V2h1dGnUG9RoU7CZ3u0PRDtS_cWKkljwrdI1OdbZqRl47hW4tg0zg6yDwjM6dfhf9t31wRW9jiHIiIdCFre1fh_380xZ-"\
        "HEfDZm6vHqOWOfb69DaVTECM22_D404WYg0B-WzLLfRFnVSsp8gFk6g0s-Iwc_mNAnKM_K_5c-dl6Lye5TQuprP1bt5SWbyB"\
        "UAxTL9VzpUdtLz8DL8L0b4se92IRRcq57SnZGF4egsw_b7xMDQyTSHiqk_6B-MrzBsJsYTbuzjPT_dnXDkq01SbtLmRYrqAi"\
        "lJ_ht6gzuGmq4QF-tp8T2VRA0smvYxmbeKlHYy-syz0h-vdGIGcFightEl_Lzs4hXXbu33mtl_NOjAALGXdfTHnZABt1OAx9"\
        "Pk9V2h1dGnUG9RoU7CW4tg0zg6yDwjMZ3u0PRDtS_cWKkljwrdI1OdbZqRl47h6dfhf9t31wRW9jiHIiIdCFre1fh_380xZt"\
        "ZcFqYZtSf9mXkC3OARMCpgeFh-zOh4O0ox2TwYMMUTU_hLgKtUY80Udt9GTDIpVRRxqUvEZ-FzTAcU8zMqAxY8SLp2VlX2zI"\
        "Pk9V2h1dGnUG9RoU7CW4tg0zg6yDwjMZ3u0PRDtS_cWKkljwqU1OdbZqRl47h6dfhf9t31wRW9jiHIiIdCFre1fh_380xZt"\
        "NU04W74RRsahOnblqDQWsbsq-gwQ"
    }

# page where data collection will stop
stop_page = 5

driver.get(f"{url}{get_params(params)}")
# add cookies and refresh the page
driver.add_cookie(cookies)
driver.refresh()

while True:
    # get all the reviews on the page
    reviews = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.gdReview')))
    # click on all "Continue reading" links on the page
    driver.execute_script(
    """
    let cr = document.querySelectorAll('div.gdReview div.px-std>div.mb')
    Array.from(cr).forEach(e => {e.click()})
    """
    )
    for idx in range(len(reviews)):
        reviews = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.gdReview')))
        rating = reviews[idx].find_element(By.CSS_SELECTOR, 'span.ratingNumber').text
        employee_situation = reviews[idx].find_element(By.CSS_SELECTOR, 'div.gdReview>div>div>span').text
        title = reviews[idx].find_element(By.CSS_SELECTOR, 'a.reviewLink').text
        auhtor_info = reviews[idx].find_element(By.CSS_SELECTOR, 'span.middle:first-child').text
        pros = reviews[idx].find_element(By.CSS_SELECTOR, 'span[data-test="pros"]').text
        cons = reviews[idx].find_element(By.CSS_SELECTOR, 'span[data-test="cons"]').text
        try:
            advice = reviews[idx].find_element(By.CSS_SELECTOR, 'span[data-test="advice-management"]').text
        except NoSuchElementException:
            advice = 'None'
        data = {
            'Title': title,
            'Rating': rating,
            'Employee_Situation': employee_situation,
            'Pros': pros.replace('\n', ' ').strip(),
            'Cons': cons.replace('\n', ' ').strip(),
            'Advice To Management': advice,
            'Auhtor Info': auhtor_info
        }
        save_to_csv(list(data.values()))
        print(data)
    
    if f"_IP{stop_page}" in driver.current_url:
        break
    driver.execute_script(
        """
        document.querySelector('button.nextButton').click()
        """
        )
    sleep(3)
    print(f"Current Page: {driver.current_url.split('_IP')[1].split('.htm')[0]}") 
driver.quit()
```
Output csv file `glassdoor.csv`:
```csv
Good,4.0,"Current Employee, more than 3 years",Flexible Positive Enthusiatic Fun Collaborative,Low leaves Low bonus LOVE LOVE LOVE,None,"Oct 27, 2022 - Software Eigineer"
Ni,5.0,Current Employee,Google join because best company,Google work friendly and lot of holidays,Excellent,"Oct 27, 2022 - Software Developer"
Software Engineer Intern,5.0,"Former Intern, less than 1 year",Good culture and good stipend,No cons as such in my experience.,None,"Oct 27, 2022 - Software Engineer Intern"
```
To avoid problems with the login window that appears and to avoid the need for authorization on the site, you can use cookies.

You only need:
```
{
     "name": "at",
     "value": "AQuAbmAwLKGMSj7gS4VKDr..."
}
```
You can get them for example by going to the `Application` tab in `DevTools` there you will see a list of `Cookies` in it select `www.glassdoor.com` then in the filter type 'at' and in the resulting list select `at` copy the value and paste it into the script.
[![cookies][1]][1]
Of course, you must do this while on the site and be logged in there.

And ofc, you can automate the login process using the capabilities of selenium, but in this case you don't need it.

Tested on `Python 3.9.10` and `Selenium 4.5.0`

**Update**:

If look at the source code of this site, you can see that the data we need is in `window.appCache` js object and can be obtained using, for example, `requests`, `BeautifulSoup`, and the `re` module.

Here is one possible solution how to extract data from this object:
```py
import re
import csv
import json
import requests
from bs4 import BeautifulSoup
from typing import Generator, Tuple, List, Any


def get_page(num: int) -> str:
    return f'https://www.glassdoor.com/Reviews/Google-Engineering-Reviews-EI_IE9079.0,6_DEPT1007_IP{num}.htm'

def save_to_csv(data: list) -> None:
    with open(file='glassdoor.csv', mode='a', encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([*data])

def get_job_title(job_titles: list, title_id: int) -> str:
    for title in job_titles:
        if title['jobTitleId'] == title_id:
            return title['jobTitle']

def get_employee_situation(review: dict) -> str:
    if review['isCurrentJob'] and review['employmentStatus'] == 'REGULAR':
        employee_situation = 'Current Employee'
    if not review['isCurrentJob'] and review['employmentStatus'] == 'REGULAR':
        employee_situation = 'Former Employee'
    if review['isCurrentJob'] and review['employmentStatus'] == 'INTERN':
        employee_situation = 'Current Intern'
    if not review['isCurrentJob'] and review['employmentStatus'] == 'INTERN':
        employee_situation = 'Former Intern'
    if review['isCurrentJob'] and review['employmentStatus'] == 'CONTRACT':
        employee_situation = 'Current Contractor'
    if not review['isCurrentJob'] and review['employmentStatus'] == 'CONTRACT':
        employee_situation = 'Former Contractor'
    if review['isCurrentJob'] and review['employmentStatus'] == 'PART_TIME':
        employee_situation = 'Current Employee - Part-time'
    if not review['isCurrentJob'] and review['employmentStatus'] == 'PART_TIME':
        employee_situation = 'Former Employee - Part-time'
    if review['isCurrentJob'] and review['employmentStatus'] == 'FREELANCE':
        employee_situation = 'Current Freelancer'
    if not review['isCurrentJob'] and review['employmentStatus'] == 'FREELANCE':
        employee_situation = 'Former Freelancer'
    return employee_situation

def get_data_by_key(data: dict, key: str) -> Generator[None, None, List[Any]]:
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                yield v
            if isinstance(v, (dict, list)):
                yield from get_data_by_key(v, key)
    elif isinstance(data, list):
        for i in data:
            yield from get_data_by_key(i, key)

def json_validation(data: str) -> dict:
    script = [s.text for s in BeautifulSoup(data, "lxml").find_all("script") if "window.appCache" in s.text][0]

    script = re.sub(r'(\"urlRegexMatchers\")(([^@])+)(\"urlParams\")', '"urlRegexMatchers":{},"urlParams"', script)
    script = re.sub(r'(undefined)', '"undefined"', script) 
    script = re.sub(r'(}}}})', '}}}', script)
    script = re.sub(r'(}}};)', '}}}}', script)
    script = re.sub(r'(window\.appCache=)', '', script)
    try:
        return json.loads(script)
    except ValueError:
        script = script.replace('},"apolloState"', ',"apolloState"')
        return json.loads(script)

params = {
    'sort.sortType': 'RD',
    'sort.ascending': 'false',
    'filter.iso3Language': 'eng'
}
headers = {
    'user-agent': 'Mozilla/5.0'
}

with requests.Session() as session:
    session.headers.update(headers)
    for i in range(1, 10):
        raw_data = session.get(get_page(i), params=params).text
        json_data = json_validation(raw_data)
        reviews = list(get_data_by_key(json_data, 'reviews'))[1]
        job_titles = list(get_data_by_key(json_data, 'jobTitlesByEmployer({\"employerId\":9079})'))

        for review in reviews:
            data = {
                'Title': review.get('summary'),
                'Rating': review.get('ratingOverall'),
                'Employee_Situation': get_employee_situation(review),
                'Pros': review.get('pros'),
                'Cons': review.get('cons'),
                'Advice To Management': review.get('advice', 'No data'),
                'Auhtor Info': get_job_title(job_titles[0], int(review['jobTitle']['__ref'].split(':')[1]))
            }
            save_to_csv(list(data.values()))
```
Output:
```csv
Software developer,5,Former Employee,learn new tech easily and get support,make our growth of individual profile,,Software Developer
Good,5,Former Employee,Amazing place to work at.,Too amazing for a normie,Let everyone be better,Software Engineer
Good,5,Former Employee,A good place to work. Good culture,"Busy, long hours some days",,Software Engineer
```
Tested on `Google Colab - [Python 3.7.15]`

  [1]: https://i.sstatic.net/2YwhI.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[user19810494](https://stackoverflow.com/users/19810494)** (2022-11-03): Is there a way to solve this using BeautifulSoup package please?
- **[Brze](https://stackoverflow.com/users/10848420)** (2022-11-05): @user19810494 with BeautifulSoup you can't press buttons, expand lists and etc. I updated answer and added another way to get data
