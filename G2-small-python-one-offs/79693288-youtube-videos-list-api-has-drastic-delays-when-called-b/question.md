---
title: "YouTube Videos.list API has drastic delays when called by requests.get"
site: stackoverflow
question_id: 79693288
url: https://stackoverflow.com/q/79693288
asked: 2025-07-07T18:34:29Z
asked_by: "openwld"
asked_by_url: https://stackoverflow.com/users/19270168
last_edited: never
tags: [python, youtube, youtube-api, youtube-data-api]
score: 0
views_at_snapshot: 96
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a8441888ddd5d366be146f120466ce288da2162d8a086e25d4938a2a91edd51b
---

# YouTube Videos.list API has drastic delays when called by requests.get

Asked by [openwld](https://stackoverflow.com/users/19270168) on Stack Overflow, <https://stackoverflow.com/q/79693288>, 2025-07-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

```py
def validate_youtube_video(link:str, sessionid:str) -> Tuple[bool, str]:
  # Returns (status, sanitized_link|error_message)
  import urllib.parse
  res = urllib.parse.urlparse(link)
  vidid = None
  if res.netloc == 'www.youtube.com' and res.path == '/watch':
    queries = res.query.split('&')
    for q in queries:
      if q.startswith('v='):
        vidid = q[2:]
  if res.netloc == 'youtu.be':
    vidid = res.path[1:]
  resp = requests.get(f'https://www.googleapis.com/youtube/v3/videos?id={vidid}&part=snippet,contentDetails,status&key=[REDACTED]').json()
  if resp['items'] == []:
    return (False, 'Invalid ID')
  if resp['items'][0]['snippet']['title'] != f'[REDACTED] {sessionid}' or resp['items'][0]['snippet']['description'] != '':
    return (False, 'Invalid title or description')
  if resp['items'][0]['status']['privacyStatus'] != 'unlisted':
    return (False, 'Privacy status is not unlisted')
  return (True, f'https://youtu.be/{vidid}')
```
This code aims to call the YouTube Videos.list API V3 to check if the video has required title, description and privacy status for anonymity. It takes less than 1 second in my browser (with the API key) but takes more than 4 minutes when called using `requests.get`. Does anyone know why?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[LMC](https://stackoverflow.com/users/2834978)** (2025-07-07): Google provides a client for API requests https://developers.google.com/youtube/v3/quickstart/python or use [requests.session](https://stackoverflow.com/a/50910695/2834978)
