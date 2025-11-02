############################################
#LIST/ARRAY
############################################

#Create a list of numbers [1, 3, 5, 7] → print all elements

NumList = [1, 3, 5, 7]
print(NumList)

# Reverse it using slicing & reverse() method
#Using reverse() method
NumList.reverse()
print(NumList)

#Using slicers
RevList = NumList[::-1]
print(RevList)

# Double every element using list comprehension
DoubleList = [x*2 for x in NumList]
print(DoubleList)

#########################################################
# STRINGS
########################################################
# Hands-on tasks:

# Reverse a string using slicing and list()
String = "Here we go!!"
RevStr = String[::-1]
print(RevStr)
#Using list()
List = list(String)
RStr = List[::-1]
print(RStr)

# Split a sentence into words and reverse word order
Words = String.split(" ")
RWords = Words[::-1]
print(RWords)

# Count occurrences of each character in a string
for i in range(len(String)):
    x = String.count(String[i])
    print(f'{String[i]} is found {x} times')

#how to avoid duplicate letters? Dictionary or something better?
letters = dict(String)
print(letters)
