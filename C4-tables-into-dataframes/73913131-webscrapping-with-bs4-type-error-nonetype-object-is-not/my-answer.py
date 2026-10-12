# Code from my Stack Overflow answer https://stackoverflow.com/a/73913602 (posted 2022-09-30), extracted verbatim; may need the question's context to run.
for video_tag in video_tags:
    video_hl = video_tag.find("a")
    if video_hl is None:
        print("No hyperlinks found inside the video tag", video_tag.attrs)
        continue
    video_url = video_hl['href']
    print(video_url)
