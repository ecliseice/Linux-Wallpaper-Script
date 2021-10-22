#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open('/root/arr')
array = f.read().split("\n")
f.close()

f = open('/root/currentNum')
number = int(f.read())
f.close()

location = */path_to_wallpaper_file/*

bashCommand = "wget -O " + location + " http://api.deckchair.com/v1/viewer/camera/" + array[number]

import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
