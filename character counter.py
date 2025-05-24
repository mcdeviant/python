#!/usr/bin/python3

import pprint
MESSAGE =  'This script counts occurrences of each character in this message. 122333444455555.'
COUNT = {}

for CHARACTER in MESSAGE.upper():
    COUNT.setdefault(CHARACTER, 0)
    COUNT[CHARACTER] = COUNT[CHARACTER] + 1

pprint.pprint(MESSAGE)
pprint.pprint(COUNT)
