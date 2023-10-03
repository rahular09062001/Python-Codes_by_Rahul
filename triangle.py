#!/usr/bin/env python3

print("Enter the angles of triangle \n")
a1=float(input("a1 = "))
a2=float(input("a2 = "))
a3=float(input("a3 = "))

a = a1+a2+a3

if(a==180.0):
    print("The values are acceptable for triangle")
else:
    print("The values are not acceptable for a triangle")
