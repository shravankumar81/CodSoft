import random
def game():
    options = ["rock", "paper", "scissors"]
    while True:
        user=int(input("Choose 1.rock, 2.paper, or 3.scissors: "))
        if user==1:
            print("user choosed rock")
            break
        elif user==2:
            print("user choosed paper")
            break
        elif user==3:
            print("user choosed scissor")
            break
    comchoice = random.choice(options)
    print(f"You chose: {user}")
    print(f"Computer chose: {comchoice}")
    if user == comchoice:
        print("It's a tie!")
    elif user == "rock" and comchoice == "scissors":
        print("You win!")
    elif user == "paper" and comchoice == "rock":
        print("You win!")
    elif user == "scissors" and comchoice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
game()
