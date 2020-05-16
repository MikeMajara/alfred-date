# This is not the script being executed. this is just a script
# to test and ease the development of the workflow. Code being
# executed is stored in info.plist and should be modified through
# alfred to take effect.
# 
# Useful documentation: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/

import os
import sys
import json

# add local library path to python path.
# needed to import 3rd party library installed.
# 
# install command example (cd to workflow directory):
# pip install --prefer-binary --target=./lib dateparser
sys.path = [os.path.abspath('./lib')] + sys.path
import dateparser

# Get argument
query = sys.argv[1]

# Start your script
# important: It's important that you print nothing else to STDOUT, or it will make your XML/JSON invalid.

dt = dateparser.parse(query)

with open("./config.json") as f:
    config = json.load(f)

fmts = config['formats']

items = [
    {
        "valid": False,
        "icon": None,
        "title": dt.strftime(fmt['format_string']),
        "subtitle": fmt['format_string'],
        "text": {
            "copy": dt.strftime(fmt['format_string']),
            "largetype": dt.strftime(fmt['format_string'])
        }
    } for fmt in fmts
]

sys.stdout.write(json.dumps({"items":items}))
