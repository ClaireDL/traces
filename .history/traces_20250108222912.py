#!/usr/bin/env python3

import json
# import pandas as pd

def scan(node):
    if isinstance(node, dict):
        for key, n in node.items():
            if key == 'operationName':
                print(node.get('operationName'))
            scan(n)

    elif isinstance(node, list):
        for n in node:
            scan(n)

def get_paths(node, parent = '', sep = '|'):
    paths = []
    if isinstance(node, dict):
        for key, n in node.items():
            if key == 'operationName':
                function = node.get('operationName')
                print(function)
            get_paths(n, paths, sep = sep)

    elif isinstance(node, list):
        for n in node:
            get_paths(n, paths, sep = sep)

    return paths

print("Traces")

with open('one_trace.json', 'r') as f:
    all_traces = json.load(f)
    for trace in all_traces["data"]:
        # scan(trace)
        functionPath = get_paths(trace)


# Print what we want in a table
# 1 Function path is the succession of nodes/operation names
# 2

# How to write into a dataframe: dict or list then convert
# df = pd.DataFrame(ds)
