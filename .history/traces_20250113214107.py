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
    operation_name = ""
    duration = ""

    if isinstance(node, dict):
        if "operationName" in node and "duration" in node:
            #print(node)
            for key, inner_node in node.items():
                if key == 'operationName' and isinstance(inner_node, str):
                    global operation_name
                    operation_name = inner_node
                    #print("   FOUND OPERATION_NAME")
                if key == 'duration' and isinstance(inner_node, int):
                    global duration
                    duration = inner_node
                print("operation name: ", operation_name, " duration: ", duration)
                get_operation_name(inner_node)

        #if "operationName" in node and "duration" in node:
        #    exit(1)

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
