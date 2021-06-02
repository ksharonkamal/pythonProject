class computer:
    def config(self):
        print("i5,16gb,1TB")

a='8'
com1=computer() #object creation, something like a constructor
com2=computer() #object creation

computer.config(com1)
computer.config(com2)

com1.config()
com2.config()
