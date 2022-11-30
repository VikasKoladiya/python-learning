"""input() func stores values always as String in Python"""

# get input from user with input() func
# input stores value (str)
print("Enter Number 1:", end=" ")
n1 = input()
print("Enter Number 2:", end=" ")
n2 = input()

# print default type of n1 and n2 (str)
print(type(n1), type(n2))

# print n1 and n2 (str)
print(n1 + n2)

# convert to int and calculate
total = int(n1) + int(n2)

# print total (int)
print(total)
