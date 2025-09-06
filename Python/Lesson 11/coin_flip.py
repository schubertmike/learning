#In this chapter we'll learn how to have our code make decisions
# we do this by evaluating different conditions and intro-ing logic

#here's an example
import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')
