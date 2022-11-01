---
title: "Payload to scrape data not working anymore"
site: stackoverflow
question_id: 74280152
url: https://stackoverflow.com/q/74280152
asked: 2022-11-01T18:15:30Z
asked_by: "ablam"
asked_by_url: https://stackoverflow.com/users/11981271
last_edited: never
tags: [python, json, beautifulsoup, screen-scraping, payload]
score: 0
views_at_snapshot: 208
answer_count: 1
accepted_answer_id: 74280997
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3326d1c107508ac926ff9b7f193a40ca28086de58963693ad59ed0ef788b11b7
---

# Payload to scrape data not working anymore

Asked by [ablam](https://stackoverflow.com/users/11981271) on Stack Overflow, <https://stackoverflow.com/q/74280152>, 2022-11-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm creating a list called `id` by scraping from the url below, but the payload I use to extract (which I've used successfully before) is not responsive. I get `JSONDecodeError: Expecting value: line 1 column 1 (char 0)` in response to `data = requests.post(url, json=payload).json()`. 

I'm not familiar with the issue: if it's an IP block from my side (upon passing a limit since I've scraped from this website many times before) or a payload expiration (although it hasn't changed in the developer tools).

I'm not sure what is going on and if someone may provide contextual understanding or perhaps mitigation so I can check for these. 

```
# Accessing data from external URL 
url = "https://www.printables.com/graphql/"

# Payload
payload = {
  "operationName": "PrintList",
  "query": "query PrintList($limit: Int!, $cursor: String, $categoryId: ID, $materialIds: [Int], $userId: ID, $printerIds: [Int], $licenses: [ID], $ordering: String, $hasModel: Boolean, $filesType: [FilterPrintFilesTypeEnum], $includeUserGcodes: Boolean, $nozzleDiameters: [Float], $weight: IntervalObject, $printDuration: IntervalObject, $publishedDateLimitDays: Int, $featured: Boolean, $featuredNow: Boolean, $usedMaterial: IntervalObject, $hasMake: Boolean, $competitionAwarded: Boolean, $onlyFollowing: Boolean, $collectedByMe: Boolean, $madeByMe: Boolean, $likedByMe: Boolean) {\n  morePrints(\n    limit: $limit\n    cursor: $cursor\n    categoryId: $categoryId\n    materialIds: $materialIds\n    printerIds: $printerIds\n    licenses: $licenses\n    userId: $userId\n    ordering: $ordering\n    hasModel: $hasModel\n    filesType: $filesType\n    nozzleDiameters: $nozzleDiameters\n    includeUserGcodes: $includeUserGcodes\n    weight: $weight\n    printDuration: $printDuration\n    publishedDateLimitDays: $publishedDateLimitDays\n    featured: $featured\n    featuredNow: $featuredNow\n    usedMaterial: $usedMaterial\n    hasMake: $hasMake\n    onlyFollowing: $onlyFollowing\n    competitionAwarded: $competitionAwarded\n    collectedByMe: $collectedByMe\n    madeByMe: $madeByMe\n    liked: $likedByMe\n  ) {\n    cursor\n    items {\n      ...PrintListFragment\n      printer {\n        id\n        __typename\n      }\n      user {\n        rating\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PrintListFragment on PrintType {\n  id\n  name\n  slug\n  ratingAvg\n  likesCount\n  liked\n  datePublished\n  dateFeatured\n  firstPublish\n  userGcodeCount\n  downloadCount\n  category {\n    id\n    path {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  modified\n  images {\n    ...ImageSimpleFragment\n    __typename\n  }\n  filesType\n  hasModel\n  nsfw\n  user {\n    ...AvatarUserFragment\n    __typename\n  }\n  ...LatestCompetitionResult\n  __typename\n}\n\nfragment AvatarUserFragment on UserType {\n  id\n  publicUsername\n  avatarFilePath\n  slug\n  badgesProfileLevel {\n    profileLevel\n    __typename\n  }\n  __typename\n}\n\nfragment LatestCompetitionResult on PrintType {\n  latestCompetitionResult {\n    placement\n    competitionId\n    __typename\n  }\n  __typename\n}\n\nfragment ImageSimpleFragment on PrintImageType {\n  id\n  filePath\n  rotation\n  __typename\n}\n",
  "variables": {
      "categoryId": None, 
      "collectedByMe": False,
      "competitionAwarded": False,
      "cursor": None,
      "featured": False,
      "filesType": ["GCODE"],
      "hasMake": False,
      "includeUserGcodes": True,
      "likedByMe": False,
      "limit": 36,
      "madeByMe": False,
      "materialIds": None,
      "nozzleDiameters": None,
      "ordering": "-likes_count_7_days",
      "printDuration": None,
      "printerIds": None,
      "publishedDateLimitDays": None,
      "weight": None,
      },
}

cnt = 0
id = []

while True:
    data = requests.post(url, json=payload).json()

    # Print all data
    # print(json.dumps(data, indent=4))

    for i in data["data"]["morePrints"]["items"]:
        cnt += 1
        id.append(i["id"])

    if not data["data"]["morePrints"]["cursor"]:
        break

    payload["variables"]["cursor"] = data["data"]["morePrints"]["cursor"]

ID = [int(x) for x in id]
```
