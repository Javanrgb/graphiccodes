
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 22:14:01 2022

@author: hp
"""

import matplotlib.pyplot as plt

print("Enter the value of x1: ")
x1 = int(input())
print("Enter the value of y1: ")
y1 = int(input())
print("Enter the value of x2: ")
x2 = int(input())
print("Enter the value of y2: ")
y2 = int(input())



dx = x2 - x1
dy = y2 - y1

if abs(dx) > abs(dy):
    steps = abs(dx)
else:
    steps = abs(dy)
xincrement = dx/steps
yincrement = dy/steps
i = 0
xcoordinates = []
ycoordinates = []
while i < steps:
    i += 1
    x1= x1 + xincrement
    y1 = y1 + yincrement
    print("X1: ", x1, "Y1: ", y1)
    xcoordinates.append(x1)
    ycoordinates.append(y1)
plt.plot(xcoordinates, ycoordinates)
plt.xlabel('X_Axis')
plt.ylabel('Y_Axis')
plt.title("DDA Algorithm")
plt.scatter(x1,y1)
plt.scatter(x2,y2)
# Show the plot
plt.show()