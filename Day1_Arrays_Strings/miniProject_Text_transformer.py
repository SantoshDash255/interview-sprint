def reverse_sentence(sentence):
    return sentence[::-1]


def reverse_word_order(sentence):
    s = sentence.split()
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return " ".join(s)


def reverse_each_word(sentence):
    s = sentence.split()
    rev = []
    for word in s:
        rev.append(word[::-1])
    return ' '.join(rev)


def count_characters(sentence):
    counts = {}
    for char in sentence:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def remove_duplicate_words(sentence):
    seen_this = set()
    s = sentence.split()
    resList = []
    for word in s:
        if word.lower() not in seen_this:
            seen_this.add(word)
            resList.append(word)
    return ' '.join(resList)

# Creating this functtion to make some space and improve readability in CLI


def print_title(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title))


def main():
    sentence = input("\nYour Sentence to play with: ")

    while True:
        print("\nLook at that!! So what are we doing with this?\n")
        print("1. Flip the whole thing backwards")
        print("2. Just flip these word sequence")
        print("3. Get in! Flip each word individually")
        print("4. How many times you had to type each letter there")
        print("5. Get rid of the duplicates. Original and unique words only!!")
        print("6. Get me outta here!! Bye now")

        choice = input(
            "\nSo guess you can read then! What do you want us to do?: \n")

        if not sentence.strip():
            print("No input detected. Why don't we give it another shot!")
            print('-'*40)
            continue
        if not choice.strip():
            print("Pick something, my Lord! What do I do with the empty enters?")
            print('-'*40)
            continue

        if choice == '1':
            print_title("Reversed Sentence entirely")
            print(reverse_sentence(sentence))
            print('-'*40)

        elif choice == '2':
            print_title("Reversed Word Order")
            print(reverse_word_order(sentence))
            print('-'*40)

        elif choice == '3':
            print_title("Reverse Each Word Individually")
            print(reverse_each_word(sentence))
            print('-'*40)

        elif choice == '4':
            print_title("Count how many times each character shows up")
            Fcount = count_characters(sentence)
            # for char, count in Fcount.items():
            #     print(f"'{char}' appears {count} times")
            # Tweaked the above 2 lines using lambda to show the most frequent letters first i.e. decending order
            for char, count in sorted(Fcount.items(), key=lambda x: x[1], reverse=True):
                print(f"'{char}' appears {count} times")
            print('-'*40)

        elif choice == '5':
            print_title("Remove duplicate words")
            print(remove_duplicate_words(sentence))
            print('-'*40)

        elif choice == '6':
            print_title("When I see you again...")
            print("\nGoodbye!")
            print('-'*40)
            break

        else:
            print("\nThat's a Red card!")
            print('-'*40)

        # Look for new sentence, if user wants. Give a choice
        change = input("\nWanna try a new sentence? (y/n): ")
        if change.lower() == 'y':
            print_title("Here we go again!!")
            sentence = input("\nOkay, what's the new line in mind?:\n ")
            print('-'*40)


if __name__ == "__main__":
    main()

# Wrapped our code in main() for future usability, instead of running directly in if__name__ = "__main__", so that we can may be import the functions later
# Example:
#     Later when we do your Day 5 mock interviews or a Flask API project, you might do this:

# from Day1_Arrays_Strings.text_transformer import remove_duplicate_words

# user_input = "this this is is clean now"
# print(remove_duplicate_words(user_input))


# Because of the main() wrapper, this works cleanly — it won’t start printing the CLI menu automatically when imported.

# ✅ TL;DR
# Concept	                Before	                                  After
# Structure	Direct      code in if __name__ == "__main__":	    Wrap logic in main()
# Entry point	             Implicit	                            Explicit
# Reusability	             Limited	                              High
# Professional style	       OK	                               ✅ Best practice
