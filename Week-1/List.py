#1. LIST (Basiic Syntax)
#Ordered: elements have positions (indices).
#Mutable: you can change contents (assign, insert, delete).
#Can contain duplicates.
#Elements are references: L[0] refers to the same object as whatever was inserted.

# empty list
L = []
print (L)

# literal with mixed types
L1 = [1, "two", 3.0, [4, 5]]
print (L1)

# from iterable
L2 = list(range(5))  # [0, 1, 2, 3, 4]
print (L2)


#2. Indexing:
#Positive index: L[0] first element.
#Negative index: L[-1] last element.

a = ["apple", "banana", "mango"]
first = a[0]   
last = a[-1]  
print(first)
print(last)


#3. Slicing(start:stop:step)
L = [0,1,2,3,4,5,6,7,8,9]

L[2:6]      # [2,3,4,5]    (start=2, stop=6)
L[:4]       # [0,1,2,3]
L[5:]       # [5,6,7,8,9]
L[::2]      # every 2nd element: [0,2,4,6,8]
L[1:8:3]    # [1,4,7]
L[::-1]     # reversed: [9,8,7,6,5,4,3,2,1,0]
L[7:2:-1]   # [7,6,5,4,3]  (reverse slice)
L[-4:1:-1]  # [6, 5, 4, 3, 2]


#Slice assignment and deletion
L4 = [0,1,2,3,4,5]
L4[1:4] = ["a","b"]  
print(L4)   # [0,a,2,3,b,5]

# delete a slice
del L4[1:3]             # remove elements at index 1 and 2
print(L4)


#Common list methods:
L6 = [3,1,4,1,5]

L6.append(9)         # add at end
print(L6)
L6.extend([2,6])     # extend by iterable
print(L6)
L6.insert(2, 99)     # insert before index 2   list.insert(index, element)
print(L6)
L6.remove(1)         # remove first occurrence of value 1
print(L6)
x = L.pop()         # pop last element (default) -> O(1)
y = L.pop(0)        # pop at index 0 -> O(n)
L6.clear()           # empty the list
#L6.index(4)          # index of first 4 (raises ValueError if not found)
L6.count(1)          # count occurrences
L6.sort()            # in-place sort (mutates)
L6.reverse()         # reverse in-place
L7 = sorted(L)      # returns new sorted list

# copy
L_copy = L.copy()   # shallow


words = ["apple","banana","pear"]
words.sort(key=len)  # sorts by length
print(words)


#List comprehensions:
x = int(input("Enter the number: "))

#squares:
squares = [x*x for x in range(10)]
print(squares)

#evens:
# with condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# nested
pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
print(pairs)


#List operations & operators:
#Concatenation: a + b → new list
C1 = [1,2,3]
C2 = [4,5,6]
C3 = C1 + C2
print(C3)

#Repetition: a * 3
a1 = [4,5,6,7,8,9]
a2 = a1*2
print(a2)