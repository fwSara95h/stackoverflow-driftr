# Code from my Stack Overflow answer https://stackoverflow.com/a/75920474 (posted 2023-04-03), extracted verbatim; may need the question's context to run.
# import os

def is_known():
    input_fp = "data/data_known.csv"
    is_new_file = not os.path.isfile(input_fp)
    with open(input_fp, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=current_card.keys())
            if is_new_file: 
                writer.writeheader()
                is_new_file = False ## update flag in case this is in a loop
            writer.writerow(current_card)
