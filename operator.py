#the floor division // rounds the result down to the nearest whole number
p = 15
t = 2
print(p // t)

#Assignment operators are used to assign values to variables
u = 5
t **= 3
print(t)

#Comparison operators are used to compare two values:
# returns True because 8 is not equal to 3
t = 8
f = 3
print(t != f)

#Logical operators are used to combine conditional statements
# returns True because 5 is greater than 3 AND 5 is less than 10
u = 7
print(u > 3 and u < 20)\

#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
x = ["chocolate", "cake"]
y = ["chocolate", "cake"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
