#-----------------------------------------------------------------------------
# Name:        Dictionaries Example 6 - Ordering a List (kinda!)
# Purpose:     And Example file demoing actors
#
# Author:      Mr. Brooks
# Created:     11-Nov-2020
# Updated:     11-Nov-2020
#-----------------------------------------------------------------------------

x = {'a': 2, 'b': 4, 'c': 3, 'd': 1, 'e': 0}

print(x.keys())
print(x.values())
print(x.items())

#https://www.w3schools.com/python/ref_func_sorted.asp
#Dicts are inherently unordered...but you can put them into a list and then order the values
#Works well if you only want to DISPLAY the sorted values
print(sorted(x.items()))  #Returns a sorted list...but how to we tell it what to sort by?

#https://docs.python.org/3/library/operator.html#operator.itemgetter
#Use the item getter command
import operator #Remember that imports should normally be at the beginning of your program
print(sorted(x.items(), key=operator.itemgetter(1))) #Tell it to sort by the second element of each tuple