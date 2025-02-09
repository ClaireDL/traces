#!/usr/bin/env python3

import json
import re
import pandas as pd
from tracestats import calculate_statistics
from prettyprint import set_pandas_display_options

def merge(source, destination):
    for key, value in source.items():
        if isinstance(value, dict):
            # get node or create one
            node = destination.setdefault(key, {})
            merge(value, node)
        else:
            destination[key] = value

    return destination

def get_node_data(node):
    """ Get the data we want to extract: operationName and duration for each node
    """
    data = {}

    # Checks if the keys of interest are present
    if "operationName" in node and "duration" in node:

        # Checks the type of the value for operationName
        if isinstance(node.get("operationName"), str):
            # Gets operationName for the node
            data["operation_name"] = node.get("operationName")

        # Checks the type of the value for duration
        if isinstance(node.get("duration"), int):
            # Gets the duration for the node
            data["node_duration"] = node.get("duration")

    # Return a dict with the data
    return data

def scan(trace_number, node, parent_path=""):
    """ Gets the function name when scanning
    """
    global collected_traces_dict

    # Checks if node is a dictionary
    if isinstance(node, dict):
        # Gets data from node
        node_data = get_node_data(node)
        if node_data:
            # Gets the complete path by adding current operation_name to node path
            current_path = parent_path + "|" + node_data["operation_name"]
            current_span_data = {
                trace_number: { # Column name
                    # Row       : value
                    current_path: node_data["node_duration"]
                }
            }
            collected_traces_dict = merge(collected_traces_dict, current_span_data)
            #collected_traces_dict = {**collected_traces_dict, **current_span_data}
        else:
            # Fab: not sure this is correct or needed
            current_path = parent_path + "|"

        # Iterates through the values in the dictionary
        for _, inner_node in node.items():
            # Recursively calls scan
            scan(trace_number, inner_node, current_path)

    if isinstance(node, list):
        for index, n in enumerate(node):
            if parent_path != "|":
                current_path = parent_path + "|" + str(index)
            else:
                current_path = parent_path
            scan(trace_number, n, current_path)

print("Traces")

collected_traces_dict = {}

# Loads the trace file and scans it
with open('traces-1734533241362.json', 'r') as f:
    all_traces = json.load(f)

    for trace_number, trace in enumerate(all_traces["data"]):
        scan(trace_number, trace)

    df = pd.DataFrame(collected_traces_dict)

    #set_pandas_display_options()
    print(df)
    exit(1)

    # Compare one trace trace to Referent trace 1
    # pivot['New'] = pivot['duration'][1].isnull() | pivot['duration'][2].isnull()
    # print(pivot)

    # Generalisation
    # for trace in pivot['duration'][2:]:
    #     pivot[trace] = pivot['duration'][1].isnull() & pivot['duration'][trace].isnull()

    # print(pivot)


    # test = ((pivot['duration'][1] == pivot['duration'][2]) | (pivot['duration'][1].isnull() & pivot['duration'][2].isnull())).all()
    # print(test)

