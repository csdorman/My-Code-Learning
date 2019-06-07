#import numpy
import sys
sys.path.append('/user/local/lib/python3.7/site-packages/numpy/')
import numpy as np
#print(sys.path)

x = input("Enter a number for x: ")

y = input("Enter a number for y: ")
xSq = x**y
print('The power of x to y is ', xSq)
xLog = np.log2(x)
print('The log base 2 of x is ', xLog)

#print('The power of ', x, ' to ', y, ' is ', x**y)
#print("The log of x is ", log2(x))

    