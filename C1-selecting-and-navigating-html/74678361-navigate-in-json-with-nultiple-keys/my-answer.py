# Code from my Stack Overflow answer https://stackoverflow.com/a/74680512 (posted 2022-12-04), extracted verbatim; may need the question's context to run.

# --- block 1 ---
data["props"]["XYZ"]["ABC"][0]["current"]

# --- block 2 ---
getNestedVal(data, 'current')

# --- block 3 ---
getNestedVal(data, 'current', 'just_expr', objName='data')
