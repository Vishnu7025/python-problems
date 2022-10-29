x = int(input("enter a year : "))
if x%400 == 0 and x%100 == 0:
    print("{} is a leap year" .format(x))
elif x%100 != 0 and x%4 == 0:
    print("{} is a leap year" .format(x))
else:
    print("{} is not a leap year" .format(x))