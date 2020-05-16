# This is not the script being executed. this is just a script
# to test and ease the development of the workflow. Code being
# executed is stored in info.plist and should be modified through
# alfred to take effect.
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

# Extract arguments from script
args = sys.argv[1].split()
query = " ".join(args[1:])

LANGUAGE_PROVIDED = True
# LANGUAGE_PROVIDED = os.environ['LANGUAGE_PROVIDED']

# Start your script
# important: It's important that you print nothing else to STDOUT, or it will make your XML/JSON invalid.


with open("./config.json") as f:
    config = json.load(f)

with open("./locales.json") as f:
    locales = json.load(f)

fmts = config['formats']
lngs = config['languages']
olang = args[0].strip()

if len(olang) == 2:
    name = locales[olang].get('name')
    format = locales[olang].get('default_format')
    olang = locales[olang].get('locale')
    
dt = dateparser.parse(query, languages=lngs)

result = {"items": []}
try:
    default_items = [
        {
            "valid": False,
            "icon": None,
            "title": fmt['format_string'],
            "subtitle": format_datetime(dt, format=fmt['format_string'], locale=olang),
            "text": {
                "copy": format_datetime(dt, format=fmt['format_string'], locale=olang),
                "largetype": format_datetime(dt, format=fmt['format_string'], locale=olang)
            }
        } for fmt in fmts
    ]
    result['items'] += default_items

    if LANGUAGE_PROVIDED:

        extra_item = {
            "valid": False,
            "icon": None,
            "title": format_datetime(dt, format=format, locale=olang),
            "subtitle": format + "Default for " + name,
            "text": {
                "copy": format_datetime(dt, format=format, locale=olang),
                "largetype": format_datetime(dt, format=format, locale=olang)
            }
        }
        result['items'] += [extra_item]

except Exception as e:
    # traceback.print_exc()
    pass

sys.stdout.write(json.dumps(result))


