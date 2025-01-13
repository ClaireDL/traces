#!/usr/bin/env python3

import json
import ijson
import pandas as pd

# def read_as_dataframe(File_json):
#     df_read_json = pd.read_json(json.dumps(File_json), orient='index')
#     print("Loading as DataFrame:")
#     return(df_read_json)


print("Traces")

# # Load Trace file into a dataframe
# with open('traces-1734533241362.json', 'r') as f:
#     data = json.load(f)
# df = pd.DataFrame(data)
# print(df)

# Open the JSON file
with open('traces-1734533241362.json', 'r') as file:
    # Parse the JSON objects one by one
    parser = ijson.items(file, 'item')

    # Iterate over the JSON objects
    for item in parser:
        print("it works")
        # Process each JSON object as needed
        print(item)
