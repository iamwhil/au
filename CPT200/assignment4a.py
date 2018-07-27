# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 20:36:49 2018

@author: Whil

This program is takes in x number then display the max, min and sum.
It asks for the user to input 20 numbers but enforcing this seems pointlessly long.

Assuming all the input is numbers.

Also the comments here are longer than the program. 
I really wanted to sort the list comprehension but it returns none and can't be turned into a list in place :(.
"""

# List comprehension with split()
ints = [int(n) for n in (input("Enter 10 numbers separated by spaces: ")).split()]
ints.sort()
print("smallest number: {smallest} \nlargest number: {largest} \nsum: {sum}".format(smallest = ints[0], largest = ints[-1], sum = sum(ints)))