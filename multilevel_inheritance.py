#Base class
class Grandfather:
    def __init__(self,grandfather):
        self.grandfather = grandfather

# Intermediate class
class Father(Grandfather):
    def __init__(self, father,grandfather):
        self.father = father
        super().__init__(grandfather)

# Derived class
class Son(Father):
    def __init__(self,son,father,grandfather):
        self.son = son
        super().__init__(father,grandfather)
    def print_name(self):
        print('Grandfather name :',self.grandfather)
        print("Father name :", self.father)
        print("Son name :", self.son)

# Driver code
obj1 = Son('Prince', 'Rampal', 'Lal mani')
print(obj1.grandfather)
obj1.print_name()