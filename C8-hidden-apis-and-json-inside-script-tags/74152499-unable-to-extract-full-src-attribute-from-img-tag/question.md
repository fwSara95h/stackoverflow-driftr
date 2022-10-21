---
title: "Unable to extract full src attribute from img tag"
site: stackoverflow
question_id: 74152499
url: https://stackoverflow.com/q/74152499
asked: 2022-10-21T10:46:31Z
asked_by: "Driftr95"
asked_by_url: https://stackoverflow.com/users/6146136
last_edited: 2023-04-06T10:22:45Z
tags: [python, html, beautifulsoup]
score: 1
views_at_snapshot: 48
answer_count: 1
accepted_answer_id: 74152500
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 765a465799377e21b776d6a4058e9a0f95d97f75ea1c48a0f6792f465cc7c24d
---

# Unable to extract full src attribute from img tag

Asked by [Driftr95](https://stackoverflow.com/users/6146136) on Stack Overflow, <https://stackoverflow.com/q/74152499>, 2022-10-21, last edited 2023-04-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

<sup>[From trying to scrape Google Search results with requests+bs4, like if <kbd>*`soup = BeautifulSoup(requests.get('https://www.google.com/search?q=best+laptops+2022').content)`*</kbd>, then any `img` tag you might find with `soup.select('img[id^="dimg"]')`.]</sup>

It seemed simple enough at first - just use `soup.find` and then `.get('src')` or `.attrs['src']`, but major chunks of the `src` has been replaced with "/////"
[![extraction code][1]][1]

<br><hr>

The value is actually much longer:
[DevTools screenshot][2]


What's baffling me is that I saved `str(soup)` as a html file, and also used `display(HTML(str(soup)))` and with both, the image is being rendered just fine - I can even copy the full src from inspecting the file.
[Colab output with fully rendered images][3]

<hr>

But even 
```python
str(soup).split('id="dimg_179" src="')[1].split('"')[0]
```
produces the same `data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==`.

I would very much appreciate any explanation of this behavior and/or some suggestions of how to extract the actual `src`. 


  [1]: https://i.sstatic.net/aX0Rh.png
  [2]: https://i.sstatic.net/r7PKG.png
  [3]: https://i.sstatic.net/jAA7n.png
