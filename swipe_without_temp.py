#Program 10
#Write a Python program to swap two variables without temp variable.

a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))

#Before swapping
print("Before swapping: a =", a, "b =", b)

#After Swapping 
a , b = b , a

print("After swapping: a =", a, "b =", b)

