# start the game 
# ask the player to make a move (r,p,s)
# pc choose the move randomly 
# pc == player > it’s a tie 
# elif (player== p and pc== r) or (player== r and pc== s) or (player== s and pc== p) > you won 
# else you lost / pc win 

import random

print("🎮 Game started!")

name = input("What is your name? ")
print(f"Welcome, {name}!")

while True:
    user = input("\nChoose your move: 'r' for rock, 'p' for paper, 's' for scissors: ")
    pc = random.choice(['r', 'p', 's'])

    print(f"{name} played: {user}")
    print("PC played: " + pc)

    if user == pc:
        print("It's a tie!")
    elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
        print("You won!")
    else:
        print("You lose!")

    # Ask if player wants to play again
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing, " + name + "!")
        break


