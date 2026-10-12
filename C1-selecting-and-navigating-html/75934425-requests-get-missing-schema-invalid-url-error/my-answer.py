# Code from my Stack Overflow answer https://stackoverflow.com/a/75951865 (posted 2023-04-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>     team_urls = [f"https//fbref.com{I}" for I in links] # <-- ?TYPO? HERE
>     for team_url in team_urls:
>

# --- block 2 ---
>         data = requests.get(team_url) # <-- error bc team_url has typo
>

# --- block 3 ---
team_urls = [f"https://fbref.com{I}" for I in links]
