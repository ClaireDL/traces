#!/usr/bin/env python3

import json
# import pandas as pd

print("Traces")

with open('traces-1734533241362.json', 'r') as f:
    all_traces = json.load(f)

    print("All keys")
    for key, n in node.items():
        print(key)

    print(all_traces)

def scan(node):
    if isinstance(node, dict):
        for key, n in node.items():
            scan(n)
    else if isinstance(node, list):
        for n in node:
            scan(n)

