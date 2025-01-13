#!/usr/bin/env python3

# https://www.freecodecamp.org/news/how-to-flatten-a-dictionary-in-python-in-4-different-ways/

import json

from collections.abc import MutableMapping

def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str ='.') -> MutableMapping:
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

with open('traces-1734533241362.json', 'r') as f:
    all_traces = json.load(f)
    for trace in all_traces["data"]:
        complete = flatten_dict(trace)
        selection = {k: trace[k] for k in list(trace)[:1]}
        print(selection)
