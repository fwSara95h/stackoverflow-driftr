# Code from my Stack Overflow answer https://stackoverflow.com/a/75546639 (posted 2023-02-23), extracted verbatim; may need the question's context to run.
with open('testaccount.json', 'r') as f: 
    data = json.load(f)

for ri, record in enumerate(data["account_details"]):
    if record["Username"] == "TestingUsername":
        new_data = {'Details': {'Preset1': {
                    'Username': 'TestingUsername',
                    'Password': 'TestingPassword3',
                    'URL': 'TestingURL.com:'          }}}

        data["account_details"][ri].update(new_data)
# print(data)

with open('testaccount.json', 'w') as f: 
    json.dump(data, f, indent=4)
