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

def extract_path_element(node, key):
    if scan(node) == key:
        print(node.values())

print("Traces")

with open('traces-1734533241362.json', 'r') as f:
    all_traces = json.load(f)
    for trace in all_traces["data"]:
        # scan(trace)
        print(extract_path_element(trace, "operationID"))

# Print what we want in a table
# 1 Function path is the succession of nodes/operation names
#
