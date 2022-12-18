---
title: "Is there a way to loop through an xml file and change tags to make them unique?"
site: stackoverflow
question_id: 74844588
url: https://stackoverflow.com/q/74844588
asked: 2022-12-18T21:35:56Z
asked_by: "PickleRick"
asked_by_url: https://stackoverflow.com/users/18696224
last_edited: never
tags: [python, xml, beautifulsoup]
score: 0
views_at_snapshot: 132
answer_count: 2
accepted_answer_id: 74845261
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4613c6757366b3abfe7c6fd8bc4403032cacc58e979d3bdd3269ea6768eb4e66
---

# Is there a way to loop through an xml file and change tags to make them unique?

Asked by [PickleRick](https://stackoverflow.com/users/18696224) on Stack Overflow, <https://stackoverflow.com/q/74844588>, 2022-12-18. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

In my XML file \[studentinfo.xml\] is there a way to modify my loop. The current one that I have [see below] works but not to my liking. What happens is that when it loops through the file to make the specified tag/tags unique it stops at 0 [see current issue]. It is important that the loop starts over at the end of each Student Screening [ <stu:StudentScreening>] and once it gets to the last student screening the loop should stop. 

There will be multiple tags that will need to be unique, which is why my code [see below] is setup like that. What am I doing wrong and what is the fix? [open to any and all options]

**note: the file is very large

#The Issue:

```
<?xml version="1.0" encoding="UTF-8"?>
<stu:StudentBreakdown>
<stu:Studentdata>
    <stu:StudentScreening>
        <st:adminid>123321</st:adminid>
        <st:namelists>
          **<sti:name0>Sam Davies</sti:name0>**
        </st:namelists>
        <st:age>15</st:age>
        <st:hair>Black</st:hair>
        <st:eyes>Blue</st:eyes>
        <st:grade>10</st:grade>
        <st:teacher>Draco Malfoy</st:teacher>
        <st:dorm>Innovation Hall</st:dorm>
        <st:namelists>
          **<sti:name0>Master Splinter</sti:name0>
          <sti:name0>Peter Griffin</sti:name0>
          <sti:name0>Louis Griffin</sti:name0>**
        </st:namelists>
        <st:status>Full Time</st:status>
        <st:description>
            <ie:gender>Male</ie:gender>
            <ie:height>6'1</ie:height>
            <ie:weight>185</ie:weight>
        </st:description>
        <st:department>
            <dep:departmentid>IDEPT12</dep:departmentid>
            <dep:departmentname>Aerospace Engineering</dep:departmentname>
        </st:department>
        <st:DateofBirth>
            <ie:month>Mar</ie:month>
            <ie:day>05</ie:day>
            <ie:year>2007</ie:year>
        </st:DateofBirth>
        <st:Roommate>
          <st:namelists>
            **<sti:name0>Tony Tiger</sti:name0>**
          </st:namelists>
        </st:Roommate>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:adminid>456654</st:adminid>
        <st:namelists>
          <sti:name0>Cassie Stone</sti:name0>
        </st:namelists>
        <st:age>14</st:age>
        <st:hair>Brown</st:hair>
        <st:grade>9</st:grade>
        <st:teacher>Luna Lovegood</st:teacher>
        <st:namelists>
          <sti:name0>Kelly Clarkson</sti:name0>
          <sti:name0>Stewie Griffin</sti:name0>
        </st:namelists>
        <st:status>Full Time</st:status>
        <st:description>
            <ie:gender>Female</ie:gender>
            <ie:height>5'5</ie:height>
            <ie:weight>150</ie:weight>
        </st:description>
        <st:department>
            <dep:departmentid>IDEPT24</dep:departmentid>
            <dep:departmentname>Earth Sciences</dep:departmentname>
        </st:department>
        <st:DateofBirth>
            <ie:month>Apr</ie:month>
            <ie:day>24</ie:day>
            <ie:year>2006</ie:year>
        </st:DateofBirth>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:adminid>789987</st:adminid>
        <st:namelists>
          <sti:name0>Derek Brandon</sti:name0>
        </st:namelists>
        <st:age>17</st:age>
        <st:eyes>green</st:eyes>
        <st:teacher>Ron Weasley</st:teacher>
        <st:dorm>Hogtie Manor</st:dorm>
        <st:namelists>
          <sti:name0>Miley Cyrus</sti:name0>
        </st:namelists>
        <st:status>Full Time</st:status>
        <st:description>
            <ie:gender>Male</ie:gender>
            <ie:height>6'5</ie:height>
            <ie:weight>198</ie:weight>
        </st:description>
        <st:department>
            <dep:departmentid>IDEPT16</dep:departmentid>
            <dep:departmentname>Mechanical Engineering</dep:departmentname>
        </st:department>
        <st:DateofBirth>
            <ie:month>Jan</ie:month>
            <ie:day>10</ie:day>
            <ie:year>2005</ie:year>
        </st:DateofBirth>
    </stu:StudentScreening>
</stu:Studentdata>
</stu:StudentBreakdown>

```

Each tag should be unique for each Student Screening [stu:StudentScreening] and I want to make them unique by adding a number on the end.

#Desired output:

```
<?xml version="1.0" encoding="UTF-8"?>
<stu:StudentBreakdown>
<stu:Studentdata>
    <stu:StudentScreening>
        <st:adminid>123321</st:adminid>
        <st:namelists>
          <sti:name0>Sam Davies</sti:name0>
        </st:namelists>
        <st:age>15</st:age>
        <st:hair>Black</st:hair>
        <st:eyes>Blue</st:eyes>
        <st:grade>10</st:grade>
        <st:teacher>Draco Malfoy</st:teacher>
        <st:dorm>Innovation Hall</st:dorm>
        <st:namelists>
          <sti:name1>Master Splinter</sti:name1>
          <sti:name2>Peter Griffin</sti:name2>
          <sti:name3>Louis Griffin</sti:name3>
        </st:namelists>
        <st:status>Full Time</st:status>
        <st:description>
            <ie:gender>Male</ie:gender>
            <ie:height>6'1</ie:height>
            <ie:weight>185</ie:weight>
        </st:description>
        <st:department>
            <dep:departmentid>IDEPT12</dep:departmentid>
            <dep:departmentname>Aerospace Engineering</dep:departmentname>
        </st:department>
        <st:DateofBirth>
            <ie:month>Mar</ie:month>
            <ie:day>05</ie:day>
            <ie:year>2007</ie:year>
        </st:DateofBirth>
        <st:Roommate>
          <st:namelists>
            <sti:name4>Tony Tiger</sti:name4>
          </st:namelists>
        </st:Roommate>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:adminid>456654</st:adminid>
        <st:namelists>
          <sti:name0>Cassie Stone</sti:name0>
        </st:namelists>
        <st:age>14</st:age>
        <st:hair>Brown</st:hair>
        <st:grade>9</st:grade>
        <st:teacher>Luna Lovegood</st:teacher>
        <st:namelists>
          <sti:name1>Kelly Clarkson</sti:name1>
          <sti:name2>Stewie Griffin</sti:name2>
        </st:namelists>
        <st:status>Full Time</st:status>
        <st:description>
            <ie:gender>Female</ie:gender>
            <ie:height>5'5</ie:height>
            <ie:weight>150</ie:weight>
        </st:description>
        <st:department>
            <dep:departmentid>IDEPT24</dep:departmentid>
            <dep:departmentname>Earth Sciences</dep:departmentname>
        </st:department>
        <st:DateofBirth>
            <ie:month>Apr</ie:month>
            <ie:day>24</ie:day>
            <ie:year>2006</ie:year>
        </st:DateofBirth>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:adminid>789987</st:adminid>
        <st:namelists>
          <sti:name0>Derek Brandon</sti:name0>
        </st:namelists>
        <st:age>17</st:age>
        <st:eyes>green</st:eyes>
        <st:teacher>Ron Weasley</st:teacher>
        <st:dorm>Hogtie Manor</st:dorm>
        <st:namelists>
          <sti:name1>Miley Cyrus</sti:name1>
        </st:namelists>
        <st:status>Full Time</st:status>
        <st:description>
            <ie:gender>Male</ie:gender>
            <ie:height>6'5</ie:height>
            <ie:weight>198</ie:weight>
        </st:description>
        <st:department>
            <dep:departmentid>IDEPT16</dep:departmentid>
            <dep:departmentname>Mechanical Engineering</dep:departmentname>
        </st:department>
        <st:DateofBirth>
            <ie:month>Jan</ie:month>
            <ie:day>10</ie:day>
            <ie:year>2005</ie:year>
        </st:DateofBirth>
    </stu:StudentScreening>
</stu:Studentdata>
</stu:StudentBreakdown>
``` 

#Current xml file:

```
<?xml version="1.0" encoding="UTF-8"?>
<stu:StudentBreakdown>
<stu:Studentdata>
    <stu:StudentScreening>
        <st:adminid>123321</st:adminid>
        <st:namelists>
          <sti:name>Sam Davies</sti:name>
        </st:namelists>
        <st:age>15</st:age>
        <st:hair>Black</st:hair>
        <st:eyes>Blue</st:eyes>
        <st:grade>10</st:grade>
        <st:teacher>Draco Malfoy</st:teacher>
        <st:dorm>Innovation Hall</st:dorm>
        <st:namelists>
          <sti:name>Master Splinter</sti:name>
          <sti:name>Peter Griffin</sti:name>
          <sti:name>Louis Griffin</sti:name>
        </st:namelists>
        <st:status>Full Time</st:status>
        <st:description>
            <ie:gender>Male</ie:gender>
            <ie:height>6'1</ie:height>
            <ie:weight>185</ie:weight>
        </st:description>
        <st:department>
            <dep:departmentid>IDEPT12</dep:departmentid>
            <dep:departmentname>Aerospace Engineering</dep:departmentname>
        </st:department>
        <st:DateofBirth>
            <ie:month>Mar</ie:month>
            <ie:day>05</ie:day>
            <ie:year>2007</ie:year>
        </st:DateofBirth>
        <st:Roommate>
          <st:namelists>
            <sti:name>Tony Tiger</sti:name>
          </st:namelists>
        </st:Roommate>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:adminid>456654</st:adminid>
        <st:namelists>
          <sti:name>Cassie Stone</sti:name>
        </st:namelists>
        <st:age>14</st:age>
        <st:hair>Brown</st:hair>
        <st:grade>9</st:grade>
        <st:teacher>Luna Lovegood</st:teacher>
        <st:namelists>
          <sti:name>Kelly Clarkson</sti:name>
          <sti:name>Stewie Griffin</sti:name>
        </st:namelists>
        <st:status>Full Time</st:status>
        <st:description>
            <ie:gender>Female</ie:gender>
            <ie:height>5'5</ie:height>
            <ie:weight>150</ie:weight>
        </st:description>
        <st:department>
            <dep:departmentid>IDEPT24</dep:departmentid>
            <dep:departmentname>Earth Sciences</dep:departmentname>
        </st:department>
        <st:DateofBirth>
            <ie:month>Apr</ie:month>
            <ie:day>24</ie:day>
            <ie:year>2006</ie:year>
        </st:DateofBirth>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:adminid>789987</st:adminid>
        <st:namelists>
          <sti:name>Derek Brandon</sti:name>
        </st:namelists>
        <st:age>17</st:age>
        <st:eyes>green</st:eyes>
        <st:teacher>Ron Weasley</st:teacher>
        <st:dorm>Hogtie Manor</st:dorm>
        <st:namelists>
          <sti:name>Miley Cyrus</sti:name>
        </st:namelists>
        <st:status>Full Time</st:status>
        <st:description>
            <ie:gender>Male</ie:gender>
            <ie:height>6'5</ie:height>
            <ie:weight>198</ie:weight>
        </st:description>
        <st:department>
            <dep:departmentid>IDEPT16</dep:departmentid>
            <dep:departmentname>Mechanical Engineering</dep:departmentname>
        </st:department>
        <st:DateofBirth>
            <ie:month>Jan</ie:month>
            <ie:day>10</ie:day>
            <ie:year>2005</ie:year>
        </st:DateofBirth>
    </stu:StudentScreening>
</stu:Studentdata>
</stu:StudentBreakdown>
```

#Current code: 

```
import pandas as pd
import re
from lxml import etree as Etr
from xml.etree import ElementTree as ET
from xml.parsers import expat
from bs4 import BeautifulSoup
import pandas_read_xml as pdx
 
with open('studentinfo.xml', 'r') as f:
    file = f.read()
soup = BeautifulSoup(file, 'lxml') 
 
enumTags = ['sti:name']
for d in [c for c in soup.descendants if c.name]:
    for name in enumTags:
        for i, t in enumerate(d.find_all(name, recursive=False)):
            t.name = f'{t.name}{i}'
print(soup.prettify)

```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Michael Butscher](https://stackoverflow.com/users/987358)** (2022-12-18): You could iterate over all "stu:StudentScreening" tags (actually the subtrees) and find and modify all "sti:name" tags in each subtree. This would be a lot cleaner than the current approach.
- **[Parfait](https://stackoverflow.com/users/1422451)** (2022-12-18): Your markup is not a well-informed XML. The `stu`, `sti`, `st`, and `ie` namespace prefixes must be defined. W3C compliant libraries like `lxml` should error out upon parsing. Please post actual XML.
- **[Michael Kay](https://stackoverflow.com/users/415448)** (2022-12-18): I wonder why you want to do this? XML with variable element names (like name1, name2, etc) is usually much harder to process than XML with fixed names. Are you sure this transformation is a good idea?
- **[PickleRick](https://stackoverflow.com/users/18696224)** (2022-12-18): @Parfait i don’t care about namespaces. When I run my code it doesn’t error. Is there a way without defining namespaces ?
- **[Parfait](https://stackoverflow.com/users/1422451)** (2022-12-19): Your code shows BeautifulSoup (which is not a full W3C conformant library). You are not directly using `lxml`. Attempting to parse with `lxml` on any of your posted markup, I get: `lxml.etree.XMLSyntaxError: Namespace prefix stu on StudentBreakdown is not defined...`
