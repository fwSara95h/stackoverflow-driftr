---
title: "Facebook Post Shares Scrapping"
site: stackoverflow
question_id: 73951098
url: https://stackoverflow.com/q/73951098
asked: 2022-10-04T16:45:50Z
asked_by: "Brahim Darham"
asked_by_url: https://stackoverflow.com/users/20061848
last_edited: 2022-10-05T05:12:58Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, web-scraping, facebook-graph-api]
score: -2
views_at_snapshot: 489
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7e5d5848148a6002ef990053b8820b23067ab708b7a14199c891edde91eeb62e
---

# Facebook Post Shares Scrapping

Asked by [Brahim Darham](https://stackoverflow.com/users/20061848) on Stack Overflow, <https://stackoverflow.com/q/73951098>, 2022-10-04, last edited 2022-10-05 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a script that extract the number of shares of a facebook post.

    
    from facebook_scraper import get_posts
     
    post_df_full=pd.DataFrame()
    
    posts = get_posts(
        "RealMadrid", extra_info=True, pages=3, 
        options={"comments": True, "shared_username": True}
    )
    for post in posts:
        post_entry=post
        fb_post_df=pd.DataFrame.from_dict(post_entry, orient="index")
        fb_post_df=fb_post_df.transpose()
        post_df_full=pd.concat([post_df_full, fb_post_df], axis=0)
    print(post["post_id"]+" get") 

But, I would like to extract the shares of the post: who shared and where he shared?
