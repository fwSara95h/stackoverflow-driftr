# Code from my Stack Overflow answer https://stackoverflow.com/a/75730126 (posted 2023-03-14), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>     if "LogDetails" in jsondata["Job"]["LoggingData"]["Logs"]:
>         jsondata["Job"]["LoggingData"]["Logs"]["LogDetails"].append(new_data)
>

# --- block 2 ---
jsonfile = {
    "Job": {
        "id": "",
        "LoggingData": {
            "Logs":{"LogDetails": [{}]} ## NOT [{"LogDetails": [{}]}]
        }
    }
}

# --- block 3 ---
if "LogDetails" in jsondata["Job"]["LoggingData"]["Logs"][0]:
    print("Joy - Found LogDetails") 
    jsondata["Job"]["LoggingData"]["Logs"][0]["LogDetails"].append(new_data)
