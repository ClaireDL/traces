#!/usr/bin/env python3

import json
import ijson
import pandas as pd

print("Traces")

# # Load Trace file into a dataframe
# with open('traces-1734533241362.json', 'r') as f:
#     data = json.load(f)
# df = pd.DataFrame(data)
# print(df)

# Open the JSON file
# Open the JSON file
with open('traces-1734533241362.json', 'r') as file:
    # Parse the JSON array items one by one
    array_items = ijson.items(file, 'item')

    # Iterate over the JSON array items
    for item in array_items:
        # Process each JSON array item as needed
        print(item)
