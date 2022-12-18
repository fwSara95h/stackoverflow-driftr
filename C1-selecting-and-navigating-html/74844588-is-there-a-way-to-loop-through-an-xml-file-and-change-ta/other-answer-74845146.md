---
title: "Is there a way to loop through an xml file and change tags to make them unique?"
site: stackoverflow
question_id: 74844588
answer_id: 74845146
url: https://stackoverflow.com/a/74845146
author: "Michael Kay"
author_url: https://stackoverflow.com/users/415448
posted: 2022-12-18T23:43:21Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 67c35934dbc17fdbc06414e926053d1b7ba325c9d0289b515d2e0a841f930277
role: another answer on the same question, kept as context; not my work
---

# Answer by [Michael Kay](https://stackoverflow.com/users/415448) — 2022-12-18

Posted on Stack Overflow, <https://stackoverflow.com/a/74845146>, 2022-12-18. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

In XSLT, use an identity template plus

    <xsl:template match="sti:name">
      <xsl:variable name="n">
        <xsl:number level="any" from="stu:StudentScreening"/>
      </xsl:variable>
      <xsl:element name="sti:name{$n}">
        <xsl:value-of select="."/>
      </xsl:element>
    </xsl:template>

By the way, telling us the file is "very large" is meaningless unless you say how large. You could be talking 1Mb, you could be talking 100Gb.
