class student:
    school="Francis GHS"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

s1=student(10,20,30)
s2=student(40,50,60)

print(s1.avg())
print(s2.avg())
print(student.info())