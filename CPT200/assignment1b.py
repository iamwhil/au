# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 21:19:56 2018

@author: Whil
"""

  
def print_header(num_spaces, employeeName):
  tabs = (num_spaces - 2 - len(employeeName)) // 2
  for i in range(0, tabs):
    print('-', end = '')

  print(" " + employeeName + " ", end = '') 
  
  for i in range(0, tabs):
    print('-', end = '')
    
  print("\n")
    
def print_attribute(indent, attribute_name, attribute):
  for i in range(0, indent):
    print(" ", end = '')
  print(attribute_name + "" + attribute)

# Variables
num_spaces = 60
indent = 8

# Input
employeeName = input("Full name: ")
employeeSSN_last4 = input("Last 4 of SSN:" )
employeePhone = input("Phone Number (###)###-#### format: ")
employeeEmail = input("Email: ")
employeeSalary = int(input("salary: "))


# Output
print_header(num_spaces, employeeName)
print_attribute(indent, "SSN:", employeeSSN_last4)
print_attribute(indent, "Phone:", employeePhone)
print_attribute(indent, "Email:", employeeEmail)
print_attribute(indent, "Salary: $", str(employeeSalary))