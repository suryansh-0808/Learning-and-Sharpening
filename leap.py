a = int(input("Enter the year : "))
if a%100==0 and a%400==0:
    print(f"{a} is a leap year.")
elif a%100 !=0 and a%4==0:
    print(f"{a} is a leap year")
else:
    print(f"{a} is not a leap year.")