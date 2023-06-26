---
title: "How do I get a specific element from a bs4.element.ResultSet?"
site: stackoverflow
question_id: 76552348
answer_id: 76555865
url: https://stackoverflow.com/a/76555865
author: "Daniel Fainberg"
author_url: https://stackoverflow.com/users/19770795
posted: 2023-06-26T10:34:12Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 97c616bc888084bbb0d3d334213a53ea25c9ab9f31e70c8609add208eace75b6
role: another answer on the same question, kept as context; not my work
---

# Answer by [Daniel Fainberg](https://stackoverflow.com/users/19770795) — 2023-06-26

Posted on Stack Overflow, <https://stackoverflow.com/a/76555865>, 2023-06-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Instead of searching for `<a>`-tags that simply _have_ an `href` attribute, as you did with

```python
soup.find_all('a', href=True)
```

you can [provide a function][1] that determines if the attribute of interest (in this case `href`) of any given tag _matches some desired pattern_ like this:

```python
import re
from typing import Callable, Optional


def attr_matches(pattern: str) -> Callable[[Optional[str]], bool]:
    def filter_attribute(attr_value: Optional[str]) -> bool:
        if attr_value is None:
            return False
        return re.compile(pattern).search(attr_value) is not None
    return filter_attribute

...

tags = soup.find_all("a", href=attr_matches("/Company"))
```

Since `find_all` returns `Tag`s, a simple list comprehension will then get you just the `href` values:

```python
urls = [tag["href"] for tag in tags]
print(urls)
```

Output: `['/Company/apple-hospitality-reit-inc', '/Company/apple-inc', '/Company/maui-land-pineapple-co-inc', '/Company/pineapple-energy-inc']`

---

This generic approach is much more flexible because you can give this `attr_matches` function any valid [RegEx][2] pattern and use it independent of what specific tag or attribute you want to filter by.

On the same web page for example, find all `<img>` tags, where the image source uri has `category` in it and ends with `webp`:

```python
tags = soup.find_all("img", src=attr_matches("category.+webp$"))
print([tag["src"] for tag in tags])
```

Output: `['/img/ar/category_premiumBadge.webp', '/img/ar/category_premiumBadge.webp', '/img/ar/category_premiumBadge.webp']`


  [1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-function
  [2]: https://docs.python.org/3/howto/regex.html
