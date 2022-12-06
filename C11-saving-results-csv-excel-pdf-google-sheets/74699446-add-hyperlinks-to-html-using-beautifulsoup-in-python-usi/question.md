---
title: "Add Hyperlinks to HTML using BeautifulSoup in Python using Anchor Text and URL stored in a CSV File"
site: stackoverflow
question_id: 74699446
url: https://stackoverflow.com/q/74699446
asked: 2022-12-06T08:33:52Z
asked_by: "Abhishek R"
asked_by_url: https://stackoverflow.com/users/5576536
last_edited: 2022-12-30T07:59:36Z
tags: [python, html, beautifulsoup]
score: 0
views_at_snapshot: 149
answer_count: 1
accepted_answer_id: 74722905
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5417117b4ec9a113acc5dbe82b36e8574275d50c2357c8cf1767a7acfd42907c
---

# Add Hyperlinks to HTML using BeautifulSoup in Python using Anchor Text and URL stored in a CSV File

Asked by [Abhishek R](https://stackoverflow.com/users/5576536) on Stack Overflow, <https://stackoverflow.com/q/74699446>, 2022-12-06, last edited 2022-12-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to write a program in python beautiful soup to hyperlink words in html using the csv file with anchor_text and hyperlink

The CSV file that has 2 columns:

| anchor_text | hyperlink |
| -------- | -------------- |
| Google    | https://www.google.com            |
| Bing   | https://bing.com            |
| Yahoo   | https://yahoo.com            |
| Active Campaign | https://activecampaign.com            |



Here is sample HTML

    <!-- wp:paragraph -->
    <p>This is a existing link <a class="test" href="https://yahoo.com/">Yahoo</a> Text</p>
    <!-- /wp:paragraph -->
    
    <!-- wp:paragraph -->
    <p>This is another Google Text</p>
    <!-- /wp:paragraph -->

    <!-- wp:paragraph -->
    <p>This is another lowercase bing Text</p>
    <!-- /wp:paragraph -->

    <!-- wp:paragraph -->
    <p>This is another multi word Active Campaign Text</p>
    <!-- /wp:paragraph -->

I want the output to be 


    <!-- wp:paragraph -->
    <p>This is a existing link <a href="https://yahoo.com/">Yahoo</a> Text</p>
    <!-- /wp:paragraph -->
    
    <!-- wp:paragraph -->
    <p>This is another <a href="https://www.google.com/">Google</a> Text</p>
    <!-- /wp:paragraph -->

    <!-- wp:paragraph -->
    <p>This is another lowercase <a href="https://bing.com/">bing</a> Text</p>
    <!-- /wp:paragraph -->

    <!-- wp:paragraph -->
    <p>This is another multi word <a href="https://activecampaign.com/">Active Campaign</a> Text</p>
    <!-- /wp:paragraph -->

Any help is appreciated
