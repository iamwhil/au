# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 21:19:56 2018

@author: Whil

This is the third assignment for the AU CPT200 course.
It asks for functions to input the users and view all users.
It also wants a global variable that displays the current number of uesrs.
Since I'd rather eat a shoe than declare and change a global variable in a function
I'll just use the count of the lenght of my employees array.
"""
def prompt_user(all_employees):
  choice = "0"
  while choice != "1" and choice != "2" and choice != "3":
    print("There are currently {l} employees in the system.".format(l = len(all_employees)))
    choice = input("Would you like to 1) enter a new user or 2) display all users information or 3) exit: ")
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

def print_basic_info(emp):
  '''
  Ugly solution, should be a .join(',') for the hash or a __print__ for the employee object.
  However if the hash is not in the right order for what ever reason we'll get bogus output.
  Receives a hash of an employee and prints out their information.
  '''
  print(emp['employeeName'] + "," + 
        emp['employeeSSN_last4'] + "," + 
        emp['employeePhone'] + "," + 
        emp['employeeEmail'] + ",$" + 
        str(emp['employeeSalary'])
        )

  
# Variables
all_employees = []
choice = "0"

while choice != "3":
  choice = prompt_user(all_employees)
  if choice == '1': 
    all_employees.append(get_employee_information())
  else:
    print_all_employees_information(all_employees)
print("bye.")