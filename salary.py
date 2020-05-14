# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:18:39 2020

@author: bansa
"""

"""
Name: 
    Clean the Messy salary        
Filename:
    salary.py
Problem Statement:
    Clean the Messy salary into integers for Data Processing
    salary = '$876,001'
    
    Remove the $
    Remove the ,
    Convert the string into integer
Hint: 
    We can use slicing concept to remove $ or remove() method 
    We can use the split and join to remove the , comma
    We can use the int() typecast to convert into integer
"""
salary = input("Enter the Salary > ")
salary1 = salary[1:]
salary1 = salary1.split(",")
salary1= "".join(salary1)
salary1= int(salary1)
print(salary1)
