#!/usr/bin/env python
#|---------------------------------------------------------------|#
#|  Usage: python db_lookup.py <database.sql> <string_to_search> |#
#|  Simple database lookup | by Chris Poole                      |#
#|---------------------------------------------------------------|#

import sys

if len(sys.argv) < 2:
    sys.exit("\033[37mUsage: python "+sys.argv[0]+" <database.sql> <string_to_search>")
    
print '''\033[32m
| --:          Simple database lookup          :-- |
| --:   github://codingplanets/DatabaseLookup  :-- |
\033[37m'''
print("\033[31m| --:        Developed by Chris Poole          :-- |\033[37m")

string = str(sys.argv[2])

with open(sys.argv[1], 'r') as data:
    for grep in data:
        if string in grep:
			print grep
