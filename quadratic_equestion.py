# Write a Python program to solve quadratic equation.

"""
The standard form of a quadratic equation is:
where
a, b and c are real numbers and
The solutions of this quadratic equation is given by:
𝑎𝑥 + 𝑏𝑥 + 𝑐 = 0
2
𝑎 ≠ 0
(−𝑏 ± (𝑏 − 4𝑎𝑐 )1/2/(2𝑎)

"""
import math
#input Coffient 

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# calculate the discriminant
d = (b ** 2) - (4 * a * c)

if d > 0:
    r1 = (- b + math.sqrt(d)) / (2 * a)
    r2 = (- b - math.sqrt(d)) / (2 * a)
    print(f"Root 1 is: {r1}")
    print(f"Root 2 is: {r2}")

elif d == 0:
    r1 = -b / (2 * a)
    print(f"Root is: {r1}")

else:
    #complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(-d)) /(2 * a)
    print(f"Root 1 is: {real_part} + {imaginary_part}i")
    print(f"Root 2 is: {real_part} - {imaginary_part}i")




