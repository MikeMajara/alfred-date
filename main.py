# This is not the script being executed. this is just a script
# to test and ease the development of the workflow. Code being
# executed is stored in info.plist and should be modified through
# alfred to take effect.
# 
# Useful documentation: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
# date format patterns: https://unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns
# Babel documentation: http://babel.pocoo.org/en/latest/dates.html?highlight=pattern#pattern-syntax


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
from babel.dates import format_datetime

# Get argument
query = sys.argv[1]

# Start your script
# important: It's important that you print nothing else to STDOUT, or it will make your XML/JSON invalid.


with open("./config.json") as f:
    config = json.load(f)

fmts = config['formats']
lngs = config['languages']
output_language = config['output_language']

dt = dateparser.parse(query, languages=lngs)

items = [
    {
        "valid": False,
        "icon": None,
        "title": format_datetime(dt, format=fmt['format_string'], locale=output_language),
        "subtitle": fmt['format_string'],
        "text": {
            "copy": format_datetime(dt, format=fmt['format_string'], locale=output_language),
            "largetype": format_datetime(dt, format=fmt['format_string'], locale=output_language)
        }
    } for fmt in fmts
]

sys.stdout.write(json.dumps({"items":items}))
