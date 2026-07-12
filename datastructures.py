# a = [12,13,14,15,16]
# a[2] = 10
# first way indexing
# for i in range(len(a)):
#     print(a[i])
# second way directly by values
# for i in a:
#     print(i)
# print(dir(list))
# help(list)  

# a = [1,2,3,2,4,5,6,2]

# a.append(7)
# print(a)
# a.insert(11,1)
# print(a)
# a.remove(2)
# print(a)
# a.pop(2)
# print(a)
# b = a.count(2)
# print(b)
# c = a.index(2)
# print(c)
# a.sort()
# b = a.copy()
# print(b)
# b=[]
# a =[100,-45,-55,3,4,-65]
# for i in a:
#     if i >=0:
#         b.append(i)
#         print(i)
# for i in a:
#     if i<0:
#         b.append(i)
#         print(i)
# b.sort()
# print("______________________________")
# for i in b:
#     print(i)
# a = [12,23,4,5,100,78,0,900]
# sum = 0
# c = 0
# for i in a:
#     sum+=i
#     c+=1
# mean = sum/c
# print(mean)
# max = a[0]
# maxi = 0
# for i in range(1,len(a)-1,1):
#     if a[i]>a[max]:
#         max = a[i]
#         maxi = i
# name = "Suryansh"
# print(name)        
# a = [92,2,93,4,5,6,7]
# max = 0
# max_2 = 0
# for i in range(1,len(a)):
#     if a[max] < a[i]:
#         max = i
#         max_2 = max_2
#     elif a[max_2]<a[i]:
#         max_2 = i
# print("Largest ",a[max])
# print(f"Second Largest number {a[max_2]} at index {max_2}")
# l = [40,30,21,15,34]

# largest = l[0]
# sec_largest = l[0]
# for i in l:
#     if i > largest :
#         sec_largest = largest
#         largest = i

#     elif i > sec_largest:
#         sec_largest = i
# print("Largest ", largest)
# print("Second Largest ",sec_largest)
# a =[]
# size = int(input("Enter size of a list : "))
# for i in range(size):
#     a.append(int(input("Enter a element :")))
# print(a)
# # to check whether it is sorted or not
# boolean = False
# for i in range(0,len(a)-1):
#     if a[i]<a[i+1]:
#         boolean = True
#         continue
#     else:
#         print("List is not sorted")
#         break
# else :
#     print("List is sorted")
a,b,c = [1,2,3]
print(type(a))
print(a)
print(b)
print(c)