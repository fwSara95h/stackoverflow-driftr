---
title: "Why does soup.get_text() include comments in some situations?"
site: stackoverflow
question_id: 74647276
url: https://stackoverflow.com/q/74647276
asked: 2022-12-01T19:32:28Z
asked_by: "Peter"
asked_by_url: https://stackoverflow.com/users/968132
last_edited: 2022-12-01T20:28:42Z
tags: [beautifulsoup, ms-word, lxml]
score: -1
views_at_snapshot: 91
answer_count: 1
accepted_answer_id: 74672659
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ee24d202f8757d7656517470f6c9052b17444c8d6836dfd58a73bd52b5ce267b
---

# Why does soup.get_text() include comments in some situations?

Asked by [Peter](https://stackoverflow.com/users/968132) on Stack Overflow, <https://stackoverflow.com/q/74647276>, 2022-12-01, last edited 2022-12-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have an HTML document that I've created by exporting a MS Word doc. In Word, I saved as the `Web Page (.HTM)` format, not the `Web Page, Filtered (.HTM)` format. 

When I run get_text on the doc, it includes the comments in the style tag for some reason. This is unexpected. BS4 *does* ignore the 2nd comment in the body as expected.

I've tried with both the `lxml` and `html.parser` parsers. Same result. 

Python 3.9.12, IPython 8.4.0, BS 4.8.2 (though when I use pkg_resources.get_distribution("bs4").version, it shows 0.0.1)

```
html = """<html>
<head>
<meta http-equiv=Content-Type content="text/html; charset=utf-8">
<meta name=Generator content="Microsoft Word 15 (filtered)">
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:Helvetica;
	panose-1:2 11 6 4 2 2 2 2 2 4;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin:0in;
	text-align:justify;
	text-justify:inter-ideograph;
	font-size:12.0pt;
	font-family:"Times New Roman",serif;}
 /* Page Definitions */
 @page WordSection1
	{size:8.5in 11.0in;
	margin:1.0in 1.25in 1.0in 1.25in;}
div.WordSection1
	{page:WordSection1;}
 /* List Definitions */
 ol
	{margin-bottom:0in;}
-->
</style>
</head>
<body lang=EN-US link=blue vlink=purple style='word-wrap:break-word'>
<div class=WordSection1>
<div style='border-top:double windowtext 2.25pt;border-left:none;border-bottom:
double windowtext 2.25pt;border-right:none;padding:1.0pt 0in 1.0pt 0in'>
<p class=MsoNormal style='margin-bottom:.25in;border:none;padding:0in'><span
style='font-size:9.0pt'>&nbsp;</span></p>
<!-- Some other random comment that get_text ignores -->
</div>
</body>
</html>"""

soup = BeautifulSoup(html, "lxml")
soup.get_text()
```
```
In [5]: soup.get_text()
Out[5]: '\n\n\n\n\n<!--\n /* Font Definitions */\n @font-face\n\t{font-family:Helvetica;\n\tpanose-1:2 11 6 4 2 2 2 2 2 4;}\n /* Style Definitions */\n p.MsoNormal, li.MsoNormal, div.MsoNormal\n\t{margin:0in;\n\ttext-align:justify;\n\ttext-justify:inter-ideograph;\n\tfont-size:12.0pt;\n\tfont-family:"Times New Roman",serif;}\n /* Page Definitions */\n @page WordSection1\n\t{size:8.5in 11.0in;\n\tmargin:1.0in 1.25in 1.0in 1.25in;}\ndiv.WordSection1\n\t{page:WordSection1;}\n /* List Definitions */\n ol\n\t{margin-bottom:0in;}\n-->\n\n\n\n\n\n\xa0\n\n\n\n\n'
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2022-12-01): could not reproduce the issue, works as expected, but to clarify may also post some information concerning versions of modules. Thanks
- **[Peter](https://stackoverflow.com/users/968132)** (2022-12-01): Strange. Let me do that. What information would you want specifically?
