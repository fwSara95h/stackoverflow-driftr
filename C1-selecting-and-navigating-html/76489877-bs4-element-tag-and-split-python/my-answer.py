# Code from my Stack Overflow answer https://stackoverflow.com/a/76498923 (posted 2023-06-18), extracted verbatim; may need the question's context to run.
date = match.find({'div': {'class': 'matchDayHeadline'}})
if date: date = date.text.split()[-1]
