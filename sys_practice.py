import sys
print(sys.version)
for i in sys.argv:
    print("sys.argv:",i)
print(sys.path)
print(sys.modules)
sys.exit()
print("ended")
