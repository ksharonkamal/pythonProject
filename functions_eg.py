print("hello world")
def call_by_val(val):
    val="i am inside call_by_val method"
    print(val)
def call_by_ref(val):
    val[1]=5
    print(val)

val="hi"
print("before calling call_by_val method",val)
call_by_val(val)
print("after calling call_by_val method",val)

val=[1,2,3]
print("before calling call_by_ref method",val)
call_by_ref(val)
print("after calling call_by_ref method",val)
