# Code from my Stack Overflow answer https://stackoverflow.com/a/74248353 (posted 2022-10-29), extracted verbatim; may need the question's context to run.

# --- block 1 ---
if not [s for s in sal_play if s.find('tr', class_='thead')]: 
    print('1')

# --- block 2 ---
if [s for s in sal_play if s.find('tr', class_='thead') is None]: 
    print('1')
