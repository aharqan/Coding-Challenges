from math import *
#To convert from any base to
#a base 10 number
def toDecimal(n, b):
    values = [int(i, b) for i in str(n)]
    values = values[:: -1]
    result = 0
    for i in range(len(values)):
        result += values[i]*b**i
