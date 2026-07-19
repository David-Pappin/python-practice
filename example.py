import random, sys

print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0

while True:
    while True:
        print(f"\n{wins} Wins, {losses} Losses, {ties} Ties")
        print("\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit ")
        move = input(">")

        if move == "r" or move == "s" or move == "p":
            break
        else:
            if move == "q":
                sys.exit()

    comp = random.randint(1,3)
    comp_move = " "

    if move == "r":
        move2 = "ROCK"
    elif move == "p":
        move2 = "PAPER"
    elif move == "s":
        move2 = "SCISSORS"

    if comp == 1:
        comp_move = "r"
        move1 = "ROCK"
        

    elif comp == 2:
        comp_move = "p"
        move1 = "PAPER"
        

    elif comp == 3:
        comp_move = "s"
        move1 = "SCISSORS"
            
    if move == comp_move:
        print(f"{move2} versus...")
        print(move1)
        print("Its a tie")
        ties += 1
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")

    elif move == "r" and comp_move == "s":
        print("ROCK versus...")
        print(move1)
        print("You win!")
        wins += 1
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")

    elif move == "p" and comp_move == "r":
        print("PAPER versus...")
        print(move1)
        print("You win!")
        wins += 1
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")

    elif move == "s" and comp_move == "p":
        print("SCISSORS versus...")
        print(move1)
        print("You win!")
        wins += 1
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")

    elif move == "r" and comp_move == "p":
        print("ROCK versus...")
        print(move1)
        print("You lose!")
        losses += 1
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")

    elif move == "p" and comp_move == "s":
        print("PAPER versus...")
        print(move1)
        print("You lose!")
        losses += 1
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    
    elif move == "s" and comp_move == "r":
        print("SCISSORS versus...")
        print(move1)
        print("You lose!")
        losses += 1
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")


