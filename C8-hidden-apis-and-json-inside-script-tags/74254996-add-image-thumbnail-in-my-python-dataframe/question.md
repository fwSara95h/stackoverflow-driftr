---
title: "Add Image/thumbnail in my python dataframe"
site: stackoverflow
question_id: 74254996
url: https://stackoverflow.com/q/74254996
asked: 2022-10-30T16:56:07Z
asked_by: "rufina_mar"
asked_by_url: https://stackoverflow.com/users/20373110
last_edited: 2022-10-31T10:06:46Z
last_editor: "Mr K."
last_editor_url: https://stackoverflow.com/users/2344363
tags: [python-3.x, dataframe, image, beautifulsoup, moviepy]
score: -1
views_at_snapshot: 204
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b53b0fded0354f49199d5cd78707b5766962828a2331cd1f14b0ff98bc19629f
---

# Add Image/thumbnail in my python dataframe

Asked by [rufina_mar](https://stackoverflow.com/users/20373110) on Stack Overflow, <https://stackoverflow.com/q/74254996>, 2022-10-30, last edited 2022-10-31 by [Mr K.](https://stackoverflow.com/users/2344363). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am working on a project where I need to create a movie database.
I have created my database and imported the links from IMDB that redirect you to the webpage. I would like to add also, the main image/thumbnail of each movie so that I can use then the csv in Power BI.[![enter image description here](https://i.sstatic.net/YEd7o.png)](https://i.sstatic.net/YEd7o.png)
However, I did not manage to do it:

I have tried this:
```
import requests
from bs4 import BeautifulSoup
import numpy as np

images = []
for i in df_database_url['Url Film']:
    r = requests.get(i)
    soup = BeautifulSoup(r.content, "html.parser")
    images.append(image_url)
```

But my goal is to have a column that includes the thumbnail for each movie.
