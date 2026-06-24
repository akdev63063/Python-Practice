"""
14. Write a python program to define a module to find Fibonacci
Numbers and import the module to another program
"""
def fab(n):
    a , b = 0 , 1
    while b < a :
        print(b , end=' ')
        a , b = b , a+b
        print()

def fab2(n):
    a , b = 0 , 1
    while b < a :
        print(b , end=' ')
        a , b = b , a+b
