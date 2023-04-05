---
title: "traversing the multi index dictionaries which is present in dataframe & store the values in a list"
site: stackoverflow
question_id: 75937977
answer_id: 75943895
url: https://stackoverflow.com/a/75943895
author: "Jamie_B"
author_url: https://stackoverflow.com/users/13174162
posted: 2023-04-05T20:56:41Z
last_edited: never
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0f0f290dc47f4ba65ff8ba0e1a243f764be580ddff509b8c03ff3bf9f6a66e3f
role: another answer on the same question, kept as context; not my work
---

# Answer by [Jamie_B](https://stackoverflow.com/users/13174162) — 2023-04-05

Posted on Stack Overflow, <https://stackoverflow.com/a/75943895>, 2023-04-05; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

This should create a list of tuple. Each tuple will be the store_id and providor pair. The apply function is used to iterate over the RESPONSE column, and pass that cell's value to the extract_details function, which handles the main data extraction part.

    def extract_details(response):
    
        res = []
    
        # Check to ensure first two keys are in the response, otherwise quit early
        if not 'store-boundary-dsp' in response:
            return res
    
        if not 'estimates' in response['store-boundary-dsp']:
            return res
    
        # Iterate through each estimate
        for estimate in response['store-boundary-dsp']['estimates']:
            # Iterate through each key, value pair for the estimage
            store_id = ''
            providor = ''
            for k, v in estimate.items():
                
                if k == 'storeExternalId':
                    store_id = v
                if k == 'provider':
                    providor = v
            res.append((store_id, providor))
                    
        return res
    
    
    # For each cell in the 'RESPONSE' column, extract out the store_id, providor pair
    response_values = data_frame['RESPONSE'].apply(extract_details).tolist()
    response_values
    
    pair_values = [val for sublist in response_values for val in sublist]
    pair_values
