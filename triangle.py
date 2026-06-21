"""Write a program that accepts the lengths of three sides of a triangle
as inputs. The program output should indicate whether or not the triangle
is a right triangle (Recall from the Pythagorean Theorem that in a right
triangle, the square of one side equals the sum of the squares of the
other two sides)."""

base = float(input("Enter Value of base: "))
per = float(input("Enter value of perpendiculer: "))
hypo = float(input("Enter value of hypotenuse: "))

if hypo ** 2 == (base ** 2 + per ** 2):
    print("Correct, Triangle")

else:
    print("Incorrect, Triangle")