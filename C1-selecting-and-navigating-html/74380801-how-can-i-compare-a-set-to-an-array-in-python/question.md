---
title: "How can I compare a set to an array in Python?"
site: stackoverflow
question_id: 74380801
url: https://stackoverflow.com/q/74380801
asked: 2022-11-09T20:09:39Z
asked_by: "Mark Leach"
asked_by_url: https://stackoverflow.com/users/20401143
last_edited: 2022-11-09T21:33:51Z
tags: [python]
score: -2
views_at_snapshot: 119
answer_count: 1
accepted_answer_id: 74384000
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e8b170019666076dd14799f659f2cd889fd26b3d46a26207faeb4fb6e42d534b
---

# How can I compare a set to an array in Python?

Asked by [Mark Leach](https://stackoverflow.com/users/20401143) on Stack Overflow, <https://stackoverflow.com/q/74380801>, 2022-11-09, last edited 2022-11-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to get all unique URLs on a web page e.g. https://www.ig.com/uk/trading-strategies (there can be duplicates) and then compare them to URLs in an array and if the URLs are unique to write data to a Google Sheet.

I'm really struggling getting all the unique URLs on a webpage e.g. https://www.ig.com/uk/trading-strategies. I thought I could append unique URLs to a list then to a set and then to a tuple to compare against the array but that doesn't seem to be working.

Do you have any insights that could help?

Thanks in advance

Mark

    obj = {r[2]: True for r in sh.get_all_values()}
    ar = []

    articles = set()
    unique = (articles)
    
    for url in urls:
        my_url = requests.get(url)
        html = my_url.content
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("h3", class_="article-category-section-title"):
            date = datetime.date.today()
            title = item.find("a", class_="primary js_target").text.strip()
            article = item.find("a", class_="primary js_target").get("href")
            abs = "https://www.ig.com"
            rel = article
            pub = rel[-6:]
            datestring = f"{pub[4:6]} {pub[2:4]} {pub[0:2]}"
            info = {"date": date, "title": title, "url":urllib.parse.urljoin(abs, rel), "published":datestring}
            article = str(info["url"].replace("https://",""))
            articles.add(article)
            if unique not in obj:
                ar.append([str(info["date"]), str(info["title"]), article, str(info["published"])])
    if ar != []:
        sh.append_rows(ar, value_input_option="USER_ENTERED")

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Nikolaj Š.](https://stackoverflow.com/users/9288580)** (2022-11-09): What's `unique = str(articles)` supposed to do?  `unique` is just a `'set()'` (a string).  It's unlikely to be found in `obj`, whatever `obj` might be.
- **[Nikolaj Š.](https://stackoverflow.com/users/9288580)** (2022-11-09): Also, is the question about `beautifulsoup` or comparing sets to lists?
- **[Mark Leach](https://stackoverflow.com/users/20401143)** (2022-11-09): Hey i just update my code and removed the string. I wanted unique to hold the contents of the set. I already did the beautiful soup part to get the data so its about comparing sets to an array.
