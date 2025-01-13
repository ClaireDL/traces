#!/usr/bin/env python3

import json
# import pandas as pd

def scan(node):
    if isinstance(node, dict):
        for key, n in node.items():
            scan(n)

    elif isinstance(node, list):
        for n in node:
            scan(n)

# def pair_up(function):
#     if 'hasChildren' in scan(n).key:
#         print()

print("Traces")

with open('one_trace.json', 'r') as f:
    all_traces = json.load(f)
    for trace in all_traces["data"]:
        if 'operationName' in scan(trace).key:
            print(trace).get('operationName')

# Print what we want in a table
# 1 Function path is the succession of nodes/operation names
# 2

# How to write into a dataframe: dict or list then convert
# df = pd.DataFrame(ds)


