import random

while True:
    answer = input("Choose Rock, Paper or Scissor :")
    answer = answer.lower()
    if answer != "rock" and answer != "paper" and answer != "scissor":
        print("Please enter correct answer")
        continue
    computer_answer = random.choice(["rock", "paper", "scissor"])
    print(f"Computer has choosed {computer_answer}")

    if computer_answer == answer:
        print("You tied")
    elif computer_answer == "paper" and answer == "rock":
        print("You Win!")
        break
    elif computer_answer == "scissor" and answer == "paper":
        print("You Win!")
        break
    elif computer_answer == "rock" and answer == "scissor":
        print("You Win!")
        break
    else:
        print("You lose, Start Again")