---
title: "Webscrapping with bs4: Type Error - 'NoneType' object is not subscriptable"
site: stackoverflow
question_id: 73913131
answer_id: 73913602
url: https://stackoverflow.com/a/73913602
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-30T20:18:52Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73913602/revisions
accepted: true
score: 0
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e0dc4e3eea1cda692e2d41df1290ab91862c0bf6088d273d541be07e51f8b724
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73913602>, 2022-09-30; **accepted**; score 0. Text as retrieved 2026-10-12.

You're probably getting the error on the `video_url = video_tag.find("a")['href']` line, since I cannot see any other place where you're indexing, which is what can [cause this error][1]. So, the error would happen because `video_tag.find("a")` returns `None`. You should wrap it for some error handling like:

    for video_tag in video_tags:
        video_hl = video_tag.find("a")
        if video_hl is None:
            print("No hyperlinks found inside the video tag", video_tag.attrs)
            continue
        video_url = video_hl['href']
        print(video_url)

(Printing the `video_tag.attrs` can help you `find` or `select` that `video` element for further inspection.)

[Actually, I can't get to that line when I run your code because I get *Total 0 videos found* so the for-loop never runs; but when I open and inspect the plex link you're using, the only `video` tag I can find is the "Watch Now" button (which does not get scraped when I run your code, for some reason), and that does not have any `a` tags in it - nor do any of the several other videos I inspected on the plex site.] 

If you're trying to get the video source link rather that hyperlinks that [will show up when a browser doesn't support HTML video][2], you can get the `src` attribute with `video_src = video_tag.get('src')`


  [1]: https://itsmycode.com/python-typeerror-nonetype-object-is-not-subscriptable/#:~:text=Conclusion-,The%20TypeError%3A%20'%20NoneType'%20object%20is%20not%20subscriptable%20error%20is,lists%2C%20dictionaries%2C%20and%20tuples.
  [2]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video#usage_notes
