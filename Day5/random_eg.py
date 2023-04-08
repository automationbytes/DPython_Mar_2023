import random
num = random.random() #0.1-1.0
print(num)

print(random.randint(999999999,9999999999))

print(random.randrange(999999999,9999999999,5))

randomlist = random.choice(["Tom","Jerry","Tim","David","Jack","Jill"])
print(randomlist)

randomset = random.choice(("Tom","Jerry","Tim","David","Jack","Jill"))
print(randomset)

lis1 = ["Tom","Jerry","Tim","David","Jack","Jill"]
random.shuffle(lis1)
print(lis1)