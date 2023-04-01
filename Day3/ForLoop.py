#range

for i in range(1,15,1):
    print(i)

print("-----------------------")

for i in range(1,15,2):
    print(i)


print("-----------------------")

for i in range(15,0,-1):
    print(i)


print("-----------------------")
#start - 0 and step - 1
for i in range(15):
    print(i)



print("-----------------------")
#step - 1
for i in range(0,50,1):
    if i == 25:
        continue
    print(i)

#for(int i =50; i>0;i--)



fruit = ["Apple","Mango","Pineapple"]
for f in fruit:
    print(f)

color = ["red","blue","green"]
fruit = ["Apple","Mango","Pineapple"]
for c in color:
    for f in fruit:
        print(c,f)
        print("Hello - Inside loop")
print("Hello - outside loop")