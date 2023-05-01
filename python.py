# x = 0;
# y = 0;

# sum = 0;

# x = input("X: ")
# y = input("Y: ")

# sum = int(x) + int(y)

# print("Answer is: ")
# print(sum)

correct = "IndyPy"
tries = 0
keepGoing = True

while keepGoing:
    tries += 1
    print("Try #", tries)

    guess = input("What is the password? ")
    if guess == correct:
        print("That's right")
        keepGoing = False
    elif tries >= 3:
        print("Too many tries, bye bye!")
        keepGoing = False
    else:
        print("Invalid password. Try again.")