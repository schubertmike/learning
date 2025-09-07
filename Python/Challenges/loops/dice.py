#rolling dice until I get snake eyes
import random
#establishing the variables
die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = die1 + die2
#looping if total is not 2
while total != 2:
#if not 2, then print nope, update variables, and keep going
  print('Nope')
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  total = die1 + die2
#if 2, break the loop and print snake eyes
print('Snake eyes!')
