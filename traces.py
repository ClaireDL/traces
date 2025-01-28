#!/usr/bin/env python3

import json
# import pandas as pd

def get_node_data(node, data=tuple()):
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
        data = data + (node_operation_name, node_duration)
    return data

def scan(node, output='data.json', complete_path=""):
    """ Gets the function name when scanning
    """

    # Checks if node is a dictionary
    if isinstance(node, dict):
        # Gets operationName and duration
        node_data = get_node_data(node)
        if node_data:
            # Gets the complete path by adding current operation_name to node path
            complete_path = complete_path + "|" + node_data[0]
            new_data = {'complete_path': complete_path, 'node_duration': node_data[1]}
            file = open(output, 'a', encoding='utf-8')
            file.write(str(new_data) + '\n')
            print("writing: ", new_data)
            file.close()
            #print("complete path: ", complete_path, " duration: ", node_data[1])

        # Iterates through the values in the dictionary
        for key, inner_node in node.items():
            # Recursively calls scan
            scan(inner_node, output, complete_path)

        # if "operationName" in node and "duration" in node:
        #     exit(1)

    if isinstance(node, list):
        for n in node:
            scan(n, output, complete_path)

print("Traces")

with open('one_trace.json', 'r') as f:
    all_traces = json.load(f)

    for trace in all_traces["data"]:
        scan(trace, 'one_trace_data_structure.json')
