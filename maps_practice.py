l1=['a1','b2','c3','d4','e5']
l2=['A1','B2','C3','D4','E5']
s1=['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']
s2=['0','1','2','3','4']
s3=['a:0','b:1','c:3']

def myFunc(a,b):
    return a+b

# fun=lambda x,y:x+y

x=map(myFunc,l1,l2)
print(list(x))

x=map(lambda x,y:x+y,l1,l2)
print(list(x))

x=map(list,s1)
print(list(x))

x=list(map(int,s2))
print(x)
print("x[3] is of type {}".format(type(x[3])))

x=list(map(tuple,s2))
print(x)
print("x[3] is of type {}".format(type(x[3])))

x=list(map(eval,s3))                              #this gives error
print(x)
print("x[3] is of type {}".format(type(x[3])))


