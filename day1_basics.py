#print & input
print("Look who's here")
name = input("enter your name: ")
print("this is ",name," typing shit" )

num = 5
Pi = 3.14
dream = "Amy & Me"
YouInOrOut = True
print(type(num),type(Pi),type(dream),type(YouInOrOut))
print(num,Pi,dream,YouInOrOut)

#Can you vote? Conditions ifelse
yourName = input("enter your name: ")
##Age = (input("enter your age: "))
###Handle int better. Had this error originally

##Age = int(input("enter your age: ")) ##Beause any input data is considered str even if int is entered, so manually changed to int
##Here's an even better way to do it i.e. take input > check if digit or not > if not convert it, or throw msg. Check this out:

Age_entered = input("enter your age: ")
if Age_entered.isnumeric(): 
    Age = int(Age_entered)
    if Age >= 18:
        print("You can vote")
    else: 
        print("not yet buddy! Wait till you're 18")
else: 
    print("Wait is that even a number!! Enter a valid age man!")

###Loop
    #FOR Loop
for i in range(5):
    print(i)

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    
    if status == 'active':
        del users[user]


# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

#While loop
        count = 0
while count < 5:
    print(count)
    count +=1

##Function
    def greet(name):
        return "Hello " + name

print(greet("Santosh"))


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

