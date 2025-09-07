#printing the season that corresponds to the month number
#the challenge didn't want me to use int input, so I had to change the numbers to strings
month = input('What month is it? note: please respond with the month number ')

if month == '1' or month == '2' or month == '3':
  print('Winter')
elif month == '4' or month == '5' month == '6':
  print('Spring')
elif month == '7' or month == '8' or month == '9':
  print('Summer')
elif month == '10' or month == '11' or month == '12':
  print('Autumn')
else:
  print('Invalid')
