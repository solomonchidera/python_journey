#!/usr/bin/python3

# Ask the user to input 2 values and store them in a variable num1 and num2
num1, num2 = input("Enter two numbers ").split()
# convert the strings to regular numbers Integer
num1 = int(num1)
num2 = int(num2)
# Add the values and store them in sum
sum = num1 + num2

#Substract the values and store them in minus
sub = num1 - num2

# Multiply the values and store them in product
mul = num1 * num2

#Divide the values and store them in division
div = num1/num2

# Get the modulo of the divided Integer

modulo = num1 % num2

# print the result

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, sub))
print("{} * {} = {}".format(num1, num2, mul))
print("{} / {} = {}".format(num1, num2, div))
print("{} % {} = {}".format(num1, num2, modulo))
print("Am done caculating")
