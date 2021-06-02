# def myMethod():
#     return 1,2,3,4
# a,b,_,_=myMethod()
#
# print("a:",a)
# print("b:",b)

# import classFile
# classFile.public_api()
# classFile._private_api()

# from classFile import *
# public_api()
# # _private_api()
#  _private_api()

# import classFile
# obj=classFile.Myclass()
# obj.__add__(5,4)


# class String:
#     def __init__(self,string):
#         self.string=string
#     def __repr__(self):
#         return('object: %s '%(self.string))
#     def __add__(self, other):
#         return self.string+other
#
# string1=String('abcd')
# string1


class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    # def __str__(self):
    #     return f'Person name is {self.name} and age is {self.age}'

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


p = Person('Pankaj', 34)

print(p.__str__())
print(p.__repr__())

