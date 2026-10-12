# Code from my Stack Overflow answer https://stackoverflow.com/a/75716929 (posted 2023-03-12), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
# import json
# with open('rules.json', 'r') as f: rules = json.load(f)

rules_list = [rule_to_lambda(r) for r in rules['rules']]

# --- block 3 ---
> [
>  ('art1', [487, 487], lambda p1, p2: (p1 is not None and 'aaaa' == p1) and (p2 is not None and 'zzzz' == p2)),
>  ('art2', [487, 487], lambda p1, p2: (p1 is not None and 'bbbb' >= p1) and (p2 is not None and 'eeee' <= p2)),
>  ('art3', [487], lambda p1: (p1 is not None and 'ffff' >= p1))
> ]
>

# --- block 4 ---
def get_property_value(prop_id, prop_vals:list):
    for p in prop_vals:
        if prop_id == p['value']['property_id']: 
            return p['value']['property_value']

# {k:get_property_value(487,v['properties_values']) for k,v in data['data'].items()}
# returns {'1': 'aaaa', '2': 'bbbb', '3': 'eeee'}

# --- block 5 ---
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

# --- block 6 ---
> 1 : ['aaaa'] ---> Article ID: art3
> 2 : ['bbbb'] ---> Article ID: art3
> 3 : ['eeee'] ---> Article ID: art3
>
