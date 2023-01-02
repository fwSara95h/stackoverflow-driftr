---
title: "Unable to get all attribute(img @src) values using xpath selenium python"
site: stackoverflow
question_id: 74984290
url: https://stackoverflow.com/q/74984290
asked: 2023-01-02T15:37:39Z
asked_by: "Siva Ranjjan"
asked_by_url: https://stackoverflow.com/users/18726958
last_edited: 2023-01-03T02:02:08Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, selenium, web-scraping, xpath]
score: 0
views_at_snapshot: 76
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5676c1bf89d84d8d2f52ec19f9d3a21234d8fdb0b44a80a6dc789eee2e4da8a5
---

# Unable to get all attribute(img @src) values using xpath selenium python

Asked by [Siva Ranjjan](https://stackoverflow.com/users/18726958) on Stack Overflow, <https://stackoverflow.com/q/74984290>, 2023-01-02, last edited 2023-01-03 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I need to get all the `src` of video banners from a YouTube page. By inspecting the page through XPath I see 171 `src` values but in selenium with XPath and CSS selector I could get some 120+ `src` values.

youtube page - https://www.youtube.com/@JohnWatsonRooney/videos

---

```python
Banners = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((
        By.XPATH, '//div[contains(@id,"dismissible")]/ytd-thumbnail/a')))
```

Above, `Banner` length is 171.

---

```python
Banners_src = []
for element in Banners:
    Banners_src.append(element.find_element_by_xpath('.//img').get_attribute('src'))
```

Size of `Banners_src` is 123 (it keeps varying - can also be 121 or 122 sometimes).

---

```python
Banners_Sample = driver.find_elements_by_xpath('//img[contains(@src, "https://i.ytimg.com")]') 
```
Size of `Banners_sample` is 123 (same result).

But when inspecting in browser using same XPath, I get 171 `src` values.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Community](https://stackoverflow.com/users/-1)** (2023-01-02): Please clarify your specific problem or provide additional details to highlight exactly what you need. As it's currently written, it's hard to tell exactly what you're asking.
