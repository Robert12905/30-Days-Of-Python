#!/usr/bin/env python3

print("", "Example 1", sep="\n", end="\n")
print(3+4,",", end=" ")
print(3-4,",", end=" ")
print(3*4,",", end=" ")
print(3%4,",", end=" ")
print(3**4,",", end=" ")
print(3//4,",", end="\n")

print("Robert Benstine ", end="\n")
print("Benstine", end="\n")
print("United States of America", end="\n")

print("", "Example 2", sep="\n", end="\n")
print("Data Types", end=":\n")
print(
        type(10), 
        type(9.8), 
        type(3.14), 
        type(4-4j), 
        type(['Asabeneh', 'Python', 'Finland']), 
        type("Robert"), 
        type("Benstine"), 
        type('USA'),

        sep="\n"
)

print("", "Example 3", sep="\n", end="\n")

empty_set=set()

muscle = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
print(
    (type(2)), # number
    (type(2.1)), # float
    (type(2j)), # complex ---- j/J are the ONLY allowed characters
#___________________________________________________________________#
    type("Roberts Code Sucks"), # string
    type(True),
    type([1,2,3,4,5]),
    type((1,2,3,4,5)),
    type(set()),
    type(muscle),
    end = "\n\n"
)

# Find an Euclidean distance between (2, 3) and (10, 8)

euclid = (
    (
        ((2-10)**2)
      + 
        ((3-8)**2)
    )
        **.5
)
print(euclid)