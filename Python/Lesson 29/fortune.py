#we can build functions from scratch!? That's awesome!
'''first we need to define the function with a name. e.g. def move_right():
code inside the function must be indented, just like with if statements and while loops.
once we are done, we can call the function. e.g. move_right()'''
import random
random_number = random.randint(1,8)

def fortune():
  random_number = random.randint(1,8)
  if random_number == 1:
    print('Don\'t pursue happiness - create it.')
  elif random_number == 2:
    print('All things are difficult before they are easy.')
  elif random_number == 3:
    print('The early bird gets the worm, but the second mouse gets the cheese.')
  elif random_number == 4:
    print('Someone in your life needs a letter from you.')
  elif random_number == 5:
    print('Don\'t just think. Act!')
  elif random_number == 6:
    print('Your heart will skip a beat.')
  elif random_number == 7:
    print('The fortune you search for is in another cookie.')
  elif random_number == 8:
    print('Why are these cookies so delicious!')

fortune()
fortune()
fortune()
