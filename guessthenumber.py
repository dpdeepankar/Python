import random

number = random.randint(1,20)

chances = 5
while chances != 0:
    guess = int(input("Guess the number between 1-20: "))

    if guess == number:
        print("YOU WIN !! you guessed it correctly")
        break
    else:
        chances-=1
        print(f"Incorrect guess. You have {chances} left")
        if guess > number:
            print("HINT: number is smaller")
        else:
            print("HINT: number is larger")
else:
    print(f"The number is : {number}")