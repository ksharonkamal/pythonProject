class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        # self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        # self.lap.show()

    class laptop:
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=student("Sharon",2)
s2=student("Sarah",3)

s1.show()
s2.show()

lap1=student.laptop()
lap2=student.laptop()

lap1.show()
lap2.show()

lap2.brand="dell"
lap2.show()