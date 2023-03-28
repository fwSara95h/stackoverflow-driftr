---
title: "How to parse XML for elements preceding a certain tag?"
site: stackoverflow
question_id: 75870697
url: https://stackoverflow.com/q/75870697
asked: 2023-03-28T20:17:17Z
asked_by: "Loïc Borcard"
asked_by_url: https://stackoverflow.com/users/11561076
last_edited: 2023-03-29T07:09:41Z
last_editor: "HedgeHog"
last_editor_url: https://stackoverflow.com/users/14460824
tags: [python, xml, beautifulsoup]
score: 1
views_at_snapshot: 47
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 669cc59a023a8257baacf312313cb751854082fdc6acf86072e8833f0f30ccbc
---

# How to parse XML for elements preceding a certain tag?

Asked by [Loïc Borcard](https://stackoverflow.com/users/11561076) on Stack Overflow, <https://stackoverflow.com/q/75870697>, 2023-03-28, last edited 2023-03-29 by [HedgeHog](https://stackoverflow.com/users/14460824). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I would like to retrieve all the sentences preceding a `xref ref-type = "bibr"`. Using this example below my input would be that:
```
xml = "This could be due to two nonmutually exclusive possibilities: first, the HB3 DNA sequence for these genes may be substantially rearranged or completely deleted relative to the reference strain, 3D7; second, only a few of these genes may be selectively expressed, as has been proposed (<xref rid="pbio-0000005-Deitsch1" ref-type="bibr">Deitsch et al. 2001</xref>). To identify regions of genomic variability between 3D7 and HB3, we performed microarray-based comparative genomic hybridization (CGH) analysis. Array-based CGH has been performed with human cDNA and bacterial artificial chromosome-based microarrays to characterize DNA copy-number changes associated with tumorigenesis (<xref rid="pbio-0000005-Gray1" ref-type="bibr">Gray and Collins 2000</xref>; <xref rid="pbio-0000005-Pollack2" ref-type="bibr">Pollack et al. 2002</xref>)."
```
output:
```
{
Array-based CGH has been performed with human cDNA and bacterial artificial chromosome-based microarrays to characterize DNA copy-number changes associated with tumorigenesis :
(<xref rid="pbio-0000005-Gray1" ref-type="bibr">Gray and Collins 2000</xref>; <xref rid="pbio-0000005-Pollack2" ref-type="bibr">Pollack et al. 2002</xref>)
}
{
This could be due to two nonmutually exclusive possibilities: first, the HB3 DNA sequence for these genes may be substantially rearranged or completely deleted relative to the reference strain, 3D7; second, only a few of these genes may be selectively expressed, as has been proposed :(<xref rid="pbio-0000005-Deitsch1" ref-type="bibr">Deitsch et al. 2001</xref>)
}
```
I tried find 

```
soup = bs(XML)

soup.find("xref", attrs={'ref-type': 'bibr'}).previous_element
```

but it only retrieves the first one and `find_all`provides a list of the citations but does not allow me to use the previous_element method.
