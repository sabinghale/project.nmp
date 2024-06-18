
# guessing the number
import random
import math
lower_num = int(input('enter the lower number: '))
upper_num = int(input('enter the upper number: '))
x = random.randint(lower_num, upper_num)
min_guess = round(math.log(upper_num - lower_num + 1, 2))
print(f'\nyou have only {min_guess} chances to guess the number!\n')
count = 0
while count < min_guess:
  count += 1
  guess = int(input('guess a number: '))

  if x == guess:
    print(f'congrulation you did it in {count} try')
    break
  elif x > guess:
     print('you guessed too small!')
  elif x < guess:
     print('you gussed is too high!')
  if count >= min_guess:
     print(f'\nThe number is {x}\n\tBetter Luck Next Time!')
          
          
          
          
          


          