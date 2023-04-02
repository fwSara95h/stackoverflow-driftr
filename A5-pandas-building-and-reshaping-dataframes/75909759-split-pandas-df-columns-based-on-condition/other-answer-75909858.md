---
title: "Split Pandas DF columns based on condition"
site: stackoverflow
question_id: 75909759
answer_id: 75909858
url: https://stackoverflow.com/a/75909858
author: "Marcelo Paco"
author_url: https://stackoverflow.com/users/11286032
posted: 2023-04-02T02:45:26Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6a4b5721fc326c1f5369f8689bd00b68a9816e2c6f1f3179ace587b067c0512a
role: another answer on the same question, kept as context; not my work
---

# Answer by [Marcelo Paco](https://stackoverflow.com/users/11286032) — 2023-04-02

Posted on Stack Overflow, <https://stackoverflow.com/a/75909858>, 2023-04-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can define your own function to `apply()` on columns `Tags1` and `Tags2`:

    import pandas as pd
    
    # Extract the movie/genre from interest columns
    def get_movie_genre(row, cols):
        # Default value
        movie = 'None'
        genre = 'None'
        # Loop through the columns
        for col_name in cols:
            # Check for none
            if row[col_name].lower() != 'none':
                # Get values for either movie or genre
                name, val = row[col_name].split(':')
                if name.lower() == 'movie':
                    movie = val
                elif name.lower() == 'genre':
                    genre = val
    
        # Set values to columns
        row[cols[0]] = movie
        row[cols[1]] = genre
    
        return row
    
    # My definition of your example dataframe
    df = pd.DataFrame({'Videold': [1234, 3456, 5678, 7890, 9012],
                        'Tags1': ['None', 'Movie:Rocky', 'Genre:Romance', 'Movie:Scream', 'Movie:Shrek'],
                        'Tags2': ['None', 'Genre:Drama', 'Movie:Love Me', 'Genre:Horror', 'None']})
    
    # Cols we are interested in apply get_movie_genre from rows
    cols_of_interest = ['Tags1', 'Tags2']
    
    # Create Movie and Genre colums from the return values of apply by row
    df[['Movies', 'Genre']] = df[cols_of_interest].apply(lambda x: get_movie_genre(x, cols_of_interest), axis=1)
    
    # Drop Tags1 and Tags2
    df = df.drop(cols_of_interest, axis=1)

Contents of `df` after manipulation:

       Videold   Movies    Genre
    0     1234     None     None
    1     3456    Rocky    Drama
    2     5678  Love Me  Romance
    3     7890   Scream   Horror
    4     9012    Shrek     None
