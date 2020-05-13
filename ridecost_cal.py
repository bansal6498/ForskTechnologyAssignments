# -*- coding: utf-8 -*-
"""
@author: Priyanshu Bansal
"""

print("Ride Cost Calculator")
distance= float(input("Enter the Total Distance Travelled- "))
cost= float(input("Enter the Cost of Deisel- "))
average= float(input("Enter the Average- "))

def ridecost_cal(distance, cost, average):
    fuel_con= distance/average
    cost_per_day= fuel_con*cost
    return(round(cost_per_day, 2))
    
print("Your Ride Cost is- ", ridecost_cal(distance, cost, average), "Rs.")