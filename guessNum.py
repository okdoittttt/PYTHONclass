import random

tires = 0
guess = 0
answer = random.randint(1, 100)

print("=========>Guess Number<=========")

while guess != answer:
    guess = int(input("Enter Number between 1 and 100: "))
    tires = tires + 1
    if tires > 9:
        print("=========>Fail<=========")
        break
    elif guess < answer:
        print("It's lower")
    elif guess > answer:
        print("It's upper")

if guess == answer:
    print("=========>That's right<=========")
    print("You Try[", tires, "]Times")
