#!/usr/bin/env python
#|---------------------------------------------|#
#|  Usage: python db_lookup.py <database.sql>  |#
#|  Simple database lookup | by Chris Poole    |#
#|---------------------------------------------|#

import sys

if len(sys.argv) < 2:
    sys.exit("\033[37mUsage: python "+sys.argv[0]+" [database.sql]")
    
print '''\033[32m
| --:  Please enter username/email/password or any  :-- |
| --:  string you want to look for.                 :-- |
\033[37m'''
print("\033[31m| --:  Devloped by Chris Poole | @codingplanets     :-- |\033[37m")

string = raw_input("String To Search: ")

with open(sys.argv[1], 'r') as data:
    for grep in data:
        if string in grep:
			print grep
