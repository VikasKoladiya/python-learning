"""
if conditions

syntax =>
        if <condition> :
                <statement>
        elif <condition> :
                <statement>
        else :
                <statement>

in keyword =>
    it is used to check whether an element is present in the array or not
"""

a = int(input())
b = int(input())

if a > b:
    print("a")
elif a < b:
    print("b")
else:
    print("equal")
print()
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

if 1 in list1:
    print("true", "1 is there")

if 10 not in list1:
    print("true", "10 is not there")
