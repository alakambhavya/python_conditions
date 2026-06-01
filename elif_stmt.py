#C.elif stmt
print("\n1.write a program to check books pages based on price.\n")
pages=int(input("enter the number of pages"))
if pages>=300 :
	print("notebook price is 100")
elif pages>=200:
	print("notesbook price is 70")
elif pages>=100:
	print("notebook price is 50")
elif pages>=80:
	print("notebook price is  30")
elif pages>=50:
	print("notebook price is 20")
else:
	print("notebook price is 0")

print("____________________")

print("\n2.week days.\n")
week=int(input("enter the number of day"))
if week==1:
	print("it is sunday")
elif week==2:
	print("it is monday")
elif week==3:
	print("it is tuesday")
elif week==4:
	print("it is wednesday")
elif week==5:
	print("it is thursday")
elif week==6:
	print("it is friday")
elif week==7:
	print("it is saturday")
else:
	print("week day  not found")

print("_________________")

print("\n3.grade calculation.\n")
marks=int(input("enter the marks"))
if marks>=90:
	print("it is A+ grade")
elif marks>=80:
	print("it is A grade")
elif marks>=70:
	print("it is B grade")
elif marks>=60:
	print("it is C grade")
elif marks>=50:
	print("it is D grade")
elif marks>=40:
	print("it is E grade")

else:
	print("student fail")

print("_______________________")

print("\n4.age category.\n")
age=int(input("enter the age"))
if age>=60:
	print("senoir cictizen")
elif age>=20:
	print("adult")
elif age>=13:
	print("teenagers")
elif age>=0:
	print("children")
else:
	print("none")

print("_______________________")

print("\n5.vowels or consonents.\n")
name="AI"
if "a" in name:
	print("a is present in name")
elif "e" in name:
	print("e is present in name")

elif "i" in name:
	print("i is present in name")

elif "o" in name:
	print("o is present in name")

elif "u" in name:
	print("u is present in name")

else:
	print(" vowels is  not present in name")

print("____________________")

print("\n6.ticket booking system.\n")
age=int(input("enter the age"))
if age<12:
	print("50% discount")
elif age>=60:
	print("30% discount")
else:
	print("no discount")

print("_______________")

print("\n7.online shopping discount.\n")
amount=int(input("enter the amount"))
if amount>=10000:
	print("30% discount")
elif amount>=5000:
	print("15% discount")
elif amount>=3000:
	print("10% discount")
elif amount>=1500:
	print("5% discount")
else:
	print("no discount")

print("_______________________")

print("\n8.employee bonus calculator.\n")
experience=int(input("enter the years of experience"))
if experience>=10:
	print("20% bonus")
elif experience>=5:
	print("10% bonus")
elif experience>=2:
	print("5% bonus")
else:
	print("no bonus")

print("________________")

print("\n9.student scholarship eligibility.\n")
marks=int(input("enter the marks"))
if marks>=95:
	print("100% scholarship")
elif marks>=85:
	print("75% scholarship")
elif marks>=75:
	print("50% scholarship")
elif marks>=65:
	print("25% scholarship")

else:
	print("no scholarship")

print("______________________")

print("\n10.mobile recharge plan.\n")
amount=int(input("enter recharge amount"))
if amount<200:
	print("basic plan")
elif amount<400:
	print("standard plan")
elif amount<700:
	print("premium plan")
else:
	print("unlimited plan")

print("____________________")

print("\n11.cricket match result.\n")
runs=int(input("enter the number of runs"))
if runs>=100:
	print("century")
elif runs>=50:
	print("half century")
elif runs>=30:
	print("good score")
else:
	print("poor score")

print("_________________")

print("\n12.mobile battery status.\n")
charge=int(input("enter the number of charge"))
if charge>=80:
	print("full charged")
elif charge>=50:
	print("good")
elif charge>=20:
	print("low")
else:
	print("danger")

print("________________")

print("\n13.Temparature.\n")
temp=int(input("enter temp"))
if temp<0:
    print("freez")
elif temp<20:
    print("cold")
elif temp<30:
    print("warm")
else:
    print("hot")
