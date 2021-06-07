import sys
a=range(1,10)
# b=range(1,10000)

print("The size aloted using range is: ")
print(sys.getsizeof(a))
print(type(a))
for n in a:
    print(n,end=" ")
