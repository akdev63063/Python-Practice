# 9. Write a Python program to convert temperatures to and from Celsius,Fahrenheit. [ Formula: c = (f-32)(5/9)]

temp = float(input("Enter temprature in C and F : "))
unit = input("Enter unit Celsius for C and Fehrenheight for F : ")

if unit == 'C' or unit == 'c':
    newtemp = 9/5 * temp + 32 
    print("Temprature in Fehrenheight: ", newtemp)

elif unit == 'F' or unit == 'f' :
    newtemp = 5/9 * (temp - 32)
    print("Temprature in Celsius: ",newtemp)

else:
    print("Invalid input")

    
