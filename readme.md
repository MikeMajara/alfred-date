# Date timestamp 🕐

## Motivation
There is a bunch of ways to get your date right, right? And now that we have intelligent operative systems that parse our dates automatically we could go to Apple Notes whenever we want to get an date automatically detected, write it down, and wait for macOS to detect it is a date, then we could go click on it and create an event...

Or we could just install this workflow parse whatever we want in whichever language we want, and copy pasta it as needed. You choose! 😉

## Usage 📜
Gets timestamp using natural language
`dt [moment]`
#### Examples
- `dt now`
- `dt 1 day ago`
- `dt in 2 weeks`
- `dt six hours ago`

You can also specify the output language for the date. This is most useful when you are wanting to get names of days or months generated, or when you want specific common format for a language. For example, germans use a dot to separate day.month.year, and americans sorting is month/day/year, as compared to spanish which is day/month/year. Note that there is a difference between the input (understanding or parsing) language and the output language.
`dtl [lang] [moment]`
#### Examples
- `dtl de mañana`
- `dtl en morgen`
- `dtl es tomorrow`

Once you have your desired timestamp
1. Navigate through the list to select a timestamp format
2. ⌘ + c to copy the result shown

#### Language support
When installed the workflow 
- is set to understand: es 🇪🇸, en 🇺🇸, de 🇩🇪
- supports as explicitly given output: en 🇺🇸, zh 🇨🇳, ru 🇷🇺, fr 🇫🇷, es 🇪🇸, de 🇩🇪, pt 🇵🇹, it 🇮🇹, ja 🇯🇵

If you want to configure the workflow it
- understands following languages (see Settings on how to set up yours): [dateparser – python parser for human readable dates — DateParser 0.7.4 documentation](https://dateparser.readthedocs.io/en/latest/#supported-languages-and-locales)
- and speaks the following languages (see Settings to set up your own): [Babel locale aliases](https://github.com/python-babel/babel/blob/8b684d56e90d593d4f431263a6a3fea1aabc0d0c/babel/core.py#L80)

## Instalation 👷🏻‍♂️
1. [Download the workflow](https://github.com/MikeMajara/alfred-date-time-stamp-parser/releases/tag/0.1.0)
2. Double click the `.alfredworkflow` file to install

💡 **Required: [Alfred Powerpack](https://www.alfredapp.com/powerpack/)**.

## Settings ⚙️
use `dtconf` to configure basic settings and locales.

settings (config.json)
- **languages**: array - languages to parse. give a hint of the language(s) the workflow would be expecting.
- **out_lang**: string - language you want the output to be in,
- **formats**: array of objects - 
    - **title**: string - menu item name to display
    - **format_string**: string - unicode compliant date format. @see [UTS #35: Unicode LDML: Dates](https://unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns)

supported locales (locales.json)
You will also find a file `locales.json`, feel free to add support for your locale if it is not there. PRs are welcome.

## Roadmap 🛣

- [x] Add locale settings 👂🏻👅 5/16/20, 6:06 PM ← this date was generated with this workflow. Could you not tell?
- [ ] Support for emojis in item results. (E.g.: to show flags)

## ACK

<div>Workflow icon made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

## License 🗝
MIT License

Copyright (c) 2020 MikeMajara
