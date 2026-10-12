# Code from my Stack Overflow answer https://stackoverflow.com/a/77084197 (posted 2023-09-11), extracted verbatim; may need the question's context to run.
for keyword in ['Meta', 'IBM']:
    URL = 'https://www.linkedin.com/search/results/companies/?keywords=' + keyword
    driver.get(url=URL)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    a_href = soup.select('span.entity-result__title-text a.app-aware-link')
    if a_href:
        link = a_href[0].get('href')
        print(f"Keyword: {keyword}, linkedin: {link}")
    else:
        print(f"Keyword: {keyword}, linkedin: Not found")
