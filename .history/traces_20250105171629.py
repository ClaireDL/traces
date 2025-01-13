#!/usr/bin/env python3

import json
import ijson
# import pandas as pd

print("Traces")

# # Load Trace file into a dataframe
# with open('traces-1734533241362.json', 'r') as f:
#     data = json.load(f)
# df = pd.DataFrame(data)
# print(df)

# Open the JSON file
with open('example.json', 'rb') as input_file:
    parser = ijson.parse(input_file)
    for parent, data_type, value in parser:
        print('parent={}, data_type={}, value={}'.format(parent, data_type, value))
