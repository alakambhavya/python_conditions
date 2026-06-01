print("\n1.Check whether a number is a three-digit number or not.\n")
num=123
if num>=100 and num<=999:
	print("num is three digit number")
else:
	print("num is not three digit number")

print("_____________")

print("\n2.Write a program to check whether a person is a child,teenage based on age.\n")
age=15
if age<13:
	print("persion is child")
else:
	print("person is teenage")

print("________________")

print("\n3.Check whether a user entered the correct OTP.\n")
otp=1433
if otp==1437:
	print("correct otp")
else:
	print("incorrect otp")

print("____________")

print("\n4.Check whether temperature is above 40°C.\n")
temp=30
if temp>40:
	print("temperature is above 40°C")
else:	
	print("temperature is normal")

print("___________")

print("\n5.Check whether a string starts with a vowel.\n")
name="alakam"
if name[0] in "aeiou":
	print("it is vowel")
else:
	print("it is  not vowel")
print("______________")

print("\n6Create a simple calculator using conditional statements.\n")
a=10
b=20
op=input("enter the OP :")
if op=='+':
	c=a+b
	print(c)
elif op=='-':
	c=b-a
	print(c)

