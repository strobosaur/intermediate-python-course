import random
dice_rolls = 2

def main():

  dice_sum = 0

  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    if (roll == 1):
      print(f'Ouch! You rolled a {roll}')
    elif (roll == 6):
      print(f'Nice! You rolled a {roll}')
    else:
      print(f'You rolled a {roll}')

  print(f'Dice roll total: {dice_sum}')

if __name__== "__main__":
  main()