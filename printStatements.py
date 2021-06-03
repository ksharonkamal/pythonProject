# print("hello ",end="")
# print("world",end="\t")
# print('new',sep="|||")
# print('world')

a=10
print("the value of a is %i" %a)
a,b=10,20
print("the value of a is %d and b is %d" %(a,b))
name="pythonTrainingSessions"
print("%s"%name)
print("hello (%20s)"%name)
print("hello (%-20s)"%name)
print("%c"%name[2])
print("%s"%name[2:9])

num=212.34312
print("num= %f"%num)

print("num= %1.2f"%num)
print("num= %2.2f"%num)
print("num= %3.2f"%num)
print("num= %4.2f"%num)
print("num= %5.2f"%num)
print("num= %6.2f"%num)
print("num= (%7.2f)"%num)
print("num= %8.2f"%num)
print("num= %9.4f"%num)
print("num= %10.2f"%num)
print("num= (%10.3f)"%num)

a,b,c=1,2,3
print("first={0}".format(a))
print("first={0} second={1}".format(a,b))
print("first={one} second={tqw}".format(one=a,tqw=b))
print("first={} second={}".format(a,c))

name,salary="alex",30000.123
print("name:{}\tsalary:{}".format(name,salary))
print("name:{0}\tsalary:{1}".format(name,salary))
print("name:{n}\tsalary:{s}".format(n=name,s=salary))
print("name:{:s}\tsalary:{:0.2f}".format(name,salary))
print("name:%s\tsalary:%0.2f"%(name,salary))
