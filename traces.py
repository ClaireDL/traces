#!/usr/bin/env python3

import json
# import pandas as pd

def scan(node):
    """ Gets the function name when scanning
    """
    # Checks if node is a dictionary
    if isinstance(node, dict):
        # Checks if the keys of interest are present
        if "operationName" in node and "duration" in node:
            # Checks the type of the value for operationName
            if isinstance(node.get("operationName"), str):
                # Gets operationName for the node
                node_operation_name = node.get("operationName")

            # Checks the type of the value for duration
            if isinstance(node.get("duration"), int):
                # Gets the duration for the node
                node_duration = node.get("duration")

            print("operation name: ", node_operation_name, " duration: ", node_duration)

        # Iterates through the values in the dictionary
        for key, inner_node in node.items():
            # Recursively call
            scan(inner_node)

        # if "operationName" in node and "duration" in node:
        #     exit(1)

    if isinstance(node, list):
        for n in node:
            scan(n)

# A function with children has:
# "hasChildren": true
# followed by "childSpanIds" with a list of spanIds

print("Traces")

with open('one_trace.json', 'r') as f:
    all_traces = json.load(f)
    for trace in all_traces["data"]:
        scan(trace)

# Print what we want in a table
# 1 Function path is the succession of nodes/operation names
# 2

# How to write into a dataframe: dict or list then convert
# df = pd.DataFrame(ds)

