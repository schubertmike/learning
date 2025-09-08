#creating a simple lottery program
import random
#setting empty lists to start
winning_numbers = []
my_numbers = []
#looping through 5 iterations for 5 different numbers
for i in range(0,5):
  #in each iteration, append each list with a random number between 1 and 69
  winning_numbers.append(random.randint(1,69))
  my_numbers.append(random.randint(1,69))

#after the loop, append each list with a random number between 1 and 26
my_numbers.append(random.randint(1,26))
winning_numbers.append(random.randint(1,26))

#print the lists
print('My Numbers: ' , my_numbers)
print('Winning Numbers: ' , winning_numbers)
