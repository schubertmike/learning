#asking for grade as an integer, then printing the corresponding grade as a string
grade = int(input('What grade are you in? '))

if grade == 9:
  print('Freshman')
elif grade == 10:
  print('Sophomore')
elif grade == 11:
  print('Junior')
elif grade == 12:
  print('Senior')
else:
  print('TBD')
