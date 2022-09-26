---
title: "Writing csv file - Python-3.x web-scrapping"
site: stackoverflow
question_id: 73858513
url: https://stackoverflow.com/q/73858513
asked: 2022-09-26T18:36:04Z
asked_by: "user19914532"
asked_by_url: (account no longer exists)
last_edited: never
tags: [python, python-3.x, web-scraping]
score: 0
views_at_snapshot: 200
answer_count: 3
accepted_answer_id: 73863336
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 67364ff8e0f645b7273c298a03b7d066dbb52e26ee7d6ec16efc0bfc334aafa4
---

# Writing csv file - Python-3.x web-scrapping

Asked by user19914532 (account no longer exists) on Stack Overflow, <https://stackoverflow.com/q/73858513>, 2022-09-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm working on web scrapping and while writing data to a csv file using following code:

    path = Path.cwd() / "data.csv"
    with path.open(mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for line in lists:
            title = line.find('a', class_='listing-search-item__link--title').text.replace('\n', '')
            writer.writerow(title)
    with path.open(mode='r', encoding='utf-8', newline='') as read_file:
        read = csv.reader(read_file)
        for line in read:
            print(line)
There are some extra spaces in file, I'm unable to avoid.
While printing data from file I'm getting the output:

    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', 'p', 'a', 'r', 't', 'm', 'e', 'n', 't', ' ', 'T', 'u', 'i', 'n', 'l', 'a', 'a', 'n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', 'p', 'a', 'r', 't', 'm', 'e', 'n', 't', ' ', 'B', 'u', 'r', 'g', 'e', 'm', 'e', 'e', 's', 't', 'e', 'r', ' ', 'V', 'a', 'n', ' ', 'H', 'a', 'a', 'r', 'e', 'n', 'l', 'a', 'a', 'n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', 'p', 'a', 'r', 't', 'm', 'e', 'n', 't', ' ', 'B', 'r', 'o', 'e', 'r', 's', 'v', 'e', 's', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', 'p', 'a', 'r', 't', 'm', 'e', 'n', 't', ' ', "'", 's', '-', 'G', 'r', 'a', 'v', 'e', 'l', 'a', 'n', 'd', 's', 'e', 'w', 'e', 'g', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2022-09-26): And what would be the url you are trying to scrape?
- **me** (2022-09-26): What do you want to do? just removing or even trimming away the empty spaces is simple enough. Are you trying to achieve something else?
- **user19914532 (account no longer exists)** (2022-09-27): @BarrythePlatipus `url = "https://www.pararius.com/apartments/schiedam"` This is url and I want only the title names for that.
- **user19914532 (account no longer exists)** (2022-09-27): @Driftr95 nothing else, just to trim these spaces, I want the actual text only that title names only. 'Apartment ruinlaan' for the first line and so on.
