---
title: "Is there a way to loop through an xml file and change specific tags according to how many times that tag comes up?"
site: stackoverflow
question_id: 74567311
answer_id: 74570024
url: https://stackoverflow.com/a/74570024
author: "Charles Han"
author_url: https://stackoverflow.com/users/11514907
posted: 2022-11-25T08:30:36Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b7d22ce07716d125a4222d85fe002e72b260c47ee7f65989706f219619f65926
role: another answer on the same question, kept as context; not my work
---

# Answer by [Charles Han](https://stackoverflow.com/users/11514907) — 2022-11-25

Posted on Stack Overflow, <https://stackoverflow.com/a/74570024>, 2022-11-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Well, I guess Harry Potter has got his magic.

The key idea is to use [XSLT][1].

Python code using lxml lib,

```Python
import lxml.etree as ET

XSL = '''
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:stu="https://www.example.com/harrypotter" xmlns:st="https://www.example.com/harrypotter">
 <xsl:template match="@*|node()">
    <xsl:copy>
        <xsl:apply-templates select="@*|node()" />
    </xsl:copy>
 </xsl:template>
 <xsl:template match="stu:StudentScreening/st:name">
        <xsl:element name="st:name{count(preceding-sibling::st:name)}"><xsl:apply-templates select="@*|node()" /></xsl:element>
 </xsl:template>
</xsl:stylesheet>
'''

dom = ET.parse('students.xml')
transform = ET.XSLT(ET.fromstring(XSL))
newdom = transform(dom)
print(ET.tostring(newdom))

newdom.write("out.xml", pretty_print=True)
```
Your input xml file named `students.xml`, which must include namespaces,

```XML
<?xml version="1.0" encoding="UTF-8"?>
<stu:StudentBreakdown xmlns:stu="https://www.example.com/harrypotter"  xmlns:st="https://www.example.com/harrypotter">
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
        <st:name>Peter Griffin</st:name>
        <st:name>Louis Griffin</st:name>
    </stu:StudentScreening>
    <stu:StudentScreening>
        <st:name>Cassie Stone</st:name>
        <st:age>14</st:age>
        <st:hair>Science</st:hair>
        <st:grade>9</st:grade>
        <st:teacher>Luna Lovegood</st:teacher>
        <st:name>Kelly Clarkson</st:name>
        <st:name>Stewie Griffin</st:name>
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

Run the Python code, and you should get a file named `out.xml`.


  [1]: https://www.w3schools.com/xml/xsl_intro.asp

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[PickleRick](https://stackoverflow.com/users/18696224)** (2022-11-29): Could you explain the need for the XSL ?
- **[Charles Han](https://stackoverflow.com/users/11514907)** (2022-11-29): XSLT is a language originally designed for transforming XML documents into other XML documents. One of the benefits of XSLT is that all the processing logic is captured inside the XSL template instead of the python code. For your problem, I thought XSLT was a natural solution as you are dealing with XML files, but I guess the other solution also works. You can read more here https://en.wikipedia.org/wiki/XSLT
- **[PickleRick](https://stackoverflow.com/users/18696224)** (2022-11-29): the namespaces were a headache, so originally I chose not to use them. The example.com/harrypotter is made up correct ?
- **[Charles Han](https://stackoverflow.com/users/11514907)** (2022-11-29): Yes, it's made up and just to pass the XML validation. You could remove the namespaces if that's not required. Then remove the namespaces in XSLT as well and it should still work.
