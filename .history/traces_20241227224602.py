#!/usr/bin/env python3

import json
import pandas as pd

def read_as_dataframe(File_json):
    data_df = pd.read_json(File_json)
    print("it worked")
    return data_df

print("Traces")
read_as_dataframe('C:/Users/chdell/Programming/traces/traces.py',)
