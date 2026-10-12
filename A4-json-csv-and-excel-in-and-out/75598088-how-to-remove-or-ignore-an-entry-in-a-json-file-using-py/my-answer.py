# Code from my Stack Overflow answer https://stackoverflow.com/a/75599180 (posted 2023-03-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import json
# with open('cloud.json') as f: data = json.load(f) ## safer than f=open...

with open ("ip.txt" ,'w') as d:
    for prefix_i in data['prefixes']:
        # if 'ipv6Prefix' not in prefix_i: d.write("{prefix_i}\n") ## OR
        if 'ipv6Prefix' in prefix_i: continue
        d.write("{}\n".format(prefix_i))
    ## list-comprehension INSTEAD OF for-loop:
    # d.write('\n'.join(str(p) for p in data['prefixes'] if 'ipv6Prefix' not in p))

# --- block 2 ---
with open ("ip.txt" ,'w') as d:
    for prefix_i in data['prefixes']:
        if 'ipv4Prefix' in prefix_i: d.write("{}\n".format(prefix_i))

# --- block 3 ---
data['prefixes'] = [p for p in data['prefixes'] if 'ipv6Prefix' not in p]

# --- block 4 ---
## to just save the list as a variable:
# ipv4Prefixes = [p for p in data['prefixes'] if 'ipv4Prefix' in p]

with open('ipv4Prefixes.json', w) as f:
    json.dump([p for p in data['prefixes'] if 'ipv4Prefix' in p], f)

# --- block 5 ---
> # for i in data['prefixes']...
>         data.pop(i)
>

# --- block 6 ---
for pi, p in enumerate(reversed(data['prefixes']), 1-len(data['prefixes'])):
    if 'ipv6Prefix' in p["prefixes"]: data['prefixes'].pop(pi)

# --- block 7 ---
>     if data[i]["prefixes"] == "ipv6Prefix":
>
