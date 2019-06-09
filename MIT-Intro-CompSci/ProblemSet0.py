import sys
sys.path.append('/user/local/lib/python3.7/site-packages/numpy/')
# print(sys.path)
import numpy as np


#Testing import syntax
# import datetime
# oTime = datetime.datetime.now()
# print oTime.isoformat()


xStr = input("Enter a number for x: ")
x = int(xStr)
yStr = input("Enter a number for y: ")
y = int(yStr)
xSq = x**y
print ("The power of x to y is " + str(xSq))



# xLog = np.log2(x)
# print('The log base 2 of x is ', xLog)

#print('The power of ', x, ' to ', y, ' is ', x**y)
#print("The log of x is ", log2(x))

    