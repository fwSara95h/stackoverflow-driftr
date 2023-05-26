---
title: "Dealing with optional python dictionary fields"
site: stackoverflow
question_id: 70988817
answer_id: 76338778
url: https://stackoverflow.com/a/76338778
author: "Willy Horizont"
author_url: https://stackoverflow.com/users/21963849
posted: 2023-05-26T07:56:13Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ca12b42e79ad4c8d2addb0678679d51bee3a7cfae8e39253536c6e103cf02c58
role: another answer on the same question, kept as context; not my work
---

# Answer by [Willy Horizont](https://stackoverflow.com/users/21963849) — 2023-05-26

Posted on Stack Overflow, <https://stackoverflow.com/a/76338778>, 2023-05-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I use reduce to achieve Javascript-like optional chaining in Python

```
from functools import reduce


data_dictionary = {
    'foo': {
        'bar': {
            'buzz': 'lightyear'
        },
        'baz': {
            'asd': 2023,
            'zxc': [
                {'patrick': 'star'},
                {'spongebob': 'squarepants'}
            ],
            'qwe': ['john', 'sarah']
        }
    },
    'hello': {
        'world': 'hello world',
    },
}


def optional_chaining_v1(dictionary={}, *property_list):
    def reduce_callback(current_result, current_dictionary):
        if current_result is None:
            return dictionary.get(current_dictionary)
        if type(current_result) != dict:
            return None
        return current_result.get(current_dictionary)
    return reduce(reduce_callback, property_list, None)


# or in one line
optional_chaining_v1 = lambda dictionary={}, *property_list: reduce(lambda current_result, current_dictionary: dictionary.get(current_dictionary) if current_result is None else None if type(current_result) != dict else current_result.get(current_dictionary), property_list, None)

# usage
optional_chaining_v1_result1 = optional_chaining_v1(data_dictionary, 'foo', 'bar', 'baz')
print('optional_chaining_v1_result1:', optional_chaining_v1_result1)
optional_chaining_v1_result2 = optional_chaining_v1(data_dictionary, 'foo', 'bar', 'buzz')
print('optional_chaining_v1_result2:', optional_chaining_v1_result2)

# optional_chaining_v1_result1: None
# optional_chaining_v1_result2: lightyear


def optional_chaining_v2(dictionary={}, list_of_property_string_separated_by_dot=''):
    property_list = list_of_property_string_separated_by_dot.split('.')

    def reduce_callback(current_result, current_dictionary):
        if current_result is None:
            return dictionary.get(current_dictionary)
        if type(current_result) != dict:
            return None
        return current_result.get(current_dictionary)
    return reduce(reduce_callback, property_list, None)


# or in one line
optional_chaining_v2 = lambda dictionary={}, list_of_property_string_separated_by_dot='': reduce(lambda current_result, current_dictionary: dictionary.get(current_dictionary) if current_result is None else None if type(current_result) != dict else current_result.get(current_dictionary), list_of_property_string_separated_by_dot.split('.'), None)

# usage
optional_chaining_v2_result1 = optional_chaining_v2(data_dictionary, 'foo.bar.baz')
print('optional_chaining_v2_result1:', optional_chaining_v2_result1)
optional_chaining_v2_result2 = optional_chaining_v2(data_dictionary, 'foo.bar.buzz')
print('optional_chaining_v2_result2:', optional_chaining_v2_result2)

# optional_chaining_v2_result1: None
# optional_chaining_v2_result2: lightyear

```
