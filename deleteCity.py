#!/usr/bin/env python3

f = open("arr","r+")
array = f.read()
f.close()
f = open("arr","w")


n = open("currentNum")
number = int(n.read())
n.close()

lines = array.split("\n")

for line in lines:
    if line != lines[number]:
        if line != "":
            f.write(line+"\n")

f.close()

downloadAndSetScript = */path_to_downloadAndSet.py/*

import subprocess; 
subprocess.Popen(downloadAndSetScript, shell=True) 
