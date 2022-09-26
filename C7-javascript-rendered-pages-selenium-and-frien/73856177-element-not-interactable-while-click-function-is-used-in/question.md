---
title: "Element not interactable while click() function is used in input type radio"
site: stackoverflow
question_id: 73856177
url: https://stackoverflow.com/q/73856177
asked: 2022-09-26T15:09:00Z
asked_by: "Amrita Stha"
asked_by_url: https://stackoverflow.com/users/4947216
last_edited: 2022-09-26T15:26:54Z
tags: [selenium, beautifulsoup, selenium-chromedriver]
score: 0
views_at_snapshot: 135
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6784b369bbacf0352ff971b09d1279d44ef7a898192d5957e0c04517ca06642b
---

# Element not interactable while click() function is used in input type radio

Asked by [Amrita Stha](https://stackoverflow.com/users/4947216) on Stack Overflow, <https://stackoverflow.com/q/73856177>, 2022-09-26, last edited 2022-09-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Input with type="radio" is not clickable. How to select the different radio button inputs using selenium and beautiful soup. Thanks in advance.

    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=r'E:/chromedriver.exe')
    driver.get(url)
    time.sleep(5)
    htmlSource = driver.page_source
    soup = BeautifulSoup(driver.page_source,'lxml')
    statement = soup.select('label:contains("Statement")')[0].input
    print(statement)
    statement.click()

Output:

	<input name="" type="radio" value="Statement"/>


However statement.click() gives error:

	statement.click()
	TypeError: 'NoneType' object is not callable
	
**P.S I've tried using xPath as well.**

	statement = driver.find_element(By.XPATH, '//input[@value=\'Statement\']')
	print(statement)
	statement.click()

Output:

	<selenium.webdriver.remote.webelement.WebElement (session="de0080d0898646c8f0053c8b2cbb1707", element="a426e341-f88c-4574-a831-5386a50cdd68")>
	
statement.click() gives follwing error	
	
	selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Md. Fazlul Hoque](https://stackoverflow.com/users/12848411)** (2022-09-26): You can't even imagine to click on an element with the help of bs4. You should share the url and only possible to click and to solve clickable problem with selenium only here
- **[KunduK](https://stackoverflow.com/users/10885684)** (2022-09-26): Can you post the html of parent element of the input element which binds the input element.
