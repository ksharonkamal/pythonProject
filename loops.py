# i=1
# while (i<=5):
#     print("hello")
#     i=i+1

# i=5
# while (i>=1):
#     print("hello")
#     i=i-1

# i=1
# while(i<=5):
#     print("hi ",end="")
#     j = 1
#     while(j<=3):
#         print("welcome ",end="")
#         j+=1
#     i+=1
#     print()

#----for loops------

# x=['Welcome',89,45.6]
# for i in x:
#     print(i)


# for i in range(10,31,2):
#     print(i," ",end="")

# for i in range(31,15,-5):
#     print(i," ",end="")


# for i in range(1,21):
#     if(i%5 != 0):
#         print(i)

#-----break------
# av=10
# x=int(input("enter how many candies you want"))
# i=1
# while(i<=x):
#     if(i>av):
#         print("out of stock")
#         break
#     print("candy",i)
#     i+=1


#-------continue------
# for i in range(1,101):
#     if((i%3==0)  or (i%5==0)):
#          continue
#     print(i)
# print("done")



#-------pass------
# for i in range(1,50):
#     if((i%3==0)  or (i%5==0)):
#          pass
#     print(i)
# print("done")


#-----Printing Patterns------
# for i in range(4):            #rows
#     for j in range(4):        #cols
#         print("# ",end="")
#     print()


# for i in range(4):
#     for j in range(i+1):
#         print("# ",end="")
#     print()



for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()
