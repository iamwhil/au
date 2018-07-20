# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:08:21 2018

@author: Whil

Assumes integer input.

"""
def get_number():
  number = -1 
  while number <= 0:
    number = int(input("Enter a number greater than 0: "))
  return number
    
def get_1_or_2():
  choice = 0
  while choice != 1 and choice != 2:
    print("Would you like to:")
    print("1) count down from {d} to 0.".format(d = number))
    print("2) display factorial of {d}.".format(d = number))
    choice = int(input("choice:"))
  return choice
    
def print_countdown(number):
  for i in range(number, 0, -1):
    print(i)
    
def calculate_factorial(number):
  product = 1
  for i in range(1, number + 1):
    product *= i
  return product
    
def print_factorial(number):
  factorial = calculate_factorial(number)
  print(factorial)
    
def display_output(choice, number):
  if choice == 1:
    print_countdown(number)
  else:
    print_factorial(number)

# Basic run
number = get_number()
choice = get_1_or_2()
display_output(choice,number)
