---
title: "How to loop through and scrape data from collapsibles on a website using Selenium?"
site: stackoverflow
question_id: 74342009
answer_id: 74342847
url: https://stackoverflow.com/a/74342847
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-07T06:44:10Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74342847/revisions
accepted: false
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 646a3d7e2cb448c07609bf9352ba83d38dac141daffcdf8a2276519046669de5
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74342847>, 2022-11-07; score 1. Text as retrieved 2026-10-12.

A note on debugging: when using `try...except`, debugging is easier if you print the exception - something like
```python 
try:
    ### CODE THAT MIGHT RAISE EXCEPTION ###
except Exception as err:
    print(str(err))
    #########  HANDLE  EXCEPTION  #########
```
that way, you might have a better idea of what went wrong.

<hr>

You're not targeting the right elements for `EC.element_to_be_clickable` and `emails = s.find_element` - in both cases, you're just targeting the first element of that type when you should be using a more specific identifying attribute like `id` or `data-target` or `data-actnum`. Also, you need to scroll to the "DETAILS" button so the click doesn't fall on something else for the last items (which is something I discovered due to `print(str(err))`). So, your `try...except` block should be changed to
```python
    try:
        dtarget = n.get_attribute('data-target')
        dSel = f'a[data-target="{dtarget}"]'
        eSel = f'{dtarget} .store-email'

        s.execute_script("arguments[0].scrollIntoView(false);", n)
        WebDriverWait(s, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, dSel)))
        n.click()
        time.sleep(3)

        emails = s.find_element(By.CSS_SELECTOR, eSel)
        email.append(emails.text)
        time.sleep(3)
    except Exception as err:
        print(str(err))
        s.quit()
        break # no point looping again after s.quit()
```

When I run it with the changes above, the `email` list ends up as
```python
['monica.bridalboutique@gmail.com', 'angelicasdesign@gmail.com', 'rbeamer@thetuxshopdm.com', 'staceysbridal@gmail.com', 'katie@somethingbluebride.com', 'info@affinitybridals.com', 'backwardsboutique16830@gmail.com']
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[noideawhatimdoingtbh](https://stackoverflow.com/users/20436783)** (2022-11-07): Wow, this is amazing. Thank you Driftr95, it is working perfectly for me. I really appreciate it and thanks for the debugging tip
