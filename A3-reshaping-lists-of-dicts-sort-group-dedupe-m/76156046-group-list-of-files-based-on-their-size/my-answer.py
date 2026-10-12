# Code from my Stack Overflow answer https://stackoverflow.com/a/76448771 (posted 2023-06-11), extracted verbatim; may need the question's context to run.
# import os

max_group_size = 100000
docs = ['Doc3.pdf', 'Doc4.pdf', 'Doc2.pdf', 'Doc5.pdf', 'Doc1.pdf', 'Doc6.pdf']

grouped_docs, cur_size_total = [[]], 0
for d in docs:
    cur_doc_size = os.path.getsize(d)

    if (cur_size_total + cur_doc_size) > max_group_size:
        cur_size_total = 0
        grouped_docs.append([])

    grouped_docs[-1].append(d)
    cur_size_total += cur_doc_size
