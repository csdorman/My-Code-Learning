import numpy as np

xStr = input("Enter a number for x")
x = int(xStr)
yStr = input("Enter a number for y")
y = int(yStr)
xSq = x**y
print("The power of x to y is " + str(xSq))

xLog = np.log2(x)
print ("The log (base2) of x is " + str(xLog))