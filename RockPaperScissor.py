
print("Welcome to the Game of Rock, Paper, Scissor")

u1 = input("Player1 name: ")
u2 = input("Player2 name: ")
choice_u1=input("Player1: Enter r for Rock, p for Paper, s for Scissor: ")
choice_u2=input("Player2: Enter r for Rock, p for Paper, s for Scissor: ")

if choice_u1.lower() == choice_u2.lower():
    print("It's a tie")
elif choice_u1.lower() == 'r' and choice_u2.lower() == 's':
    print(u1+" wins!!")
elif choice_u1.lower() == 'p' and choice_u2.lower() == 'r':
    print(u1+" wins!!")
elif choice_u1.lower() == 's' and choice_u2.lower() == 'p':
    print(u1+" wins!!")
else:
    print(u2+" wins!!")