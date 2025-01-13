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
with open('citylots.json', 'rb') as input_file:
    parser = ijson.parse(input_file)
    # load json iteratively
        parser = ijson.parse(input_file)
        for prefix, event, value in parser:
            print('prefix={}, event={}, value={}'.format(prefix, event, value))
