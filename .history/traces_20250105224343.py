#!/usr/bin/env python3

import json
# import pandas as pd

print("Traces")

with open('traces-1734533241362.json', 'r') as f:
    all_traces = json.load(f)

    print("All keys")
    for node in all_traces["data"]:
        print(key)

def scan(node):
    if isinstance(node, dict):
        for key, n in node.items():
            scan(n)
    elif isinstance(node, list):
        for n in node:
            scan(n)

