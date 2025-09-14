#A dictionary is a collection of key–value pairs.
#Keys are unique & immutable (string, number, tuple).
#Values can be of any type (even lists, sets, or other dicts).
#Defined with curly braces {} and colons :.

student = {
    "name": "Aaina",
    "age": 21,
    "course": "Python"
}

print(student)


#Creating Dictionaries
d1 = {"a": 1, "b": 2, "c": 3}
d2 = dict(x=10, y=20, z=30)         # using dict()
d3 = dict([("name", "Ali"), ("age", 21)])  # from list of tuples
d = {} # empty dict
print(d1)
print(d2)
print(d3)


#Accessing Values
student = {"name": "Aaina", "age": 20}

print(student["name"])      # Aaina
print(student.get("age"))   # 20
print(student.get("grade", "Not Found"))  # returns default if missing


#Modifying Dictionary
student["age"] = 23             # update
student["course"] = "Gen AI"     # add new key
print(student)


#Removing Elements
student2 = {"name": "AYESHA", "age": 25, "course": "Programming for AI"}

print(student2.pop("age"))          # removes key, returns value
print(student2.popitem())           # removes last inserted key–value
#del student["course"]       # delete key
#student.clear()             # empty dictionary
print(student2)
student2.clear()    
print(student2)


#Dictionary Methods:
person = {"name": "Sara", "age": 25}

print(person.keys())        # dict_keys(['name','age'])
print(person.values())      # dict_values(['Sara',25])
print(person.items())       # dict_items([('name','Sara'),('age',25)])

for k, v in person.items():
    print(k, ":", v)

#Nesting (Dictionary inside Dictionary):
students = {
    "Ali": {"age": 20, "course": "Math"},
    "Sara": {"age": 22, "course": "Physics"}
}

print(students["Ali"]["course"])   # Math


#Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print(squares)   # {0:0, 1:1, 2:4, 3:9, 4:16}

even_squares = {x: x**2 for x in range(10) if x%2==0}
print(even_squares)


#Real-Life Use Cases
#JSON-like data (APIs, configs).
#Storing student records, employee details.
#Word frequency counting.