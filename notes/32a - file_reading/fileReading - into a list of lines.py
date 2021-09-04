#-----------------------------------------------------------------------------
# Name:        File Reading (fileReading - into a list of lines.py)
# Purpose:     To provide examples of how to read from files.
#              Example from http://openbookproject.net/thinkcs/python/english3e/files.html
#
# Author:      Mr. Brooks
# Created:     21-Oct-2020
# Updated:     21-Oct-2020
#-----------------------------------------------------------------------------
#
f = open("fruit.txt", "r") # Open the file
fileList = f.readlines()         # Read the file into a list
f.close()                  # Close the file

print(fileList)