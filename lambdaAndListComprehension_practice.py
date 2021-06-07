def mul(n):
    return lambda a:a*n
def sum():
    return lambda a,b:a+b

multiplier=mul(2)
print(multiplier)
print(type(multiplier))
print(multiplier(11))

myfunc=sum()
print(myfunc(10,20))

################################
str=["andrew","steven","gorge","paul","mathew","john"]
str2=[x if "a" in x else x+x for x in str]
print(str2)

list1=[1,2,3,4]
list2=[5,6,7]
result_list=[x*y for x in list1 for y in list2]
print(result_list)
