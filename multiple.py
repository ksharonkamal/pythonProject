#base class1
class Mother:
    mothername = ""
    def mother(self):
        print(mothername)

# Base class2
class Father:
    fathername = ""
    def father(self):
        print(fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Mother Name:",self.mothername)
        print("Father Name:",self.fathername)

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()