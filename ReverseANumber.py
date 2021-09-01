#Write a Python program that accepts a word from the user and reverse it.
a=int(input())
reverse=0
while(a>0):
    n=a%10
    reverse=reverse*10+n
    a=a//10
print(reverse)
