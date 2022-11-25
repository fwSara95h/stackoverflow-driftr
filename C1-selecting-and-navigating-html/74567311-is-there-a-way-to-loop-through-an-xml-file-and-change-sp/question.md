---
title: "Is there a way to loop through an xml file and change specific tags according to how many times that tag comes up?"
site: stackoverflow
question_id: 74567311
url: https://stackoverflow.com/q/74567311
asked: 2022-11-25T00:20:07Z
asked_by: "PickleRick"
asked_by_url: https://stackoverflow.com/users/18696224
last_edited: never
tags: [python, xml, dataframe, beautifulsoup]
score: 1
views_at_snapshot: 97
answer_count: 2
accepted_answer_id: 74570172
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 701057ac76af36006eac1913b07b065243ae1ec859441be5c2038f09a8d9fd7d
---

# Is there a way to loop through an xml file and change specific tags according to how many times that tag comes up?

Asked by [PickleRick](https://stackoverflow.com/users/18696224) on Stack Overflow, <https://stackoverflow.com/q/74567311>, 2022-11-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

In my XML file \[studentinfo.xml\] is there a way to loop through the xml file and change specific tags (and specific child tags) [there will be multiple ones that need to change] and add a number on the end? 

**The file is significantly larger

```
<?xml version="1.0" encoding="UTF-8"?>
<stu:StudentBreakdown>
<stu:Studentdata>
    <stu:StudentScreening>
        <st:name>Sam Davies</st:name>
        <st:age>15</st:age>
        <st:hair>Black</st:hair>
        <st:eyes>Blue</st:eyes>
        <st:grade>10</st:grade>
        <st:teacher>Draco Malfoy</st:teacher>
        <st:dorm>Innovation Hall</st:dorm>
        <st:name>Master Splinter</st:name>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:name>Cassie Stone</st:name>
        <st:age>14</st:age>
        <st:hair>Science</st:hair>
        <st:grade>9</st:grade>
        <st:teacher>Luna Lovegood</st:teacher>
        <st:name>Kelly Clarkson</st:name>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:name>Derek Brandon</st:name>
        <st:age>17</st:age>
        <st:eyes>green</st:eyes>
        <st:teacher>Ron Weasley</st:teacher>
        <st:dorm>Hogtie Manor</st:dorm>
        <st:name>Miley Cyrus</st:name>
    </stu:StudentScreening>
</stu:Studentdata>
</stu:StudentBreakdown>
```

Each tag should be unique for each Student Screening and I want to make them unique by adding a number on the end, see below for desired ouput: 

```
<?xml version="1.0" encoding="UTF-8"?>
<stu:StudentBreakdown>
<stu:Studentdata>
    <stu:StudentScreening>
        <st:name0>Sam Davies</st:name0>
        <st:age>15</st:age>
        <st:hair>Black</st:hair>
        <st:eyes>Blue</st:eyes>
        <st:grade>10</st:grade>
        <st:teacher>Draco Malfoy</st:teacher>
        <st:dorm>Innovation Hall</st:dorm>
        <st:name1>Master Splinter</st:name1>
        <st:name2>Peter Griffin</st:name2>
        <st:name3>Louis Griffin</st:name3>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:name0>Cassie Stone</st:name0>
        <st:age>14</st:age>
        <st:hair>Science</st:hair>
        <st:grade>9</st:grade>
        <st:teacher>Luna Lovegood</st:teacher>
        <st:name1>Kelly Clarkson</st:name1>
        <st:name2>Stewie Griffin</st:name2>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:name0>Derek Brandon</st:name0>
        <st:age>17</st:age>
        <st:eyes>green</st:eyes>
        <st:teacher>Ron Weasley</st:teacher>
        <st:dorm>Hogtie Manor</st:dorm>
        <st:name1>Miley Cyrus</st:name1>
    </stu:StudentScreening>
</stu:Studentdata>
</stu:StudentBreakdown>
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Duniyadnd](https://stackoverflow.com/users/293291)** (2022-11-25): any particular reason you may not want to put an attribute a single time in the `stu:StudentScreening` node? e.g. `<stu:StudentScreening id="123">`
