"""
Dictionary is used to store data in "key":"value" format (like JSON)
It is made with { }

syntax==> dictionary name = { "key":"value" , "key2":"value2" , .... }

**value of any key can also be different dictionary
"""

# assigning dictionary
dictionary1 = {
    "Person": {
        "City": "Surat",
        "Age": "19"
    },
    "Animal": {
        "Type": "Dog",
        "Name": "Rocky"
    },
    "Bird": "Peacock"
}

print(dictionary1)

# making copy of dictionary1
dictionary2 = dictionary1.copy()

# update dictionary and add insect to the dictionary
dictionary1.update({"Insect": "Bee"})
dictionary1["Other Key"] = "Other Value"

print(dictionary1)
print(dictionary2)  # does not have any effect on the copy

# change the value of bird (peacock --> sparrow)
dictionary2["Bird"] = "Sparrow"
print(dictionary2)

# printing the keys,values and item of the dictionary
print(dictionary1.keys())
print(dictionary1.items())
print(dictionary1.values())

# printing keys of inner dictionary
print(dictionary1["Person"].keys())

# printing particular value
print(dictionary1["Insect"])
print(dictionary1["Person"]["Age"])

# removing items from dictionary
print(dictionary1.pop("Other Key"))
print(dictionary1)
print(dictionary1.popitem())
print(dictionary1)

# using del function
del dictionary1["Animal"]
print(dictionary1)

# dictionary functions

# return dictionary with specified key and value
print(dict.fromkeys("Person"))
print(dict.fromkeys("Person", "value"))
"""
dict.clear() ==> removes all elements from dict
dict.get() ==> gets value of specified key

dict.setdefault() ==> returns the value of specified key
                      if key doesn't exist then create key and store specified value
"""
print(dictionary1.setdefault("Bird", "Sparrow"))
print(dictionary1.setdefault("Insect", "Bee"))
print(dictionary1)
