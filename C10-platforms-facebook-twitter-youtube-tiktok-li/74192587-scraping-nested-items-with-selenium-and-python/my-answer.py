# Code from my Stack Overflow answer https://stackoverflow.com/a/74197108 (posted 2022-10-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
containers = soup.select('div[class*="CommentContent"]') # comment content
commentItems = soup.select('div[class*="CommentItem"]') # outermost comment containers
commentTexts = soup.select('div[class*="CommentContent"] p[class*="CommentText"]') # same as find_all('p',{'data-e2e':'comment-level-1'})
commenterNames = soup.select('div[class*="CommentContent"] span[class*="UserName"]') # usernames of commenters

# --- block 2 ---
containers = browser.find_element_by_xpath('//div[contains(@class, "CommentContent")]')  
commentItems = browser.find_element_by_xpath('//div[contains(@class, "CommentItem")]') 
commentTexts = browser.find_element_by_xpath('//div[contains(@class, "CommentContent")]//p[contains(@class, "CommentText")]') 
commenterNames = browser.find_element_by_xpath('//div[contains(@class, "CommentContent")]//span[contains(@class, "UserName")]')
