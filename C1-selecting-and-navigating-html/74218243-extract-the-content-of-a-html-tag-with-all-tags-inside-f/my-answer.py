# Code from my Stack Overflow answer https://stackoverflow.com/a/74235005 (posted 2022-10-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
''.join(soup_object.contents)

# --- block 2 ---
'\n'.join(soup_object.prettify().split('\n')[1:-1])
