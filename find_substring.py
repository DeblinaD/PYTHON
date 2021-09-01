#write a program in python to check whether the given input is available in the string or not.
a=input()
b=input()
if (a.find(b))==-1:
    print("Not present")
else:
    print("Available")
