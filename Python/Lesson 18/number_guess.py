# more while loops
#original loop
guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries = tries + 1
print("You got it!")

#modified loop
guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries = tries + 1
if tries >= 5:
  print('Oh no! you ran out of tries')
if guess == 6:
  print("You got it!")

#this loop checks for the guess and the number of tries
#if the number of tries matches or exceeds the condition in the while loop, then it prints a failure message
#if the guess = 6, then it prints a success message
#this does not account for if the guess is 6 and the number of tries = 5. But that solution might be as simple as including 2 conditions with an and operator
