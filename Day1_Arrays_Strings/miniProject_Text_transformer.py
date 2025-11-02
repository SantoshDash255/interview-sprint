def reverse_sentence(sentence):
    return sentence[::-1]
    pass

def reverse_word_order(sentence):
    s = sentence.split()
    left,right = 0, len(s)-1
    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
    return " ".join(s)
    pass

def reverse_each_word(sentence):
    s = sentence.split()
    rev = []
    for word in s:
        rev.append(word[::-1]) 
    return ' '.join(rev)
    pass

def count_characters(sentence):
    counts = {}
    for char in sentence:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
    pass

def remove_duplicate_words(sentence):
    SeenSet = set()
    s = sentence.split()
    resList = []
    for word in s:
        if word not in SeenSet:
            SeenSet.add(word)
            resList.append(word)
    return ' '.join(resList)
    pass


if __name__ == "__main__":
    sentence = input("\nYour Sentence to play with: ")

while True:
    print("\nLook at that!! So what are we doing with this?")
    print("1. Flip the whole thing backwards")
    print("2. Just flip these word sequence")
    print("3. Get in! Flip each word individually")
    print("4. How many times you had to type each letter there")
    print("5. Get rid of the duplicates. Original and unique words only!!")
    print("6. Get me outta here!! Bye now")
    choice = input("\nSo guess you can read then! What do you want us to do?: \n")
    
    if choice == '1':
        print(reverse_sentence(sentence))
    elif choice == '2':
        print(reverse_word_order(sentence))
    elif choice == '3':
        print(reverse_each_word(sentence))
    elif choice == '4':
        print(count_characters(sentence))
    elif choice == '5':
        print(remove_duplicate_words(sentence))
    elif choice == '6':
        print("\nGoodbye!")
        break
    else:
        print("\nThat's a Red card!")



 

    


