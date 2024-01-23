import numpy

print("Hello, world!")

#print("Enter string")
#wish=input()
#print("Your wish is", wish)

var = (5 + 4) / 3
print(var)

print(10 ** 3 == 1000)

# Conditional statements
age = 0
if age >= 18:
    print('adult')
else:
    if age<0:
        print('negative age variable')
    else:
        print('child')

# Loops
#for number in [1, 2, 3, 4, 5]:
    #print(number)

# Loops
my_list = [3, 6, 9]
for x in my_list:
    print(x / 3)

# Functions
def is_adult(age):

    if age >= 18:
        print('adult')
    else:
        print('child')

# Use the function that was just created.
is_adult(14)

# Use the built-in sorted() function.
new_list = [20, 25, 10, 5]

print(sorted(new_list))

magic = 'hocus pocus'
print(type(magic))
intVar = 27
print(type(intVar))
floatVar = 98.3
print(type(floatVar))
letterVar = 'a'
print(type(letterVar))