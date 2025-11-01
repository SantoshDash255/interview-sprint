##function that takes a number and prints all even numbers from 0 to that number. Well I'll throw in the sum of all nums from 0 as well!!

def sum(num):
    total = 0
    for i in range(num+1):
        total += i
        if i % 2 == 0: print(i)       
    return total

LimitEntered = input("Enter the number you wish to sum starting from 0: ")
if LimitEntered.isdigit(): 
    Limit = int(LimitEntered)
    print("\nOkay so here are the even numbers: \n")
    print("Your total is", sum(Limit))
else:
    print("Enter a valid number dude!!")