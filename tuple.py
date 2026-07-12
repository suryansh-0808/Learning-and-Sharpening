# a = (1,2,3,4)
# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)
# d = (1)
# print(type(d))
# print(d)


# HASH
a= {1,2,3,4}
b={4,7,8,9}

s = a|b
print(s)

p = a&b
print(p)

q = a-b
print(q)

# r = b.difference(a)
r = b-a
print(r)

# s = a.symmetric_difference(b)
s = a^b
print(s)