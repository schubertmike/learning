#starting to learn functions

'''learning about the DRY principle: reducing repetition and writing good clean code
functions are a big part of this. They are reusable blocks of code that perform specific tasks. To execute this, we just need to write the name of the function and parentheses
Python has 68 built in functions. we have already used print, input, len'''

#use 4 built in functions we've already used and 1 built in function we haven't
ghibli = []

for i in range(25): #range let's me specify a range of numbers, or in this case, iterations
  q1 = input('what studio ghibli movies have you watched? ') #input lets me ask a question and have the user write back
  if q1 == 'no more':
    break
  else:
    ghibli.append(q1)
if len(ghibli) == 1: #len takes the amount of items in the list, or the length of a string
  print('you\'ve watched', len(ghibli), 'movie!')
else:
  print('you\'ve watched', len(ghibli), 'movies!') 
print(ghibli)#print simply repeats something back to me, it can be a number it can be math, it can be a string or a list etc
print(sorted(ghibli))#sorted, in this case, sorts the string in alphabetical order
