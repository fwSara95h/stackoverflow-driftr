---
title: "Stuck on this function"
site: stackoverflow
question_id: 75925033
url: https://stackoverflow.com/q/75925033
asked: 2023-04-04T02:18:39Z
asked_by: "kakuro"
asked_by_url: https://stackoverflow.com/users/21561070
last_edited: 2023-04-04T03:59:10Z
last_editor: "Yash Mehta"
last_editor_url: https://stackoverflow.com/users/20172954
tags: [python, python-3.x, function, dictionary, nested]
score: 3
views_at_snapshot: 193
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 831f9496f33825caab761b6059b79b13143db35577a774f065e73c6db2774b05
---

# Stuck on this function

Asked by [kakuro](https://stackoverflow.com/users/21561070) on Stack Overflow, <https://stackoverflow.com/q/75925033>, 2023-04-04, last edited 2023-04-04 by [Yash Mehta](https://stackoverflow.com/users/20172954). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

    def moves_to_nested_dict(moves: list[list[str]]) -> dict[tuple[str, int], dict]:
        """
        Convert <games> into a nested dictionary representing the sequence of moves
        made in the games.
    
        Each list in <games> corresponds to one game, with the i'th str being the
        i'th move of the game.
    
        The nested dictionary's keys are tuples containing the string representing
        the move made on that turn and an integer indicating how many games ended
        immediately after this move. See the docstring example below.
    
        The values of each nested dictionary are themselves nested dictionaries of
        this structure. An empty dictionary is stored as the value for a move that
        will correspond to a leaf
    
        Note: to keep the docstring short, we use single letters in place
              of real chess moves, as it has no impact on the logic of how this
              code needs to be implemented, since it should work for arbitary
              strings used to denote moves.
    
    
        >>> moves_to_nested_dict([[]])  # empty lists are ignored
        {}
        >>> moves_to_nested_dict([])
        {}
        >>> moves_to_nested_dict([['a'], []])
        {('a', 1): {}}
        >>> d = moves_to_nested_dict([["a", "b", "c"],
        ...                           ["a", "b"], ["d", "e"], ["d", "e"]])
        >>> d
        {('a', 0): {('b', 1): {('c', 1): {}}}, ('d', 0): {('e', 2): {}}}
        >>> d = moves_to_nested_dict([
        ...    ["a", "b", "c"], ["a", "b"], ["d", "e", "a"], ["d", "e"]])
        >>> d
        {('a', 0): {('b', 1): {('c', 1): {}}}, ('d', 0): {('e', 1): {('a', 1): {}}}}
        """

i've been trying to solve this function but i'm kinda stuck. I know how to write the general structure but have no idea how to get the number correctly. Can someone help implement

this is what I've done:

    result = {}
    for game_moves in moves:
        if len(game_moves) == 0:
            continue
        current_dict = result
        num_ended_games = 0
        for move in game_moves[:-1]:
            key = (move, num_ended_games)
            if key not in current_dict:
                current_dict[key] = {}
            current_dict = current_dict[key]
            num_ended_games = 0
        last_move = game_moves[-1]
        key = (last_move, num_ended_games)
        if key not in current_dict:
            current_dict[key] = {}
        current_dict = current_dict[key]
        num_ended_games += 1
    return result

and the error messages are

**Failed example:**
    `d`

**Expected:**

    {('a', 0): {('b', 1): {('c', 1): {}}}, ('d', 0): {('e', 2): {}}}

**Got:**

    {('a', 0): {('b', 0): {('c', 0): {}}}, ('d', 0): {('e', 0): {}}}

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Michael Butscher](https://stackoverflow.com/users/987358)** (2023-04-04): (1) Format the code correctly. (2) Find a title to describe the problem in a better way. (3) Describe the problem in the question better. What happens, what should happen? Show error messages (if any) completely as properly formatted text in the question.
- **[Joran Beasley](https://stackoverflow.com/users/541038)** (2023-04-04): please add your attempt ... copy and paste this homework problem usually results in downvotes to oblivion
