#A set is an unordered, mutable collection of unique elements.
#Defined with curly braces { } or with set() constructor.
#no duplicates allowed.

s = {1, 2, 3, 3, 4}
print(s)   # {1, 2, 3, 4}  (duplicate removed)

#Real life analogy:
#A set is like your basket of fruits — you can’t have the same apple twice in the set, it only keeps unique ones.
#Order doesn’t matter.

#Creating Sets;
s1 = {1, 2, 3}
s2 = set([10, 20, 20, 30])   # from list
s3 = set("banana")           # from string → {'b','a','n'}

print(s1)
print(s2)
print(s3)


#Properties
#Unordered → no indexing/slicing like lists.
#Mutable → can add/remove elements.
#Unique elements only.

#. Basic Operations
s = {1, 2, 3}

s.add(4)           # add single element
s.update([5, 6])   # add multiple elements
print(s)           # {1,2,3,4,5,6}

s.remove(2)        # removes 2; error if not present
s.discard(10)      # no error if not found
x = s.pop()        # removes random element
print(x, s)

s.clear()          # empty the set


#Set Operations
A = {1,2,3,4}
B = {3,4,5,6}

print(A | B)    # union → {1,2,3,4,5,6}
print(A & B)    # intersection → {3,4}
print(A - B)    # difference → {1,2}
print(A ^ B)    # symmetric diff → {1,2,5,6}


#Membership Testing
fruits = {"apple", "banana", "mango"}

print("apple" in fruits)   # True
print("grape" in fruits)   # False


#Frozenset (Immutable Set)
fs = frozenset([1,2,3])
# fs.add(4)   ❌ error


