class student:
    school="Francis GHS"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self): #Accessor Method
        return self.m1

    def set_m1(self,value): #Mutator Method
        self.m1=value

s1=student(10,20,30)
s2=student(40,50,60)

print(s1.avg())
print(s2.avg())

s2.set_m1(11)

print(s1.get_m1())
print(s2.get_m1())