# This program prints the list using reverse,sort,copy!

import os

List1 = [8,9,3,6,1,10]
List1.reverse()
print("The reversed list is", List1)

List2 = [91,67,120,34,76,54,78,87,56,64,345]
List2.sort()
print("The sorted list is", List2)

List3 = []
List3 = List1.copy()
print("List3 =", List3)

Indexvalue = List2[2:6]
print("The index values are",Indexvalue)
