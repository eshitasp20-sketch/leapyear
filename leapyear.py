year = int (input("Enter a year:"))
if (year % 4 == 0 ):
    print("It is  a leap year")
else:
    print("It is not a leap year")


yr1 = int (input("Enter yr1:\n"))
yr2 = int (input("Enter yr2:\n"))
if( yr1 % 4 == 0 and (yr1 % 100 != 0 or yr1 % 400 == 0) ):
     print(" yr1 is Leap Year")
else:
    print ("yr1 is not leap year")

if( yr2 % 4 == 0 and (yr2 % 100 != 0 or yr2 % 400 == 0) ): 
    print(" yr2 is Leap Year")
else:
     print(" yr2 is not Leap Year")

