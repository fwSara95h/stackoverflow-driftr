---
title: "Scraping Glassdoor returns duplicate entries"
site: stackoverflow
question_id: 74193851
url: https://stackoverflow.com/q/74193851
asked: 2022-10-25T12:09:15Z
asked_by: "Zoya Aqib"
asked_by_url: https://stackoverflow.com/users/15606732
last_edited: 2022-10-30T10:40:34Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [selenium, web-scraping, beautifulsoup, selenium-chromedriver]
score: 0
views_at_snapshot: 447
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 51df2e0234f22528a2870533dc338bcf2f4b875bd230075c076a0bc38f8e481c
---

# Scraping Glassdoor returns duplicate entries

Asked by [Zoya Aqib](https://stackoverflow.com/users/15606732) on Stack Overflow, <https://stackoverflow.com/q/74193851>, 2022-10-25, last edited 2022-10-30 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So I am trying to scrape job posts from Glassdoor using Requests, Beautiful Soup and Selenium. The entire code works except that, even after scraping data from 30 pages, most entries turn out to be duplicates (almost 80% of them!). Its not a headless scraper so I know it is going to each new page. What could be the reason for so many duplicate entries? Could it be some sort of anti-scraping tool being used by Glassdoor or is something off in my code?


The result turns out to be 870 entries of which a whopping 690 are duplicates! 

My code:
```python
def glassdoor_scraper(url):
    
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    
    # Getting to the page where we want to start scraping
    jobs_search_title = driver.find_element(By.ID, 'KeywordSearch')
    jobs_search_title.send_keys('Data Analyst')
    jobs_search_location = driver.find_element(By.ID, 'LocationSearch')
    
    time.sleep(1)
    
    jobs_search_location.clear()
    jobs_search_location.send_keys('United States')
    click_search = driver.find_element(By.ID, 'HeroSearchButton')
    click_search.click()
    
    for page_num in range(1,10):
        time.sleep(10)
        
        res = requests.get(driver.current_url)
        soup = BeautifulSoup(res.text,'html.parser')
        
        time.sleep(2)

        companies = soup.select('.css-l2wjgv.e1n63ojh0.jobLink')
        for company in companies:
            companies_list.append(company.text)
    
        positions = soup.select('.jobLink.css-1rd3saf.eigr9kq2')
        for position in positions:
            positions_list.append(position.text)
    
        locations = soup.select('.css-l2fjlt.pr-xxsm.css-iii9i8.e1rrn5ka0')
        for location in locations:
            locations_list.append(location.text)
    
        job_post = soup.select('.eigr9kq3')
        for job in job_post:
            salary_info = job.select('.e1wijj242')
            if len(salary_info) > 0:
                for salary in salary_info:
                    salaries_list.append(salary.text)
            else:
                salaries_list.append('Salary Not Found')
    
        ratings = soup.select('.e1rrn5ka3')
        for index, rating in enumerate(ratings):
            if len(rating.text) > 0:
                ratings_list.append(rating.text)
            else:
                ratings_list.append('Rating Not Found')
        
        
        next_page = driver.find_elements(By.CLASS_NAME, 'e13qs2073')[1]
        next_page.click()
        time.sleep(5)
        try:
            close_jobalert_popup = driver.find_element(By.CLASS_NAME, 'modal_closeIcon')
        except:
            pass
        else:
            time.sleep(1)
            close_jobalert_popup.click()        
        continue
    
    #driver.close()
    print(f'{len(companies_list)} jobs found for you!')
    
    global glassdoor_dataset
    
    glassdoor_dataset = pd.DataFrame(
    {'Company Name': companies_list,
     'Company Rating': ratings_list,
     'Position Title': positions_list,
     'Location' : locations_list,
     'Est. Salary' : salaries_list
    })
    
    glassdoor_dataset.to_csv(r'glassdoor_jobs_scraped.csv')
```
