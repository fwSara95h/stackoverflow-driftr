---
title: "is there a better way to get the data form beautiful soup query?"
site: stackoverflow
question_id: 74590759
answer_id: 74591114
url: https://stackoverflow.com/a/74591114
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-27T15:06:15Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74591114/revisions
accepted: false
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c6392bcfa1f9c0945b58c0408e7a98f1e0cdd9042c4bb5a78ccc39678ffd5524
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74591114>, 2022-11-27; score 1. Text as retrieved 2026-10-12.

I can't say what could be considered *elegant*, but I usually get data like this using `.get` and list comprehension
```python
ionOptions = [{
    'ion': option.get_text(' ').strip(),
    'ion-formula': option.get('data-formula'),
    'm_z': option.get('data-mass-z-ratio')
} for option in soup.select('option[data-mass-z-ratio][data-formula]')]
```
and `ionOptions` would look like
```python
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
```

**Note:** You can use `.find_all('option')` or `.select('option')` instead of *`.select('option[data-mass-z-ratio][data-formula]')`*, but then the first `option` tag would also get included:
```python
{'ion': '(Select m/z)', 'ion-formula': None, 'm_z': None}
```

---

You could print it in sections
```python
for o in ionOptions:
    for k, v in o.items(): print(f'{k:>15} = {v}')
    print('-'*40)
```
output:
```lang-none
            ion = [M+H]+
    ion-formula = C18H38NO2
            m_z = 300.2897
----------------------------------------
            ion = [M+H-H2O]+
    ion-formula = C18H36NO
            m_z = 282.2791
----------------------------------------
            ion = [M.]+
    ion-formula = C18H37NO2
            m_z = 299.2819
----------------------------------------
            ion = [M+2H]2+
    ion-formula = C18H39NO2
            m_z = 150.6485
----------------------------------------
            ion = [M+3H]3+
    ion-formula = C18H40NO2
            m_z = 100.7681
----------------------------------------
            ion = [M+4H]4+
    ion-formula = C18H41NO2
            m_z = 75.8279
----------------------------------------
            ion = [M+K]+
    ion-formula = C18H37KNO2
            m_z = 338.2456
----------------------------------------
            ion = [M+2K]2+
    ion-formula = C18H37K2NO2
            m_z = 188.6044
----------------------------------------
            ion = [M+2K-H]+
    ion-formula = C18H36K2NO2
            m_z = 376.2015
----------------------------------------
            ion = [M+Na]+
    ion-formula = C18H37NNaO2
            m_z = 322.2716
----------------------------------------
            ion = [M+2Na]2+
    ion-formula = C18H37NNa2O2
            m_z = 172.6304
----------------------------------------
            ion = [M+2Na-H]+
    ion-formula = C18H36NNa2O2
            m_z = 344.2536
----------------------------------------
            ion = [M+Li]+
    ion-formula = C18H37LiNO2
            m_z = 306.2979
----------------------------------------
            ion = [M+2Li]2+
    ion-formula = C18H37Li2NO2
            m_z = 156.6567
----------------------------------------
            ion = [M+NH4]+
    ion-formula = C18H41N2O2
            m_z = 317.3162
----------------------------------------
            ion = [M-H]-
    ion-formula = C18H36NO2
            m_z = 298.2752
----------------------------------------
            ion = [M-2H]2-
    ion-formula = C18H35NO2
            m_z = 148.6339
----------------------------------------
            ion = [M-3H]3-
    ion-formula = C18H34NO2
            m_z = 98.7535
----------------------------------------
            ion = [M-4H]4-
    ion-formula = C18H33NO2
            m_z = 73.8133
----------------------------------------
            ion = [M+Cl]-
    ion-formula = C18H37ClNO2
            m_z = 334.2518
----------------------------------------
            ion = [M+OAc]-
    ion-formula = C20H40NO4
            m_z = 358.2963
----------------------------------------
            ion = [M+HCOO]-
    ion-formula = C19H38NO4
            m_z = 344.2806
----------------------------------------
            ion = M(neutral)
    ion-formula = C18H37NO2
            m_z = 299.2824
----------------------------------------
```

---

I personally prefer to use pandas to get a tabular format:
```python
# import pandas

print(pandas.DataFrame(ionOptions).to_markdown(index=False))    
```
output:
```lang-none
| ion        | ion-formula   |      m_z |
|:-----------|:--------------|---------:|
| [M+H]+     | C18H38NO2     | 300.29   |
| [M+H-H2O]+ | C18H36NO      | 282.279  |
| [M.]+      | C18H37NO2     | 299.282  |
| [M+2H]2+   | C18H39NO2     | 150.649  |
| [M+3H]3+   | C18H40NO2     | 100.768  |
| [M+4H]4+   | C18H41NO2     |  75.8279 |
| [M+K]+     | C18H37KNO2    | 338.246  |
| [M+2K]2+   | C18H37K2NO2   | 188.604  |
| [M+2K-H]+  | C18H36K2NO2   | 376.202  |
| [M+Na]+    | C18H37NNaO2   | 322.272  |
| [M+2Na]2+  | C18H37NNa2O2  | 172.63   |
| [M+2Na-H]+ | C18H36NNa2O2  | 344.254  |
| [M+Li]+    | C18H37LiNO2   | 306.298  |
| [M+2Li]2+  | C18H37Li2NO2  | 156.657  |
| [M+NH4]+   | C18H41N2O2    | 317.316  |
| [M-H]-     | C18H36NO2     | 298.275  |
| [M-2H]2-   | C18H35NO2     | 148.634  |
| [M-3H]3-   | C18H34NO2     |  98.7535 |
| [M-4H]4-   | C18H33NO2     |  73.8133 |
| [M+Cl]-    | C18H37ClNO2   | 334.252  |
| [M+OAc]-   | C20H40NO4     | 358.296  |
| [M+HCOO]-  | C19H38NO4     | 344.281  |
| M(neutral) | C18H37NO2     | 299.282  |
```
