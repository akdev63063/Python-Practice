"""WPP to read to string and convert all even index to Upper case."""
#Example 1

"""
s = input("Enter any Strings: ")
l1 = list(s)
for i in range (len(l1)):
    if i % 2 == 0:
        l1[i] = l1[i].upper()
print(l1)
"""

# Example 2
def myfun():
    s = input("Enter any Strings: ")
    l1 = list(s)
    for i in range (len(l1)):
        if i % 2 == 0:
            l1[i] = l1[i].upper()
    print(l1)

myfun()



    
