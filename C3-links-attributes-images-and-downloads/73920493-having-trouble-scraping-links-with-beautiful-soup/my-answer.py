# Code from my Stack Overflow answer https://stackoverflow.com/a/73928663 (posted 2022-10-02), extracted verbatim; may need the question's context to run.
links_h = [link.find('a').get("href")for link in house if link.find('a')]
