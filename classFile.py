#Python class_file.py FOR underscore.py example
def public_api():
    print ("public api")
def _private_api():
    print ("private api")

class Myclass():
    def __add__(self,a,b):
        print (a*b)