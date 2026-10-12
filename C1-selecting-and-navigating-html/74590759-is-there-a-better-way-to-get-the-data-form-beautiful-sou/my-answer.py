# Code from my Stack Overflow answer https://stackoverflow.com/a/74591114 (posted 2022-11-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
ionOptions = [{
    'ion': option.get_text(' ').strip(),
    'ion-formula': option.get('data-formula'),
    'm_z': option.get('data-mass-z-ratio')
} for option in soup.select('option[data-mass-z-ratio][data-formula]')]

# --- block 2 ---
[{'ion': '[M+H]+', 'ion-formula': 'C18H38NO2', 'm_z': '300.2897'},
 {'ion': '[M+H-H2O]+', 'ion-formula': 'C18H36NO', 'm_z': '282.2791'},
 {'ion': '[M.]+', 'ion-formula': 'C18H37NO2', 'm_z': '299.2819'},
 {'ion': '[M+2H]2+', 'ion-formula': 'C18H39NO2', 'm_z': '150.6485'},
 {'ion': '[M+3H]3+', 'ion-formula': 'C18H40NO2', 'm_z': '100.7681'},
 {'ion': '[M+4H]4+', 'ion-formula': 'C18H41NO2', 'm_z': '75.8279'},
 {'ion': '[M+K]+', 'ion-formula': 'C18H37KNO2', 'm_z': '338.2456'},
 {'ion': '[M+2K]2+', 'ion-formula': 'C18H37K2NO2', 'm_z': '188.6044'},
 {'ion': '[M+2K-H]+', 'ion-formula': 'C18H36K2NO2', 'm_z': '376.2015'},
 {'ion': '[M+Na]+', 'ion-formula': 'C18H37NNaO2', 'm_z': '322.2716'},
 {'ion': '[M+2Na]2+', 'ion-formula': 'C18H37NNa2O2', 'm_z': '172.6304'},
 {'ion': '[M+2Na-H]+', 'ion-formula': 'C18H36NNa2O2', 'm_z': '344.2536'},
 {'ion': '[M+Li]+', 'ion-formula': 'C18H37LiNO2', 'm_z': '306.2979'},
 {'ion': '[M+2Li]2+', 'ion-formula': 'C18H37Li2NO2', 'm_z': '156.6567'},
 {'ion': '[M+NH4]+', 'ion-formula': 'C18H41N2O2', 'm_z': '317.3162'},
 {'ion': '[M-H]-', 'ion-formula': 'C18H36NO2', 'm_z': '298.2752'},
 {'ion': '[M-2H]2-', 'ion-formula': 'C18H35NO2', 'm_z': '148.6339'},
 {'ion': '[M-3H]3-', 'ion-formula': 'C18H34NO2', 'm_z': '98.7535'},
 {'ion': '[M-4H]4-', 'ion-formula': 'C18H33NO2', 'm_z': '73.8133'},
 {'ion': '[M+Cl]-', 'ion-formula': 'C18H37ClNO2', 'm_z': '334.2518'},
 {'ion': '[M+OAc]-', 'ion-formula': 'C20H40NO4', 'm_z': '358.2963'},
 {'ion': '[M+HCOO]-', 'ion-formula': 'C19H38NO4', 'm_z': '344.2806'},
 {'ion': 'M(neutral)', 'ion-formula': 'C18H37NO2', 'm_z': '299.2824'}]

# --- block 3 ---
{'ion': '(Select m/z)', 'ion-formula': None, 'm_z': None}

# --- block 4 ---
for o in ionOptions:
    for k, v in o.items(): print(f'{k:>15} = {v}')
    print('-'*40)

# --- block 5 ---
# import pandas

print(pandas.DataFrame(ionOptions).to_markdown(index=False))
