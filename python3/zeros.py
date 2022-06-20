# Write a program that will calculate the number of trailing zeros in a 
# factorial of a given number.
#
# N! = 1 * 2 * 3 * ... * N
#
# Be careful 1000! has 2568 digits...
#
# For more info, see: http://mathworld.wolfram.com/Factorial.html


def zeros(n):
    c = 0
    for i in range(1, 100):
        c += n//(5**i)
    return c
