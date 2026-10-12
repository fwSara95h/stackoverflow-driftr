# Code from my Stack Overflow answer https://stackoverflow.com/a/75940405 (posted 2023-04-05), extracted verbatim; may need the question's context to run.
def calculate_playlist_length(playlist_url):
    pSoup = BeautifulSoup((r:=requests.get(playlist_url)).content, 'html.parser') 
    rStatus = f'<Response [{r.status_code} {r.reason}]> from {r.url}'

    jScript = pSoup.select_one('script:-soup-contains("var ytInitialData")')
    try: 
        jData = json.loads(jScript.string.split('=',1)[-1].strip().rstrip(';'))

        keysList = [
            'contents', 'twoColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer',
            'content', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer',
            'contents', 0, 'playlistVideoListRenderer', 'contents'
        ]
        for k in keysList: jData = jData[k]
        vidLength = lambda v: int(v['playlistVideoRenderer'].get('lengthSeconds',0))

        total_seconds = sum([vidLength(vid) for vid in jData])
    except Exception as e: total_seconds, _ = 0, print(f'{rStatus}\n{e!r}') 
    return (total_seconds//3600), ((total_seconds%3600)//60), (total_seconds%60)
