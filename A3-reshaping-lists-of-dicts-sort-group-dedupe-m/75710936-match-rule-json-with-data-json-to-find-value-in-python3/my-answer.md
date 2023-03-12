---
title: "Match rule json with data json to find value in python3"
site: stackoverflow
question_id: 75710936
answer_id: 75716929
url: https://stackoverflow.com/a/75716929
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-12T23:10:24Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75716929/revisions
accepted: true
score: 1
chapter: A3
chapter_title: "Reshaping lists of dicts: sort, group, dedupe, merge"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4fa3aee1d4221fc4cc10508bb7ebb641c576ff9df39144993c0d38c4e73e508e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75716929>, 2023-03-12; **accepted**; score 1. Text as retrieved 2026-10-12.

> *Looking for efficient way of doing it. Don't want so many for loops*

You could convert each `properties_rule` list into a function or [`lambda`](https://www.programiz.com/python-programming/anonymous-function) expression (accompanied by a list of `propertyId`s to extract the arguments and an `articleId` to return).

```py
def rule_to_lambda(rule_dict):
    opRef = {'EQ': '==', 'GTE': '>=', 'LTE': '<=', 'GT': '>', 'LT': '<'}

    lStr1, lStr2, prop_ids, andOr = 'lambda ', ':', [], ''
    for ri, pr in enumerate(rule_dict['properties_rule'], 1):
        prop_ids.append(pr['propertyId'])
        prVal, lStr1 = pr['value'], f'{lStr1}{"" if ri == 1 else ", "}p{ri}'

        if ri != 1: lStr2 += f' {andOr}'
        andOr = 'or' if pr.get('logicalOperator')=='OR' else 'and'

        cond = f'{repr(prVal)} {opRef.get(pr["condition"])} p{ri}'
        lStr2 += f' (p{ri} is not None and {cond})'

    # no rules to check --> return True by default     
    if not prop_ids: lStr1, lStr2 = 'lambda *x', ': True'
 
    return rule_dict['articleId'], prop_ids, eval(lStr1+lStr2)
```

<sup>Note that using [`eval`](https://www.programiz.com/python-programming/methods/built-in/eval) is often [considered unsafe](https://www.codiga.io/blog/python-eval/), but I think it's alright in this case since you know exactly what can go into `lStr1+lStr2` (except for `pr['value']`, but that's coming from parsed JSON, so it won't be an expression).</sup>

If used on the sample of `rules.json` in your question,

```py
# import json
# with open('rules.json', 'r') as f: rules = json.load(f)

rules_list = [rule_to_lambda(r) for r in rules['rules']]
```

then `rules_list` would [effectively] be the same as

>```py
> [
>  ('art1', [487, 487], lambda p1, p2: (p1 is not None and 'aaaa' == p1) and (p2 is not None and 'zzzz' == p2)),
>  ('art2', [487, 487], lambda p1, p2: (p1 is not None and 'bbbb' >= p1) and (p2 is not None and 'eeee' <= p2)),
>  ('art3', [487], lambda p1: (p1 is not None and 'ffff' >= p1))
> ]
>```

[You'll still have to loop through every rule for every `properties_values` in `data`, but this way you only have to loop through every `properties_rule` dictionary once, and then you can use the `lambda` expressions created.]

---

Since you need the `property_value` (that corresponds to the `property_id`s) as arguments for the `lambda` expressions, you might also want to use a function to find the `property_value` of a `data` value based on a `property_id`:

```py
def get_property_value(prop_id, prop_vals:list):
    for p in prop_vals:
        if prop_id == p['value']['property_id']: 
            return p['value']['property_value']

# {k:get_property_value(487,v['properties_values']) for k,v in data['data'].items()}
# returns {'1': 'aaaa', '2': 'bbbb', '3': 'eeee'}
```

---

Now you can loop though `data` like

```py
# import json
# with open('rules.json', 'r') as f: rules = json.load(f)
# with open('data.json', 'r') as f: data = json.load(f)

# rules_list = [rule_to_lambda(r) for r in rules['rules']]
for k, v in data['data'].items():
    for a, prop_ids, ruleFunc in rules_list:
        pvals = v['properties_values'] 
        pvals = [get_property_value(pi, pvals) for pi in prop_ids]
        if ruleFunc(*pvals):
            print(k, ':', pvals, '---> Article ID:', a)
            break ## print only for the first rule that matches
    else: print(k, '---> Default Article ID')
```

With your sample `data.json` and `rules.json`, this prints *`Article ID: art3`* on all 3 lines, but that's unsurprising since the `art1` and `art2` rule are impossible unless `p1` and `p2` are different [and they aren't since `prop_ids` for both rules is `[487,487]`].

> ```py
> 1 : ['aaaa'] ---> Article ID: art3
> 2 : ['bbbb'] ---> Article ID: art3
> 3 : ['eeee'] ---> Article ID: art3
> ```
