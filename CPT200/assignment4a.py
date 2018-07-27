# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 20:36:49 2018

@author: Whil

This program is designed to take in 20 numbers, then display the max, min and sum.
I'll do 10.
Assuming all the input is numbers.
"""

# List comprehension with split()
ints = [int(n) for n in (input("Enter 10 numbers separated by spaces: ")).split()]
ints.sort()

print("smallest number: {smallest}".format(smallest = ints[0]))
print("largest number: %d" % (ints[-1]))
print("Sum: %d" % sum(ints))
