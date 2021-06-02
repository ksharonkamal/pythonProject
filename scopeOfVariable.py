# def foo():
#     x = 20
#
#     def bar():
#         global x
#         x = 25
#
#     print("Before calling bar: ", x)
#     print("Calling bar now")
#     bar()
#     print("After calling bar: ", x)
#
#
# foo()
# print("x in main: ", x)
# x=30
# print("x in main: ", x)

# c = 1  # global variable
#
#
# def add():
#     global c
#     c = c + 2  # increment c by 2
#     print(c)
# add()

def outer():
    a = 5
    def inner():
        nonlocal a
        a = 10
    inner()
    print(a) #10
outer()

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
# print("x:", x)