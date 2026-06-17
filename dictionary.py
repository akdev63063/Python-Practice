# 7. Write a program to demonstrate working with dictionaries in python.

dic1 ={1 : "Akash",
        2: "Ajay",
        3: "Vijay",
        4: "Ravi",
        5: "Shani"
      }

print(dic1[1])
print(dic1[2])
print(dic1[3])
print(dic1[4])
print(dic1) #print dictionary 
# 1. get() Key ki value return karta hai.
print(dic1.get(1))
# 2. keys() Sabhi keys return karta hai.
print(dic1.keys())
# 2. keys() Sabhi keys return karta hai.
print(dic1.values())
# 4. items() Key-value pairs return karta hai.
print(dic1.items())
#update() Dictionary update karta hai.
dic1.update({6 : "shivu"})
print(dic1)
# 6. pop() Specific key remove karta hai.
print(dic1.pop(1))
# 7. popitem() Last inserted item remove karta hai
print(dic1.popitem())
# 9. copy() Dictionary ki copy banata hai.
dic2 = dic1.copy()
print(dic2)
# 10. setdefault() Key exist na ho to value insert karta hai.
print(dic1.setdefault(7,"ak"))
print(dic1)
# Dictionary Traversal
for key, value in dic1.items():
    print(key, value)

print(dic2.clear())