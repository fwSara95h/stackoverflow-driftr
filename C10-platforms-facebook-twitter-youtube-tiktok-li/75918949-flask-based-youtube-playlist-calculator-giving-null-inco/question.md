---
title: "Flask-based youtube playlist calculator giving null/incorrect output"
site: stackoverflow
question_id: 75918949
url: https://stackoverflow.com/q/75918949
asked: 2023-04-03T11:25:54Z
asked_by: "DevOpsnoob"
asked_by_url: https://stackoverflow.com/users/16619969
last_edited: never
tags: [python, flask, beautifulsoup]
score: 0
views_at_snapshot: 81
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: be31743cf06c924565ad00ef4f38ff0929ff17027c87ad3b08fc039723d04dc1
---

# Flask-based youtube playlist calculator giving null/incorrect output

Asked by [DevOpsnoob](https://stackoverflow.com/users/16619969) on Stack Overflow, <https://stackoverflow.com/q/75918949>, 2023-04-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So, I'm creating a youtube playlist calculator whicxh takes the playlist URl as input from the user, this web-app is wtritten in Flask framework.
Code:

    from flask import Flask, render_template, request
    import re
    import requests
    from bs4 import BeautifulSoup

    app = Flask(__name__)

    def calculate_playlist_length(playlist_url):
      html = requests.get(playlist_url).text
      soup = BeautifulSoup(html, 'html.parser')
      total_seconds = 0

      for span in soup.select('span.ytd-thumbnail-overlay-time-status-renderer'):
          match = re.search(r'(\d+):(\d+)', span.text.strip())
          if match:
             minutes, seconds = match.groups()
             total_seconds += int(minutes) * 60 + int(seconds)

       hours = total_seconds // 3600
       minutes = (total_seconds % 3600) // 60
       seconds = total_seconds % 60

       return hours, minutes, seconds

    @app.route('/', methods=['GET', 'POST'])
    def index():
       if request.method == 'POST':
          playlist_url = request.form['playlist_url']
          hours, minutes, seconds = calculate_playlist_length(playlist_url)
          return render_template('result.html', hours=hours, minutes=minutes, 
            seconds=seconds)

        return render_template('index.html')

    if __name__ == '__main__':
         app.run(debug=True)



But on running the app, which compiles succesfully and input a valid and public playlist. I get this output: 

    The total length of the playlist is 0:00:00.

How do I fix this? I have tried multiple URLs but the outuput is same. Also furthur down the line, I want to host this project on GCP and use YouTube APIs. So please guide me for that too.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[baduker](https://stackoverflow.com/users/6106791)** (2023-04-03): Does this answer your question? [How do I get video durations with YouTube API version 3?](https://stackoverflow.com/questions/15596753/how-do-i-get-video-durations-with-youtube-api-version-3)
