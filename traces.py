#!/usr/bin/env python3

import json
import pandas as pd

def get_node_data(node, data={}):
    """ Get the data we want to extract: operationName and duration for each node
    """
    node_operation_name = ""
    node_duration = -1

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
        # Creates a new tuple with the data we need
        data = {"operation_name": node_operation_name, "duration": node_duration}
    return data

def scan(node, complete_path=""):
    """ Gets the function name when scanning
    """
    # Checks if node is a dictionary
    if isinstance(node, dict):
        # Gets operationName and duration
        node_data = get_node_data(node)
        if node_data:
            # Gets the complete path by adding current operation_name to node path
            complete_path = complete_path + "|" + node_data.get("operation_name")
            node_duration = node_data.get("duration")
            global flattened_trace
            global counter
            node_complete = {"trace_number": counter, "complete_path": complete_path, "duration": node_duration}

            flattened_trace.append(node_complete)
            #print(complete_path, node_duration)

        # Iterates through the values in the dictionary
        for key, inner_node in node.items():
            # Recursively calls scan
            scan(inner_node, complete_path)

        # if "operationName" in node and "duration" in node:
        #     exit(1)

    if isinstance(node, list):
        for n in node:
            scan(n, complete_path)

print("Traces")

# Loads the trace file and scans it
with open('trace_simplified.json', 'r') as f:
    all_traces = json.load(f)
    counter = 0
    flattened_trace = list({})
    for trace in all_traces["data"]:
        counter += 1
        #flattened_trace.append(counter_info)
        scan(trace)
    df = pd.DataFrame(flattened_trace)
    df_first_3 = df.head(3)
    print(df)
