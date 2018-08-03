# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 20:08:11 2018
@author: Whil
Problem 5a
Read in a file and check the scores in it against the correct scores.
This could be customizeable by setting the student_scores as an argv variable.
I have chosent to hard code it.
"""
def import_scores():
  file = open('student_scores.txt', 'r')
  raw_scores = file.readlines()
  file.close
  return raw_scores

def process_raw_scores(raw_scores):
  scores = []
  for i, score in enumerate(raw_scores):
    score = score.strip()
    scores.append(score[-1].upper())
  return scores

def grade_scores(answer_key, scores):
  assessment = []
  for i in range(0,len(answer_key)):
    if answer_key[i] == scores[i]:
      assessment.append(True)
    else:
      assessment.append(False)
  return assessment

def calculate_percentage(assessment):
  num_right = 0
  for i in assessment:
    if i == True:
      num_right += 1
  return float(num_right/len(assessment) * 100.0)

def print_pass_fail(percentage):
  if percentage >= 50 :
    print("PASS - %.2f" % percentage)
  else:
    print("FAIL - %.2f" % percentage)

def print_details(assessment, scores, answer_key):
  for i, value in enumerate(assessment):
    if value == True:
      print("{num}. {score} - Correct".format(score = scores[i], num = i + 1) )
    else:
      print("X. {score} - Correct answer: {correct_answer}".format(score = scores[i], correct_answer = answer_key[i]))

# Basic run
answer_key = ['B', 'D', 'A', 'A', 'B', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
scores = process_raw_scores(import_scores())
assessment = grade_scores(answer_key, scores)
percentage = calculate_percentage(assessment)
print_pass_fail(percentage)
print_details(assessment, scores, answer_key)
