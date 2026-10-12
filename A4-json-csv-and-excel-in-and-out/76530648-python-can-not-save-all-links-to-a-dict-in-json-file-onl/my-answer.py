# Code from my Stack Overflow answer https://stackoverflow.com/a/76530840 (posted 2023-06-22), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>     all_links_dict = {}
>     for item in name_link:
>         value_links = ("https://www.sothebysrealty.com" + item.get("href"))
>     all_links_dict[number + 1] = value_links
>

# --- block 2 ---
all_links_dict = {}
for item in name_link:
    value_links = ("https://www.sothebysrealty.com" + item.get("href"))
    number += 1
    all_links_dict[number] = value_links

# --- block 3 ---
>     with open("all_links_dict.json", "w", encoding="utf-8-sig") as file:
>         json.dump(all_links_dict, file, indent=4, ensure_ascii=False)
>
