---
title: "Elements able to be found using XPATH but not using CSS Selector. Am I searching using the correct value?"
site: stackoverflow
question_id: 73942961
url: https://stackoverflow.com/q/73942961
asked: 2022-10-04T03:49:22Z
asked_by: "Xaldin"
asked_by_url: https://stackoverflow.com/users/20154862
last_edited: never
tags: [python, selenium, web-scraping]
score: 0
views_at_snapshot: 187
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 399f2e4453b37a6b6b928c1427ea33e6024a77c70cd878662796c2597969be40
---

# Elements able to be found using XPATH but not using CSS Selector. Am I searching using the correct value?

Asked by [Xaldin](https://stackoverflow.com/users/20154862) on Stack Overflow, <https://stackoverflow.com/q/73942961>, 2022-10-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to extract data from multiple pages of search results where the HTML in question looks like so:

```
<ul>
    <li class="Card___StyledLi4-ulg8ho-7 jmevwM">...</li>
    <li class="Card___StyledLi4-ulg8ho-7 jmevwM">...</li>
    <li class="Card___StyledLi4-ulg8ho-7 jmevwM">...</li>
</ul>
```

I want to extract the text from the "li" tags, so I have:

    text_data = WebDriverWait(driver,10).until(EC.visibility_of_all_element_located((By.XPATH,'Card___StyledLi4-ulg8ho-7.jmevwM')
    
    print(text_data.text)

to wait and target "li" item. However, I get a "TimeoutException" error.

However, if I try to locate a single "li" item using the XPATH under the same conditions, the data is returned which leads me to question if I am inputting the class correctly?

Can anyone tell me what I'm doing wrong? Please let me know if there is any further information, you'd like me to provide.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-10-04): the data returned was correct with just `li` ? I've left an answer - if it doesn't work then please include one or more of the links you're scraping from so that your case is more reproducible. [Also, I think you've left 2 brackets open in `.until` when copying that line.]
- **[Xaldin](https://stackoverflow.com/users/20154862)** (2022-10-04): Your answer works! I have a follow up question, however. The code runs, but I only get the data of some of the “li” elements, instead of all of them. However, if I don’t use “WebDriverWait” and just scrape using “.findelements”, I get all the “li” information? Is there a reason for this?
- **me** (2022-10-04): I can't tell for sure without the link (normally it's the other way around), but maybe the site has some javascript changing some of the classes after a while? Are you using the exact same selector/xpath in both cases? [Also, why did you use `wait` in the first place? Generally `wait...until` are not used unless necessary...]
- **[Xaldin](https://stackoverflow.com/users/20154862)** (2022-10-05): My apologies! The link is findtreatment.gov. I did manage to figure it out, but if you could still provide some insight on why I'm only getting some of the elements and not all, I would really appreciate it! I'm still new to webscraping and really python in general. In the past when I've scraped the page, I have had instances where the page didn't load in time, so now I pretty much just implement `wait` wherever I plan to interact with the page. I didn't know this wasn't the norm lol
- **me** (2022-10-05): can I ask what you're searching under? I tested with Brooklyn and I get nothing right after clicking the search button without the wait and always 10 items after - I also tried checking in 0.05s intervals, and it just jumps from 0 to 10 after 0.6s [12 loops] and then stays constant
- **me** (2022-10-05): does you search result have less than 10 items? maybe it immediately creates 10 blank items then fills them and then deletes if any are unnecessary; I don't really think that's a likely scenario - this is rather baffling...
- **me** (2022-10-05): [and it *is* normal to wait if you had loading delays in the past dw. I thought you just added wait from the first scrape]
- **[Xaldin](https://stackoverflow.com/users/20154862)** (2022-10-06): My search was ZipCode "16565", 100+ miles, and Treatment Type "Residential" (3000+) results. My search result with the `WebDriverWait` was only 7, but 10 without it
- **me** (2022-10-06): Does it happen only on the last page (which has less than 10 results) or on other pages also? [I can't test myself rn since I'm afc.] If it's only on the last page then it's as I speculated before (that 10 blank its are generated first then filled and culled),  but if it's happening on other pages too, then I'm still baffled. Maybe there's a bug in `EC.visibility...` that makes it think all elements are visible before they are, something unique in the site's js that `EC` hasn't accounted for...
