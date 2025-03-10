import random


print("Let's play it.")

player = int(input("1 for rock\n 2 for paper\n 3 for scissors:\n"))

# it is a short form of writing if else 
print("you chose rock")if player == 1 else print("you chose paper") if player == 2 else print("you chose scissors")

if(player>3):
    print("Choose between 1,2 and 3")

else:
    comp = random.randint(1,3);
    if(comp == 1):
        print("computer chose rock")

    elif(comp == 2):
        print("computer chose paper")

    else:
        print("computer chose scissors")

    if(comp == player):
        print("drow play again:")

    else:
        if(comp == 1 and player == 2):
            print("you won")
        elif(comp == 1 and player == 3):
            print("Heh... you lose")
        elif(comp == 2 and player == 1):
            print("Heh... You lose")
        elif(comp == 2 and player == 3):
            print("you won ")
        elif(comp == 3 and player == 1):
            print("you won")
        else:
            print("Heh... You lose")