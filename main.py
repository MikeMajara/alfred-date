# This script is duplicated and functionality is implemented for
# both locigs: (with | without) language. Logic should be common
# and only change is LANGUAGE_PROVIDED.
# 
# $WORKFLOW_DIRECTORY/main.py is not the script being executed. 
# it is just a script to test and ease the development of the workflow. 
# Code being executed is stored in info.plist and should be modified through
# alfred to take effect.
# 
# important: print nothing else to STDOUT, or it will make your XML/JSON invalid.
# 
# Useful documentation: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
# date format patterns: https://unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns
# Babel documentation: http://babel.pocoo.org/en/latest/dates.html?highlight=pattern#pattern-syntax

import os, sys
import traceback
import json

# add local library path to python path.
# needed to import 3rd party library installed.
# 
# install command example (cd to workflow directory):
# pip install --prefer-binary --target=./lib dateparser
sys.path = [os.path.abspath('./lib')] + sys.path

import dateparser
from babel.dates import format_datetime

LANGUAGE_PROVIDED = True

# Extract arguments from script
args = sys.argv[1].split()

with open("./config.json") as f:
    config = json.load(f)

with open("./locales.json") as f:
    locales = json.load(f)

fmts = config['formats']
lngs = config['languages']

if LANGUAGE_PROVIDED:
    query = " ".join(args[1:])
    out_lang = args[0].strip()
    if len(out_lang) == 2:
        name = locales[out_lang].get('name')
        format = locales[out_lang].get('default_format')
        out_lang = locales[out_lang].get('locale')
else:
    query = " ".join(args)
    out_lang = config['out_lang']
    
dt = dateparser.parse(query, languages=lngs)

result = {"items": []}
try:
    default_items = [
        {
            "valid": False,
            "icon": None,
            "title": fmt['format_string'],
            "subtitle": format_datetime(dt, format=fmt['format_string'], locale=out_lang),
            "text": {
                "copy": format_datetime(dt, format=fmt['format_string'], locale=out_lang),
                "largetype": format_datetime(dt, format=fmt['format_string'], locale=out_lang)
            }
        } for fmt in fmts
    ]
    result['items'] += default_items

    if LANGUAGE_PROVIDED:

        extra_item = {
            "valid": False,
            "icon": None,
            "title": format_datetime(dt, format=format, locale=out_lang),
            "subtitle": format + " - Default for " + name,
            "text": {
                "copy": format_datetime(dt, format=format, locale=out_lang),
                "largetype": format_datetime(dt, format=format, locale=out_lang)
            }
        }
        result['items'] += [extra_item]

except Exception as e:
    traceback.print_exc()
    # pass

sys.stdout.write(json.dumps(result))
