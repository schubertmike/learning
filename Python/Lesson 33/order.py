#i needed a lot of help with this one. Functions still confuse me a big
menu = ['Cheeseburger','Fries','Soda','Ice Cream','Cookie']
def welcome():
  print('Welcome to yumtown, here\'s our menu of yummy eats!')
  print('=================')
  print('1 - Cheeseburger')
  print('2 - Fries')
  print('3 - Soda')
  print('4 - Ice Cream')
  print('5 - Cookie')
  print('=================')
    

def get_item(x):
  if x == 1:
    return 'Cheeseburger'
  elif x == 2:
    return 'Fries'
  elif x == 3:
    return 'Soda'
  elif x == 4:
    return 'Ice Cream'
  elif x == 5:    
    return 'Cookie'

welcome()

option = int(input('What would you like to eat, today? '))
print(get_item(option))
