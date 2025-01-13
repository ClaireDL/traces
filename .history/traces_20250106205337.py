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


print("Traces")

with open('traces-1734533241362.json', 'r') as f:
    all_traces = json.load(f)
    for trace in all_traces["data"]:
        scan(trace)

# Print what we want in a table
# 1 Function path is the succession of nodes/operation names
#
