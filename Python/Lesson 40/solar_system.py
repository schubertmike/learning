#we can import directly from something by doing this "from module_name import objects"
#the as keyword lets us alias things
#por ejemplo:
from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury':
  r = 2440
elif random_planet == 'Venus':
  r = 6052
elif random_planet == 'Earth':
  r = 6371
elif random_planet == 'Mars':
  r = 3390
elif random_planet == 'Saturn':
  r = 58232
else:
  print('Oops! an error occurred')

area = 4*pi*r**2

print('Planet: '+ random_planet)
print('Area: ' + str(round(area,2)))
