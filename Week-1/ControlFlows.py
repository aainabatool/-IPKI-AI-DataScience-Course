#Conditions:
#if/else:
print("IF/ELSE")
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote!")
else:
    print("You are too young to vote.")


#Elif
print("Elif")
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


#Loops:
print("Loops")
#1. For Loop:
print("For Loop")
for i in range(1, 6):
    print("Number:", i)

#continue/break:
for i in range(1, 11):
    if i == 5:
        continue
    print(i)



# While loop
print("While Loop")
count = 1
while count <= 5:
    print("Count is", count)
    count += 1

