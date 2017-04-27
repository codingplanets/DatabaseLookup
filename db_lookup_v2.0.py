#!/usr/bin/env python
#|-------------------------------------------------------------------|#
#|  Usage: python db_lookup.py <string_to_search> </root/databases>  |#
#|  Simple database lookup | by Chris Poole                          |#
#|-------------------------------------------------------------------|#

import sys, os, time

if len(sys.argv) < 2:
    sys.exit("\033[37mUsage: python "+sys.argv[0]+" <string_to_search> </root/databases>")
    
print '''\033[32m
| --:          Simple database lookup          :-- |
| --:   github://codingplanets/DatabaseLookup  :-- |
\033[37m'''
print("\033[31m| --:  Devloped by Chris Poole | @codingplanets     :-- |\033[37m")

string = sys.argv[1]
databases = str(sys.argv[2])

os.system('grep -a -i -nr '+ sys.argv[1] +' '+ sys.argv[2] +'')
