---
title: "How to fix beautiful soup list index out of range"
site: stackoverflow
question_id: 74525562
url: https://stackoverflow.com/q/74525562
asked: 2022-11-21T22:28:30Z
asked_by: "TANG TANG"
asked_by_url: https://stackoverflow.com/users/20566942
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 113
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d559cf4947f37724b256f76145f43482218487a4b5a835e4db57cc6a037160ef
---

# How to fix beautiful soup list index out of range

Asked by [TANG TANG](https://stackoverflow.com/users/20566942) on Stack Overflow, <https://stackoverflow.com/q/74525562>, 2022-11-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to get specific information from the website. It is okey to run first four url, but when we run the fifth one, we get 'IndexError: list index out of range' at 'company = soup.select('.companyName')[0].get_text().strip()'.

we have url like
https://www.indeed.com/jobs?q=data analyst&l=remote

```
## Number of postings to scrape
postings = 100

jn=0

for i in range(0, postings, 10):
    driver.get(url + "&start=" + str(i))
    driver.implicitly_wait(3)

    jobs = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')

    for job in jobs:
        result_html = job.get_attribute('innerHTML')
        soup = BeautifulSoup(result_html, 'html.parser')
        
        jn += 1
        
        liens = job.find_elements(By.TAG_NAME, "a")
        links = liens[0].get_attribute("href")
        
        title = soup.select('.jobTitle')[0].get_text().strip()
        company = soup.select('.companyName')[0].get_text().strip()
        location = soup.select('.companyLocation')[0].get_text().strip()
        try:
            salary = soup.select('.salary-snippet-container')[0].get_text().strip()
        except:
            salary = 'NaN'
        try:
            rating = soup.select('.ratingNumber')[0].get_text().strip()
        except:
            rating = 'NaN'
        try:
            date = soup.select('.date')[0].get_text().strip()
        except:
            date = 'NaN'
        try:
            description = soup.select('.job-snippet')[0].get_text().strip()
        except:
            description = ''
       
        dataframe = pd.concat([dataframe, pd.DataFrame([{'Title': title,
                                          "Company": company,
                                          'Location': location,
                                          'Rating': rating,
                                          'Date': date,
                                          "Salary": salary,
                                          "Description": description,
                                          "Links": links}])], ignore_index=True)
        print("Job number {0:4d} added - {1:s}".format(jn,title))
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Tim Roberts](https://stackoverflow.com/users/1883316)** (2022-11-21): That would imply that the listing doesn't have a tag with class `companyName`.  Just check for None before you reference `[0]`.
