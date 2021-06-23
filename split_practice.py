# str="hi my name is peter, i'm 26 years old"
# x=str.split(",")
# print(x)

str="hi my name is peter, i'm 26 years old, and i'm here, to learn, Python"
x=str.rsplit(", ",2)
print(x)
print()
for i in x:
    print("i={}\n".format(i))

a=('a','b','c','d','e','f','g','h')
x=slice(8,0,-3)
print(x)
print(type(x))
print(a[x])

a=['a','b','c','d','e','f','g','h']
x=slice(0,8,3)
print(x)
print(type(x))
print(a[x])
