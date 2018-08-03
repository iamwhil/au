# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 20:08:11 2018

@author: Whil

Problem 5a
Read in a file and check the scores in it against the correct scores.
"""

def process_raw_scores(raw_scores):
  scores = []
  for i, score in enumerate(raw_scores):
    score = score.strip()
    scores.append(score[-1].upper())
  return scores

def grade_scores(answer_key, scores):
  assessment = []
  for i in len(answer_key):
      if answer_key[i] == scores[i]
        assessment.append(true)
    else
      


answer_key = [B, D, A, A, B, A, B, A, C, D, B, C, D, A, D, C, C, B, D, A]
scores = []
right_wrong  = []

file = open('student_scores.txt', 'r')
raw_scores = file.readlines()
file.close

scores = process_raw_scores(raw_scores)
assessment = grade_scores(answer_key, scores)
