# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 21:19:56 2018

@author: Whil

This is the fourth assignment for the AU CPT200 course.
It continues on the employee system.
This time it wants us to again reformat the output of the names.
It also wants a basic strict search on SSN.
And update user with given SSN.
I have omitted error checking on user input as I believe that is what 
assignment 5 is all about.
"""

def prompt_user(all_employees):
  choice = "0"
  while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
    print("There are currently {l} employees in the system.".format(l = len(all_employees)))
    choice = input("Would you like to: \n1) enter a new user or 2)\nDisplay all users information\n3) Search for user by SSN\n4) Update a user\n5)exit: ")
  return choice

def get_employee_information():
  employee = {}
  employee['employeeName'] = input("Full name: ")
  employee['employeeSSN_last4'] = input("Last 4 of SSN:" )
  employee['employeePhone'] = input("Phone Number (###)###-#### format: ")
  employee['employeeEmail'] = input("Email: ")
  employee['employeeSalary'] = int(input("salary: "))
  return employee

def print_all_employees_information(all_employees):
  print(" ")
  for employee in all_employees:
    print_basic_info(employee)
  print(" ")

def print_basic_info(employee):
  num_spaces = 62
  indent = 5
  print_header(num_spaces, employee['employeeName'])
  print_attribute(indent, "SSN:", employee['employeeSSN_last4'])
  print_attribute(indent, "Phone:", employee['employeePhone'])
  print_attribute(indent, "Email:", employee['employeeEmail'])
  print_attribute(indent, "Salary: $", str(employee['employeeSalary']))
  print_footer(num_spaces)
  
def print_header(num_spaces, employeeName):
  tabs = (num_spaces - 2 - len(employeeName)) // 2
  print(tabs * "-", end = '')
  print(" " + employeeName + " ", end = '') 
  print(tabs * "-")
    
def print_attribute(indent, attribute_name, attribute):
  for i in range(0, indent):
    print(" ", end = '')
  print(attribute_name + "" + attribute)
  
def print_footer(num_spaces):
  print(num_spaces * "-")
  
def find_employee_by_ssn(all_employees):
  ssn = get_ssn()
  index = get_employee_index(all_employees, ssn)
  if index != -1 :
    print_basic_info(all_employees[index])
  else:
    print("\nEmployee with SSN: %s not found.\n" % ssn)
  return index

def get_ssn():
  ssn = input("Please enter the employee's ssn: ")
  return ssn

def get_employee_index(all_employees, ssn):
  index = -1
  for i, employee in enumerate(all_employees):
    if ssn in employee.values():
      index = i
  return index
  
def update_employee(all_employees):
  employee_index = find_employee_by_ssn(all_employees)
  if employee_index != -1 :
    print("\nEditing employee with SSN {ssn}:".format(ssn = all_employees[employee_index]['employeeSSN_last4']))
    all_employees[employee_index] = get_employee_information()

# Variables
all_employees = []
choice = "0"

while choice != "5":
  choice = prompt_user(all_employees)
  if choice == '1':
    all_employees.append(get_employee_information())
  elif choice == '2':
    print_all_employees_information(all_employees)
  elif choice =='3':
    find_employee_by_ssn(all_employees)
  elif choice == '4':
    update_employee(all_employees)
  
print("bye.")
