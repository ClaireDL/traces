#!/usr/bin/env python3

import json
import pandas as pd

# def read_as_dataframe(File_json):
#     df_read_json = pd.read_json(json.dumps(File_json), orient='index')
#     print("Loading as DataFrame:")
#     return(df_read_json)

print("Traces")
df_read_json = pd.read_json(json.dumps('C:/Users/chdell/Programming/traces/example.py'), orient='index')
print(data)
