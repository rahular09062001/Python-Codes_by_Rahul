#!/usr/bin/env python3

print("This  program will print the leap  year in the given input  range")

print("Enter the year limit \n")
year1=int(input("Lower limit \n"))
year2=int(input("Upper limit \n"))


k=0

if(year1 <  year2):

    print("Leap Year in the Given Range are")

    for i in range(year1,year2,1):

        if(i%100 == 0 and i%400 ==0):
            print(i)
            k=k+1
        elif(i%4 == 0 and i%100 != 0):
            print(i)
            k=k+1
       
    print("Total  number of leap  year =",k)

else:
    print("The range is not acceptable")
