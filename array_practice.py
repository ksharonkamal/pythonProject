# importing "array" for array creations
import array as arr
# creating an array with integer type
a = arr.array('i', [1, 2, 3]) #integer
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3]) #double
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
print(type(b))

# array with int type
a = arr.array('i', [1, 2, 3])
# inserting array
a.insert(1, 4) # inserting 4 in 1 index
print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()
a.append(5)
print ("Array after appending : ", end =" ")
for i in (a):
    print (i, end =" ")
print()

a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("Access element is: ", a[1])

print ("The popped element is : ", end ="")
print (a.pop(2))
print ("Array after popping : ", end =" ")
for i in (a):
    print (i, end =" ")
print()

sliced_array = a[3:]
print ("sliced_Array after slicing : ", end =" ")
for i in (sliced_array):
    print (i, end =" ")
print()
print ("Array after slicing : ", end =" ")
for i in (a):
    print (i, end =" ")
print()


# array('i', [4, 5, 6])