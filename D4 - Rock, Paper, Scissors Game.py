import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissors = [rock, paper, scissors]

print("Welcome to the Rock Paper Scissors game!")
user_input = int(input("Please type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
if user_input < 0 or user_input > 2:
    print("Please type 1 or 2")
else:
    print("You pick: ")
    print(rock_paper_scissors[user_input])
    computer_choice = random.randint(0,2)
    print(f"Computer choose: " + rock_paper_scissors[computer_choice])

    if user_input > 2 or user_input < 0:
        print("Please type 0, 1, or 2")
    elif user_input == 2 and computer_choice == 0:
        print("You lose!")
    elif user_input == computer_choice:
        print("It's a draw!")
    elif user_input > computer_choice:
        print("You win!")
    elif user_input < computer_choice:
        print("You lose!")

# if user_input == 1:
#     print(f"you pick: {rock}")
# elif user_input == 2:
#     print(f"You pick: {paper}")
# elif user_input == 3:
#     print(f"You pick: {scissors}")
# else:
#     print("Please type 1 or 2 or 3\n")

