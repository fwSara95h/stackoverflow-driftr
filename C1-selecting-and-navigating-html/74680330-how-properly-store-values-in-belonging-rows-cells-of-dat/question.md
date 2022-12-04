---
title: "How properly store values in belonging rows/cells of dataframe while scraping with Beautiful Soup?"
site: stackoverflow
question_id: 74680330
url: https://stackoverflow.com/q/74680330
asked: 2022-12-04T19:47:48Z
asked_by: "drupaljac"
asked_by_url: https://stackoverflow.com/users/13264096
last_edited: 2022-12-05T16:01:50Z
last_editor: "TylerH"
last_editor_url: https://stackoverflow.com/users/2756409
tags: [python, pandas, dataframe, beautifulsoup]
score: -1
views_at_snapshot: 50
answer_count: 1
accepted_answer_id: 74681188
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e94ca12052dc77c2aa86a904ea05c7373c3f36c65e89431c5c77a11622a95381
---

# How properly store values in belonging rows/cells of dataframe while scraping with Beautiful Soup?

Asked by [drupaljac](https://stackoverflow.com/users/13264096) on Stack Overflow, <https://stackoverflow.com/q/74680330>, 2022-12-04, last edited 2022-12-05 by [TylerH](https://stackoverflow.com/users/2756409). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So, I am trying to scrape data from a journal. 


While I can successfully scrape titles of papers, keywords, and so on, and save them in dataframe properly when it comes to collecting authors' names, **each mentioned author of the paper after the first one is stored in a new row**. The same problem applies to affiliations. 
 

It’s making stored data useless and unrelated, obviously. Thus, instead of having the same number of rows, I get stuck with a useless dataframe.


It is my understanding that the problem arises because the program doesn’t “know” to store all the data associated with each paper in separate rows. Additionally, some papers only have one author, while others have 3-4. For example, authors need to be stored in a "NameSurname, NameSurname, NameSurname..." format within separate rows containing information about each research paper: authors, affiliations, etc.

But when it comes to specifying classes that I intend to scrape, I am uncertain how to set up the Python (BS4) code properly.

Here's a snippet of the relevant code from the simple scraper:

```
title = []
authors = []
afiliations = []

for i in urls: 
    page = requests.get(link)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")
    for t in soup.select(".obj_article_details .page_title"):
        title.append(t.get_text(strip=True))
    for au in soup.select(".obj_article_details .authors .name"):
        authors.append(au.get_text(strip=True))
    for af in soup.select(".obj_article_details .item.authors .affiliation"):
        affiliations.append(af.get_text(strip=True))
    time.sleep(3)
```

Also, here is a structure of section which i am intending to scrape



```
...
<article class="obj_article_details">	
 <h1 class="page_title">
   Lorem ipsum dolor sit amet
 </h1>
  <div class="row">
   <div class="main_entry">
<section class="item authors">
  <ul class="authors">
    <li>
      <span class="name">Brandon Scott </span>
      <span class="affiliation"> Villanova University, Pennsylvania </span>
    </li>
    <li>
      <span class="name">Alvaro Cote </span>
      <span class="affiliation">Carleton College, Minnesota</span>
    </li>
  </ul>
</section>

...
```


What I am getting now:


```
    |Authors       |  Affiliation                       | 
    +--------------+------------------------------------+
    |Brandon Scott | Villanova University, Pennsylvania |
    +--------------+------------------------------------+
    |Alvaro Cote   | Carleton College, Minnesota        |
    +--------------+------------------------------------+
    |...           | ...                                |
```

What i want:

```
    |Authors                     |  Affiliation         | 
    +--------------+------------------------------------+
    |Brandon Scott, Alvaro Cote | Villanova University..|
    +--------------+------------------------------------+
    |...           |...                                 |
    +--------------+------------------------------------+
    |...           |...                                 |
```
