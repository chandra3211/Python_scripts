'''Variable - a variable is a container (storage area) to hold data. we use the assignment operator = to assign a value to a variable.
we can assign multiple variables'''
a, b, c = 5, 3.2, 'Hello'

print(a,b,c)

#output - 5 3.2 Hello

'''If we want to assign the same value to multiple variables at once, we can do this as:'''
a = b = 5
print(a)
print(b)

output:
5
5

Tuple Assignment:
x,y=(50,100)
print(x)
50
print(y)
100

List Assignment:
x,y=[100,200]
print(x,y)
100 200

a,b,c=10,20,30
print(a,b,c)
10 20 30
sequence assignment: Any sequence of names can be assigned to any sequence of values and python assign the value at a time by postition.
a,b,c='hai'
print(a)
h
print(b)
a
print(c)
i
extended sequence unpacking:
p,*q="Hello"
print(p)
H
print(*q)
['e','l','l','o']  
below are the conditions to write variables:
1. A variable name must start with a letter or underscore character(a-z) (_).
2. A variable name cant start with number.
3. A variable names are only have alpha-numeric characters and underscores (A-z, 0-9, _). (special characters are not allowed).
4. variable names are case-sensitive (name, Name, NAME are three different variabes).
5. variable name should not match with python keyword.


