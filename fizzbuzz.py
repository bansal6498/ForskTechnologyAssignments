# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:45:56 2020

@author: bansa
"""

"""
Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 50(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
    User Input not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
"""
number = 1 
while(number<51):
    if number%15 == 0:
        print('FizzBuzz')
    elif number%5 == 0:
        print('Buzz')
    elif number%3 == 0:
        print("Fizz")
    else:
        print(number)
    number+=1