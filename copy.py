"""16. Write a script named copyfile.py. This script should prompt the user
for the names of two text files. The contents of the first file should be
input and written to the second file"""

infile = input("Enter the file Name with Extension: ")
outfile = input("Enter the file name with Extension: ")
f1 = open(infile,'r')
f2 = open(outfile,'w')
content =f1.read()
f2.write(content)
f1.close()
f2.close()

"""
infile = input("Enter the file Name with Extension: ")
outfile = input("Enter the file name with Extension: ")

f1 = open(infile, 'r')
f2 = open(outfile, 'w')

content = f1.read()   # Read contents of source file
f2.write(content)     # Write contents to destination file

f1.close()
f2.close()

print("File copied successfully!")
"""

