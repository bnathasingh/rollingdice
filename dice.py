"""A simple die roller

Author: Brandon Nathasingh bn243
Date: September 10, 2019"""
import random
first = int(input('Type the first number: '))
last = int(input('Type the last number: '))
d1 = random.randint(first, last)
d2 = random.randint(first, last)
roll = d1+d2
print('Choosing two numbers between ' + str(first) + ' and ' + str(last) + '.')
print ('The sum is ' + str(roll) + '.')
