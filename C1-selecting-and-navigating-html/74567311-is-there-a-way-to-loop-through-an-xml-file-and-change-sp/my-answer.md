---
title: "Is there a way to loop through an xml file and change specific tags according to how many times that tag comes up?"
site: stackoverflow
question_id: 74567311
answer_id: 74570172
url: https://stackoverflow.com/a/74570172
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-25T08:45:16Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74570172/revisions
accepted: true
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: abc0c2ea9f4522969f005d422cc08b315620ef86f0f78e6482c445afcdcc2c78
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74570172>, 2022-11-25; **accepted**; score 1. Text as retrieved 2026-10-12.

In bs4, you can assign a new name to Tag simply with `Tag.name = 'NEW_NAME'`, so you just have to enumerate and loop through.

(I pasted your first xml snippet to `xmlStr`.)
```python
xSoup = BeautifulSoup(xmlStr, 'lxml') ## do NOT use 'xml' parser here unless you want to lose namespaces

enumTags = ['st:name', 'stu:studentscreening']
for d in [c for c in xSoup.descendants if c.name]:
    for name in enumTags:
        for i, t in enumerate(d.find_all(name, recursive=False)):
            t.name = f'{t.name}{i}'
```
(You didn't number `studentscreening` in your question, but I wanted to give an example with multiple tags to number; and, setting `recursive=False` reduces redundancies as it restricts `find` to direct children only.)

Now, `print(xSoup)` will give the output
```HTML
<?xml version="1.0" encoding="UTF-8"?><html><body><stu:studentbreakdown>
<stu:studentdata>
<stu:studentscreening0>
<st:name0>Sam Davies</st:name0>
<st:age>15</st:age>
<st:hair>Black</st:hair>
<st:eyes>Blue</st:eyes>
<st:grade>10</st:grade>
<st:teacher>Draco Malfoy</st:teacher>
<st:dorm>Innovation Hall</st:dorm>
<st:name1>Master Splinter</st:name1>
</stu:studentscreening0>
<stu:studentscreening1>
<st:name0>Cassie Stone</st:name0>
<st:age>14</st:age>
<st:hair>Science</st:hair>
<st:grade>9</st:grade>
<st:teacher>Luna Lovegood</st:teacher>
<st:name1>Kelly Clarkson</st:name1>
</stu:studentscreening1>
<stu:studentscreening2>
<st:name0>Derek Brandon</st:name0>
<st:age>17</st:age>
<st:eyes>green</st:eyes>
<st:teacher>Ron Weasley</st:teacher>
<st:dorm>Hogtie Manor</st:dorm>
<st:name1>Miley Cyrus</st:name1>
</stu:studentscreening2>
</stu:studentdata>
</stu:studentbreakdown>
</body></html>
```
(You can also save it [to 'x.xml' for example] with `with open('x.xml', 'wb') as f: f.write(xSoup.prettify('utf-8'))`)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[PickleRick](https://stackoverflow.com/users/18696224)** (2022-11-29): is there a reason why the indents [specifying the child tags] where not used in your answer? Also I didn't number stu:studentscreening because it wasn't giving me a headache lol.
- **[PickleRick](https://stackoverflow.com/users/18696224)** (2022-11-29): Is the [c.name] in relation to the [st:name] tag? Also is the d.find_all in regards to finding the tags with ' name ' in it? Im getting an error when trying to use this. Your answer is exactly what I want my output to be, with the exception of the indents being in there as well.
- **me** (2022-11-29): @Tej About the indent, using `xSoup.prettify()` instead of `str(xSoup)` makes it [like this](https://i.sstatic.net/bepph.png), but it takes up more space [so I didn't paste it like that in the answer], and I don't know how to control the indent
- **me** (2022-11-29): @Tej what error are you getting? no, `c.name` doesn't have anything to do with `st:name` specifically. it's just a lazy way of checking if `c` is a Tag [and not a string/comment/etc] since Tags have names [like `st:name` but `st:age` and `body` are *also* Tag names]. Anyways the check is so that `find_all` doesn't give error later, so I guess it would be more appropriate `if callable(getattr(c, 'find_all'))` [instead of `if c.name`] to check that `c` has a `find_all` function .... but I'm curious about your error bc I've never had issue with the lazy method before...
- **[PickleRick](https://stackoverflow.com/users/18696224)** (2022-12-01): Hey I got it to work, but its only reading the first occurrence. Do you know how to get it to iterate over the entire xml file ? Would you like an example of what its doing ?
- **me** (2022-12-01): @Tej yes please [it should be taking care of all occurrences] - could you upload the original file, your code, and the output to drive/pastebin/jsfiddle and share the link?
- **[PickleRick](https://stackoverflow.com/users/18696224)** (2022-12-08): I will provide what I can. I apologize for the late reply.
- **[PickleRick](https://stackoverflow.com/users/18696224)** (2022-12-12): I have a pastebin, anything would help, https://pastebin.com/u/tjack5
- **me** (2022-12-12): @Tej I've added edits to your code [ https://pastebin.com/k4XsHCkR - the output links are in comments at the top ]. How were you saving the edited soup btw? It kind of looks like a save from the very first iteration only...
- **[PickleRick](https://stackoverflow.com/users/18696224)** (2022-12-12): I didn't get that far [as in saving the edited soup], I wanted to make sure it gave me the desired output first then I would worry about saving the edited soup lol.
- **me** (2022-12-12): @Tej I see, but it must have printed a crazy amount, so it might have still been better to print the entire soup outside the loop....anyway, does it work now?
