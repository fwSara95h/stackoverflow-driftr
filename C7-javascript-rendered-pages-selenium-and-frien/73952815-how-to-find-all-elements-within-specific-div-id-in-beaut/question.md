---
title: "How to find all elements within specific div ID in Beautiful Soup and Selenium"
site: stackoverflow
question_id: 73952815
url: https://stackoverflow.com/q/73952815
asked: 2022-10-04T19:32:41Z
asked_by: "Emilio Conde"
asked_by_url: https://stackoverflow.com/users/19064016
last_edited: never
tags: [javascript, html, selenium, beautifulsoup, linkedin-api]
score: 1
views_at_snapshot: 315
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f7f13ba5b83603e9b11e1b42b2b48fef9a71bfbf0165909c98d00af2347a3383
---

# How to find all elements within specific div ID in Beautiful Soup and Selenium

Asked by [Emilio Conde](https://stackoverflow.com/users/19064016) on Stack Overflow, <https://stackoverflow.com/q/73952815>, 2022-10-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Hey everyone I'm trying to scrape linkedin info. I've got this source code. My problem is I know how to get the info with the section ID, however this ID changes on every page refresh


<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-html -->

    <section id="ember443" class="artdeco-card ember-view relative break-words pb3 mt2 " tabindex="-1"><!---->

        <div id="experience" class="pv-profile-card-anchor"></div>
                <!---->

                <div class="pvs-list__outer-container">
    <!---->    <ul class="pvs-list
            ph5 display-flex flex-row flex-wrap
            ">
            <li class="artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column">
                    <!----><div class="pvs-entity
        pvs-entity--padded pvs-list__item--no-padding-when-nested
        
        ">
      <div>
            <a data-field="experience_company_logo" class="optional-action-target-wrapper 
            display-flex" target="_self" href="https://www.linkedin.com/company/22316561/">
            <div class="ivm-image-view-model  pvs-entity__image ">
        <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">

    </div>
      </div>
        </a>

      </div>

      <div class="display-flex flex-column full-width align-self-center">
        <div class="display-flex flex-row justify-space-between">
            <div class="
              display-flex flex-column full-width">
        
            <div class="display-flex align-items-center">
                <span class="mr1 t-bold">
                  <span aria-hidden="true"><!---->CEO &amp; Founder<!----></span><span class="visually-hidden"><!---->CEO &amp; Founder<!----></span>
                </span>
    <!----><!----><!---->        </div>
              <span class="t-14 t-normal">
                <span aria-hidden="true"><!---->Runa<!----></span><span class="visually-hidden"><!---->Runa<!----></span>
              </span>
              <span class="t-14 t-normal t-black--light">
                <span aria-hidden="true"><!---->Jan 2018 - Present · 4 yrs 10 mos<!----></span><span class="visually-hidden"><!---->Jan 2018 - Present · 4 yrs 10 mos<!----></span>
              </span>
              <span class="t-14 t-normal t-black--light">
                <span aria-hidden="true"><!---->Mexico City Area, Mexico<!----></span><span class="visually-hidden"><!---->Mexico City Area, Mexico<!----></span>
              </span>
          
      

<!-- end snippet -->

I've achieved to get all the sections with this class with: 

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-html -->

    experiences = soup.find_all("section", {"class": "artdeco-card ember-view relative break-words pb3 mt2"})

<!-- end snippet -->

However I need the text within the div id "experience" section. I've tried with: 

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-html -->

    div = soup.find_all(id="experience")

<!-- end snippet -->

But it only gets me that tag and nothing else. Any ideas on how could I get the jobs info within the specific "experience" section? Thank you so much in advance

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Ryan Wilson](https://stackoverflow.com/users/4830196)** (2022-10-04): Perhaps this will help: [beautifulsoup-innerhtml](https://stackoverflow.com/questions/8112922/beautifulsoup-innerhtml)
