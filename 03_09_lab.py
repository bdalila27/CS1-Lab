# -*- coding: utf-8 -*-
"""03/09 lab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C25NlF4kJvFrJ3NA29KPM0rVjI8DKGCO
"""

#1 Length of argument
def func1():
  a=input()
  b=len(a)
  return a,b
func1()

#2 Sum of numbers 0-10
def Sum():
  counter=0
  for i in range(11):
    counter+=i
  return counter
Sum()

#3 Even characters
def even():
  c=input()
  return c[::2]
even()

#4 Mirror numbers
def Check():
  n=input()
  if(n[0:1]==n[:-2:-1]):
    return True
  return False
Check()