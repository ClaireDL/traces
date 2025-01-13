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

def get_paths(node, parent = ' ', sep = ' | '):
    paths = []
    if isinstance(node, dict):
        for key, n in node.items():
            if 'operationName' in items.keys():
                path = parent + sep + n.values()
                path.extend(get_path(n, paths, sep = sep))

    elif isinstance(node, list):
        for n in node:
            scan(n)
    return dict

print("Traces")

with open('one_trace.json', 'r') as f:
    all_traces = json.load(f)
    for trace in all_traces["data"]:
        # scan(trace)
        get_paths(trace)

# Print what we want in a table
# 1 Function path is the succession of nodes/operation names
# 2

# How to write into a dataframe: dict or list then convert
# df = pd.DataFrame(ds)
