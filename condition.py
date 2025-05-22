#1.even or odd
int=7
if int%2==0:
     print("even number")
else:
     print("odd number")

# 2.Write a program that takes two numbers as input and prints the larger number. 
# If they are equal, print "Both numbers are equal".

# a=9
# b=9
# if a==b:
#     print("both are equal number")
# else:  
#        print("large number")

a=int(input("enter the number"))
b=int(input("enter the number"))
if a==b:
      print("large number")
else:
      print("both are equal")


#3. postive or negative

num = int(input("Enter a number: "))

# Checking the condition
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

# 4.vote

s=int(input("enter the number"))
if s>=18:
    print(" you are eligible for vote")
else:
    print(" you are not eligible for vote")


# 5.Write a program that takes a student's marks (out of 100) and prints:
# "Pass" if marks are 40 or more
# "Fail" if marks are less than 40


a=98
if a>=40:
    print("exam pass")
else:
    print("exam fail")
