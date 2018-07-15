# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 21:19:56 2018

@author: Whil

This is the second assignment for AU's Python CPT200 course.
I have assumed that future iterations of this program will utilize 
classes and that a user will be defined in those iterations.
Otherwise it would be better to create an employee class which contains
the desired information.
"""
  
def get_employee_information():
  employee = {}
  employee['employeeName'] = input("Full name: ")
  employee['employeeSSN_last4'] = input("Last 4 of SSN:" )
  employee['employeePhone'] = input("Phone Number (###)###-#### format: ")
  employee['employeeEmail'] = input("Email: ")
  employee['employeeSalary'] = int(input("salary: "))
  return employee
  
def get_employees_data():
  all_employees = []
  more = True
  print("You are about to input up to 5 employees' information.")
  for i in range(0, 5):
    if more:
      print("Please input employee {num}'s information".format(num = i + 1))
      all_employees.append(get_employee_information())
      more = stop_inputting_users("input")
  return all_employees

def stop_inputting_users(method):
  more = input("Would you like to {m} more users? yes/no: ".format(m = method))
  if more == 'no' or more == 'No':
    return False
  elif more == "yes" or more == "Yes":
    return True
  else:
    return False
  
def retrieve_employees_data(all_employees):
  print_employee_data = True
  if print_employee_data:
    employee_number = int(input("Enter employee number (1 to {l}) to retrieve information: ".format(l = len(all_employees))))
    try:
      print_basic_info(all_employees[employee_number - 1])
    except:
      print("Employee {n} not found or information incorrect.".format(n = employee_number))
    print_employee_data = stop_inputting_users("retrieve")

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

# Basic run.
all_employees = get_employees_data()
retrieve_employees_data(all_employees)
    
