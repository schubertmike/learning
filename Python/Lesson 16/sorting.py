#sorting hat quiz
#initial point assignments
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
#1st question print with options and asking for input of answer
print('Do you like Dawn or Dusk?')
print('1: Dawn')
print('2: Dusk')
q1 = int(input('Please answer with either 1, or 2: '))

#logic to assign score to a house
if q1 == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif q1 == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print('Wrong input')
#question 2
print('When I\'m dead, I want people to remember me as:')
print('1 - The Good')
print('2 - The Great')
print('3 - The Wise')
print('4 - The Bold')
q2 = int(input('Please answer between 1-4: '))
#logic for question 2
if q2 == 4:
  Gryffindor = Gryffindor + 2
elif q2 == 3:
  Ravenclaw = Ravenclaw + 2
elif q2 == 1:
  Hufflepuff = Hufflepuff + 2
elif q2 == 2:
  Slytherin = Slytherin + 2
else:
  print('Wrong input')
#question 3
print('Which kind of instrument most pleases your ear? ')
print('1 - The violin')
print('2 - The trumpet')
print('3 - The piano')
print('4 - The drum')
q3 = int(input('Please answer between 1-4: '))
#logic for question 3
if q3 == 4:
  Gryffindor = Gryffindor + 4
elif q3 == 3:
  Ravenclaw = Ravenclaw + 4
elif q3 == 2:
  Hufflepuff = Hufflepuff + 4
elif q3 == 1:
  Slytherin = Slytherin + 4
else:
  print('Wrong input')
#print scores
print('Gryffindor: ', Gryffindor)
print('Ravenclaw: ', Ravenclaw)
print('Hufflepuff: ', Hufflepuff)
print('Slytherin: ', Slytherin)
