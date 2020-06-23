#!/usr/bin/env python3

import os
from json import dumps
from hashlib import md5


def calc_file_md5(filename):
    m = md5()

    with open(filename, 'rb') as f:
        m.update(f.read())

    return m.hexdigest()


result = {
    "clean": [],
    "infected": []
}

for path, _, files in os.walk("clean"):
    for f in files:
        file_path = '{}/{}'.format(path, f)
        t = {
            "md5": calc_file_md5(file_path),
            "name": file_path,
            "type": os.path.basename(path)
        }
        result["clean"].append(t)

for path, _, files in os.walk("infected"):
    for f in files:
        file_path = '{}/{}'.format(path, f)
        t = {
            "md5": calc_file_md5(file_path),
            "name": file_path,
            "type": os.path.basename(path)
        }
        result["infected"].append(t)

with open('files.json', 'w') as f:
    f.write(dumps(result, indent=4, sort_keys=True))

