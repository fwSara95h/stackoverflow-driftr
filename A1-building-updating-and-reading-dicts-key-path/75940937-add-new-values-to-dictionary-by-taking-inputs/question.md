---
title: "Add new values to dictionary by taking inputs"
site: stackoverflow
question_id: 75940937
url: https://stackoverflow.com/q/75940937
asked: 2023-04-05T14:52:55Z
asked_by: "Param Dhingana"
asked_by_url: https://stackoverflow.com/users/17261398
last_edited: never
tags: [python, dictionary, tkinter, tkinter-entry]
score: -1
views_at_snapshot: 85
answer_count: 1
accepted_answer_id: 75949885
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bfc24c0e0c33d0ebd06add67dbd11bf25e790748a4ca3b82a06377bedc0325b4
---

# Add new values to dictionary by taking inputs

Asked by [Param Dhingana](https://stackoverflow.com/users/17261398) on Stack Overflow, <https://stackoverflow.com/q/75940937>, 2023-04-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have this following code, where I want to add the new values and add new row to the dictionary if some conditions are satisfied. And then print the dictionary in a text_widget.


```
def add_preprocessing_operation():
            # Clear the text_widget4 before updating
            text_widget4.delete('1.0', tk.END)

            # Get the inputs from the user
            sr_num_operation = int(input1.get())
            column_name = input2.get()

            # Call the check_preprocessing_operation() function
            preprocessing_dict = {}
            try:
                check_preprocessing_operation(df, sr_num_operation, column_name, preprocessing_dict)
            except ValueError as e:
                # Show a pop-up message if there is an error
                messagebox.showerror("Error", e)
                return

            # If there are any preprocessing operations in the dictionary, print them to text_widget4
            if preprocessing_dict:
                table = tabulate(preprocessing_dict.items(), headers=["Column Name", "Data-Preprocessing Operation"], tablefmt="grid", numalign="center", stralign="center")
                text_widget4.insert(tk.END, table)

            # If there are more than one row, add a newline character
            if table.count('\n') > 1:
                text_widget4.insert(tk.END, '\n')
                    
        def check_preprocessing_operation(df, sr_num_operation, column_name, preprocessing_dict):
            if sr_num_operation not in range(1, 10) or column_name not in df.columns:
                if sr_num_operation not in range(1, 10):
                    print("Invalid operation entered. Check list for reference!")
                if column_name not in df.columns:
                    print("Column ", column_name, " does not exist in the DataFrame.")
                return

            preprocessing_operation = preprocessing_operations[sr_num_operation]

            if len(preprocessing_dict) >= 10:
                raise ValueError("Maximum number of preprocessing operations reached. Cannot add more operations.")

            if preprocessing_operation == "Remove Rows with Null Values":
                if df[column_name].isnull().values.any():
                    messagebox.showerror("Error", "Operation cannot be applied to column. Column does not contains null values.")
                    return
                else:
                    preprocessing_dict.setdefault(column_name, []).append(preprocessing_operation)

            elif preprocessing_operation in ["Replace Null Values by Mean", "Replace Null Values by Median", "Replace Null Values by Mode"]:
                if df[column_name].dtype.kind not in 'fi':
                    messagebox.showerror("Error", "Operation cannot be applied to column. Column does not contain numeric data.")
                    return
                else:
                    preprocessing_dict.setdefault(column_name, []).append(preprocessing_operation)

            elif preprocessing_operation == "Perform One Hot Encoding":
                if df[column_name].dtype.kind not in 'O':
                    messagebox.showerror("Error", "Operation cannot be applied to column. Column does not contain categorical data.")
                    return
                else:
                    preprocessing_dict.setdefault(column_name, []).append(preprocessing_operation)

            elif preprocessing_operation == "Perform Label Encoding":
                if df[column_name].dtype.kind not in 'O':
                    messagebox.showerror("Error", "Operation cannot be applied to column. Column does not contain categorical data.")
                    return
                else:
                    preprocessing_dict.setdefault(column_name, []).append(preprocessing_operation)

            elif preprocessing_operation in ["Perform Min Max Scaling", "Perform Standardization", "Find Outliers and Remove the Rows with Outliers"]:
                if df[column_name].dtype.kind not in 'fi':
                    messagebox.showerror("Error", "Operation cannot be applied to column. Column does not contain numeric data.")
                    return
                else:
                    preprocessing_dict.setdefault(column_name, []).append(preprocessing_operation)

            else:
                print("Invalid operation entered.")

        
        add_button = tk.Button(inputs_frame, text="Add", width=10, command=add_preprocessing_operation)        
        add_button.grid(row=2, column=0, columnspan=2, pady=5)
```


But this code rather seems to over-write the dictionary and not add value in rows to it! For an overview, the screenshots are pasted below

[![In Step 1](https://i.sstatic.net/sBu6U.png)](https://i.sstatic.net/sBu6U.png)

[![In Step 2](https://i.sstatic.net/c8hwf.png)](https://i.sstatic.net/c8hwf.png)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-04-05): Is the indentation in your code snippet correct? Is `def check_preprocessing_operation` really supposed to be a nested function inside `def add_preprocessing_operation`?
- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-04-05): Every time you call the function you do `preprocessing_dict = {}` which makes a new, empty dictionary. How do you expect to accumulate values over time if you do that? You need to create the dictionary just once, and update it in the function.
- **[JonSG](https://stackoverflow.com/users/218663)** (2023-04-05): every time you call `add_preprocessing_operation()` you reset `preprocessing_dict`
- **[JRiggles](https://stackoverflow.com/users/8512262)** (2023-04-05): Does [this answer](https://stackoverflow.com/a/1024851/8512262) help? It (and the comments below) discuss appending new keys to an existing dictionary
