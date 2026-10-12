# Code from my Stack Overflow answer https://stackoverflow.com/a/79579163 (posted 2025-04-17), extracted verbatim; may need the question's context to run.
> def extract_details(item):
>     # Check if language attribute is English
>     lang = item.get("lang", "en")
>     if lang != "en":
>         return None  # Skip non-English
>
