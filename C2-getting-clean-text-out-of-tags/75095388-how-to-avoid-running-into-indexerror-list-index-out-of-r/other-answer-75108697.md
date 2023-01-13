---
title: "How to avoid running into IndexError: list index out of range error if an element is nonexistent while parsing xml with BeautifulSoup in python"
site: stackoverflow
question_id: 75095388
answer_id: 75108697
url: https://stackoverflow.com/a/75108697
author: "Jack Fleeting"
author_url: https://stackoverflow.com/users/9448090
posted: 2023-01-13T11:39:06Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 21f93ae3fd4f43c79a4e62425ffa4899c5bd222b9b7e3ee754414c440fe6da3f
role: another answer on the same question, kept as context; not my work
---

# Answer by [Jack Fleeting](https://stackoverflow.com/users/9448090) — 2023-01-13

Posted on Stack Overflow, <https://stackoverflow.com/a/75108697>, 2023-01-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

First, as to why lxml is better than BeautifulSoup for xml, the answer is simple: the best way to query xml is with xpath. lxml supports xpath (though only version 1.0; for more complex xml and queries you will need xpath 2.0 to 3.1 and a library like elementpath). BS doesn't support xpath, though it does have excellent support for css selectors, which works better with html.

Having said all that - in your particular case, you probably don't need lxml either - only pandas and a one liner! Though you haven't shown your expected output, my guess is you expect the output below. Note that in your sample xml there is probability an error: the 2nd `<EntrySynopsisDetail_1_0>` has `<CategoryOfEntry>` twice, so I removed one:

    entries = """<Entries>
     <EntrySynopsisDetail_1_0>
            <EntryID>262148</EntryID>
            <EntryTitle>Establishment of the Graduate Internship Program</EntryTitle>
            <CategoryOfEntry>ENG</CategoryOfEntry>
    </EntrySynopsisDetail_1_0>
      
    <EntrySynopsisDetail_1_0>
    		<EntryID>2667654</EntryID>
            <EntryTitle>Call for Mobility Program</EntryTitle>
            <CategoryOfEntry>MAT</CategoryOfEntry>
     </EntrySynopsisDetail_1_0>
    </Entries>"""

    pd.read_xml(entries,xpath="//EntrySynopsisDetail_1_0")

Output:

    EntryID 	   EntryTitle 	                       CategoryOfEntry
    0 	262148 	    Establishment of the Graduate Internship Program 	ENG
    1 	2667654 	Call for Mobility Program 	                      MAT

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[tachyon](https://stackoverflow.com/users/9122160)** (2023-01-13): Thanks for the explanation. The XML file actually has multiple occurrences of CategoryOfEntry in many elements, and in some cases, it does not have this tag which is why there is an index error arising from my piece of code.
- **[tachyon](https://stackoverflow.com/users/9122160)** (2023-01-13): Also, how do you replace ENG and MAT with English and Mathematics? I want the keys to be replaced with the provided values.
- **[Jack Fleeting](https://stackoverflow.com/users/9448090)** (2023-01-13): @tachyon I see; in that case, it may, depending on the structure, become difficult or impossible to convert the xml into a dataframe; you may have to just query the xml directly with xpath (assuming it is otherwise well formed - if not, it's not really xml), or contact whoever creates the xml and ask them to fix the structure.
- **[tachyon](https://stackoverflow.com/users/9122160)** (2023-01-13): that is a great insight - thanks.
