#this will calculate the area of the following shapes:
#square, rectangle, triangle, circle
import math
print('===============')
print('Area Calculator')
print('===============')

print('1 - Triangle')
print('2 - Square')
print('3 - Rectangle')
print('4 - Circle')
print('5 - I\'m finished')

shape = int(input('Which shape would you like to find the area for? Please pick a number from above '))
area = 0

if shape == 1:
  base = int(input('What is the base of the triangle? '))
  height = int(input('What is the height of the triangle? '))
elif shape == 2:
  side =  int(input('What\'s the length of one of the sides of the square? '))
elif shape == 3: 
  length = int(input('What is the length of the rectangle? (the longer side) '))
  width = int(input('What is the width of the rectangle? (the shorter side) '))
elif shape == 4:
  radius = int(input('What is the radius of the circle? (take diameter, aka the measurement from end end to the opposite end, and divide by 2) '))
else:
  print('I\'ll be here when you need me to calculate the area! ')



