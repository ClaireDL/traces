#!/usr/bin/env python3

import json
# import pandas as pd

def scan1(node):
    """ First version that just scans the data structure recursively
    """
    if isinstance(node, dict):
        for key, n in node.items():
            if key == 'operationName':
                print(node.get('operationName'))
            scan1(n)

    elif isinstance(node, list):
        for n in node:
            scan1(n)

def scan2(node):
    """ Second version that does not work: node_operation_name and node_duration are re-initialised
    before reaching the second key-value pair (key= 'duration')
    """
    if isinstance(node, dict):
        if "operationName" in node and "duration" in node:
            print(node.get("operationName"), node.get("duration"))

        for key, inner_node in node.items():
            print(key + " : " + str(inner_node))
            node_operation_name = ""
            node_duration = 0

            print("FOUND OPERATION_NAME ", node_operation_name)
            if key == 'operationName' and isinstance(inner_node, str):
                node_operation_name += inner_node
                node_operation_name = inner_node
                print("   FOUND OPERATION_NAME")
                print(node_operation_name)

            if key == 'duration' and isinstance(inner_node, int):
                node_duration += inner_node
                print("   FOUND DURATION")
                print(node_duration)

            if node_operation_name != "" and node_duration is not None:
                print("FOUND OPERATION_NAME AND DURATION")
                print("", node_operation_name,"", node_duration)

            scan(inner_node)

        if "operationName" in node and "duration" in node:
            exit(1)

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

