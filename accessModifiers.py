# # defining a class Employee
# class Employee:
#     # constructor
#     def __init__(self, name, sal):
#         self._name = name; # protected attribute
#         self._sal = sal; # protected attribute
#     def _display(self):
#         print ("Emp Name:",self._name)
#         print("Emp sal:",self._sal)
#
# # defining a child class
# class HR(Employee):
#     # member function task
#     def task(self):
#         print ("Emp Name:",self._name)
#
# emp=HR("Ash",200000)
# emp._display()
# emp.task()

# defining class Employee for private
class Employee:
    def __init__(self, name, sal):
        self.__name = name; # private attribute
        self.__sal = sal; # private attribute

emp=Employee('asdf',10000)
print(dir(emp))
print(emp._Employee__name, emp._Employee__sal)
