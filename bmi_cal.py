# -*- coding: utf-8 -*-
"""
@author: Priyanshu Bansal
"""

print("BMI CALCULATOR")
weight= float(input("Enter the Weight in kg- "))

print("1 Feet = 0.3048 m & 1 Inch = 0.0254 m")

height= float(input("Enter the Height in Meter- "))

def bmi_index(weight, height):
    a = float(weight/(height*height))
    return(round(a,2))

print("Your BMI is-" , bmi_index(weight, height))
