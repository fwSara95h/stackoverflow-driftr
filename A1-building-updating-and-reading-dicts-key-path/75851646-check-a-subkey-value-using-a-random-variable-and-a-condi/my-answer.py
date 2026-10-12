# Code from my Stack Overflow answer https://stackoverflow.com/a/75851696 (posted 2023-03-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
if data[random_data]["gender"] == "male":
    print(random_data, ": word is Male")
else:
    print(random_data, ": word is Female")

# --- block 2 ---
print(random_data, ": word is", "Male" if data[random_data]["gender"]=="male" else "Female")

# --- block 3 ---
print(random_data, ": word is", data[random_data]["gender"].capitalize())
