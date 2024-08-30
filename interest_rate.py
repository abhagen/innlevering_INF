# Problem 2.2. Growth of a bank deposit Let r be a bank’s interest rate in
# percent per year. An initial amount P will then grow to A = P(1 + r/100)^n
# after n years. Write a program that computes how much money 1000 euros have
# grown to after three years with 5 percent interest rate, and prints the amount
# in the terminal.

P = 1000 # setter den initielle summen
r = .05 # setter renta
n = 3 # setter antallet år

A = P * (1+r/100 )**n # formelen.

print(A) # printe beløpet. 

# Jeg kunne eventuelt skrevet noe a la:
# print("After 3 years 1000 euros have grown to " + str(A) + " euros.") 
# for å "skrive det ut".