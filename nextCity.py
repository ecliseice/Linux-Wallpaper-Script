#!/usr/bin/env python3

f = open("arr","r+")
array = f.read()
f.close()


n = open("currentNum")
number = int(n.read())+1
n.close()
n = open("currentNum","w")
n.write(str(number))


lines = array.split("\n")

f.close()

downloadAndSetScript = */path_to_downloadAndSet.py/*

import subprocess; 
subprocess.Popen(downloadAndSetScript, shell=True) 
