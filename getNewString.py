#!/usr/bin/env python3

arrFile = */path_to_ArrayFile/*

f = open(arrFile)
text = f.read()

array = text.split("\n")


CurrentNum = */path_to_CurrentNum/*

f = open(CurrentNum)
number = int(f.read())


if number < len(array):
    print number
    my_file = open(CurrentNum, "w")
    number = number + 1
    my_file.write(str(number))
    my_file.close()
else:
    my_file = open(CurrentNum, "w")
    number = 0
    my_file.write(str(number))
    my_file.close()
