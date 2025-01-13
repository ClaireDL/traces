#!/usr/bin/env python3

import json
import pandas as pd

def read_as_dataframe(File_json):
    df_read_json = pd.read_json(json.dumps(File_json), orient='index')
    print("DataFrame using pd.read_json() method:")
    return(df_read_json)

print("Traces")
data = read_as_dataframe('C:/Users/chdell/Programming/traces/traces.py',)
print(data)
