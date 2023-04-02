---
title: "Create dictionary through text file"
site: stackoverflow
question_id: 75914200
answer_id: 75914626
url: https://stackoverflow.com/a/75914626
author: "C. Pappy"
author_url: https://stackoverflow.com/users/8072841
posted: 2023-04-02T21:07:52Z
last_edited: 2023-04-03T02:31:02Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bb0fec3dbfea4bcbebb544218662e93ecd360ac215ad0f1100df2cc8c2ad465d
role: another answer on the same question, kept as context; not my work
---

# Answer by [C. Pappy](https://stackoverflow.com/users/8072841) — 2023-04-02

Posted on Stack Overflow, <https://stackoverflow.com/a/75914626>, 2023-04-02, last edited 2023-04-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

This solution takes advantage of the pandas library's dataframe functionality. 

    import pandas as pd
    
    print(f'Country   Wins Years')
    data = pd.read_csv('world_cup_champions.txt') # Create a pandas dataframe fron the data
    bycountry = data.groupby('Country')  # Group the dataframe by country
    for country, df in bycountry:  # For each (country) group
        years = [str(x[1]['Year']) for x in df.iterrows()] # Extract the years into a list
        print(f'{country:<10} {len(years)}  ', ', '.join(years))  # Print results

Which can be simplified to:

    import pandas
    
    print(f'Country   Wins Years')
    for country, df in pandas.read_csv('world_cup_champions.txt').groupby('Country'):
        years = [str(x[1]['Year']) for x in df.iterrows()]
        print(f'{country:<10} {len(years)}  ', ', '.join(years))
Output:

    Country   Wins Years
    Argentina  2   1978, 1986
    Brazil     5   1958, 1962, 1970, 1994, 2002
    England    1   1966
    France     1   1998
    Germany    4   1954, 1974, 1990, 2014
    Italy      4   1934, 1938, 1982, 2006
    Spain      1   2010
    Uruguay    2   1930, 1950
