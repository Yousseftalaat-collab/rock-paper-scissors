import random

print("🎮 Game Started!")

name = input("What is your name? ")
print(f"Welcome, {name}!")

while True:
    print("\nChoose your move:")
    print("Type 'r' for Rock")
    print("Type 'p' for Paper")
    print("Type 's' for Scissors")

    user = input("Your move: ").lower()

    if user not in ['r', 'p', 's']:
        print("Invalid choice. Please enter 'r', 'p', or 's'.")
        continue

    pc = random.choice(['r', 'p', 's'])

    print(f"\n{name} played: {user}")
    print(f"Computer played: {pc}")

    if user == pc:
        print("It's a tie!")
    elif (user == 'r' and pc == 's') or (user == 'p' and pc == 'r') or (user == 's' and pc == 'p'):
        print("You won!")
    else:
        print("You lost!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {name}! Goodbye! 👋")
        break
