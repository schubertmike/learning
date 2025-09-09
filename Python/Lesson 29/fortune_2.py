#rewriting the function without the if statement
import random
fortune_answer = ['Don\'t pursue happiness – create it.',
'All things are difficult before they are easy.',
'The early bird gets the worm, but the second mouse gets the cheese.',
'Someone in your life needs a letter from you.',
'Don\'t just think. Act!',
'Your heart will skip a beat.',
'The fortune you search for is in another cookie.',
'Why are these cookies so delicious!']

def fortune():
  random_number = random.randint(1,8)
  for i in range(random_number):
    print(fortune_answer[random_number])
    break
  
fortune()
fortune()
fortune()
