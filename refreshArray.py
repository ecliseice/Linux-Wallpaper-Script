#!/usr/bin/env python3

ApiTextFile = */path_to_TEXT_file/*

f = open(ApiTextFile)
text = f.read()

import re

result = re.findall(r'_id":"[a-z0-9]+', text)

ArrayFile = */path_to_Arr_file/*

my_file = open(ArrayFile, "w")

for element in result:
    id = element.replace('"', '').split(':')
    my_file.write(id[1] + "\n")

my_file.close()
