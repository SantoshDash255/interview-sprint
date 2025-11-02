
#########################################################
# STRINGS
########################################################
# Hands-on tasks:

# Count occurrences of each character in a string
String = "Here we go!!"
for i in range(len(String)):
    x = String.count(String[i])
    print(f'{String[i]} is found {x} times')

#how to avoid duplicate letters in output? Using Dictionary?
def frequency(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] +=  1
        else:
            counts[char] = 1
    return counts
print(frequency("Here we go!!"))




