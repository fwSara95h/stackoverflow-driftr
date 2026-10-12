# Code from my Stack Overflow answer https://stackoverflow.com/a/74240970 (posted 2022-10-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for page_num in range(1, 10):
    time.sleep(10)

    scrapedUrls.append(driver.current_url)

    res = requests.get(driver.current_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # soup = BeautifulSoup(driver.page_source, 'html.parser') # no noticable improvement

    time.sleep(2)

    filteredListings = [
        di for di in soup.select('li[data-id]') if
        di.get('data-id') not in datId_list
    ]
    datId_list += [di.get('data-id') for di in filteredListings] 

    companies_list += [
        t.select_one('.css-l2wjgv.e1n63ojh0.jobLink').get_text(strip=True)
        if t.select_one('.css-l2wjgv.e1n63ojh0.jobLink')
        else None for t in filteredListings
    ]

    positions_list += [
        t.select_one('.jobLink.css-1rd3saf.eigr9kq2').get_text(strip=True)
        if t.select_one('.jobLink.css-1rd3saf.eigr9kq2')
        else None for t in filteredListings
    ]

    locations_list += [
        t.select_one(
            '.css-l2fjlt.pr-xxsm.css-iii9i8.e1rrn5ka0').get_text(strip=True)
        if t.select_one('.css-l2fjlt.pr-xxsm.css-iii9i8.e1rrn5ka0')
        else None for t in filteredListings
    ]

    job_post = [
        t.select('.eigr9kq3 .e1wijj242') for t in filteredListings
    ]
    salaries_list += [
        'Salary Not Found' if not j else
        (j[0].text if len(j) == 1 else [s.text for s in j])
        for j in job_post
    ]

    ratings_list += [
        t.select_one('.e1rrn5ka3').get_text(strip=True)
        if t.select_one('.e1rrn5ka3')
        else 'Rating Not Found' for t in filteredListings
    ]

# --- block 2 ---
dfDict = {'Data-Id': datId_list,
          'Company Name': companies_list,
          'Company Rating': ratings_list,
          'Position Title': positions_list,
          'Location': locations_list,
          'Est. Salary': salaries_list
          }
for k in dfDict:
    print(k, len(dfDict[k]))
glassdoor_dataset = pd.DataFrame(dfDict)
glassdoor_dataset.set_index('Data-Id', drop=True)

glassdoor_dataset.to_csv(r'glassdoor_jobs_scraped.csv')
