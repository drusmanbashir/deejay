# encoding: utf-8
# Desc – Script to Generate Pygments Styles.
# Author – Robert Tagg - http://www.rt-coding.com
# Usage – In terminal type: python filename.py pygments.css

import sys

from pygments.formatters import HtmlFormatter
from pygments.styles import get_all_styles

# Grab all the possible styles
styles = list(get_all_styles())

print("\nAll built in styles for Pygments: ")
for style in styles:
    print('- ' + style)

# Enter name of style from the above list.
pick_style = raw_input('\nEnter name of chosen style: ')

# Check user input is a valid style
while pick_style not in styles:
    print('A Style with that name does not exist. Please try again.')
    pick_style = raw_input('\nEnter name of chosen style: ')       
else:
    # If valid then create the CSS file
    f = open(sys.argv[1], 'w')
    f.write(HtmlFormatter(style=pick_style).get_style_defs('.highlight'))
    f.close()
    print('Style successfully generated.')
