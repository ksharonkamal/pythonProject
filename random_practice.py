import random

li=[10,20,30,40,50,60,70,80,90]
print("random number from li:",random.choice(li))

list2=random.randrange(30,50,3)
print("randome number from list2 :",list2)

print("li list before shuffling:",li)
random.shuffle(li)
print("li list after shuffling:",li)