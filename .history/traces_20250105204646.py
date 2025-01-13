#!/usr/bin/env python3

import json
# import ijson
# import pandas as pd

print("Traces")

# # Load Trace file into a dataframe
# with open('traces-1734533241362.json', 'r') as f:
#     data = json.load(f)
# df = pd.DataFrame(data)
# print(df)

# Open the JSON file and parse it with ijson
# with open('trace2.json', 'rb') as input_file:
#     parser = ijson.parse(input_file)
#     # load json iteratively
#     parser = ijson.parse(input_file)
#     for prefix, event, value in parser:
#         print('prefix={}, event={}, value={}'.format(prefix, event, value))

with open('traces2.json', 'r') as f:
    data = json.load(f)
    print(data)
