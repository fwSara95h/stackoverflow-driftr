---
title: "bs4.element.Tag and split, python"
site: stackoverflow
question_id: 76489877
url: https://stackoverflow.com/q/76489877
asked: 2023-06-16T11:48:33Z
asked_by: "andyrat"
asked_by_url: https://stackoverflow.com/users/22083701
last_edited: 2023-06-16T11:49:38Z
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 86
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e1cbf2e00406b0c3bb177f38a2b13a3c9f41440362be7d016a7cb975af46de36
---

# bs4.element.Tag and split, python

Asked by [andyrat](https://stackoverflow.com/users/22083701) on Stack Overflow, <https://stackoverflow.com/q/76489877>, 2023-06-16, last edited 2023-06-16. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to use the split method, but I'm getting an error. What am I doing wrong, tell me please?

TypeError: 'NoneType' object is not callable

    def get_parsed_page(url, delay=0.5):
        data = solver.request_get(url)
        return BeautifulSoup(data.solution.response, "lxml")

    def get_matches():
        global MATCH_WITH_COUNTDOWN
        matches = get_parsed_page("https://****/matches/")
        matches_list = []
    
        matchdays = matches.find_all("div", {"class": "upcomingMatchesSection"});
        for match in matchdays:
            matchDetails = match.find_all("div", {"class": "upcomingMatch"})
            print(type(match.find({'div': {'class': 'matchDayHeadline'}})))
            date = match.find({'div': {'class': 'matchDayHeadline'}}).split()[-1]

Expected no error. Im trying remove split

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Gedas Miksenas](https://stackoverflow.com/users/9198074)** (2023-06-16): Try: match.find({'div': {'class': 'matchDayHeadline'}}).text.split()[-1]
