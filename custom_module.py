def add(a,b,c):
    return a + b + c
def subtract(a,b):
    return a - b
def product(a,b):
    return a*b
def average(a,b,c):
    return a + b + c / 3

import custom_module

print("Addition:", custom_module.add(7, 6, 5))
print("Subtraction:", custom_module.subtract(2, 5))
print("Product:", custom_module.product(7, 6))
print("Average:", custom_module.average(9, 9, 9))