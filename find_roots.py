# Given a quadratic equation
# ax2 + bx + c = 0,
# the two roots are
# x1 = {−b + sqrt(b^2 − 4ac)}/{2a}
# x2 = {−b - sqrt(b^2 − 4ac)}/{2a}

# Make a program evaluating the roots of
# 6x^2 − 5x + 1 = 0. 
# Print out both roots with two decimals.

import math

# Fra kvadratet har vi a = 6, b = -5 og c = 1
a = 6
b = -5
c = 1
x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
print("Røttene er: ")
print("x1 = " + str(round(x1,2)) + ", x2 = " + str(round(x2,2)))