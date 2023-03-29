---
title: "How to get text in BS and add a tag around it"
site: stackoverflow
question_id: 75879570
url: https://stackoverflow.com/q/75879570
asked: 2023-03-29T16:00:22Z
asked_by: "KWunsch"
asked_by_url: https://stackoverflow.com/users/15513340
last_edited: 2023-03-29T17:30:32Z
tags: [beautifulsoup]
score: 0
views_at_snapshot: 160
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 96542edc90e1b907e6bf666370ad60cd919ccb4ac50c2753dee1978b480e5f93
---

# How to get text in BS and add a tag around it

Asked by [KWunsch](https://stackoverflow.com/users/15513340) on Stack Overflow, <https://stackoverflow.com/q/75879570>, 2023-03-29, last edited 2023-03-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have an XML-snippet that looks a little bit like this: 

        <p> 
        lorem ipsum dolor <hi>a</hi>met. 
        Thing_A, <thing>Thing_B</thing>, Thing_C 
        </p>

The final structure should look sth. like this: 

    <p> lorem ipsum dolor <hi>a</met>. 
    <thing>Thing_A</thing>, <thing>Thing_B</thing>, <thing>Thing_C</thing>
    </p>

I figured I'll create a list like this 

    things = ['Thing_A', 'Thing_B', 'Thing_C']
and search for all things and surround them with a tag. 
However, I couldn't find any info on doing that in the documentation. So I am searching for help :-D 

Here is my code so far: 

    text = things[0]
    print(text)
    stelle = soup.find(text)
    print(stelle)
    tag = soup.new_tag('rs')
    tag.append(text)
    print(tag)

----
 the output is: 

Thing_A
None
<rs>Thing_A</rs>

I have played around a lot and not found a working solution ... 

The output for my solution that is linked in comments with the weird <body>-tag

        <body><tei xml:id="pa029" xmlns="http://www.tei-c.org/ns/1.0">
        <teiheader>
    <!-- The TEI-header from before-->
        </teiheader>
        <!--  <standOff/>-->
        <text>
        <pb n="29v"></pb>
        <p>
     {some content}
    </p>
    </text>
    </tei>
    </body>

when the correct way would be `<text><body>{some content} </body></text></tei>`

Has anyone any hints for me? 
all the best, 
K
