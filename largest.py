# 8. Write a python program to find largest of three numbers. 
a = int(input("Enter First Number :  "))
b = int(input("Enter Secend Number :  "))
c = int(input("Enter Third Number :  "))

if (a > b) and (a > c):
    {
    print(a,"A is greater")
    }
elif (b > c) and (b > a):
    {
        print(b,"B is Greater")
    }
else:
    print(c,"C is Greater")

