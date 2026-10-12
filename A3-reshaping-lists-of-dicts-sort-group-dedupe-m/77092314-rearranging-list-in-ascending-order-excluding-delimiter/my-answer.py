# Code from my Stack Overflow answer https://stackoverflow.com/a/77092374 (posted 2023-09-12), extracted verbatim; may need the question's context to run.
# Includes later revisions by: Kelly Bundy (https://stackoverflow.com/users/12671057), revision 2, 2023-09-12, CC BY-SA 4.0.

# --- block 1 ---
list1 = ['1=8.06225774829855', '2=2.23606797749979', '3=8.602325267042627', '4=7.280109889280518', '5=3.1622776601683795']

# --- block 2 ---
list2 = sorted(list1, key=lambda s: float(s.split('=')[-1]))
# list2 = ['2=2.23606797749979', '5=3.1622776601683795', '4=7.280109889280518', '1=8.06225774829855', '3=8.602325267042627']

# --- block 3 ---
list1.sort(key=lambda s: float(s.split('=')[-1]))
# list1 = ['2=2.23606797749979', '5=3.1622776601683795', '4=7.280109889280518', '1=8.06225774829855', '3=8.602325267042627']
