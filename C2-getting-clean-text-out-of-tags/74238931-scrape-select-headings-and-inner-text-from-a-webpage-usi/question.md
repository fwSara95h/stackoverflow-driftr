---
title: "Scrape select headings and inner text from a webpage using BeautifulSoup?"
site: stackoverflow
question_id: 74238931
url: https://stackoverflow.com/q/74238931
asked: 2022-10-28T17:29:39Z
asked_by: "Outbound"
asked_by_url: https://stackoverflow.com/users/20134661
last_edited: 2022-10-28T19:08:59Z
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 897
answer_count: 1
accepted_answer_id: 74243113
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b6403f9f1af056ee0088742c788b6ca6b63229ed9def73cbff04bbc4116b8194
---

# Scrape select headings and inner text from a webpage using BeautifulSoup?

Asked by [Outbound](https://stackoverflow.com/users/20134661) on Stack Overflow, <https://stackoverflow.com/q/74238931>, 2022-10-28, last edited 2022-10-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Source - a blog post URL

I want to get the inner text of both the Heading tags AND the body copy within that tag into a table output that looks like this

    H2;{H2 tag inner tex}; {p tag(s) inner text}
    H3;{H2 tag inner tex}; {p tag(s) inner text}
    H2;{H2 tag inner tex}; {p tag(s) inner text}
    H3;{H2 tag inner tex}; {p tag(s) inner text}
    H4;{H2 tag inner tex}; {p tag(s) inner text}
    ...

Content of H2, H3, H4 tags are desired
And there might be multiple paragraphs within these tags, so getting them separated by a new line would be awesome. 

Can BeautifulSoup do this?

I can get the innertext of the tags out, but don't know how to get the inner text of p tags out, especially when they are more than one. Or to format this so I can save as a CSV.

    from bs4 import BeautifulSoup
    import requests
    website = requests.get('https://venngage.com/blog/landing-page-examples/')
    preString =  {'h1': '', 'h2': '\t', 'h3':'\t\t', 'h4':'\t\t\t'}
    soup = BeautifulSoup(website.content, 'html.parser')
    tags = soup.find_all(['h1', 'h2', 'h3'])
    for soups in tags:
        preStr = preString[soups.name] if soups.name in preString else ''
        print(preStr+soups.string)
    

Thanks in advance for your help.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[darren](https://stackoverflow.com/users/7318120)** (2022-10-28): yes, you can achieve this (with and without bs4), but what have you tried so far ? the question needs sufficient code for a minimal reproducible example: https://stackoverflow.com/help/minimal-reproducible-example
- **[Outbound](https://stackoverflow.com/users/20134661)** (2022-10-28): Thanks for your reply - Updated my post with what I tried
- **[darren](https://stackoverflow.com/users/7318120)** (2022-10-28): it looks like you are close with this:  `p_tags = soup.find_all(['p'])` would get this.
- **[Outbound](https://stackoverflow.com/users/20134661)** (2022-10-29): Thanks - yeah what I'm struggling with is how to format it in the form of a tabular output as described above
