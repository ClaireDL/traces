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
objects = ijson.items('example.json', "earth.europe.item")
cities = (o for o in objects if o['type'] == 'city')
for city in cities:
    print(city)
