import random


choice = input('Want To Role The Dice?   y/n')




def main():
    dice_sides = [1, 2, 3, 4, 5, 6]

    dice_roll_1 = random.choice(dice_sides)
    dice_roll_2 = random.choice(dice_sides)

    print(f'{dice_roll_1} \n{dice_roll_2}')





if choice == 'y':
    main()

