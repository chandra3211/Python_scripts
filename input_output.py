input() function:
1. The input() function is used to read data from keyboard.
2. it reads data into string format by default.
3. we should convert data into specific format from string before using them.
4. To convert use the int, float, str functions.
     - int(2.3) returns 2, int("123") returns 123
     - float(6) returns 6.0, float("3.14") returns 3.14
     - str(123) returns "123"
5. if conversion not possible then it will give an error.

a = input("enter a number")
b = input("enter a number")
inputs:
enter a number10
enter a number20
print(a)
10
print(b)
20
c= a+b; print(c)
output:
1020
note: it print 1020 instead of 30 because it takes string as input values by default.
a = int(input("enter a number"))
b = int(input("enter a number"))
enter a number10
enter a number20
c = a+b; print(c)
output: 30
  
print() function:
The print() function prints the specific text or value on the screen.

print("Hello","my","name","is","Chandra")
ouput: Hello my name is Chandra

print("Hello","my","name","is","Chandra", sep="\n") #sep means seperate
Hello
my
name
is
Chandra 
print("Hello","my","name","is","Chandra", sep="-")
Hello-my-name-is-Chandra
print("Hello", end=" ") #end operator is used to merge both prints.
print("Good Morning")
output: Hello Good Morning

a=10
b=4.5
print("%d is integer and %f is an float"%(a,b))
output: 10 is integer and 4.500000 is an float
note: %d used for all interger vaule and %f used for all float value
  %(a,b) it should in order mean %d is integer specify integer value first then %f second
a=10
b=4.5
print("%f is integer and %d is an float"%(b,a))
output: 4.500000 is integer and 10 is an float
  
c=10/3
print("C=%f"%c)
notepad: 3.333333
c=10/3
print("C=%.2f"%c)
notepad: 3.33
a=10
b=20.55
print(a,"is a integer",b,"is a float")
10 is a integer 20.55 is a float
  
  
  
