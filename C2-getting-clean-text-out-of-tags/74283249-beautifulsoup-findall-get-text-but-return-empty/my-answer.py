# Code from my Stack Overflow answer https://stackoverflow.com/a/74283516 (posted 2022-11-02), extracted verbatim; may need the question's context to run.
str(soup.find('style')).strip()[7:-8].strip()
