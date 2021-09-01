#Write a Python program to check a triangle is equilateral, isosceles or scalene. Note :An equilateral triangle is a triangle in which all three sides are equal.A scalene triangle is a triangle that has three unequal sides.An isosceles triangle is a triangle with (at least) two equal sides.
a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print("It is equlateral triangle")
elif a==b!=c or a==c!=b or c==b!=a:
    print("Its an isosceles triangle")
else:
    print("Its scelene triangle")
