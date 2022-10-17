---
title: "Reusable Beautiful Soup Parser/Config?"
site: stackoverflow
question_id: 74098931
url: https://stackoverflow.com/q/74098931
asked: 2022-10-17T14:39:13Z
asked_by: "frumsky"
asked_by_url: https://stackoverflow.com/users/13085376
last_edited: never
tags: [python, selenium, web-scraping, beautifulsoup, web-crawler]
score: 1
views_at_snapshot: 270
answer_count: 1
accepted_answer_id: 74104518
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: df2dfd1f146d20e4b10907db50a64b8709cdf39524ec045b1c4dc7a3f38ec0e0
---

# Reusable Beautiful Soup Parser/Config?

Asked by [frumsky](https://stackoverflow.com/users/13085376) on Stack Overflow, <https://stackoverflow.com/q/74098931>, 2022-10-17. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a Selenium-based web crawler application that monitors over 100 different medical publications, with more being added regularly. Each of these publications has a different site structure, so I've tried to make the web crawler as general and re-usable as possible (especially because this is intended for use by other colleagues). For each crawler, the user specifies a list of regex URL patterns that the crawler is allowed to crawl. From there, the crawler will grab any links found as well as specified sections of the HTML. This has been useful in downloading large amounts of content in a fraction of the time it would take to do manually.

I'm now trying to figure out a way to generate custom reports based on the HTML of a certain page. For example, when crawling X site, export a JSON file that shows the number of issues on the page, the name of each issue, the number of articles under each issue, then the title and author names of each of those articles. The page I'll use as an example and test case is https://www.paediatrieschweiz.ch/zeitschriften/

I've created a list comprehension that produces my desired output. 
```
url = "https://www.paediatrieschweiz.ch/zeitschriften/"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

report = [{
    'Issue': (unit.find('p', {'class': 'section__spitzmarke'}).text).strip(), 
    'Articles': [{
        'Title': ((article.find('h3', {'class': 'teaser__title'}).text).strip()),
        'Author': ((article.find('p', {'class': 'teaser__authors'}).text).strip())
    } for article in unit.find_all('article')]} 
    for unit in soup.find_all('div', {'class': 'section__inner'})]
```

Sample JSON output:
```
[
    {
        "Issue": "Paediatrica Vol. 33-3/2022",
        "Articles": [
            {
                "Title": "Editorial",
                "Author": "Daniela Kaiser, Florian Schaub"
            },
            {
                "Title": "Interview mit Dr. med. Germann Clenin",
                "Author": "Florian Schaub, Daniela Kaiser"
            },
            {
                "Title": "Ern\u00e4hrung f\u00fcr sportliche Kinder und Jugendliche",
                "Author": "Simone Reber"
            },
            {
                "Title": "Diabetes und Sport",
                "Author": "Paolo Tonella"
            },
            {
                "Title": "Asthma und Belastung",
                "Author": "Isabelle Rochat"
            },
            {
                "Title": "Sport bei Kindern und Jugendlichen mit rheumatischer Erkrankung",
                "Author": "Daniela Kaiser"
            },
            {
                "Title": "H\u00e4mophilie und Sport",
                "Author": "Denise Etzweiler, Manuela Albisetti"
            },
            {
                "Title": "Apophysen - die Achillesferse junger Sportler",
                "Author": "Florian Schaub"
            },
            {
                "Title": "R\u00fcckenschmerzen bei Athleten im Wachstumsalter",
                "Author": "Markus Renggli"
            },
            {
                "Title": "COVID-19 bei jugendlichen AthletenInnen: Diagnose und Return to Sports",
                "Author": "Susi Kriemler, Jannos Siaplaouras, Holger F\u00f6rster, Christine Joisten"
            },
            {
                "Title": "Schutz von Kindern und Jugendlichen im Sport",
                "Author": "Daniela Kaiser"
            }
        ]
    },
    {
        "Issue": "Paediatrica Vol. 33-2/2022",
        "Articles": [
            {
                "Title": "Editorial",
                "Author": "Caroline Schnider, Jean-Cristoph Caubet"
            },
            {
                "Title": "Der prim\u00e4re Immundefekt \u2013 Ein praktischer Leitfaden f\u00fcr den Kinderarzt",
                "Author": "Tiphaine Arlabosse, Katerina Theodoropoulou, Fabio Candotti"
            },
            {
                "Title": "Arzneimittelallergien bei Kindern: was sollten Kinder\u00e4rzte wissen?",
                "Author": "Felicitas Bellutti Enders, Mich\u00e8le Roth, Samuel Roethlisberger"
            },
            {
                "Title": "Orale Immuntherapie bei Nahrungsmittelallergien im Kindesalter",
                "Author": "Yannick Perrin, Caroline Roduit"
            },
            {
                "Title": "Autoimmunit\u00e4t in der P\u00e4diatrie: \u00dcberlegungen der p\u00e4diatrischen Rheumatologie",
                "Author": "Florence A. Aeschlimann, Raffaella Carlomagno"
```

However, if possible I'd like to avoid using a custom Python statement or function for each individual crawler, as each would require different code. Each crawler has it's own JSON config file which specifies the start URL, allowed URL patterns, desired content to download, etc. 

My initial idea was to create a JSON config to specify the Beautiful Soup elements to scrape and store in a dictionary - something that a colleague who does not write code would be able to set up. My idea was something like this...

```
{
    "name": "Paedriactia",
    "unit": {
        "selector": {
            "name": "div",
            "attrs": {"class": "section__inner"},
            "find_all": true
        }, 
        "items": {
            "issue": {
                "name": "p", "attrs": {"class": "section__spitzmarke"}, "get_text": true
            } 
        }, 
        "subunits": {
            "articles": {
                "selector": {
                    "name": "article",
                    "find_all": true
                },
                "items": {
                    "Title": {
                        "name": "h3",
                        "attrs": {"class": "teaser__title"},
                        "get_text": true
                    }
                }
            }
        }
    }
}
```

...along with a Python function that would be able to parse the HTML according to the config and produce a JSON output. 

However, I'm at a total loss as to how to do this, especially when it comes to handling nested elements. Each time I've tried to approach this on my own I've totally confused myself and have ended up back at the start.

If any of this makese sense, would anyone have any advice or idea of how to approach this sort of Beautiful Soup config?

I'm also fairly proficient in writing code with Beautiful Soup, so I'm open to the idea of writing custom Beautiful Soup functions and statements for each crawler (and perhaps even training others to do the same). If I take this route, where would be the best place to store all of that custom code and import it? Would I be able to have some sort of "parse.py" file in each crawler folder and import its function only as needed (I.e., when that specific crawler is run?)

If helpful, an example of the current structure of the web crawler projects is below:

[![enter image description here][1]][1]


  [1]: https://i.sstatic.net/7QwZX.png
