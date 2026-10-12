# Code from my Stack Overflow answer https://stackoverflow.com/a/79693432 (posted 2025-07-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
from urllib.parse import urlparse, parse_qs
from googleapiclient.discovery import build

# Set up the YouTube API client
API_KEY = "YOUR_API_KEY_HERE" 
youtube = build("youtube", "v3", developerKey=API_KEY)

# --- block 2 ---
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
