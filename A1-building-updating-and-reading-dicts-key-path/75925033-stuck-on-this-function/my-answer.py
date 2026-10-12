# Code from my Stack Overflow answer https://stackoverflow.com/a/75926769 (posted 2023-04-04), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>     num_ended_games = 0 ## beginning of loop
>

# --- block 2 ---
>         key = (move, num_ended_games)
>         if key not in current_dict:
>

# --- block 3 ---
>     num_ended_games += 1 ## end of loop
>

# --- block 4 ---
def moves_to_nested_dict(moves: list[list[str]]) -> dict[tuple[str,int], dict]:
    result = {}
    for game_moves in moves:
        cur_dict = result

        for reverse_index, move in enumerate(game_moves, 1-len(game_moves)):
            cur_key = [k for k in cur_dict if k[0]==move]            
            if not cur_key: cur_dict[(cur_key := (move, 0))] = {}
            else: cur_key = cur_key[0]

            if not reverse_index: ## <-- reverse_index=0 on last move
                cur_dict[(move, cur_key[1]+1)] = cur_dict.pop(cur_key)
            else: cur_dict = cur_dict[cur_key]
    return result

# --- block 5 ---
def moves_to_nested_dict(moves: list[list[str]]) -> dict[str,dict]:
    result = {}
    for game in moves:
        cur_dict = result
        for move in game: 
            cur_dict = cur_dict.setdefault(move, {'__games_ended__':0}) # (move,{})
        if game: cur_dict['__games_ended__'] = cur_dict.get('__games_ended__',0)+1
    return result

# --- block 6 ---
moves_to_nested_dict([['a','b'], ['a','b'], ['a','b','c'], ['d','a'], ['a','d']])

# --- block 7 ---
> {
>   'a': {
>     '__games_ended__': 0,
>     'b': {'__games_ended__': 2, 'c': {'__games_ended__': 1}},
>     'd': {'__games_ended__': 1}
>   },
>   'd': {'__games_ended__': 0, 'a': {'__games_ended__': 1}}
> }
>
