# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:11:04 2018

@author: Whil
"""

primary_colors = ('red', 'yellow', '', 'blue')
output_colors = ('red', 'orange', 'yellow', 'purple', 'green', '', 'blue')

input_color_1 = input("Input a color: ")
input_color_2 = input("Input a second color: ")

if input_color_1 in primary_colors and input_color_2 in primary_colors:
  sum = primary_colors.index(input_color_1) + primary_colors.index(input_color_2)
  print("Additive color: ", output_colors[sum])
else:
  print("Please input primar colors - red, yellow, or blue")