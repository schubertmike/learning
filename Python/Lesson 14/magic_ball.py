#exploring random and randint
#randome is a module in the standard libary that can perform random-ish number generation and operation
#randint gives us a random integer within the parameters

#let's use these to create a magic 8 ball

import random

#random.randint(1, 9)

#sets the answer parameters between 1 and 9
magic_ball = random.randint(1, 9)

#asks the input question
input('What is your question? ')

#logic for random answer responses
if magic_ball == 1:
  print('Yes - definitely')
elif magic_ball == 2:
  print('It is decidedly so')
elif magic_ball == 3:
  print('Without a doubt')
elif magic_ball == 4:
  print('Reply hazy, try again')
elif magic_ball == 5:
  print('Ask again later')
elif magic_ball == 6:
  print('Better not tell you now')
elif magic_ball == 7:
  print('My sources say no')
elif magic_ball == 8:
  print('Outlook not so good')
else:     
  print('Very doubtful')
