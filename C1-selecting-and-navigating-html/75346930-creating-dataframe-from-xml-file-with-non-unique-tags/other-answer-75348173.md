---
title: "Creating dataframe from XML file with non-unique tags"
site: stackoverflow
question_id: 75346930
answer_id: 75348173
url: https://stackoverflow.com/a/75348173
author: "Hermann12"
author_url: https://stackoverflow.com/users/12621346
posted: 2023-02-04T20:30:21Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7efb368be2a4bc44e8e42000b12d4db5ba62ad02bd6b397bb80fb81ad0940d70
role: another answer on the same question, kept as context; not my work
---

# Answer by [Hermann12](https://stackoverflow.com/users/12621346) — 2023-02-04

Posted on Stack Overflow, <https://stackoverflow.com/a/75348173>, 2023-02-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

How looks your code? Here is my try.

    import xml.etree.ElementTree as ET
    import pandas as pd
    
    tree = ET.parse("zzTab.xml")
    root = tree.getroot()
    
    ns = "{http://sffe-ra.org/schema/1999/2023/BXF}"
    list_of_interest = [f"{ns}PathName", f"{ns}BHGXId", f"{ns}BrandName"]
    
    PathName_dir_list = []
    PathName_file_list = []
    BHGXId_list = []
    BrandName_list = []
    
    for elem in root.iter():
        #print(elem.tag, elem.text)
        if elem.tag in list_of_interest:
            if elem.tag == f"{ns}PathName" and '.mp4' not in elem.text:
                #print("Dir:",elem.text)
                PathName_dir_list.append(elem.text)
            if elem.tag == f"{ns}PathName" and '.mp4' in elem.text:
                #print("File:",elem.text)
                PathName_file_list.append(elem.text)          
            if elem.tag == f"{ns}BHGXId":
                #print("ID", elem.text)
                BHGXId_list.append(elem.text)
            if elem.tag == f"{ns}BrandName":
                print("Brand", elem.text)
                BrandName_list.append(elem.text)
    
    t = zip(PathName_dir_list, PathName_file_list,  BHGXId_list, BrandName_list,)
    list_of_tuples = list(t)
    
    df = pd.DataFrame(list_of_tuples, columns = ['Path', 'File', 'ID', 'Brand'])
    df.to_csv('file_list.csv')
    print(df)
