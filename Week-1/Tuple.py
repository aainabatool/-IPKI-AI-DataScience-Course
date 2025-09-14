
#A tuple is an ordered, immutable sequence.
#Defined with parentheses ( ).
#Can hold mixed data types, even nested tuples.

t1 = (1, 2, 3)
t2 = ("apple", "banana", "mango")
t3 = (1, "hello", 3.14, [10, 20])
print(t1)
print(t2)
print(t3)

t = (5,)
print(type(t))   # <class 'tuple'>


#Indexing and Slicing
#Tuples behave like lists for accessing elements.
t = (10, 20, 30, 40, 50)

print(t[0])      # 10
print(t[-1])     # 50
print(t[1:4])    # (20, 30, 40)
print(t[::-1])   # (50, 40, 30, 20, 10)


#Tuple Operations
t1 = (1, 2, 3)
t2 = (4, 5)

print(t1 + t2)      # concatenation → (1,2,3,4,5)
print(t1 * 3)       # repetition → (1,2,3,1,2,3,1,2,3)
print(len(t1))      # length → 3
print(2 in t1)      # membership → True


#Immutability
#You cannot change elements of a tuple after creation.
#But if it contains a mutable object (like a list), that list can be modified.

t = (1, 2, [3, 4])
t[2][0] = 99
print(t)    # (1, 2, [99, 4])

t[0] = 1
print(t)