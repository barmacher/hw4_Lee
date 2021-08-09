import calculator
import random

a = int(input("Enter a: "))
b = int(input("Enter b: "))

res = calculator.Calculator(a,b)
print("Result sum:",res.plus())
print("Result minus", res.minus())
print("Result delit", res.delit())
print("Result umnog", res.umnog())

from random import randint
lst = [randint(1, 100) for i in range(20)]
print(lst)

