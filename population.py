# Problem 2.3. Population growth
# The growth of a population can often be described by a logistic function
# N(t) = B / (1 + Ce^{−kt}) ,
# where B is the carrying capacity of the species in the environment, i.e., the
# maximum size of the population that the environment can sustain indefinitely.
# The constant k tells us something about how fast the population grows, while C
# is given by the initial conditions. Let us consider a bacterial colony where the
# carrying capacity is B = 50000, and k = 0.2h^{−1} (where h is the unit of hours).
# The population is 5000 at t = 0. Use the initial condition to determine C and
# write a program that finds the number of bacteria in the colony after 24 hours.
# Hint: To find C you insert t = 0 in the expression above, and solve the
# resulting equation for C. This gives a formula for calculating C as a function of
# N and B, and this formula can be used directly in your program.

# Solving for C with t = 0 gives C = B/N - 1 = 50000/5000 - 1 = 49

import math # Trenger denne for exp-funksjonen

B = 50000 # carrying capacity
C = 49 # Regna ut ovenfor
t = 24 # antall timer

N = B / (1 + C*math.exp(-0.2*t)) # Formel

print(N)