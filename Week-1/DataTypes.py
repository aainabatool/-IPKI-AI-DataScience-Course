#Variables:
x = 12
y = "Ali"

#DataTypes:
#1. Numerical:
age = 19      #int
height = 5.4  #float
z = 3 + 4j   #complex

print(age)
print(height)
print(z)
print(z.real)

#2.String:
name_1 = "aaina"
name_2 = 'batool'
print(name_1)
print("My name is:", name_2)

print("I am doing great.")

#3. Boolean
is_True = True
is_valid = False

#4. List -> hols multiple values
fruits = ['apple', 'banana', 'peach', 'avocado']
print(fruits)
print(fruits[0])
print(fruits[:2])
print(fruits[1:])

#append
fruits.append("watermelon")
print(fruits)

#insert
fruits.insert(1, "orange")
print(fruits)

#del/remove
fruits.remove("banana")     #deletes by value
print(fruits)

fruits.pop()                #delets by index, default by last 
print(fruits)

#5. Dicionaries:
student = {"name": "Ali", "age": 18, "grade" : "A"}
print(student["name"])
print(student["age"])
print(student)

info = {
    "name" : "Hamdan",
    "age"  : 21,
    "marks": [21,43,67],
    "address": {"street": 17, "city": "rawalpindi"}
}
print(info)

#Input:
user = input("Enter youre name? ")
print("Hello", user)

