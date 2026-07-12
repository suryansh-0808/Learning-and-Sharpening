# for i in range(5) :
# print("I Love You")
# a = "Suryansh"
# print(a[1:3:1])
# num = int(input("Enter a number to print table : "))
# max = (num*10)+1
# for i in range(num,max,num):
# a = input("Enter a string to print : ")
# length = len(a)
# for i in range(0,length):
#     print(a[i])#     print(i)"Sur
# a = "Suryansh Agarwal"
# for i in a:
#     print(i)
# for i in range(21):
#     if(i==20):
#         print("Bhoo")
#         break
#     print(i)
# else:
#      print("Yooo")
# a = int(input("Enter how many time it should be print : "))
# for i in range(0,a,1):
#     print("Hello World")
# a = int(input("Enter a number to which natural numbers should be print : "))
# for i in range(1,a+1,1):
#     print(i)
# a = int(input("Enter a number from which to be printed to 1 : "))
# for i in range(a,0,-1):
#     print(i)
# a = int(input("Enter a number to print its table : "))
# for i in range(a,a*10+1,a):
#     print(i)
# a = int(input("Enter a number : "))
# sum = 0
# t = 1
# for i in range(t,a+1,1):
#     sum+=t
#     t+=1
# print(sum)
# a = int(input("Enter a number to print its factorial : "))
# p = 1
# for i in range(a,0,-1):
#     p*=i
# print(p)
# a = int(input("Enter a number : "))
# sume = 0
# sumo = 0
# for i in range(1,a+1,1):
#     if i%2==0:
#         sume+=i
#     else:
#         sumo+=i
# print(f"Sum of even number in range is {sume}")
# print(f"Sum of odd number in range is {sumo}")

# calculating factors
# a = int(input("Enter a number to print its factors :  "))
# for i in range(1,a+1,):
#     if a%i==0:
#         print(i)

# perfect number
# sum = 0
# n = int(input("Enter a number to check perfect number :  "))
# for i in range(1,n):
#     if n%i==0:
#         print(i)
#         sum+=i
# if sum==n:
#     print(f"{n} is a perfect number.")        
# else:
#     print(f"{n} is not a perfect number.")

# string reverse
# a = input("Enter a string : ")
# nstr = ""
# length = len(a)
# for i in range(length-1,-1,-1):
#     nstr+=a[i]
# print(nstr)

# palimdrome string 
# nstr = ""
# a = input("Enter a string to check wether a palindrome or not : ")
# for i in range(len(a)-1,-1,-1):
#     nstr+=a[i]
# if a==nstr :
#     print(f"{a} is a Palindrome String.")
# else:
#     print(f"{a} is not a Palindrome String.")  

# checking
# char = 0
# num = 0
# sym = 0
# a = input("Enter a String : ")
# for i in range(0,len(a),1):
#     if a[i].isdigit():
#         num+=1
#     elif a[i].isalpha():
#         char+=1
#     else:
#         sym+=1
# print(f"Number of characters are {char}")
# print(f"Number of digits are {num}")
# print(f"Number of symbols are {sym}")
# print(chr(97))

i =1
# while i<=30:
#     print(i)
#     i+=1
# n = int(input("Enter a number : "))

# copy = n
# rev = 0

# while n > 0:
#     r = n % 10
#     rev = rev * 10 + r
#     n= n // 10

# if copy == rev:
#     print("True")

# else:
#     print("False")
# import random
# tries = 0
# a = random.randint(1,11)
# while True :  
#         guess = int(input("Guess a number between 1-10 : "))
#         if a == guess :
#                 tries+=1
#                 print(f"You won in {tries} tries")
#                 break
#         elif guess < a:
#                print("Your guess is little low")
#                tries+=1
#         elif guess > a:
#                print("Your guess is little high")
#                tries+=1
#         else:
#             print("You lost")
# def hello():
#     print("This is a hello function so I am doing Hello")
# def addition(a,b):
#     sum = a+b
#     print(f"Sum of the numbers is : {sum}")
# n1 = int(input("Enter a number : "))
# n2 = int(input("Enter another number : "))
# hello()
# addition(n1,n2)
# addition(3)
# def printing(name , age):
#     print(f"Hello {name},Happy {age}")
# # nam = input("Enter your name :")
# # age = input("Enter your age : ")
# printing(21,"Suryansh")
# def addition(a,b):
#     sum = a+b
#     return sum
# sum = addition(12,2)
# print(sum)
# dis = 0.0
# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# bud = int(input("Enter your budget : "))
# mob = int(input("Enter your Mobile No."))
# if bud>20000:
#     dis = bud - (0.20*bud)
# elif bud>=10000:
#     dis = bud - (0.1*bud)
# else:
#     dis = bud - (0.05*bud)
# print("Name\t\t     Age\t\tMob No.\t\t              Total Amount")
# print(f"{name}\t\t{age}\t\t{mob}\t\t{dis}")
# def palindrome(str):
#     revstr = ""
#     for i in range(len(str)-1,-1,-1):
#         revstr+=str[i]
#     return revstr

# palindrome

# str = input("Enter a String : ")
# revstr = palindrome(str)
# if str == revstr:
#     print(f"{str} is a palindromic string.")
# else:
#     print(f"{str} is not a palindromic string.")
# while True : 
#     print("Do you want to continue?\nY or y for \"Yes\" N or n for \"No\"")
#     choice = input()
#     if choice == 'Y' or choice == 'y':
#         str = input("Enter a String : ")
#         revstr = palindrome(str)
#         if str == revstr:
#             print(f"{str} is a palindromic string.")
#         else:
#             print(f"{str} is not a palindromic string.")
#     elif choice == 'N' or choice == 'n':
#         break
#     else:
#         print("Wrong choice entered")
        
    