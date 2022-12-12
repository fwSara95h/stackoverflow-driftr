---
title: "How do I use find_all or select more precisely in this case?"
site: stackoverflow
question_id: 74777050
url: https://stackoverflow.com/q/74777050
asked: 2022-12-12T20:39:23Z
asked_by: "yfr code"
asked_by_url: https://stackoverflow.com/users/15109461
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 38
answer_count: 1
accepted_answer_id: 74779366
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0b1d3147743ce587f3f7479c974e07db6f2ff2a2097da9c3176c1a9560ec8699
---

# How do I use find_all or select more precisely in this case?

Asked by [yfr code](https://stackoverflow.com/users/15109461) on Stack Overflow, <https://stackoverflow.com/q/74777050>, 2022-12-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

When I run the following code after importing stuff:
```page = 1
Fighter1Main = []
for i in range(1,3):
			url = Request(f"https://www.sherdog.com/events/a-{page}", headers={'User-Agent': 'Mozilla/5.0'})
			response = urlopen(url).read()
			soup = BeautifulSoup(response, "html.parser")
			for test2 in soup.find_all(class_="fighter left_side"):
				test3 = test2.find_all(itemprop="url")
				Fighter1Main.append(test3)
			page = page + 1
```
I get:
```
[[<a href="/fighter/Todd-Medina-61" itemprop="url">
<img alt="Todd 'El Tiburon' Medina" itemprop="image" src="/image_crop/200/300/_images/fighter/20140801074225_IMG_5098.JPG" title="Todd 'El Tiburon' Medina">
</img></a>], [<a href="/fighter/Ricco-Rodriguez-8" itemprop="url">
<img alt="Ricco 'Suave' Rodriguez" itemprop="image" src="/image_crop/200/300/_images/fighter/20141225125221_1MG_9472.JPG" title="Ricco 'Suave' Rodriguez">
</img></a>]]
```
But I was expecting:
```
<a href="/fighter/Todd-Medina-61" itemprop="url">
<a href="/fighter/Ricco-Rodriguez-8" itemprop="url">
```
This is the type of webpage in question https://www.sherdog.com/events/a-1

I also tried using css select and got the same result. 
```
for test2 in soup.select('.fighter.left_side [itemprop="url"]'):
				Fighter1Main.append(test2)
```
I thought I was using it correctly but I'm not sure how else to narrow it down to what I want.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Rivered](https://stackoverflow.com/users/9536233)** (2022-12-12): I guess, seeing from your returned list, that the itemprop="url" is part of your a tag. Perhaps you can try to just do something like ```test2.find_all('a', href=True)``` or ```test2.find_all('a')```?
