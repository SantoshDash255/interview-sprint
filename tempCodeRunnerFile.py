def unique_letters (text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        elif char == ' ': 
            pass
        else:
            counts[char] = 1
    return counts

x = unique_letters("Here we go!!")
max = list(x.keys())
max.sort()

sd = {i: x[i] for i in max}
print(sd)