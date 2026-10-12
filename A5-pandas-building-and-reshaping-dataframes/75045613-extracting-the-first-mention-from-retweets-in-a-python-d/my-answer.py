# Code from my Stack Overflow answer https://stackoverflow.com/a/75045740 (posted 2023-01-08), extracted verbatim; may need the question's context to run.
# allowedChars = '' # '+-.' # add allowed characters
record['usr_rt'] = ['' if not rt == 'RT' else ''.join(
    c for c in txt.split('@', 1)[-1].split(':')[0].lower() 
    if c.isalpha() or c.isdigit() # or c in allowedChars
) for txt, rt in zip(record['text_con_RT_t'], record['rt'])]
