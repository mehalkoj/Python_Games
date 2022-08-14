# Rock Paper Scissors

import random

entry_prompt = input("Will You Like To Play?   y/n")




def main():


    user = input("r = Rock, p = Paper, s = Scissors")
    computer = random.choice(['r', 'p', 's'])

   

    # Tie OutComes
    if user == computer:
        return 'tie'

    if win(user, computer) == True:
        print("You Win Bitch!")
    else: print("Lol you lost bitch!")



def win(player, cpu):
    if (player == 'r' and cpu == 's') or (player == 'p' and cpu == 'r') or (player == 's' and cpu == 'p'):
        return True
    

# if Statement for Game Selection
if entry_prompt == 'y':
     main()
else:
    print("ok")

