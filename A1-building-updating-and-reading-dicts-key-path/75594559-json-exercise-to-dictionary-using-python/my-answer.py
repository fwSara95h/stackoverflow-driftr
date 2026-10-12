# Code from my Stack Overflow answer https://stackoverflow.com/a/75595401 (posted 2023-02-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def format_empData(val, key, enforce=False, defaultVal=None):
    if key == 'ID':
        try: return int(val[0] if val and isinstance(val, list) else val)
        except: return defaultVal if enforce else val
    return str(val)

# --- block 2 ---
managerId = 3
for di, dept in enumerate(department):
    if dept['ID'] == managerId:
        department[di]['employees'].append(
            {k: format_empData(v, k) for k, v in employee.items()})
        break

# --- block 3 ---
> [{'ID': 1, 'Name': 'John', 'Role': 'Manager',
>   'employees': [{'ID': 4, 'Name': 'Mike', 'Role': 'Engineer'}]},
>  {'ID': 3, 'Name': 'Sam', 'Role': 'Manager',
>   'employees': [{'ID': 2, 'Name': 'Jack', 'Role': 'Analyst'}]}]
>
