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
