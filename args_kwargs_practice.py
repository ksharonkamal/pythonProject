# def my_sum(*args):
#     result = 0
#     # Iterating over the Python args tuple
#     for x in args:
#         result += x
#     return result
# print(my_sum(5,10,20))
#
# def concatenate(**kwargs):
#     result = ""
#     for arg in kwargs.values():
#         result += arg
#     return result
# print(concatenate(a="Real ", b="Python ", c="Is ", d="Great", e="!"))

# # correct function definition
# def my_function(a, b, *args, **kwargs):
#     pass
# # wrong function definition
# def my_function(a, b, **kwargs, *args):
#     pass


def arg_printer(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)
arg_printer(1, 4, 6, 5, param1=5, param2=6)
