import random
listofwords = ['tessa','friday','jarvis','wonder','doctor','strange']
numberofchances = 3

selectedword = random.choice(listofwords).lower()
guessword=[]
alreadyguessed = []
for i in range(len(selectedword)):
    guessword.append('_')


while numberofchances != 0:
    print("Guess the word: "+" ".join(guessword).upper())

    guess = input("Enter guess letter: ").lower()
    
    if guess in alreadyguessed:
        print(guess+" is already used. Try again")
        continue
    else:
        alreadyguessed.append(guess)
    
    if guess in selectedword:
        index_pos_list = [i for i in range(len(selectedword)) if selectedword[i]==guess]
        for i in index_pos_list:
            guessword[i]=guess
    else:
        numberofchances-=1
    
    if numberofchances == 0:
        print("YOU LOSE !! Correct word is "+ selectedword)
        break
    else:
        print(f"Incorrect guess, you lose a chance. you have {numberofchances} left")


    if '_' not in guessword:
        numberofchances=0
        print(selectedword.upper())
        print("YOU WIN !! You guessed the word right.")