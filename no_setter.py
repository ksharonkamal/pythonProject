class nosetter(object):
    def __init__(self,num):
        self._value = num

    @property
    def get_func(self):
        return self._value

x = nosetter(500)
print(x.get_func)

x.get_func = 900
print(x.get_func)


# def mk(x):
#     def mk1():
#         print("Decorated")
#         x()
#     return mk1
#
# def mk2():
#     print("Ordinary")
#
# p = mk(mk2)
# p()