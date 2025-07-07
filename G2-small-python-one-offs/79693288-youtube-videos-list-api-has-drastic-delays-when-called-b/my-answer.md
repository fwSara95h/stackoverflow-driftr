---
title: "YouTube Videos.list API has drastic delays when called by requests.get"
site: stackoverflow
question_id: 79693288
answer_id: 79693432
url: https://stackoverflow.com/a/79693432
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2025-07-07T21:32:55Z
last_edited: 2025-07-07T21:42:17Z
revisions: 2
revision_history: https://stackoverflow.com/posts/79693432/revisions
accepted: false
score: 0
chapter: G2
chapter_title: "Small Python one-offs"
cluster: python-misc
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bd9807228b5ffde63385420ccbd20af3c809df6d489da0af7666500a5e119a73
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2025-07-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/79693432>, 2025-07-07, last edited 2025-07-07; score 0. Text as retrieved 2026-10-12.

You should try using the [client API/library](https://developers.google.com/youtube/v3/quickstart/python) provided by google as suggested in [@LMC](https://stackoverflow.com/users/2834978/lmc)'s [comment](https://stackoverflow.com/questions/79693288/youtube-videos-list-api-has-drastic-delays-when-called-by-requests-get#comment140571576_79693288). Requests might be slowed down due to being repeatedly blocked or delayed by lower-level issues (DNS, TLS, retry waits, etc.). Using `requests.Session()` **might** make all requests *after* the first one faster.

---

With the client API, your function might look something like:

```py
from urllib.parse import urlparse, parse_qs
from googleapiclient.discovery import build

# Set up the YouTube API client
API_KEY = "YOUR_API_KEY_HERE" 
youtube = build("youtube", "v3", developerKey=API_KEY)
```

```py
def validate_youtube_video(link: str, sessionid: str):

    # Extract video ID
    res, vidid = urlparse(link), None
    allow_nls = ("www.youtube.com", "youtube.com")
    if res.netloc in allow_nls and res.path == "/watch":
        qs = parse_qs(res.query)
        vidid = qs.get("v", [None])[0]
    elif res.netloc in ("youtu.be",):
        vidid = res.path.lstrip("/")

    if not vidid: return False, "Could not extract video ID"

    # Call the API
    resp = youtube.videos().list(part="snippet,status", id=vidid).execute()

    
    if not (items := resp.get("items", [])): return False, "Invalid ID"
    snip = items[0]["snippet"]
    stat = items[0]["status"]

    # Conditions
    snip_title = f"[REDACTED] {sessionid}"
    if snip.get("title") != snip_title or snip.get("description", "") != "":
        return False, "Invalid title or description"

    if stat.get("privacyStatus") != "unlisted":
        return False, "Privacy status is not unlisted"

    return True, f"https://youtu.be/{vidid}"
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[openwld](https://stackoverflow.com/users/19270168)** (2025-07-08): So I've just tried what you mentioned, and the code now raises `TimeoutError: timed out`.
- **[openwld](https://stackoverflow.com/users/19270168)** (2025-07-08): @openwld The endpoint still works fine in my browser.
- **me** (2025-07-08): @openwld Does the timeout happen at `build` or when calling the yt data api with `youtube.videos().list...`?
- **[openwld](https://stackoverflow.com/users/19270168)** (2025-07-08): When calling the api with `youtube.videos().list`
- **me** (2025-07-09): @openwld weird. are you sure you're not seeing a cached response on your browser? [try clearing cache and trying again on browser...] my only suggestion at this point would be to [monitor network logs](https://support.happyfox.com/kb/article/882-accessing-the-browser-console-and-network-logs/) when testing the API on browser and then replicating that req with [curlconverter](https://curlconverter.com/)
- **[openwld](https://stackoverflow.com/users/19270168)** (2025-07-09): So it works fine when the request is converted to curl (somehow I can't reply to the original comment) and I'm not seeing a cached response on my browser 😭
- **me** (2025-07-09): @openwld [yeah looks like reply-nesting only goes down like 2 levels] anyways, this looks like a network optimization issue (proxy/DNS/firewall) in your Python networking stack, not something I know a lot about unfortunately. You can just continue to use `requests.get` with the params from your network logs but not sure how long the cookies etc will last before you need fresh ones (you can send those params to `build` via the  `http` param too, but `requests.get` may be simpler at this point).
- **me** (2025-07-09): @openwld Also, btw have you checked if your API key has any restrictions regarding HTTP referrers or IP addresses, or any rate-limits based on user-agent/IP address/request origin/etc?
