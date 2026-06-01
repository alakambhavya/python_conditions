#D.nested if stmt
print("\n1.check whether a number is positive.if positive,check whether it is even or odd.\n")
num=int(input("enter the number"))
if num>0:
	if num%2==0:
		print("number is even")
	else:
		print("number is odd")
else:
	print("number is negetive")

print("__________")

print("\n2.check whether a username is correct.if yes,check whether the password is correct.\n")
username="bhavya"
password="bhanu@123"
if  username=="bhavya":
	if password=="bhanu@123":
		print("login success")
	else:
		print("login unsuccess")
else:
	print("invalid username")

print("__________________")

print("\n3.check whether a number is greater than 100.if yes,check whether it is divisible by 5.\n")
num=int(input("enter a number"))
if num>100:
	if num%5==0:
		print("divisible by 5")
	else:
		print("not divisible by 5")
else:
	print("number is not greater than 100")

print("_____________________")

print("\n4.check whether a number is positive.if yes,check whether it is a single digit number.\n")
num=int(input("enter a number"))
if num>0:
	if num<10:
		print("positive single digit")
	else:
		print("not positive single digit")
else:
	print("it is not a positive number")

print("_____________")

print("\n5.check whether a student passed the exam.if passed,check whether the grade is A or B.\n")
marks=85
if marks>=35:
	if marks>=75:
		print("grade A")
	else:
		print("grade B")
else:
		 print("fail")

print("__________________")

print("\n6.check whether a shop is open.if open,check whether the required item is available.\n")
shop_open="true"
item_available="false"
if shop_open:
	if item_available=="true":
		print("item  available")
	else:
		print("item not available")
else:
	print("shop closed")

print("_______________")

print("\n7.check whether a number is divisible by 5.if yes,check whether it is also divisible by 10.\n")
num=25
if num%5==0:
	if num%10==0:
		print("divisible by 5 and 10")
	else:
		print("not divisible by 5 and 10")
else:
	print("not divisible by 5")

