#!/usr/bin/env python3

print("Enter the details of simple polynomial")
print(''' 
+--------------------------------------------------------+
| The polynomial we are considering here is of the form  |
| f(x) = a(x^n) + b(x^(n-1)) + ... + c(x^2) + dx + e = 0 |
+--------------------------------------------------------+
        ''')
print("Enter the total number of terms in the simple polynomial \n")
term_num = int(input())

coeff = []
expo = []

for i in range (0,term_num,1):

    print("Enter the coefficent of term ",i)
    val=float(input())
    coeff.append(val)
    print("Enter the exponential value of term ",i)
    val=float(input())
    expo.append(val)

print("Coefficent = ",coeff)
print("Exponential = ",expo)

print(" Enter the value of x in the polynomial")
val=float(input())

        

def fn(x):
    k=0
    for i in range (0,term_num,1):
       k= k + coeff[i]*(x**expo[i])
    return k

def fn1(j):
    l=0
    for i in range (0,term_num):
        l= l + (expo[i]*coeff[i])*(j**(expo[i]-1.0))
    return l


print("****** RESULT *********")
print("F(x) = ",fn(val))
print("d^2(F(x))/dx ",fn1(val))


