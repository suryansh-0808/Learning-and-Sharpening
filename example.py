# list_1 = [1,2,3,print("")]
# for i in list_1:
#     print(i)
# # list_1[1] = 600
# # print(list_1[1])



# tuple_1 = (1,2,3,4,5,6)
# print(type(tuple_1))
# # for i in range(6):
# #     print(tuple_1[i])
# # tuple_1[1] = 4
# # print(tuple_1[1])




# sets_1 = {1,2,3,4,5,5,6,1,4,2}
# sets_1.update(2)
# print(sets_1)
# # print(type(sets_1))
# # for i in sets_1:
# #     print(i)



# dict_1 = {1:20,2:100,17:30}
# dict_1[9] = 5000 
# dict_1[1] = 200000000

# for i in dict_1:
#     print(i)

# print("................................")

# for i in dict_1:
#     print(dict_1[i])

# print("..................................")

# for i in dict_1.values():
#     print(i)
# print()


# Deep Copy v/s Shallow Copy
# print("Deep copy")
# a = [1,2,3,4,5]
# b = a
# print(f" B - {b}")
# a.append(6)
# print("B - ",b)

# print("Shallow Copy")
# c = [1,2,3,4,5]
# d = c.copy()
# print(f"D - {d}")
# c.append(100)
# print(f"C - {c}")
# print(f"D - {d}")



# d = {1:10,2:20,3:30,4:40}
# d.update(10,200)
# print(d.items())

# d1 = {1:10,2:20,3:30}
# d2 ={4:40,5:50,6:60}
# sum = 0
# for i in d1.values():
#     sum +=i
# print(sum)

# l1 = [1,2,3,4,1,1,2,3,4,5,6,6,6,4,3,2,]
# d = {}
# for i in l1:
#     if i in d.keys():
#         d[i] +=1
#     else :
#         d[i] = 1

# print(d)
# a = 12
# b = int(input("Enter a numebr : "))
# try : 
#     print(a/b)
# except Exception as eas:
#     print(eas)
# else:
#     print("There is no error")
# finally :
#     print("Htt dalle")
# print("abc")


# a = int(input("Enter your age : "))
# try :
#     if a < 10 or a > 18:
#         raise ValueError("your age doesnot support")
#     else:
#         print("Welcome ")
# except Exception as err : 
#     print(f"an error occured{err}")

# print("Starting soon..............")

# r = open("superman.txt",'a')

# r.write("/n Hello sucker")

# r.close()

yes = open("sauce.txt","a")
yes.write("Aur laadle kesa h ?? ")
yes.close()
