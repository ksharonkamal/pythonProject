class computer:
    def __init__(self):
        self.name="Sharon"
        self.age=25

    def update(self):
        self.age=30

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1=computer()
c2=computer()

print(c1.name," ",c1.age)
print(c2.name," ",c2.age)

c1.name="Ashish"
c1.age=19

print(c1.name," ",c1.age)
print(c2.name," ",c2.age)

c1.update()

print(c1.name," ",c1.age)
print(c2.name," ",c2.age)

if c1.compare(c2):
    print("ages are same")
else:
    print("ages are different")