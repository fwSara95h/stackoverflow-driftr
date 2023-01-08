---
title: "Extract Data from <script> in html"
site: stackoverflow
question_id: 75046158
answer_id: 75050526
url: https://stackoverflow.com/a/75050526
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-08T19:02:54Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75050526/revisions
accepted: true
score: 1
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-json-in-script
helpers_referenced: [findObj_inJS]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5f0825a68be0f064087c5a2ec90a1553bc611fe7eb8d6ffd11da003d35fa3066
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75050526>, 2023-01-08; **accepted**; score 1. Text as retrieved 2026-10-12.

<sup>**Note:** I think selenium would definitely be the better approach for scraping this site. The function below is meant for sites with far more readable JavaScript (where the target information is conveniently packaged in JSON).</sup>

I have a function **[`findObj_inJS`](https://pastebin.com/UVcLniSG)** that uses [`slimit`](https://slimit.readthedocs.io/en/latest/) to parse JavaScript and extract variables and other values. The scripts on this page are not very readable, but if you use the function as below,

```python
jScript = soup.find(lambda s: s.name=='script' and 'window.__NUXT__' in s.text)
jScript = jScript.text if jScript else '0 SCRIPTS CONTAINING "window.__NUXT__"'
jsStr = jScript.replace('class:', 'was_class:').replace('default:', 'was_default:')
jsData = findObj_inJS(jsStr, [
    'info_text', 'info_title', 'search_text', 'date_of_entry',
    'info_bar_items', 'important_info_items', 'main_title', 'second_title'
], findAll=True, jStrict=False)
```

then `jsData` [as JSON] looks like 

```json
{
  "info_text": [
    "בפרויקט יפו בשדרה  .\n\nדירת 4 חדרים מהמגזינים, יפיפייה ומוארת הפונה לגינה פנימית ושקטה.\n\n99 מ\"ר + 12 מ\"ר מרפסת, מטבח חדש ומאובזר, סוויטת הורים מפנקת חניה תת קרקעית ומחסן.\n\nלוקיישן מרהיב מרחק הליכה משוק הפשפשים, הנמל, יפו העתיקה ובקרבת תחנת הרכבת הקלה"
  ],
  "info_title": [
    "על הנכס"
  ],
  "search_text": [
    "דירה דירות למכירה חדרים ב תל אביב יפו , מכללת תל אביב יפו, דקר , חסידי האומות 22 $FurnitureInfo בפרויקט יפו בשדרה  .\n\nדירת 4 חדרים מהמגזינים, יפיפייה ומוארת הפונה לגינה פנימית ושקטה.\n\n99 מ\"ר + 12 מ\"ר מרפסת, מטבח חדש ומאובזר, סוויטת הורים מפנקת חניה תת קרקעית ומחסן.\n\nלוקיישן מרהיב מרחק הליכה משוק הפשפשים, הנמל, יפו העתיקה ובקרבת תחנת הרכבת הקלה. רון (לשלוח ווטסאפ אם לא זמין) דירה 4 $Floor_text $TotalFloor_text $Amudim_text $Furniture_text $PandorDoors_text מיזוג מעלית חניה $Grating_text גישה לנכים אזור תל אביב יפו $Immediate_text ממ\"ד מרפסת מחסן $sunpatio_text ₪ $Meshupatz_text $Porch_text $yehidatdiur_text במצב שמור הצג רחוב הצג מספר בית מזגן תדיראן עם מחיר, עם תמונה, חניה, הצג רק מושבים וקיבוצים, מעלית, מיזוג, מיזוג, ממ\"ד, מרפסת, מחסן, גישה לנכים, מזגן תדיראן, הצג רחוב, הצג מספר בית 4 חדרים | 111 מ״ר | 8 חסידי האומות 22 , מכללת תל אביב יפו, דקר"
  ],
  "date_of_entry": [
    "כניסה גמישה",
    "2022-12-28 00:00:00"
  ],
  "info_bar_items": [
    "[{\n  key: bs,\n  title: cF,\n  label: I,\n  titleWithoutLabel: a$\n},{\n  key: dE,\n  title: \"קומה 8\",\n  label: dD,\n  titleWithoutLabel: aF\n},{\n  key: \"meter\",\n  title: cG,\n  label: ip,\n  titleWithoutLabel: \"111\"\n},{\n  key: \"entrance\",\n  title: iq,\n  label: h,\n  titleWithoutLabel: iq\n}]"
  ],
  "important_info_items": [
    "[{\n  value: cz,\n  key: aR\n},{\n  key: \"רחוב\",\n  value: dC\n},{\n  value: \"8 מתוך 11 \",\n  key: dD\n},{\n  key: \"מ\\\"ר בנוי\",\n  value: \"99\"\n},{\n  value: \"לא צוין\",\n  key: \"מ\\\"ר גינה\"\n},{\n  link_url: \"http:\\u002F\\u002Fhomeprices.yad2.co.il\\u002Fneighborhood\\u002Fתל אביב יפו\\u002Fחסידי האומות-22\",\n  key: \"נתוני השכונה\",\n  value: \"לחץ כאן\"\n}]"
  ],
  "main_title": [
    "דירה למכירה בתל אביב יפו",
    "דירה&nbsp;למכירה&nbsp;בתל אביב יפו"
  ],
  "second_title": [
    "חסידי האומות 22 מכללת תל אביב יפו, דקר",
    "חסידי האומות&nbsp;22&nbsp;מכללת תל אביב יפו, דקר"
  ]
}
```

I can't read Hebrew, but I feel like at least some of the data you want is in there....

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **user19022072 (account no longer exists)** (2023-01-09): I need to scrape more than 10K pages so selenium will be way more slower... You did great job thanks !
- **me** (2023-01-09): @yoavlv12 glad to help! slimit can take a few sec to parse too, so you might want to take a look at the API as well? something like [`requests.get('https://www.yad2.co.il/api/item/ajyw4gne').json()`](https://i.sstatic.net/ekekq.png) - the only issue is that sometimes it gets redirected to a captcha....
- **user19022072 (account no longer exists)** (2023-01-09): Thanks again ! I have already find a way to pass the captcha
- **me** (2023-01-09): @yoavlv12 may I ask how? I'm terrible at getting past any security and this could be useful in the future
