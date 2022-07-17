---
title: "Ignore / skip tags when prettifying with BeautifulSoup"
site: stackoverflow
question_id: 73011981
url: https://stackoverflow.com/q/73011981
asked: 2022-07-17T12:56:23Z
asked_by: "questiondude"
asked_by_url: https://stackoverflow.com/users/2031993
last_edited: 2022-07-25T09:12:27Z
tags: [beautifulsoup]
score: 0
views_at_snapshot: 829
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 58a06b2197eb4e5b41343a25f6be4aa1253d6d3870a24751608d65a47ddd47a8
---

# Ignore / skip tags when prettifying with BeautifulSoup

Asked by [questiondude](https://stackoverflow.com/users/2031993) on Stack Overflow, <https://stackoverflow.com/q/73011981>, 2022-07-17, last edited 2022-07-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Is it possible to ignore / skip certain tags when parsing and prettifying an HTML-document with BeautifulSoup?

I am using BeautifulSoup to prettify HTML-documents with large embedded SVG-images. There is no need to prettify the SVG-images and all of their child-elements. As performance is critical for this application, I thought I might be able to save some runtime by ignoring / skipping the SVG-elements when prettifying the HTML, and just include the SVG-elements as they originally were in the input.

I am aware of SoupStrainer but it seems to do the exact opposite of what I need. I have also read many of the posts here on StackOverflow and elsewhere, and none of them seem to address this issue.

## Example

	# Messy HTML code.
	messy = \
	"""
	<html>  <head>
	   <title>
	   
		   Some title</title>
		</head> <body>
	<svg>Don't parse and prettify this!</svg>
	</body> </html>
	"""

	# Prettify the HTML code.
	from bs4 import BeautifulSoup
	pretty = BeautifulSoup(markup=messy, features='html.parser').prettify()

Which produces the result:

	<html>
	 <head>
	  <title>
	   Some title
	  </title>
	 </head>
	 <body>
	  <svg>
	   Don't parse and prettify this!
	  </svg>
	 </body>
	</html>

Note that the `<svg>` element has also been parsed and prettified by BeautifulSoup. Is there a way to avoid this?

Thanks!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2022-07-17): It is hard to give an exact answer based on that little input - Help us to help you - Please improve your question, so that we can reproduce your issue. How to create [mcve] Thanks
