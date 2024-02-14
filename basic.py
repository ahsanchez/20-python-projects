# python program
'''
multi line comments
first python program
'''
a = 5
b = 10

c = a+b
print("a + b =",c)

#value = input("Enter some value: ")
#print (value)
#print (type(value))

#intValue =int(input("Enter some value: "))
intValue = 20
print (intValue)
print (type(intValue))

if intValue%2==0:
    print("Number is even:", intValue)
else:
    print("Number is odd:", intValue)

# tables
for i in range(1,11):
    print(i)

fruits = ["apple", "orange", "banana", "pear"] # list == array
print (fruits[3])
print (fruits)
print (type(fruits))

fruitsTuple = ("apple", "orange", "banana", "pear") # tuple
print (type(fruitsTuple))
print (fruitsTuple[1])
print (fruitsTuple)

fruitsSet = {"apple", "orange", "banana", "pear"} # set
print (type(fruitsSet))
# No se puede hacer con un set: print (fruitsSet[1])
print (fruitsSet)