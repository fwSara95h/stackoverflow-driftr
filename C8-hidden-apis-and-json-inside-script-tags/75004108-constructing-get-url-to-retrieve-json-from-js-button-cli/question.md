---
title: "Constructing GET url to retrieve JSON from JS button click function"
site: stackoverflow
question_id: 75004108
url: https://stackoverflow.com/q/75004108
asked: 2023-01-04T10:30:29Z
asked_by: "Tendekai Muchenje"
asked_by_url: https://stackoverflow.com/users/1029902
last_edited: never
tags: [javascript, python, web-scraping, get]
score: 0
views_at_snapshot: 289
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: aeca774c9a62fb0ab5b327c9ebe4b09fda60989509459fbd204c4e383ece9edc
---

# Constructing GET url to retrieve JSON from JS button click function

Asked by [Tendekai Muchenje](https://stackoverflow.com/users/1029902) on Stack Overflow, <https://stackoverflow.com/q/75004108>, 2023-01-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape this page using requests and BeautifulSoup in Python but the page is in Javascript so I am including both tags for the question. The page is

https://untappd.com/v/southern-cross-kitchen/469603

and others like it, but it has a 'Show More' button. I want to avoid using a headless browser so I went snooping around for the JavaScript behind this to see if I can find a url, get or post request.

After some inspection, this is the button's code:
 

    <a class="yellow button more show-more-section track-click" data-href=":moremenu" data-menu-id="78074484" data-section-id="286735920" data-track="venue" data-venue-id="469603" href="javascript:void(0);">

and it is controlled and redirected by this function:

    $(document).on("click", ".show-more-menu-section", (function() {
            var e = $(this);
            $(e).hide();
            var t = $(this).attr("data-venue-id"),
                a = $(this).attr("data-menu-id"),
                n = $(".section-area .menu-section").length;
            return $(".section-loading").addClass("active"), $.ajax({
                url: "/venue/more_menu_section/" + t + "/" + n,
                type: "GET",
                data: "menu_id=" + a,
                dataType: "json",
                error: function(t) {
                    $(".section-loading").removeClass("active"), $(e).show(), $.notifyBar({
                        html: "Hmm. Something went wrong. Please try again!",
                        delay: 2e3,
                        animationSpeed: "normal"
                    })
                },
                success: function(t) {
                    $(".section-loading").removeClass("active"), "" == t.view ? $(e).hide() : (trackMenuView("viewMoreMenuSection"), t.count >= 15 ? ($(e).show(), $(".section-area").append(t.view)) : $(".section-area").append(t.view), handleNew())
                }
            })

which is contained in https://assets.untappd.com/assets/v3/js/venue/venue.menu.min.js?v=2.7.10

So for the required values in the function, `t`, `a` and `n` are:

    t = 469603
    n = 78074484
    a = 1

I am now trying to construct the url using this `url` part of the function which is:

    url: "/venue/more_menu_section/" + t + "/" + n


Using `https://www.untappd.com` as my base url, I have tried the following urls with no luck:

```/venue/more_menu_section/469603/1?data=%7B%22menu_id%22%3A%2278074484%22%7D```

```/venue/more_menu_section/469603/1?data%3D%7B%22menu_id%22%3A78074484%7D```

```/venue/more_menu_section/469603/1?data=%7B%22menu_id%22%3A78074484%7D```

```/venue/more_menu_section/469603/1?data={"menu_id":78074484}```


As a result, I have not been able to programmatically retrieve the data. I really would want to avoid using webdrivers and headless browsers to simulate clicks so I am guessing this should be possible with a GET request. Creating that url is proving a challenge. 

How can I do create the right url to fetch?
