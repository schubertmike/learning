import random
play = 'yes'
print('===================')
print('Rock Paper Scissors')
print('===================')
print('1 - ✊')
print('2 - ✋')
print('3 - ✌️')

while play == 'yes':
  user = int(input('Rock paper scissors shoot (pick a number): '))
  cpu = random.randint(1,3)

  print(user)
  print(cpu)

  if user == cpu:
    print('You tied!')
  elif user == 1 and cpu == 2:
    print('CPU Wins! You rock has been surrounded')
  elif user == 1 and cpu == 3:
    print('You win! You\'ve smashed their scissors')
  elif user == 2 and cpu == 1:
    print('You win! You\'ve engulfed their rock')
  elif user == 2 and cpu == 3:
    print('CPU wins! Your paper has been cut to pieces')
  elif user == 3 and cpu == 1:
    print('CPU wins! you scissors have been destroyed')
  elif user == 3 and cpu == 2:
    print('You win! You shredded their paper')
  play = input('want to keep playing? ')
print('Thanks for playing!')  
