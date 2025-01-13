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

def get_operation_name(node):
    """ Gets the function name when scanning
    """
    if isinstance(node, dict):
        for key, n in node.items():
            node_operation_name = None
            node_duration = None

            if key == 'operationName' and isinstance(n, str):
                operation_name = n
            if key == 'duration' and isinstance(n, int):
                duration = n

            if node_operation_name is not None and node_duration is not None:
            print(operation_name, " ", duration)
            get_operation_name(n)

    elif isinstance(node, list):
        for n in node:
            get_operation_name(n)


# A function with children has:
# "hasChildren": true
# followed by "childSpanIds" with a list of spanIds

print("Traces")

with open('one_trace.json', 'r') as f:
    all_traces = json.load(f)
    for trace in all_traces["data"]:
        # scan(trace)
        get_operation_name(trace)

# Print what we want in a table
# 1 Function path is the succession of nodes/operation names
# 2

# How to write into a dataframe: dict or list then convert
# df = pd.DataFrame(ds)
