# 12. Write a python program to find factorial of a number using Recursion. 

def rec_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * rec_factorial(n-1)
    
num = int(input("Enter a number: "))

if num < 0:
    print("Negative Number can not find Factorial Number")

else:
    print(f"factorial of {num} is : {rec_factorial(num)}")
    

        
